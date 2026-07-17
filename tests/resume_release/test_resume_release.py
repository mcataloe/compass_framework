from __future__ import annotations

import json
import shutil
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock

from tools.resume_release.cli import main as cli_main
from tools.resume_release.constants import CHECK_IDS, FAIL, PASS, UNKNOWN
from tools.resume_release.contracts import ContractError, load_coverage, load_inputs
from tools.resume_release.engine import ResumeReleaseEngine, sha256_file
from tools.resume_release.models import PageMetrics, RenderOutcome
from tools.resume_release.render import measure_pgm


CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>
</Types>
"""

ROOT_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>
"""

DOCUMENT_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>
</Relationships>
"""

STYLES_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:style w:type="paragraph" w:default="1" w:styleId="Body">
    <w:name w:val="Body"/>
    <w:pPr><w:spacing w:before="0" w:after="0"/></w:pPr>
    <w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/><w:color w:val="000000"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading">
    <w:name w:val="Heading"/>
    <w:pPr><w:keepNext/><w:spacing w:before="0" w:after="0"/></w:pPr>
    <w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/><w:sz w:val="22"/><w:color w:val="000000"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Bullet">
    <w:name w:val="Bullet"/>
    <w:pPr><w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr><w:ind w:left="720" w:hanging="360"/><w:spacing w:before="0" w:after="0"/></w:pPr>
    <w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="22"/><w:color w:val="000000"/></w:rPr>
  </w:style>
</w:styles>
"""

NUMBERING_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:abstractNum w:abstractNumId="0">
    <w:lvl w:ilvl="0"><w:numFmt w:val="bullet"/><w:lvlText w:val="•"/></w:lvl>
  </w:abstractNum>
  <w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num>
</w:numbering>
"""


def document_xml(*, manual_break: bool = False, forced_break: bool = False) -> str:
    break_xml = '<w:r><w:br w:type="page"/></w:r>' if manual_break else ""
    forced_xml = "<w:pageBreakBefore/>" if forced_break else ""
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    <w:p><w:pPr><w:pStyle w:val="Heading"/>{forced_xml}</w:pPr><w:r><w:t>SECTION_A</w:t></w:r>{break_xml}</w:p>
    <w:p><w:pPr><w:pStyle w:val="Body"/></w:pPr><w:r><w:t>ROLE_A ANCHOR_A 2+ years</w:t></w:r></w:p>
    <w:p><w:pPr><w:pStyle w:val="Bullet"/></w:pPr><w:r><w:t>Neutral capability statement</w:t></w:r></w:p>
    <w:sectPr><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="1080" w:right="1080" w:bottom="1080" w:left="1080"/></w:sectPr>
  </w:body>
</w:document>
"""


def write_docx(
    path: Path,
    *,
    malformed: bool = False,
    omit_part: str | None = None,
    malformed_part: str | None = None,
    invalid_list: bool = False,
    invalid_numbering_relationship: bool = False,
    invalid_list_format: bool = False,
    manual_break: bool = False,
    forced_break: bool = False,
    style_forced_break: bool = False,
) -> None:
    if malformed:
        path.write_bytes(b"not-a-zip-package")
        return
    styles = STYLES_XML
    if invalid_list:
        styles = styles.replace(
            '<w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>', ""
        )
    if style_forced_break:
        styles = styles.replace("<w:keepNext/>", "<w:keepNext/><w:pageBreakBefore/>")
    numbering = NUMBERING_XML
    if invalid_numbering_relationship:
        numbering = numbering.replace('<w:abstractNumId w:val="0"/>', '<w:abstractNumId w:val="999"/>')
    if invalid_list_format:
        numbering = numbering.replace('<w:numFmt w:val="bullet"/>', '<w:numFmt w:val="decimal"/>')
    parts = {
        "[Content_Types].xml": CONTENT_TYPES,
        "_rels/.rels": ROOT_RELS,
        "word/document.xml": document_xml(
            manual_break=manual_break, forced_break=forced_break
        ),
        "word/styles.xml": styles,
        "word/numbering.xml": numbering,
        "word/_rels/document.xml.rels": DOCUMENT_RELS,
    }
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as package:
        for name, content in parts.items():
            if name != omit_part:
                package.writestr(name, "<malformed" if name == malformed_part else content)


