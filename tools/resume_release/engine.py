"""Deterministic validation, manifest construction, and atomic publication."""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import tempfile
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from .constants import (
    FAIL,
    MANIFEST_SCHEMA_VERSION,
    PASS,
    UNKNOWN,
    VALIDATOR_NAME,
    VALIDATOR_VERSION,
)
from .contracts import LoadedInputs
from .docx import DocxInspector, style_mismatches
from .models import CheckResult, RenderOutcome, aggregate_status
from .render import SystemRenderer


class PublicationTransaction:
    """Holds rollback backups until the success manifest is durable."""

    def __init__(self, prepared: list[tuple[Path, Path, Path | None]]):
        self.prepared = prepared
        self.replaced: list[tuple[Path, Path | None]] = []

    def replace(self) -> None:
        try:
            for temporary, target, backup in self.prepared:
                os.replace(temporary, target)
                self.replaced.append((target, backup))
        except OSError:
            self.rollback()
            raise

    def commit(self) -> None:
        for _, _, backup in self.prepared:
            if backup and backup.exists():
                try:
                    backup.unlink()
                except OSError:
                    pass
        self._clean_temporaries()

    def rollback(self) -> None:
        for target, backup in reversed(self.replaced):
            try:
                if backup and backup.exists():
                    os.replace(backup, target)
                elif target.exists():
                    target.unlink()
            except OSError:
                pass
        self._clean_temporaries()

    def _clean_temporaries(self) -> None:
        for temporary, _, backup in self.prepared:
            for path in (temporary, backup):
                if path and path.exists():
                    try:
                        path.unlink()
                    except OSError:
                        pass


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _normalized(value: str) -> str:
    return " ".join(value.split()).casefold()


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _result(
    check_id: str,
    status: str,
    code: str,
    message: str = "",
    measurements: dict[str, str | int | float | bool | None] | None = None,
    evidence_paths: tuple[str, ...] = (),
) -> CheckResult:
    return CheckResult(
        id=check_id,
        status=status,
        diagnostic_code=code,
        message=message,
        measurements=measurements or {},
        evidence_paths=evidence_paths,
    )


