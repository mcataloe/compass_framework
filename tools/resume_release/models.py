"""Internal result models used by the validator and manifest writer."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .constants import FAIL, PASS, UNKNOWN


@dataclass(frozen=True)
class CheckResult:
    id: str
    status: str
    diagnostic_code: str
    message: str = ""
    measurements: dict[str, str | int | float | bool | None] = field(default_factory=dict)
    evidence_paths: tuple[str, ...] = ()
    required: bool = True

    def to_manifest(self) -> dict[str, Any]:
        result: dict[str, Any] = {
            "id": self.id,
            "required": self.required,
            "status": self.status,
            "diagnostic_code": self.diagnostic_code,
        }
        if self.message:
            result["message"] = self.message[:1000]
        if self.measurements:
            result["measurements"] = self.measurements
        if self.evidence_paths:
            result["evidence_paths"] = list(self.evidence_paths)
        return result


@dataclass(frozen=True)
class PageMetrics:
    page_number: int
    path: Path
    width: int
    height: int
    ink_ratio: float
    bottom_whitespace_ratio: float


@dataclass(frozen=True)
class RenderOutcome:
    status: str
    diagnostic_code: str
    message: str = ""
    pages: tuple[PageMetrics, ...] = ()
    renderer_versions: dict[str, str] = field(default_factory=dict)


def aggregate_status(results: list[CheckResult]) -> str:
    required = [result for result in results if result.required]
    if any(result.status == FAIL for result in required):
        return FAIL
    if any(result.status == UNKNOWN for result in required):
        return UNKNOWN
    return PASS
