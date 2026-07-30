"""OOXML package inspection using only ZIP and ElementTree."""

from __future__ import annotations

import io
import re
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET
from xml.parsers import expat

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
MC_NS = "http://schemas.openxmlformats.org/markup-compatibility/2006"
NS = {"w": W_NS}
MAX_PACKAGE_MEMBERS = 10_000
MAX_UNCOMPRESSED_BYTES = 100 * 1024 * 1024
XML_DECLARED_ENCODING = re.compile(
    br"^\s*<\?xml\s+[^>]*encoding\s*=\s*(['\"])([^'\"]+)\1",
    re.IGNORECASE,
)
COMPATIBILITY_PREFIX_ATTRIBUTES = {
    "Ignorable",
    "MustUnderstand",
    "PreserveAttributes",
    "PreserveElements",
    "ProcessContent",
}


def qn(local: str) -> str:
    return f"{{{W_NS}}}{local}"


def _value(element: ET.Element | None) -> str | None:
    if element is None:
        return None
    return element.get(qn("val"))


def _integer(value: str | None) -> int | None:
    try:
        return int(value) if value is not None else None
    except ValueError:
        return None


def _on(element: ET.Element | None) -> bool:
    if element is None:
        return False
    value = element.get(qn("val"))
    return value is None or value.lower() not in {"0", "false", "off", "no"}


@dataclass(frozen=True)
class Paragraph:
    index: int
    text: str
    style_id: str | None
    num_id: int | None
    left_indent: int | None
    hanging_indent: int | None
    keep_next: bool
    page_break_before: bool
    manual_page_breaks: int


@dataclass(frozen=True)
class StyleInfo:
    style_id: str
    font_family: str | None
    font_size_half_points: int | None
    bold: bool
    color_hex: str | None
    space_before_twips: int | None
    space_after_twips: int | None
    num_id: int | None
    left_indent: int | None
    hanging_indent: int | None
    keep_next: bool
    page_break_before: bool


@dataclass(frozen=True)
class SectionMargins:
    top: int | None
    right: int | None
    bottom: int | None
    left: int | None


class DocxInspectionError(ValueError):
    pass


def _validate_xml_encoding_and_namespaces(data: bytes) -> str | None:
    declared = XML_DECLARED_ENCODING.match(data)
    if declared:
        try:
            data.decode(declared.group(2).decode("ascii"), errors="strict")
        except (LookupError, UnicodeDecodeError, UnicodeError):
            return "XML declared encoding does not match part bytes"

    scopes: list[dict[str, str]] = []
    pending: dict[str, str] = {}

    def namespace_start(prefix: str | None, uri: str) -> None:
        pending[prefix or ""] = uri

    def start(name: str, attributes: dict[str, str]) -> None:
        scope = dict(scopes[-1]) if scopes else {}
        scope.update(pending)
        pending.clear()
        scopes.append(scope)

        for attribute_name, value in attributes.items():
            if " " not in attribute_name:
                continue
            uri, local = attribute_name.split(" ", 1)
            if uri != MC_NS or local not in COMPATIBILITY_PREFIX_ATTRIBUTES:
                continue
            for token in value.split():
                prefix = token.split(":", 1)[0]
                if prefix not in scope:
                    raise DocxInspectionError(
                        f"undeclared markup-compatibility prefix: {prefix}"
                    )

        if name == f"{MC_NS} Choice":
            for token in attributes.get("Requires", "").split():
                if token not in scope:
                    raise DocxInspectionError(
                        f"undeclared markup-compatibility prefix: {token}"
                    )

    def end(_name: str) -> None:
        scopes.pop()

    parser = expat.ParserCreate(namespace_separator=" ")
    parser.StartNamespaceDeclHandler = namespace_start
    parser.StartElementHandler = start
    parser.EndElementHandler = end
    try:
        parser.Parse(data, True)
    except (expat.ExpatError, DocxInspectionError, UnicodeError) as exc:
        return str(exc) or exc.__class__.__name__
    return None