class ResumeReleaseEngine:
    def __init__(self, renderer: Any | None = None):
        self.renderer = renderer or SystemRenderer()

    def run(
        self,
        *,
        mode: str,
        loaded: LoadedInputs,
        docx_path: Path | None,
        markdown_path: Path | None,
        manifest_out: Path,
        render_dir: Path,
        output_docx: Path | None = None,
        output_markdown: Path | None = None,
    ) -> tuple[dict[str, Any], int]:
        started_at = _utc_now()
        contract = loaded.contract
        required_ids = contract["required_checks"]
        input_records, input_hashes = self._input_records(
            loaded, docx_path=docx_path, markdown_path=markdown_path
        )
        inspector = (
            DocxInspector(docx_path)
            if docx_path is not None and docx_path.is_file()
            else None
        )
        markdown_text = self._read_markdown(markdown_path)
        render_outcome = self._render(
            contract=contract,
            docx_path=docx_path,
            render_dir=render_dir,
        )

        results = {
            "policy.current": self._check_policy(contract),
            "profile.current": self._check_profile(contract),
            "input.hashes": self._check_input_hashes(contract, docx_path, markdown_path),
            "filename.actual": self._check_filenames(contract, docx_path, markdown_path),
            "docx.package": self._check_package(contract, docx_path, inspector),
            "docx.styles": self._check_styles(contract, inspector),
            "docx.native_lists": self._check_native_lists(contract, inspector),
            "docx.indentation": self._check_indentation(contract, inspector),
            "docx.margins": self._check_margins(contract, inspector),
            "docx.breaks": self._check_breaks(contract, inspector),
            "docx.keep_next": self._check_keep_next(contract, inspector),
            "content.markdown_docx_parity": self._check_content_parity(
                contract, inspector, markdown_path, markdown_text
            ),
            "content.employment_coverage": self._check_employment_coverage(
                contract, loaded.coverage, inspector
            ),
            "content.experience_duration": self._check_experience_duration(
                contract, loaded.coverage, inspector
            ),
            "render.available": self._check_render_available(contract, render_outcome),
            "render.pages": self._check_render_pages(contract, render_outcome),
            "render.whitespace": self._check_render_whitespace(contract, render_outcome),
            "render.blank_pages": self._check_blank_pages(contract, render_outcome),
            "visual.every_page_review": self._check_visual_review(
                contract,
                loaded.attestation,
                render_outcome,
                input_hashes.get("docx"),
            ),
            "release.atomic_publication": _result(
                "release.atomic_publication",
                PASS,
                "publication.not_attempted",
                "Final paths were not modified during validation.",
            ),
        }

        ordered = [results[check_id] for check_id in required_ids]
        prepublication_status = aggregate_status(ordered)
        publication: dict[str, Any] = {
            "requested": mode == "release",
            "attempted": False,
            "published": False,
            "final_artifacts": [],
        }
        transaction: PublicationTransaction | None = None

        if mode == "release" and prepublication_status == PASS:
            publication["attempted"] = True
            try:
                pairs = self._publication_pairs(
                    docx_path, markdown_path, output_docx, output_markdown
                )
                transaction = self._begin_atomic_publish(
                    pairs, contract["publication"]["overwrite_policy"]
                )
            except OSError as exc:
                results["release.atomic_publication"] = _result(
                    "release.atomic_publication",
                    UNKNOWN,
                    "publication.failed",
                    f"Atomic publication was rolled back ({exc.__class__.__name__}).",
                )
                publication["diagnostic_code"] = "publication.failed"
            else:
                results["release.atomic_publication"] = _result(
                    "release.atomic_publication",
                    PASS,
                    "publication.completed",
                    measurements={"artifact_count": len(pairs)},
                )
                publication["published"] = True
                publication["diagnostic_code"] = "publication.completed"
                publication["final_artifacts"] = [
                    {
                        "kind": kind,
                        "path": str(target.resolve()),
                        "actual_filename": target.name,
                        "sha256": sha256_file(target),
                    }
                    for kind, _, target in pairs
                ]
        elif mode == "release":
            results["release.atomic_publication"] = _result(
                "release.atomic_publication",
                PASS,
                "publication.blocked",
                "Final paths were left unchanged because validation did not pass.",
            )
            publication["diagnostic_code"] = "publication.blocked"
        else:
            publication["diagnostic_code"] = "publication.not_requested"

        ordered = [results[check_id] for check_id in required_ids]
        aggregate = aggregate_status(ordered)
        finished_at = _utc_now()
        manifest_id = self._manifest_id(contract, mode, input_records)
        manifest = {
            "schema_version": MANIFEST_SCHEMA_VERSION,
            "manifest_id": manifest_id,
            "validator": {
                "name": VALIDATOR_NAME,
                "version": VALIDATOR_VERSION,
                "runtime": f"python-{os.sys.version_info.major}.{os.sys.version_info.minor}",
                "renderer_versions": render_outcome.renderer_versions,
            },
            "contract": {
                "contract_id": contract["contract_id"],
                "schema_version": contract["schema_version"],
                "profile_id": contract["profile"]["id"],
                "profile_version": contract["profile"]["version"],
                "policy_identity": contract["policy_identity"],
                "sha256": sha256_file(loaded.contract_path),
            },
            "started_at": started_at,
            "finished_at": finished_at,
            "inputs": input_records,
            "checks": [result.to_manifest() for result in ordered],
            "aggregate_status": aggregate,
            "publication": publication,
        }
        try:
            self._atomic_write_json(manifest_out, manifest)
        except OSError:
            if transaction is not None:
                transaction.rollback()
            raise
        else:
            if transaction is not None:
                transaction.commit()
        exit_code = 0 if aggregate == PASS else 1 if aggregate == FAIL else 2
        if mode == "release" and not publication["published"] and aggregate == PASS:
            exit_code = 2
        return manifest, exit_code

    def _input_records(
        self,
        loaded: LoadedInputs,
        *,
        docx_path: Path | None,
        markdown_path: Path | None,
    ) -> tuple[list[dict[str, str]], dict[str, str]]:
        values: list[tuple[str, Path | None]] = [
            ("docx", docx_path),
            ("markdown", markdown_path),
            ("contract", loaded.contract_path),
            ("coverage_plan", loaded.coverage_path),
            ("visual_attestation", loaded.attestation_path),
        ]
        records: list[dict[str, str]] = []
        hashes: dict[str, str] = {}
        for kind, path in values:
            if path is None or not path.is_file():
                continue
            digest = sha256_file(path)
            hashes[kind] = digest
            records.append(
                {
                    "kind": kind,
                    "staged_path": str(path.resolve()),
                    "actual_filename": path.name,
                    "sha256": digest,
                }
            )
        return records, hashes

    @staticmethod
    def _read_markdown(path: Path | None) -> str | None:
        if path is None or not path.is_file():
            return None
        try:
            return path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            return None

    @staticmethod
    def _check_policy(contract: dict[str, Any]) -> CheckResult:
        policy = contract["policy_identity"]
        valid = bool(policy.get("framework_version") and policy.get("source_policy_version"))
        return _result(
            "policy.current",
            PASS if valid else UNKNOWN,
            "policy.identity_recorded" if valid else "policy.identity_unavailable",
        )

    @staticmethod
    def _check_profile(contract: dict[str, Any]) -> CheckResult:
        profile = contract["profile"]
        digest = profile.get("sha256", "")
        valid = bool(profile.get("id") and profile.get("version") and re.fullmatch(r"[0-9a-fA-F]{64}", digest))
        return _result(
            "profile.current",
            PASS if valid else UNKNOWN,
            "profile.identity_recorded" if valid else "profile.identity_unavailable",
        )

    @staticmethod
    def _check_input_hashes(
        contract: dict[str, Any], docx_path: Path | None, markdown_path: Path | None
    ) -> CheckResult:
        paths = {"docx": docx_path, "markdown": markdown_path}
        configured = set(contract["artifact"]["formats"])
        unexpected = [
            kind
            for kind, path in paths.items()
            if path is not None and path.is_file() and kind not in configured
        ]
        if unexpected:
            return _result(
                "input.hashes",
                FAIL,
                "input.unconfigured_artifact",
                measurements={"unexpected_artifact_count": len(unexpected)},
            )
        missing = [
            kind
            for kind in contract["artifact"]["formats"]
            if kind in paths and (paths[kind] is None or not paths[kind].is_file())
        ]
        if missing:
            return _result(
                "input.hashes",
                UNKNOWN,
                "input.required_artifact_missing",
                measurements={"missing_artifact_count": len(missing)},
            )
        return _result("input.hashes", PASS, "input.hashes_recorded")

    @staticmethod
    def _check_filenames(
        contract: dict[str, Any], docx_path: Path | None, markdown_path: Path | None
    ) -> CheckResult:
        pattern = re.compile(contract["artifact"]["filename_pattern"])
        paths = [path for path in (docx_path, markdown_path) if path is not None and path.is_file()]
        if not paths:
            return _result("filename.actual", UNKNOWN, "filename.no_artifact")
        encoded = sum(1 for path in paths if re.search(r"%[0-9a-fA-F]{2}", path.name))
        mismatched = sum(1 for path in paths if pattern.fullmatch(path.name) is None)
        if encoded or mismatched:
            return _result(
                "filename.actual",
                FAIL,
                "filename.contract_mismatch",
                measurements={"url_encoded_count": encoded, "pattern_mismatch_count": mismatched},
            )
        return _result("filename.actual", PASS, "filename.matches_contract")

    @staticmethod
    def _check_package(
        contract: dict[str, Any], docx_path: Path | None, inspector: DocxInspector | None
    ) -> CheckResult:
        if "docx" not in contract["artifact"]["formats"]:
            return _result("docx.package", PASS, "docx.not_configured")
        if docx_path is None or not docx_path.is_file() or inspector is None:
            return _result("docx.package", UNKNOWN, "docx.missing")
        valid, problems = inspector.package_check(contract["docx"]["required_parts"])
        return _result(
            "docx.package",
            PASS if valid else FAIL,
            "docx.package_valid" if valid else "docx.package_invalid",
            measurements={"problem_count": len(problems)},
        )

    @staticmethod
    def _inspector_ready(inspector: DocxInspector | None) -> bool:
        return bool(inspector and not inspector.package_error and inspector.document is not None)

    def _check_styles(self, contract: dict[str, Any], inspector: DocxInspector | None) -> CheckResult:
        if not self._inspector_ready(inspector):
            return _result("docx.styles", UNKNOWN, "docx.structure_unavailable")
        mismatches = 0
        for rule in contract["docx"]["style_rules"]:
            mismatches += len(style_mismatches(inspector.styles.get(rule["paragraph_style"]), rule))
        return _result(
            "docx.styles",
            PASS if mismatches == 0 else FAIL,
            "docx.styles_match" if mismatches == 0 else "docx.styles_mismatch",
            measurements={"mismatch_count": mismatches},
        )

    def _check_native_lists(self, contract: dict[str, Any], inspector: DocxInspector | None) -> CheckResult:
        if not self._inspector_ready(inspector):
            return _result("docx.native_lists", UNKNOWN, "docx.structure_unavailable")
        violations = 0
        matched = 0
        for rule in contract["docx"]["list_rules"]:
            paragraphs = inspector.paragraphs_for_style(rule["paragraph_style"])
            matched += len(paragraphs)
            if not paragraphs:
                violations += 1
            for paragraph in paragraphs:
                num_id = inspector.effective_num_id(paragraph)
                if (
                    num_id is None
                    or num_id not in inspector.numbering_ids
                    or inspector.numbering_map.get(num_id) not in inspector.abstract_numbering_ids
                    or "bullet"
                    not in inspector.abstract_numbering_formats.get(
                        inspector.numbering_map.get(num_id, -1), set()
                    )
                ):
                    violations += 1
        return _result(
            "docx.native_lists",
            PASS if violations == 0 else FAIL,
            "docx.native_lists_valid" if violations == 0 else "docx.native_lists_invalid",
            measurements={"paragraph_count": matched, "violation_count": violations},
        )

    def _check_indentation(self, contract: dict[str, Any], inspector: DocxInspector | None) -> CheckResult:
        if not self._inspector_ready(inspector):
            return _result("docx.indentation", UNKNOWN, "docx.structure_unavailable")
        violations = 0
        for rule in contract["docx"]["list_rules"]:
            tolerance = rule.get("tolerance_twips", 0)
            for paragraph in inspector.paragraphs_for_style(rule["paragraph_style"]):
                left, hanging = inspector.effective_indentation(paragraph)
                if left is None or abs(left - rule["left_indent_twips"]) > tolerance:
                    violations += 1
                if hanging is None or abs(hanging - rule["hanging_indent_twips"]) > tolerance:
                    violations += 1
        return _result(
            "docx.indentation",
            PASS if violations == 0 else FAIL,
            "docx.indentation_valid" if violations == 0 else "docx.indentation_invalid",
            measurements={"violation_count": violations},
        )

    def _check_margins(self, contract: dict[str, Any], inspector: DocxInspector | None) -> CheckResult:
        if not self._inspector_ready(inspector):
            return _result("docx.margins", UNKNOWN, "docx.structure_unavailable")
        expected = contract["docx"]["layout_rules"].get("section_margins", {})
        tolerance = contract["docx"]["layout_rules"].get("margin_tolerance_twips", 0)
        if expected and not inspector.sections:
            return _result("docx.margins", FAIL, "docx.section_margins_missing")
        violations = 0
        for section in inspector.sections:
            for key, expected_value in expected.items():
                actual = getattr(section, key)
                if actual is None or abs(actual - expected_value) > tolerance:
                    violations += 1
        return _result(
            "docx.margins",
            PASS if violations == 0 else FAIL,
            "docx.margins_valid" if violations == 0 else "docx.margins_invalid",
            measurements={"section_count": len(inspector.sections), "violation_count": violations},
        )

    def _check_breaks(self, contract: dict[str, Any], inspector: DocxInspector | None) -> CheckResult:
        if not self._inspector_ready(inspector):
            return _result("docx.breaks", UNKNOWN, "docx.structure_unavailable")
        rules = contract["docx"]["break_rules"]
        allowed = set(rules.get("allowed_paragraph_styles", []))
        violations = 0
        manual_count = 0
        forced_count = 0
        for paragraph in inspector.paragraphs:
            manual_count += paragraph.manual_page_breaks
            page_break_before = inspector.effective_page_break_before(paragraph)
            forced_count += int(page_break_before)
            if paragraph.manual_page_breaks:
                if rules["manual_page_breaks"] == "forbid":
                    violations += paragraph.manual_page_breaks
                elif rules["manual_page_breaks"] == "allow_configured" and paragraph.style_id not in allowed:
                    violations += paragraph.manual_page_breaks
            if page_break_before:
                if rules["page_break_before"] == "forbid":
                    violations += 1
                elif rules["page_break_before"] == "allow_configured" and paragraph.style_id not in allowed:
                    violations += 1
        return _result(
            "docx.breaks",
            PASS if violations == 0 else FAIL,
            "docx.breaks_valid" if violations == 0 else "docx.breaks_invalid",
            measurements={
                "manual_page_break_count": manual_count,
                "page_break_before_count": forced_count,
                "violation_count": violations,
            },
        )

    def _check_keep_next(self, contract: dict[str, Any], inspector: DocxInspector | None) -> CheckResult:
        if not self._inspector_ready(inspector):
            return _result("docx.keep_next", UNKNOWN, "docx.structure_unavailable")
        violations = 0
        for rule in contract["docx"]["keep_next_rules"]:
            paragraphs = inspector.paragraphs_for_style(rule["paragraph_style"])
            if not paragraphs:
                violations += 1
                continue
            if rule["required"]:
                violations += sum(not inspector.effective_keep_next(item) for item in paragraphs)
        return _result(
            "docx.keep_next",
            PASS if violations == 0 else FAIL,
            "docx.keep_next_valid" if violations == 0 else "docx.keep_next_invalid",
            measurements={"violation_count": violations},
        )

    def _check_content_parity(
        self,
        contract: dict[str, Any],
        inspector: DocxInspector | None,
        markdown_path: Path | None,
        markdown_text: str | None,
    ) -> CheckResult:
        if not self._inspector_ready(inspector):
            return _result("content.markdown_docx_parity", UNKNOWN, "content.docx_text_unavailable")
        content = contract["content"]
        docx_text = inspector.normalized_text()
        missing_sections = sum(
            1 for section in content["required_sections"] if _normalized(section) not in docx_text
        )
        parity = content["markdown_docx_parity"]
        if parity["required"] and (markdown_path is None or markdown_text is None):
            return _result(
                "content.markdown_docx_parity",
                UNKNOWN,
                "content.markdown_unavailable",
                measurements={"missing_section_count": missing_sections},
            )
        missing_anchors = 0
        if parity["required"]:
            normalized_markdown = _normalized(markdown_text or "")
            for anchor in parity["anchors"]:
                normalized_anchor = _normalized(anchor)
                if normalized_anchor not in docx_text or normalized_anchor not in normalized_markdown:
                    missing_anchors += 1
        violations = missing_sections + missing_anchors
        return _result(
            "content.markdown_docx_parity",
            PASS if violations == 0 else FAIL,
            "content.parity_valid" if violations == 0 else "content.parity_invalid",
            measurements={
                "missing_section_count": missing_sections,
                "missing_anchor_count": missing_anchors,
            },
        )

    def _check_employment_coverage(
        self,
        contract: dict[str, Any],
        coverage: dict[str, Any] | None,
        inspector: DocxInspector | None,
    ) -> CheckResult:
        required = contract["content"]["employment_coverage"]["required"]
        if not required and coverage is None:
            return _result("content.employment_coverage", PASS, "coverage.not_required")
        if coverage is None:
            return _result("content.employment_coverage", UNKNOWN, "coverage.plan_unavailable")
        if not self._inspector_ready(inspector):
            return _result("content.employment_coverage", UNKNOWN, "coverage.docx_text_unavailable")
        text = inspector.normalized_text()
        violations = 0
        excluded = 0
        for role in coverage["roles"]:
            if role["disposition"] == "excluded":
                excluded += 1
                if not role.get("reason"):
                    violations += 1
                continue
            label = role.get("display_label") or role.get("resume_section")
            if not label or _normalized(label) not in text:
                violations += 1
        return _result(
            "content.employment_coverage",
            PASS if violations == 0 else FAIL,
            "coverage.complete" if violations == 0 else "coverage.incomplete",
            measurements={
                "role_count": len(coverage["roles"]),
                "excluded_role_count": excluded,
                "violation_count": violations,
            },
        )

    def _check_experience_duration(
        self,
        contract: dict[str, Any],
        coverage: dict[str, Any] | None,
        inspector: DocxInspector | None,
    ) -> CheckResult:
        required = contract["content"]["experience_duration"]["required"]
        if not required and coverage is None:
            return _result("content.experience_duration", PASS, "experience.not_required")
        if coverage is None:
            return _result("content.experience_duration", UNKNOWN, "experience.plan_unavailable")
        claim = coverage["experience_claim"]
        if not claim["included"]:
            return _result(
                "content.experience_duration",
                FAIL if required else PASS,
                "experience.claim_missing" if required else "experience.claim_not_included",
            )
        if not self._inspector_ready(inspector):
            return _result("content.experience_duration", UNKNOWN, "experience.docx_text_unavailable")
        method = claim.get("calculation_method")
        configured_method = contract["content"]["experience_duration"]["calculation_method"]
        try:
            as_of_date = date.fromisoformat(coverage["as_of_date"])
            if method != configured_method:
                raise ValueError("coverage calculation method differs from contract")
            if method == "union_of_calendar_intervals":
                years = self._union_years(claim["qualifying_intervals"], as_of_date)
                expected_label = claim["rendered_label"]
                sufficient = years + 1e-9 >= float(claim["minimum_years"])
            elif method == "elapsed_full_years_from_start_date":
                years = self._elapsed_full_years(
                    date.fromisoformat(claim["anchor_start_date"]), as_of_date
                )
                expected_label = f"{years}+ years"
                sufficient = (
                    float(claim["minimum_years"]) == years
                    and claim["rendered_label"] == expected_label
                )
            else:
                raise ValueError("unsupported experience calculation method")
        except (TypeError, ValueError, KeyError):
            return _result("content.experience_duration", FAIL, "experience.interval_invalid")
        label_present = _normalized(expected_label) in inspector.normalized_text()
        valid = label_present and sufficient
        return _result(
            "content.experience_duration",
            PASS if valid else FAIL,
            "experience.valid" if valid else "experience.mismatch",
            measurements={
                "calculated_years": round(years, 4),
                "minimum_years": float(claim["minimum_years"]),
                "label_present": label_present,
            },
        )

    @staticmethod
    def _elapsed_full_years(start_date: date, as_of_date: date) -> int:
        if as_of_date < start_date:
            raise ValueError("experience anchor is after the as-of date")
        anniversary_pending = (as_of_date.month, as_of_date.day) < (
            start_date.month,
            start_date.day,
        )
        return as_of_date.year - start_date.year - int(anniversary_pending)

    @staticmethod
    def _union_years(intervals: list[dict[str, Any]], as_of_date: date) -> float:
        parsed: list[tuple[date, date]] = []
        for interval in intervals:
            start = date.fromisoformat(interval["start_date"])
            raw_end = interval.get("end_date")
            end = as_of_date if interval.get("current") or raw_end is None else date.fromisoformat(raw_end)
            if end < start:
                raise ValueError("interval ends before it starts")
            parsed.append((start, end))
        parsed.sort()
        merged: list[list[date]] = []
        for start, end in parsed:
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            elif end > merged[-1][1]:
                merged[-1][1] = end
        total_days = sum((end - start).days for start, end in merged)
        return total_days / 365.2425

    def _render(
        self, *, contract: dict[str, Any], docx_path: Path | None, render_dir: Path
    ) -> RenderOutcome:
        if not contract["render"]["required"]:
            return RenderOutcome(PASS, "renderer.not_required")
        if docx_path is None or not docx_path.is_file():
            return RenderOutcome(UNKNOWN, "renderer.input_unavailable")
        return self.renderer.render(
            docx_path,
            render_dir,
            contract["render"]["supported_renderers"],
        )

    @staticmethod
    def _check_render_available(contract: dict[str, Any], outcome: RenderOutcome) -> CheckResult:
        if not contract["render"]["required"]:
            return _result("render.available", PASS, "renderer.not_required")
        return _result("render.available", outcome.status, outcome.diagnostic_code, outcome.message)

    @staticmethod
    def _check_render_pages(contract: dict[str, Any], outcome: RenderOutcome) -> CheckResult:
        if not contract["render"]["required"]:
            return _result("render.pages", PASS, "render.pages_not_required")
        if outcome.status != PASS:
            return _result("render.pages", UNKNOWN, "render.pages_unavailable")
        valid = bool(outcome.pages)
        return _result(
            "render.pages",
            PASS if valid else UNKNOWN,
            "render.pages_created" if valid else "render.pages_unavailable",
            measurements={"page_count": len(outcome.pages)},
            evidence_paths=tuple(str(page.path.resolve()) for page in outcome.pages),
        )

    @staticmethod
    def _check_render_whitespace(contract: dict[str, Any], outcome: RenderOutcome) -> CheckResult:
        render = contract["render"]
        if not render["required"]:
            return _result("render.whitespace", PASS, "render.whitespace_not_required")
        if outcome.status != PASS or not outcome.pages:
            return _result("render.whitespace", UNKNOWN, "render.geometry_unavailable")
        pages = list(outcome.pages)
        checked = pages if render.get("final_page_whitespace_check", False) else pages[:-1]
        threshold = render["max_non_final_bottom_whitespace_ratio"]
        violations = sum(page.bottom_whitespace_ratio > threshold for page in checked)
        maximum = max((page.bottom_whitespace_ratio for page in checked), default=0.0)
        return _result(
            "render.whitespace",
            PASS if violations == 0 else FAIL,
            "render.whitespace_valid" if violations == 0 else "render.whitespace_excessive",
            measurements={
                "checked_page_count": len(checked),
                "violation_count": violations,
                "maximum_bottom_whitespace_ratio": round(maximum, 8),
            },
        )

    @staticmethod
    def _check_blank_pages(contract: dict[str, Any], outcome: RenderOutcome) -> CheckResult:
        render = contract["render"]
        if not render["required"]:
            return _result("render.blank_pages", PASS, "render.blank_pages_not_required")
        if outcome.status != PASS or not outcome.pages:
            return _result("render.blank_pages", UNKNOWN, "render.geometry_unavailable")
        threshold = render["nearly_blank_page_max_ink_ratio"]
        violations = sum(page.ink_ratio <= threshold for page in outcome.pages)
        return _result(
            "render.blank_pages",
            PASS if violations == 0 else FAIL,
            "render.blank_pages_absent" if violations == 0 else "render.blank_pages_detected",
            measurements={"nearly_blank_page_count": violations},
        )

    @staticmethod
    def _check_visual_review(
        contract: dict[str, Any],
        attestation: dict[str, Any] | None,
        outcome: RenderOutcome,
        artifact_hash: str | None,
    ) -> CheckResult:
        if not contract["visual_review"]["required"]:
            return _result("visual.every_page_review", PASS, "visual.review_not_required")
        if outcome.status != PASS or not outcome.pages:
            return _result("visual.every_page_review", UNKNOWN, "visual.pages_unavailable")
        if attestation is None:
            return _result("visual.every_page_review", UNKNOWN, "visual.attestation_missing")
        expected_pages = list(range(1, len(outcome.pages) + 1))
        valid = (
            artifact_hash is not None
            and attestation["artifact_sha256"].casefold() == artifact_hash.casefold()
            and attestation["page_count"] == len(outcome.pages)
            and sorted(set(attestation["reviewed_pages"])) == expected_pages
        )
        return _result(
            "visual.every_page_review",
            PASS if valid else FAIL,
            "visual.attestation_valid" if valid else "visual.attestation_invalid",
            measurements={
                "rendered_page_count": len(outcome.pages),
                "reviewed_page_count": len(set(attestation["reviewed_pages"])),
            },
        )

    @staticmethod
    def _publication_pairs(
        docx_path: Path | None,
        markdown_path: Path | None,
        output_docx: Path | None,
        output_markdown: Path | None,
    ) -> list[tuple[str, Path, Path]]:
        pairs: list[tuple[str, Path, Path]] = []
        if docx_path is not None and output_docx is not None:
            pairs.append(("docx", docx_path, output_docx))
        if markdown_path is not None and output_markdown is not None:
            pairs.append(("markdown", markdown_path, output_markdown))
        if not pairs:
            raise OSError("no publication targets were provided")
        source_paths = {
            path.resolve() for path in (docx_path, markdown_path) if path is not None
        }
        target_paths = [target.resolve() for _, _, target in pairs]
        if len(target_paths) != len(set(target_paths)):
            raise OSError("final artifact paths must be unique")
        if any(target in source_paths for target in target_paths):
            raise OSError("final artifact paths must not overlap staged inputs")
        return pairs

    @staticmethod
    def _begin_atomic_publish(
        pairs: list[tuple[str, Path, Path]], overwrite_policy: str
    ) -> PublicationTransaction:
        prepared: list[tuple[Path, Path, Path | None]] = []
        try:
            for _, source, target in pairs:
                if source.resolve() == target.resolve():
                    raise OSError("staged and final paths must differ")
                if not source.is_file() or not target.parent.is_dir():
                    raise OSError("publication source or target directory is unavailable")
                if target.exists() and overwrite_policy == "forbid":
                    raise OSError("target exists and overwrite is forbidden")
                descriptor, temporary_name = tempfile.mkstemp(
                    prefix=f".{target.name}.", suffix=".publish", dir=target.parent
                )
                os.close(descriptor)
                temporary = Path(temporary_name)
                shutil.copyfile(source, temporary)
                # Windows requires a writable descriptor for fsync.
                with temporary.open("rb+") as stream:
                    os.fsync(stream.fileno())
                backup = None
                if target.exists():
                    descriptor, backup_name = tempfile.mkstemp(
                        prefix=f".{target.name}.", suffix=".backup", dir=target.parent
                    )
                    os.close(descriptor)
                    backup = Path(backup_name)
                    shutil.copyfile(target, backup)
                prepared.append((temporary, target, backup))
            transaction = PublicationTransaction(prepared)
            transaction.replace()
            return transaction
        except OSError:
            for temporary, _, backup in prepared:
                for path in (temporary, backup):
                    if path and path.exists():
                        try:
                            path.unlink()
                        except OSError:
                            pass
            raise

    @staticmethod
    def _atomic_write_json(path: Path, value: dict[str, Any]) -> None:
        if not path.parent.is_dir():
            raise OSError("manifest output directory is unavailable")
        descriptor, temporary_name = tempfile.mkstemp(
            prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
        )
        temporary = Path(temporary_name)
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as stream:
                json.dump(value, stream, indent=2, sort_keys=True, ensure_ascii=False)
                stream.write("\n")
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temporary, path)
        finally:
            if temporary.exists():
                temporary.unlink()

    @staticmethod
    def _manifest_id(
        contract: dict[str, Any], mode: str, records: list[dict[str, str]]
    ) -> str:
        identity = {
            "contract_id": contract["contract_id"],
            "mode": mode,
            "inputs": [(record["kind"], record["sha256"]) for record in records],
        }
        encoded = json.dumps(identity, sort_keys=True, separators=(",", ":")).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()
