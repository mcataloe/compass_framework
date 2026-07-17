"""Safe system-renderer adapter and dependency-free page geometry."""

from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
from pathlib import Path

from .constants import PASS, UNKNOWN
from .models import PageMetrics, RenderOutcome

RENDER_TIMEOUT_SECONDS = 120
INK_THRESHOLD = 245


def _tool_version(executable: str, version_argument: str = "--version") -> str:
    try:
        completed = subprocess.run(
            [executable, version_argument],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (OSError, subprocess.SubprocessError):
        return "unavailable"
    output = (completed.stdout or completed.stderr).strip().splitlines()
    return output[0][:200] if output else "unknown"


def _pgm_tokens(data: bytes):
    index = 0
    length = len(data)
    while index < length:
        while index < length and data[index] in b" \t\r\n":
            index += 1
        if index < length and data[index] == 35:
            while index < length and data[index] not in b"\r\n":
                index += 1
            continue
        if index >= length:
            break
        start = index
        while index < length and data[index] not in b" \t\r\n#":
            index += 1
        yield data[start:index], index


def measure_pgm(path: Path, page_number: int) -> PageMetrics:
    data = path.read_bytes()
    tokens = _pgm_tokens(data)
    try:
        magic, _ = next(tokens)
        width_token, _ = next(tokens)
        height_token, _ = next(tokens)
        max_token, header_index = next(tokens)
    except StopIteration as exc:
        raise ValueError("incomplete PGM header") from exc
    if magic not in {b"P2", b"P5"}:
        raise ValueError("unsupported bitmap format")
    width = int(width_token)
    height = int(height_token)
    maximum = int(max_token)
    if width <= 0 or height <= 0 or maximum <= 0 or maximum > 255:
        raise ValueError("invalid PGM dimensions")
    if magic == b"P5":
        pixel_start = header_index
        if data[pixel_start : pixel_start + 2] == b"\r\n":
            pixel_start += 2
        elif pixel_start < len(data) and data[pixel_start] in b" \t\r\n":
            pixel_start += 1
        else:
            raise ValueError("missing PGM header separator")
        pixels = data[pixel_start : pixel_start + width * height]
        if len(pixels) != width * height:
            raise ValueError("incomplete PGM pixel data")
    else:
        remaining = list(tokens)
        try:
            pixels = bytes(min(255, int(token) * 255 // maximum) for token, _ in remaining)
        except ValueError as exc:
            raise ValueError("invalid PGM pixel data") from exc
        if len(pixels) != width * height:
            raise ValueError("incomplete PGM pixel data")
    ink_count = 0
    last_ink_row = -1
    for offset, pixel in enumerate(pixels):
        if pixel < INK_THRESHOLD:
            ink_count += 1
            last_ink_row = max(last_ink_row, offset // width)
    total = width * height
    ink_ratio = ink_count / total
    bottom_ratio = 1.0 if last_ink_row < 0 else (height - last_ink_row - 1) / height
    return PageMetrics(
        page_number=page_number,
        path=path,
        width=width,
        height=height,
        ink_ratio=round(ink_ratio, 8),
        bottom_whitespace_ratio=round(bottom_ratio, 8),
    )


class SystemRenderer:
    """LibreOffice-to-PDF plus Poppler-to-PGM renderer."""

    def render(self, docx_path: Path, render_dir: Path, supported: list[str]) -> RenderOutcome:
        supported_normalized = {item.casefold() for item in supported}
        soffice = shutil.which("soffice") or shutil.which("libreoffice")
        pdftoppm = shutil.which("pdftoppm")
        if not ({"libreoffice", "soffice"} & supported_normalized):
            return RenderOutcome(UNKNOWN, "renderer.unsupported", "No supported renderer was configured.")
        if not soffice or not pdftoppm:
            return RenderOutcome(UNKNOWN, "renderer.unavailable", "Required system renderer tools are unavailable.")

        render_dir.mkdir(parents=True, exist_ok=True)
        versions = {
            "libreoffice": _tool_version(soffice),
            "pdftoppm": _tool_version(pdftoppm, "-v"),
        }
        try:
            with tempfile.TemporaryDirectory(prefix=".resume-render-", dir=render_dir) as temporary:
                temporary_path = Path(temporary)
                input_path = temporary_path / "input.docx"
                profile_path = temporary_path / "libreoffice-profile"
                profile_path.mkdir()
                shutil.copyfile(docx_path, input_path)
                conversion = subprocess.run(
                    [
                        soffice,
                        "--headless",
                        f"-env:UserInstallation={profile_path.resolve().as_uri()}",
                        "--convert-to",
                        "pdf",
                        "--outdir",
                        str(temporary_path),
                        str(input_path),
                    ],
                    check=False,
                    capture_output=True,
                    text=True,
                    timeout=RENDER_TIMEOUT_SECONDS,
                )
                pdf_path = temporary_path / "input.pdf"
                if conversion.returncode != 0 or not pdf_path.is_file():
                    return RenderOutcome(
                        UNKNOWN,
                        "renderer.conversion_failed",
                        "The configured document renderer did not produce a PDF.",
                        renderer_versions=versions,
                    )
                raster = subprocess.run(
                    [pdftoppm, "-gray", "-r", "72", str(pdf_path), str(temporary_path / "page")],
                    check=False,
                    capture_output=True,
                    text=True,
                    timeout=RENDER_TIMEOUT_SECONDS,
                )
                generated = sorted(temporary_path.glob("page-*.pgm"))
                if raster.returncode != 0 or not generated:
                    return RenderOutcome(
                        UNKNOWN,
                        "renderer.raster_failed",
                        "The configured page renderer did not produce page bitmaps.",
                        renderer_versions=versions,
                    )
                pages: list[PageMetrics] = []
                for page_number, generated_path in enumerate(generated, start=1):
                    evidence = render_dir / f"resume-page-{page_number:04d}.pgm"
                    temporary_evidence = render_dir / f".resume-page-{page_number:04d}.tmp"
                    try:
                        shutil.copyfile(generated_path, temporary_evidence)
                        os.replace(temporary_evidence, evidence)
                    finally:
                        if temporary_evidence.exists():
                            temporary_evidence.unlink()
                    pages.append(measure_pgm(evidence, page_number))
                return RenderOutcome(
                    PASS,
                    "renderer.completed",
                    pages=tuple(pages),
                    renderer_versions=versions,
                )
        except (OSError, subprocess.SubprocessError, ValueError) as exc:
            return RenderOutcome(
                UNKNOWN,
                "renderer.execution_error",
                f"Renderer execution was incomplete ({exc.__class__.__name__}).",
                renderer_versions=versions,
            )