class DocxInspector:
    """Parses the bounded structural subset required by the release contract."""

    def __init__(self, path: Path):
        self.path = path
        self.parts: dict[str, bytes] = {}
        self.package_error: str | None = None
        self.xml_errors: dict[str, str] = {}
        self.document: ET.Element | None = None
        self.styles_root: ET.Element | None = None
        self.numbering_root: ET.Element | None = None
        self.paragraphs: list[Paragraph] = []
        self.styles: dict[str, StyleInfo] = {}
        self.numbering_ids: set[int] = set()
        self.abstract_numbering_ids: set[int] = set()
        self.numbering_map: dict[int, int] = {}
        self.abstract_numbering_formats: dict[int, set[str]] = {}
        self.sections: list[SectionMargins] = []
        self._load()

    def _load(self) -> None:
        try:
            with zipfile.ZipFile(self.path) as package:
                infos = package.infolist()
                if len(infos) > MAX_PACKAGE_MEMBERS:
                    raise DocxInspectionError("package member limit exceeded")
                if sum(info.file_size for info in infos) > MAX_UNCOMPRESSED_BYTES:
                    raise DocxInspectionError("package expansion limit exceeded")
                for info in infos:
                    if info.is_dir():
                        continue
                    self.parts[info.filename] = package.read(info)
        except (OSError, zipfile.BadZipFile, RuntimeError, DocxInspectionError) as exc:
            self.package_error = str(exc) or exc.__class__.__name__
            return

        self.document = self._parse_part("word/document.xml")
        self.styles_root = self._parse_part("word/styles.xml")
        self.numbering_root = self._parse_part("word/numbering.xml")
        if self.document is not None:
            self.paragraphs = self._parse_paragraphs(self.document)
            self.sections = self._parse_sections(self.document)
        if self.styles_root is not None:
            self.styles = self._parse_styles(self.styles_root)
        if self.numbering_root is not None:
            self._parse_numbering(self.numbering_root)

    def _parse_part(self, name: str) -> ET.Element | None:
        data = self.parts.get(name)
        if data is None:
            return None
        try:
            return ET.parse(io.BytesIO(data)).getroot()
        except ET.ParseError as exc:
            self.xml_errors[name] = f"XML parse error at line {exc.position[0]}"
            return None

    def package_check(self, required_parts: list[str]) -> tuple[bool, list[str]]:
        if self.package_error:
            return False, ["package_unreadable"]
        missing = [part for part in required_parts if part not in self.parts]
        xml_parts = [
            part for part in self.parts if part.endswith(".xml") or part.endswith(".rels")
        ]
        for part in xml_parts:
            if part in self.xml_errors:
                continue
            if problem := _validate_xml_encoding_and_namespaces(self.parts[part]):
                self.xml_errors[part] = problem
        invalid = sorted(self.xml_errors)
        return not missing and not invalid, missing + invalid

    def normalized_text(self) -> str:
        return " ".join(" ".join(paragraph.text.split()) for paragraph in self.paragraphs).casefold()

    def paragraphs_for_style(self, style_id: str) -> list[Paragraph]:
        return [paragraph for paragraph in self.paragraphs if paragraph.style_id == style_id]

    def effective_num_id(self, paragraph: Paragraph) -> int | None:
        if paragraph.num_id is not None:
            return paragraph.num_id
        style = self.styles.get(paragraph.style_id or "")
        return style.num_id if style else None

    def effective_indentation(self, paragraph: Paragraph) -> tuple[int | None, int | None]:
        style = self.styles.get(paragraph.style_id or "")
        left = paragraph.left_indent
        hanging = paragraph.hanging_indent
        if style:
            left = left if left is not None else style.left_indent
            hanging = hanging if hanging is not None else style.hanging_indent
        return left, hanging

    def effective_keep_next(self, paragraph: Paragraph) -> bool:
        style = self.styles.get(paragraph.style_id or "")
        return paragraph.keep_next or bool(style and style.keep_next)

    def effective_page_break_before(self, paragraph: Paragraph) -> bool:
        style = self.styles.get(paragraph.style_id or "")
        return paragraph.page_break_before or bool(style and style.page_break_before)

    def _parse_paragraphs(self, root: ET.Element) -> list[Paragraph]:
        paragraphs: list[Paragraph] = []
        for index, node in enumerate(root.findall(".//w:p", NS)):
            ppr = node.find("w:pPr", NS)
            style_id = _value(ppr.find("w:pStyle", NS)) if ppr is not None else None
            num_id = None
            left = None
            hanging = None
            keep_next = False
            page_break_before = False
            if ppr is not None:
                num_id = _integer(_value(ppr.find("w:numPr/w:numId", NS)))
                ind = ppr.find("w:ind", NS)
                if ind is not None:
                    left = _integer(ind.get(qn("left")))
                    hanging = _integer(ind.get(qn("hanging")))
                keep_next = _on(ppr.find("w:keepNext", NS))
                page_break_before = _on(ppr.find("w:pageBreakBefore", NS))
            text = "".join(item.text or "" for item in node.findall(".//w:t", NS))
            manual = sum(
                1
                for item in node.findall(".//w:br", NS)
                if item.get(qn("type")) == "page"
            )
            paragraphs.append(
                Paragraph(
                    index=index,
                    text=text,
                    style_id=style_id,
                    num_id=num_id,
                    left_indent=left,
                    hanging_indent=hanging,
                    keep_next=keep_next,
                    page_break_before=page_break_before,
                    manual_page_breaks=manual,
                )
            )
        return paragraphs

    def _parse_styles(self, root: ET.Element) -> dict[str, StyleInfo]:
        styles: dict[str, StyleInfo] = {}
        for node in root.findall("w:style", NS):
            style_id = node.get(qn("styleId"))
            if not style_id:
                continue
            ppr = node.find("w:pPr", NS)
            rpr = node.find("w:rPr", NS)
            rfonts = rpr.find("w:rFonts", NS) if rpr is not None else None
            spacing = ppr.find("w:spacing", NS) if ppr is not None else None
            ind = ppr.find("w:ind", NS) if ppr is not None else None
            styles[style_id] = StyleInfo(
                style_id=style_id,
                font_family=(
                    rfonts.get(qn("ascii")) or rfonts.get(qn("hAnsi"))
                    if rfonts is not None
                    else None
                ),
                font_size_half_points=_integer(_value(rpr.find("w:sz", NS))) if rpr is not None else None,
                bold=_on(rpr.find("w:b", NS)) if rpr is not None else False,
                color_hex=_value(rpr.find("w:color", NS)) if rpr is not None else None,
                space_before_twips=_integer(spacing.get(qn("before"))) if spacing is not None else None,
                space_after_twips=_integer(spacing.get(qn("after"))) if spacing is not None else None,
                num_id=_integer(_value(ppr.find("w:numPr/w:numId", NS))) if ppr is not None else None,
                left_indent=_integer(ind.get(qn("left"))) if ind is not None else None,
                hanging_indent=_integer(ind.get(qn("hanging"))) if ind is not None else None,
                keep_next=_on(ppr.find("w:keepNext", NS)) if ppr is not None else False,
                page_break_before=(
                    _on(ppr.find("w:pageBreakBefore", NS)) if ppr is not None else False
                ),
            )
        return styles

    def _parse_numbering(self, root: ET.Element) -> None:
        for node in root.findall("w:num", NS):
            num_id = _integer(node.get(qn("numId")))
            abstract_id = _integer(_value(node.find("w:abstractNumId", NS)))
            if num_id is not None:
                self.numbering_ids.add(num_id)
                if abstract_id is not None:
                    self.numbering_map[num_id] = abstract_id
        self.abstract_numbering_ids = {
            value
            for node in root.findall("w:abstractNum", NS)
            if (value := _integer(node.get(qn("abstractNumId")))) is not None
        }
        for node in root.findall("w:abstractNum", NS):
            abstract_id = _integer(node.get(qn("abstractNumId")))
            if abstract_id is None:
                continue
            self.abstract_numbering_formats[abstract_id] = {
                value
                for format_node in node.findall("w:lvl/w:numFmt", NS)
                if (value := _value(format_node)) is not None
            }

    def _parse_sections(self, root: ET.Element) -> list[SectionMargins]:
        sections: list[SectionMargins] = []
        for section in root.findall(".//w:sectPr", NS):
            margins = section.find("w:pgMar", NS)
            if margins is None:
                continue
            sections.append(
                SectionMargins(
                    top=_integer(margins.get(qn("top"))),
                    right=_integer(margins.get(qn("right"))),
                    bottom=_integer(margins.get(qn("bottom"))),
                    left=_integer(margins.get(qn("left"))),
                )
            )
        return sections


def style_mismatches(actual: StyleInfo | None, expected: dict[str, Any]) -> list[str]:
    if actual is None:
        return ["missing_style"]
    mapping = {
        "font_family": actual.font_family,
        "font_size_half_points": actual.font_size_half_points,
        "bold": actual.bold,
        "color_hex": actual.color_hex,
        "space_before_twips": actual.space_before_twips,
        "space_after_twips": actual.space_after_twips,
    }
    mismatches: list[str] = []
    for key, expected_value in expected.items():
        if key == "paragraph_style":
            continue
        actual_value = mapping.get(key)
        if key in {"font_family", "color_hex"} and isinstance(actual_value, str):
            actual_value = actual_value.casefold()
            expected_value = str(expected_value).casefold()
        if actual_value != expected_value:
            mismatches.append(key)
    return mismatches