def base_contract() -> dict:
    return {
        "schema_version": "1.0.0",
        "contract_id": "synthetic-contract",
        "profile": {"id": "synthetic-profile", "version": "1", "sha256": "0" * 64},
        "policy_identity": {
            "framework_version": "vNext 2026-07.4",
            "source_policy_version": "synthetic-1",
        },
        "required_checks": list(CHECK_IDS),
        "artifact": {
            "formats": ["docx", "markdown"],
            "filename_pattern": r"^Resume\.(?:docx|md)$",
            "forbid_url_encoded_filename": True,
        },
        "docx": {
            "required_parts": [
                "[Content_Types].xml",
                "_rels/.rels",
                "word/document.xml",
                "word/styles.xml",
                "word/numbering.xml",
            ],
            "style_rules": [
                {
                    "paragraph_style": "Body",
                    "font_family": "Arial",
                    "font_size_half_points": 22,
                    "bold": False,
                    "color_hex": "000000",
                    "space_before_twips": 0,
                    "space_after_twips": 0,
                },
                {
                    "paragraph_style": "Heading",
                    "font_family": "Arial",
                    "font_size_half_points": 22,
                    "bold": True,
                    "color_hex": "000000",
                    "space_before_twips": 0,
                    "space_after_twips": 0,
                },
                {
                    "paragraph_style": "Bullet",
                    "font_family": "Arial",
                    "font_size_half_points": 22,
                    "bold": False,
                    "color_hex": "000000",
                    "space_before_twips": 0,
                    "space_after_twips": 0,
                },
            ],
            "list_rules": [
                {
                    "paragraph_style": "Bullet",
                    "native_numbering_required": True,
                    "left_indent_twips": 720,
                    "hanging_indent_twips": 360,
                    "tolerance_twips": 0,
                }
            ],
            "layout_rules": {
                "margin_tolerance_twips": 0,
                "section_margins": {"top": 1080, "right": 1080, "bottom": 1080, "left": 1080},
            },
            "break_rules": {
                "manual_page_breaks": "forbid",
                "page_break_before": "forbid",
                "allowed_paragraph_styles": [],
            },
            "keep_next_rules": [{"paragraph_style": "Heading", "required": True}],
        },
        "content": {
            "required_sections": ["SECTION_A", "ROLE_A"],
            "markdown_docx_parity": {"required": True, "anchors": ["ANCHOR_A"]},
            "employment_coverage": {
                "required": True,
                "allowed_dispositions": ["detailed", "compressed", "excluded"],
            },
            "experience_duration": {
                "required": True,
                "calculation_method": "union_of_calendar_intervals",
            },
        },
        "render": {
            "required": False,
            "supported_renderers": ["libreoffice"],
            "page_images_required": True,
            "max_non_final_bottom_whitespace_ratio": 0.5,
            "nearly_blank_page_max_ink_ratio": 0.001,
            "final_page_whitespace_check": False,
        },
        "visual_review": {"required": False, "scope": "every_page"},
        "publication": {
            "atomic": True,
            "final_path_on_pass_only": True,
            "overwrite_policy": "replace_on_pass",
        },
        "privacy": {"diagnostic_mode": "metadata_only", "include_full_text": False},
    }


def base_coverage() -> dict:
    return {
        "schema_version": "1.0.0",
        "plan_id": "synthetic-plan",
        "artifact_id": "synthetic-artifact",
        "as_of_date": "2023-01-01",
        "source_identity": {"policy_version": "synthetic-1", "source_refs": ["source-a"]},
        "roles": [
            {
                "role_id": "role-a",
                "display_label": "ROLE_A",
                "source_refs": ["source-a"],
                "disposition": "detailed",
                "resume_section": "ROLE_A",
                "employment_interval": {
                    "start_date": "2020-01-01",
                    "end_date": "2023-01-01",
                    "current": False,
                },
            }
        ],
        "experience_claim": {
            "included": True,
            "rendered_label": "2+ years",
            "minimum_years": 2,
            "calculation_method": "union_of_calendar_intervals",
            "qualifying_intervals": [
                {
                    "start_date": "2020-01-01",
                    "end_date": "2023-01-01",
                    "current": False,
                }
            ],
        },
    }


class FakeRenderer:
    def __init__(self, outcome: RenderOutcome):
        self.outcome = outcome

    def render(self, docx_path: Path, render_dir: Path, supported: list[str]) -> RenderOutcome:
        return self.outcome


def page(number: int, path: Path, *, ink: float = 0.02, bottom: float = 0.1) -> PageMetrics:
    return PageMetrics(number, path, 612, 792, ink, bottom)


class ResumeReleaseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.docx = self.root / "Resume.docx"
        self.markdown = self.root / "Resume.md"
        self.contract_path = self.root / "contract.json"
        self.coverage_path = self.root / "coverage.json"
        self.manifest = self.root / "manifest.json"
        self.render_dir = self.root / "rendered"
        self.render_dir.mkdir()
        write_docx(self.docx)
        self.markdown.write_text("SECTION_A ROLE_A ANCHOR_A 2+ years\n", encoding="utf-8")
        self.contract = base_contract()
        self.coverage = base_coverage()
        self._write_inputs()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _write_inputs(self) -> None:
        self.contract_path.write_text(json.dumps(self.contract), encoding="utf-8")
        self.coverage_path.write_text(json.dumps(self.coverage), encoding="utf-8")

    def _run(
        self,
        *,
        mode: str = "validate",
        renderer: FakeRenderer | None = None,
        attestation_path: Path | None = None,
        output_docx: Path | None = None,
        output_markdown: Path | None = None,
    ):
        self._write_inputs()
        loaded = load_inputs(self.contract_path, self.coverage_path, attestation_path)
        return ResumeReleaseEngine(renderer=renderer).run(
            mode=mode,
            loaded=loaded,
            docx_path=self.docx,
            markdown_path=self.markdown,
            manifest_out=self.manifest,
            render_dir=self.render_dir,
            output_docx=output_docx,
            output_markdown=output_markdown,
        )

    @staticmethod
    def _status(manifest: dict, check_id: str) -> str:
        return next(check["status"] for check in manifest["checks"] if check["id"] == check_id)

    def test_valid_minimal_contract_and_package_pass(self) -> None:
        manifest, code = self._run()
        self.assertEqual(code, 0)
        self.assertEqual(manifest["aggregate_status"], PASS)
        self.assertEqual(manifest["schema_version"], "1.0.1")
        self.assertEqual(manifest["contract"]["policy_identity"]["framework_version"], "vNext 2026-07.4")

    def test_malformed_docx_fails_package(self) -> None:
        write_docx(self.docx, malformed=True)
        manifest, code = self._run()
        self.assertEqual(code, 1)
        self.assertEqual(self._status(manifest, "docx.package"), FAIL)

    def test_missing_required_ooxml_part_fails(self) -> None:
        write_docx(self.docx, omit_part="word/styles.xml")
        manifest, _ = self._run()
        self.assertEqual(self._status(manifest, "docx.package"), FAIL)

    def test_malformed_required_ooxml_part_fails(self) -> None:
        write_docx(self.docx, malformed_part="[Content_Types].xml")
        manifest, _ = self._run()
        self.assertEqual(self._status(manifest, "docx.package"), FAIL)

    def test_invalid_native_list_semantics_fail(self) -> None:
        write_docx(self.docx, invalid_list=True)
        manifest, _ = self._run()
        self.assertEqual(self._status(manifest, "docx.native_lists"), FAIL)

    def test_invalid_numbering_relationship_fails(self) -> None:
        write_docx(self.docx, invalid_numbering_relationship=True)
        manifest, _ = self._run()
        self.assertEqual(self._status(manifest, "docx.native_lists"), FAIL)

    def test_non_bullet_list_format_fails(self) -> None:
        write_docx(self.docx, invalid_list_format=True)
        manifest, _ = self._run()
        self.assertEqual(self._status(manifest, "docx.native_lists"), FAIL)

    def test_manual_page_break_fails(self) -> None:
        write_docx(self.docx, manual_break=True)
        manifest, _ = self._run()
        self.assertEqual(self._status(manifest, "docx.breaks"), FAIL)

    def test_forced_page_break_fails(self) -> None:
        write_docx(self.docx, forced_break=True)
        manifest, _ = self._run()
        self.assertEqual(self._status(manifest, "docx.breaks"), FAIL)

    def test_style_forced_page_break_fails(self) -> None:
        write_docx(self.docx, style_forced_break=True)
        manifest, _ = self._run()
        self.assertEqual(self._status(manifest, "docx.breaks"), FAIL)

    def test_missing_role_accounting_fails(self) -> None:
        self.coverage["roles"][0]["display_label"] = "ROLE_NOT_PRESENT"
        self.coverage["roles"][0]["resume_section"] = "ROLE_NOT_PRESENT"
        manifest, _ = self._run()
        self.assertEqual(self._status(manifest, "content.employment_coverage"), FAIL)

    def test_excluded_role_without_reason_is_invalid_input(self) -> None:
        self.coverage["roles"][0]["disposition"] = "excluded"
        self.coverage["roles"][0].pop("reason", None)
        self._write_inputs()
        with self.assertRaises(ContractError):
            load_coverage(self.coverage_path)

    def test_experience_duration_mismatch_fails(self) -> None:
        self.coverage["experience_claim"]["minimum_years"] = 10
        manifest, _ = self._run()
        self.assertEqual(self._status(manifest, "content.experience_duration"), FAIL)

    def test_markdown_docx_anchor_mismatch_fails(self) -> None:
        self.markdown.write_text("SECTION_A ROLE_A 2+ years\n", encoding="utf-8")
        manifest, _ = self._run()
        self.assertEqual(self._status(manifest, "content.markdown_docx_parity"), FAIL)

    def test_missing_renderer_is_unknown_and_blocks(self) -> None:
        self.contract["render"]["required"] = True
        renderer = FakeRenderer(RenderOutcome(UNKNOWN, "renderer.unavailable"))
        manifest, code = self._run(renderer=renderer)
        self.assertEqual(code, 2)
        self.assertEqual(self._status(manifest, "render.available"), UNKNOWN)

    def test_render_failure_is_unknown(self) -> None:
        self.contract["render"]["required"] = True
        renderer = FakeRenderer(RenderOutcome(UNKNOWN, "renderer.conversion_failed"))
        manifest, _ = self._run(renderer=renderer)
        self.assertEqual(self._status(manifest, "render.pages"), UNKNOWN)

    def test_excessive_non_final_whitespace_fails(self) -> None:
        self.contract["render"]["required"] = True
        outcome = RenderOutcome(
            PASS,
            "renderer.completed",
            pages=(page(1, self.root / "p1.pgm", bottom=0.8), page(2, self.root / "p2.pgm")),
        )
        manifest, _ = self._run(renderer=FakeRenderer(outcome))
        self.assertEqual(self._status(manifest, "render.whitespace"), FAIL)

    def test_nearly_blank_page_fails(self) -> None:
        self.contract["render"]["required"] = True
        outcome = RenderOutcome(
            PASS,
            "renderer.completed",
            pages=(page(1, self.root / "p1.pgm", ink=0.0001),),
        )
        manifest, _ = self._run(renderer=FakeRenderer(outcome))
        self.assertEqual(self._status(manifest, "render.blank_pages"), FAIL)

    def test_pgm_geometry_measurement(self) -> None:
        bitmap = self.root / "page.pgm"
        bitmap.write_bytes(b"P2\n2 4\n255\n255 255 0 255 255 255 255 255\n")
        metrics = measure_pgm(bitmap, 1)
        self.assertEqual(metrics.ink_ratio, 0.125)
        self.assertEqual(metrics.bottom_whitespace_ratio, 0.5)

    def test_missing_visual_attestation_is_unknown(self) -> None:
        self.contract["render"]["required"] = True
        self.contract["visual_review"]["required"] = True
        outcome = RenderOutcome(
            PASS,
            "renderer.completed",
            pages=(page(1, self.root / "p1.pgm"),),
        )
        manifest, _ = self._run(renderer=FakeRenderer(outcome))
        self.assertEqual(self._status(manifest, "visual.every_page_review"), UNKNOWN)

    def test_valid_visual_attestation_passes(self) -> None:
        self.contract["render"]["required"] = True
        self.contract["visual_review"] = {
            "required": True,
            "scope": "every_page",
            "attestation_schema_version": "1.0.0",
        }
        attestation = self.root / "attestation.json"
        attestation.write_text(
            json.dumps(
                {
                    "schema_version": "1.0.0",
                    "artifact_sha256": sha256_file(self.docx),
                    "page_count": 1,
                    "reviewed_pages": [1],
                    "reviewer_type": "human",
                    "attested_at": "2026-01-01T00:00:00Z",
                }
            ),
            encoding="utf-8",
        )
        outcome = RenderOutcome(
            PASS,
            "renderer.completed",
            pages=(page(1, self.root / "p1.pgm"),),
        )
        manifest, _ = self._run(
            renderer=FakeRenderer(outcome), attestation_path=attestation
        )
        self.assertEqual(self._status(manifest, "visual.every_page_review"), PASS)

    def test_failed_validation_does_not_overwrite_final(self) -> None:
        final = self.root / "Final.docx"
        final.write_bytes(b"existing-final")
        self.coverage["experience_claim"]["minimum_years"] = 10
        manifest, code = self._run(mode="release", output_docx=final)
        self.assertEqual(code, 1)
        self.assertEqual(final.read_bytes(), b"existing-final")
        self.assertFalse(manifest["publication"]["attempted"])

    def test_unknown_validation_does_not_create_final(self) -> None:
        final = self.root / "Final.docx"
        self.contract["render"]["required"] = True
        renderer = FakeRenderer(RenderOutcome(UNKNOWN, "renderer.unavailable"))
        manifest, code = self._run(mode="release", renderer=renderer, output_docx=final)
        self.assertEqual(code, 2)
        self.assertFalse(final.exists())
        self.assertFalse(manifest["publication"]["attempted"])

    def test_passing_validation_atomically_publishes(self) -> None:
        final_docx = self.root / "Final.docx"
        final_markdown = self.root / "Final.md"
        final_docx.write_bytes(b"old")
        final_markdown.write_text("old", encoding="utf-8")
        manifest, code = self._run(
            mode="release", output_docx=final_docx, output_markdown=final_markdown
        )
        self.assertEqual(code, 0)
        self.assertEqual(final_docx.read_bytes(), self.docx.read_bytes())
        self.assertEqual(final_markdown.read_text(encoding="utf-8"), self.markdown.read_text(encoding="utf-8"))
        self.assertTrue(manifest["publication"]["published"])
        self.assertEqual(len(manifest["publication"]["final_artifacts"]), 2)

    def test_publication_failure_keeps_existing_final(self) -> None:
        final = self.root / "Final.docx"
        final.write_bytes(b"existing-final")
        self.contract["publication"]["overwrite_policy"] = "forbid"
        manifest, code = self._run(mode="release", output_docx=final)
        self.assertEqual(code, 2)
        self.assertEqual(manifest["aggregate_status"], UNKNOWN)
        self.assertTrue(manifest["publication"]["attempted"])
        self.assertFalse(manifest["publication"]["published"])
        self.assertEqual(final.read_bytes(), b"existing-final")

    def test_manifest_write_failure_rolls_back_publication(self) -> None:
        final = self.root / "Final.docx"
        final.write_bytes(b"existing-final")
        self._write_inputs()
        loaded = load_inputs(self.contract_path, self.coverage_path, None)
        engine = ResumeReleaseEngine()
        with mock.patch.object(engine, "_atomic_write_json", side_effect=OSError("synthetic")):
            with self.assertRaises(OSError):
                engine.run(
                    mode="release",
                    loaded=loaded,
                    docx_path=self.docx,
                    markdown_path=self.markdown,
                    manifest_out=self.manifest,
                    render_dir=self.render_dir,
                    output_docx=final,
                )
        self.assertEqual(final.read_bytes(), b"existing-final")

    def test_actual_filename_rejects_url_encoding(self) -> None:
        encoded = self.root / "Resume%20Bad.docx"
        shutil.copyfile(self.docx, encoded)
        self.docx = encoded
        self.contract["artifact"]["filename_pattern"] = r"^Resume.*\.docx$"
        self.contract["artifact"]["formats"] = ["docx"]
        manifest, _ = self._run()
        self.assertEqual(self._status(manifest, "filename.actual"), FAIL)

    def test_manifest_identity_is_stable_for_same_inputs(self) -> None:
        first, _ = self._run()
        second, _ = self._run()
        self.assertEqual(first["manifest_id"], second["manifest_id"])

    def test_cli_invalid_contract_returns_64(self) -> None:
        self.contract["schema_version"] = "unsupported"
        self._write_inputs()
        code = cli_main(
            [
                "validate",
                "--docx",
                str(self.docx),
                "--markdown",
                str(self.markdown),
                "--contract",
                str(self.contract_path),
                "--coverage",
                str(self.coverage_path),
                "--manifest-out",
                str(self.manifest),
                "--render-dir",
                str(self.render_dir),
            ]
        )
        self.assertEqual(code, 64)

    def test_required_check_cannot_be_silently_omitted(self) -> None:
        self.contract["required_checks"].remove("render.whitespace")
        self._write_inputs()
        with self.assertRaises(ContractError):
            load_inputs(self.contract_path, self.coverage_path, None)


if __name__ == "__main__":
    unittest.main()
