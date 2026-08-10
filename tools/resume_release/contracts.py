"""Strict, dependency-free loading for the public JSON contracts."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any

from .constants import (
    ATTESTATION_SCHEMA_VERSION,
    CHECK_IDS,
    CONTRACT_SCHEMA_VERSION,
    COVERAGE_SCHEMA_VERSION,
)


class ContractError(ValueError):
    """Raised when invocation input cannot enter artifact validation."""


def load_json(path: Path, label: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ContractError(f"{label} is unreadable: {exc.strerror or exc}") from exc
    except json.JSONDecodeError as exc:
        raise ContractError(f"{label} is not valid JSON at line {exc.lineno}") from exc
    if not isinstance(value, dict):
        raise ContractError(f"{label} must be a JSON object")
    return value


def _require_object(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ContractError(f"{label} must be an object")
    return value


def _require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise ContractError(f"{label} must be a non-empty string")
    return value


def _require_list(value: Any, label: str) -> list[Any]:
    if not isinstance(value, list):
        raise ContractError(f"{label} must be an array")
    return value


@dataclass(frozen=True)
class LoadedInputs:
    contract_path: Path
    contract: dict[str, Any]
    coverage_path: Path | None
    coverage: dict[str, Any] | None
    attestation_path: Path | None
    attestation: dict[str, Any] | None


def load_contract(path: Path) -> dict[str, Any]:
    contract = load_json(path, "release contract")
    if contract.get("schema_version") != CONTRACT_SCHEMA_VERSION:
        raise ContractError(
            f"unsupported release contract schema_version; expected {CONTRACT_SCHEMA_VERSION}"
        )
    for key in (
        "contract_id",
        "profile",
        "policy_identity",
        "required_checks",
        "artifact",
        "docx",
        "content",
        "render",
        "visual_review",
        "publication",
        "privacy",
    ):
        if key not in contract:
            raise ContractError(f"release contract is missing {key}")
    _require_string(contract["contract_id"], "contract_id")
    profile = _require_object(contract["profile"], "profile")
    for key in ("id", "version", "sha256"):
        _require_string(profile.get(key), f"profile.{key}")
    if re.fullmatch(r"[0-9a-fA-F]{64}", profile["sha256"]) is None:
        raise ContractError("profile.sha256 must be a SHA-256 value")
    policy = _require_object(contract["policy_identity"], "policy_identity")
    for key in ("framework_version", "source_policy_version"):
        _require_string(policy.get(key), f"policy_identity.{key}")
    if "source_policy_sha256" in policy and re.fullmatch(
        r"[0-9a-fA-F]{64}", _require_string(policy["source_policy_sha256"], "policy_identity.source_policy_sha256")
    ) is None:
        raise ContractError("policy_identity.source_policy_sha256 must be a SHA-256 value")
    checks = _require_list(contract["required_checks"], "required_checks")
    if not checks or len(checks) != len(set(checks)):
        raise ContractError("required_checks must be non-empty and unique")
    unknown = [check for check in checks if check not in CHECK_IDS]
    if unknown:
        raise ContractError("required_checks contains an unsupported check identifier")
    if set(checks) != set(CHECK_IDS):
        raise ContractError("required_checks must include every stable local-release check")
    artifact = _require_object(contract["artifact"], "artifact")
    formats = _require_list(artifact.get("formats"), "artifact.formats")
    if not formats or any(value not in {"docx", "pdf", "markdown"} for value in formats):
        raise ContractError("artifact.formats contains an unsupported format")
    if "pdf" in formats:
        raise ContractError("validator version 1.2.0 accepts staged DOCX and Markdown, not staged PDF")
    if "docx" not in formats:
        raise ContractError("validator version 1.2.0 requires DOCX in artifact.formats")
    pattern = _require_string(artifact.get("filename_pattern"), "artifact.filename_pattern")
    try:
        re.compile(pattern)
    except re.error as exc:
        raise ContractError("artifact.filename_pattern is not a valid regular expression") from exc
    for key in ("forbid_url_encoded_filename", "require_delivery_name_receipt"):
        if key in artifact and not isinstance(artifact[key], bool):
            raise ContractError(f"artifact.{key} must be a boolean")
    for key in ("docx", "content", "render", "visual_review", "publication", "privacy"):
        _require_object(contract[key], key)
    docx = contract["docx"]
    for key in ("required_parts", "style_rules", "list_rules", "layout_rules", "break_rules", "keep_next_rules"):
        if key not in docx:
            raise ContractError(f"docx is missing {key}")
    for key in ("required_parts", "style_rules", "list_rules", "keep_next_rules"):
        _require_list(docx[key], f"docx.{key}")
    if not docx["required_parts"] or any(
        not isinstance(part, str) or not part for part in docx["required_parts"]
    ):
        raise ContractError("docx.required_parts must contain non-empty strings")
    for index, raw_rule in enumerate(docx["style_rules"]):
        rule = _require_object(raw_rule, f"docx.style_rules[{index}]")
        _require_string(rule.get("paragraph_style"), f"docx.style_rules[{index}].paragraph_style")
    for index, raw_rule in enumerate(docx["list_rules"]):
        rule = _require_object(raw_rule, f"docx.list_rules[{index}]")
        for key in ("paragraph_style", "native_numbering_required", "left_indent_twips", "hanging_indent_twips"):
            if key not in rule:
                raise ContractError(f"docx.list_rules[{index}] is missing {key}")
        _require_string(rule["paragraph_style"], f"docx.list_rules[{index}].paragraph_style")
        if rule["native_numbering_required"] is not True:
            raise ContractError("docx.list_rules native_numbering_required must be true")
        if any(
            not isinstance(rule[key], int) or rule[key] < 0
            for key in ("left_indent_twips", "hanging_indent_twips")
        ):
            raise ContractError("docx.list_rules indentation values must be non-negative integers")
    for index, raw_rule in enumerate(docx["keep_next_rules"]):
        rule = _require_object(raw_rule, f"docx.keep_next_rules[{index}]")
        _require_string(rule.get("paragraph_style"), f"docx.keep_next_rules[{index}].paragraph_style")
        if not isinstance(rule.get("required"), bool):
            raise ContractError(f"docx.keep_next_rules[{index}].required must be a boolean")
    layout = _require_object(docx["layout_rules"], "docx.layout_rules")
    if "section_margins" in layout:
        margins = _require_object(layout["section_margins"], "docx.layout_rules.section_margins")
        if any(not isinstance(value, int) or value < 0 for value in margins.values()):
            raise ContractError("docx section margins must be non-negative integers")
    breaks = _require_object(docx["break_rules"], "docx.break_rules")
    if breaks.get("manual_page_breaks") not in {"forbid", "allow_configured", "allow"}:
        raise ContractError("docx.break_rules.manual_page_breaks is invalid")
    if breaks.get("page_break_before") not in {"forbid", "allow_configured", "allow"}:
        raise ContractError("docx.break_rules.page_break_before is invalid")
    content = contract["content"]
    for key in ("required_sections", "markdown_docx_parity", "employment_coverage", "experience_duration"):
        if key not in content:
            raise ContractError(f"content is missing {key}")
    _require_list(content["required_sections"], "content.required_sections")
    if any(not isinstance(value, str) or not value for value in content["required_sections"]):
        raise ContractError("content.required_sections must contain non-empty strings")
    parity = _require_object(content["markdown_docx_parity"], "content.markdown_docx_parity")
    if not isinstance(parity.get("required"), bool):
        raise ContractError("content.markdown_docx_parity.required must be a boolean")
    anchors = _require_list(parity.get("anchors"), "content.markdown_docx_parity.anchors")
    if any(not isinstance(value, str) or not value for value in anchors):
        raise ContractError("content.markdown_docx_parity.anchors must contain non-empty strings")
    coverage_rule = _require_object(content["employment_coverage"], "content.employment_coverage")
    experience_rule = _require_object(content["experience_duration"], "content.experience_duration")
    if not isinstance(coverage_rule.get("required"), bool) or not isinstance(experience_rule.get("required"), bool):
        raise ContractError("content required flags must be booleans")
    allowed_dispositions = _require_list(
        coverage_rule.get("allowed_dispositions"), "content.employment_coverage.allowed_dispositions"
    )
    if set(allowed_dispositions) != {"detailed", "compressed", "excluded"}:
        raise ContractError("content.employment_coverage.allowed_dispositions is incomplete")
    if experience_rule.get("calculation_method") not in {
        "union_of_calendar_intervals",
        "elapsed_full_years_from_start_date",
    }:
        raise ContractError("content.experience_duration.calculation_method is unsupported")
    render = contract["render"]
    for key in (
        "required",
        "supported_renderers",
        "page_images_required",
        "max_non_final_bottom_whitespace_ratio",
        "nearly_blank_page_max_ink_ratio",
    ):
        if key not in render:
            raise ContractError(f"render is missing {key}")
    if not isinstance(render["required"], bool):
        raise ContractError("render.required must be a boolean")
    if not isinstance(render["page_images_required"], bool):
        raise ContractError("render.page_images_required must be a boolean")
    renderers = _require_list(render["supported_renderers"], "render.supported_renderers")
    if not renderers:
        raise ContractError("render.supported_renderers must not be empty")
    for key in ("max_non_final_bottom_whitespace_ratio", "nearly_blank_page_max_ink_ratio"):
        value = render[key]
        if not isinstance(value, (int, float)) or not 0 <= value <= 1:
            raise ContractError(f"render.{key} must be between 0 and 1")
    visual = contract["visual_review"]
    if not isinstance(visual.get("required"), bool) or visual.get("scope") != "every_page":
        raise ContractError("visual_review must define a boolean required flag and every_page scope")
    if (
        "attestation_schema_version" in visual
        and visual["attestation_schema_version"] != ATTESTATION_SCHEMA_VERSION
    ):
        raise ContractError("visual_review.attestation_schema_version is unsupported")
    if contract["publication"].get("atomic") is not True:
        raise ContractError("publication.atomic must be true")
    if contract["publication"].get("final_path_on_pass_only") is not True:
        raise ContractError("publication.final_path_on_pass_only must be true")
    if contract["publication"].get("overwrite_policy") not in {"forbid", "replace_on_pass"}:
        raise ContractError("publication.overwrite_policy is invalid")
    if contract["privacy"].get("include_full_text") is not False:
        raise ContractError("privacy.include_full_text must be false")
    return contract


def load_coverage(path: Path) -> dict[str, Any]:
    coverage = load_json(path, "employment coverage plan")
    if coverage.get("schema_version") != COVERAGE_SCHEMA_VERSION:
        raise ContractError(
            f"unsupported employment coverage schema_version; expected {COVERAGE_SCHEMA_VERSION}"
        )
    for key in ("plan_id", "artifact_id", "as_of_date", "source_identity", "roles", "experience_claim"):
        if key not in coverage:
            raise ContractError(f"employment coverage plan is missing {key}")
    try:
        date.fromisoformat(_require_string(coverage["as_of_date"], "as_of_date"))
    except ValueError as exc:
        raise ContractError("as_of_date must be an ISO date") from exc
    source_identity = _require_object(coverage["source_identity"], "source_identity")
    _require_string(source_identity.get("policy_version"), "source_identity.policy_version")
    source_refs = _require_list(source_identity.get("source_refs"), "source_identity.source_refs")
    if not source_refs:
        raise ContractError("source_identity.source_refs must not be empty")
    roles = _require_list(coverage["roles"], "roles")
    if not roles:
        raise ContractError("roles must contain at least one role")
    role_ids: set[str] = set()
    role_start_dates: dict[str, str] = {}
    for index, raw_role in enumerate(roles):
        role = _require_object(raw_role, f"roles[{index}]")
        role_id = _require_string(role.get("role_id"), f"roles[{index}].role_id")
        if role_id in role_ids:
            raise ContractError("role_id values must be unique")
        role_ids.add(role_id)
        refs = _require_list(role.get("source_refs"), f"roles[{index}].source_refs")
        if not refs or any(not isinstance(ref, str) or not ref for ref in refs):
            raise ContractError(f"roles[{index}].source_refs must be non-empty strings")
        disposition = role.get("disposition")
        if disposition not in {"detailed", "compressed", "excluded"}:
            raise ContractError(f"roles[{index}].disposition is invalid")
        if disposition == "excluded":
            _require_string(role.get("reason"), f"roles[{index}].reason")
        else:
            _require_string(role.get("resume_section"), f"roles[{index}].resume_section")
        interval = _require_object(role.get("employment_interval"), f"roles[{index}].employment_interval")
        try:
            date.fromisoformat(
                _require_string(interval.get("start_date"), f"roles[{index}].employment_interval.start_date")
            )
            if interval.get("end_date") is not None:
                date.fromisoformat(
                    _require_string(interval.get("end_date"), f"roles[{index}].employment_interval.end_date")
                )
        except ValueError as exc:
            raise ContractError(f"roles[{index}].employment_interval contains an invalid date") from exc
        role_start_dates[role_id] = interval["start_date"]
    claim = _require_object(coverage["experience_claim"], "experience_claim")
    if not isinstance(claim.get("included"), bool):
        raise ContractError("experience_claim.included must be a boolean")
    if claim["included"]:
        for key in ("rendered_label", "minimum_years", "calculation_method"):
            if key not in claim:
                raise ContractError(f"experience_claim is missing {key}")
        _require_string(claim["rendered_label"], "experience_claim.rendered_label")
        if not isinstance(claim["minimum_years"], (int, float)) or claim["minimum_years"] < 0:
            raise ContractError("experience_claim.minimum_years must be non-negative")
        method = claim["calculation_method"]
        if method not in {
            "union_of_calendar_intervals",
            "elapsed_full_years_from_start_date",
        }:
            raise ContractError("experience_claim.calculation_method is unsupported")
        if method == "union_of_calendar_intervals":
            qualifying = _require_list(claim.get("qualifying_intervals"), "experience_claim.qualifying_intervals")
            if not qualifying:
                raise ContractError("experience_claim.qualifying_intervals must not be empty")
            for index, raw_interval in enumerate(qualifying):
                interval = _require_object(raw_interval, f"experience_claim.qualifying_intervals[{index}]")
                try:
                    date.fromisoformat(
                        _require_string(interval.get("start_date"), f"experience_claim.qualifying_intervals[{index}].start_date")
                    )
                    if interval.get("end_date") is not None:
                        date.fromisoformat(
                            _require_string(interval.get("end_date"), f"experience_claim.qualifying_intervals[{index}].end_date")
                        )
                except ValueError as exc:
                    raise ContractError("experience_claim.qualifying_intervals contains an invalid date") from exc
        else:
            anchor_role_id = _require_string(
                claim.get("anchor_role_id"), "experience_claim.anchor_role_id"
            )
            if anchor_role_id not in role_ids:
                raise ContractError("experience_claim.anchor_role_id must reference a coverage role")
            try:
                anchor_start_date = _require_string(
                    claim.get("anchor_start_date"), "experience_claim.anchor_start_date"
                )
                date.fromisoformat(anchor_start_date)
            except ValueError as exc:
                raise ContractError("experience_claim.anchor_start_date is invalid") from exc
            if role_start_dates[anchor_role_id] != anchor_start_date:
                raise ContractError(
                    "experience_claim.anchor_start_date must match the anchor role start date"
                )
    return coverage


def load_attestation(path: Path) -> dict[str, Any]:
    attestation = load_json(path, "visual-review attestation")
    if attestation.get("schema_version") != ATTESTATION_SCHEMA_VERSION:
        raise ContractError(
            f"unsupported visual attestation schema_version; expected {ATTESTATION_SCHEMA_VERSION}"
        )
    _require_string(attestation.get("artifact_sha256"), "artifact_sha256")
    if re.fullmatch(r"[0-9a-fA-F]{64}", attestation["artifact_sha256"]) is None:
        raise ContractError("artifact_sha256 must be a SHA-256 value")
    page_count = attestation.get("page_count")
    if not isinstance(page_count, int) or page_count < 1:
        raise ContractError("page_count must be a positive integer")
    reviewed = _require_list(attestation.get("reviewed_pages"), "reviewed_pages")
    if any(not isinstance(page, int) or page < 1 for page in reviewed):
        raise ContractError("reviewed_pages must contain positive integers")
    if len(reviewed) != len(set(reviewed)):
        raise ContractError("reviewed_pages must be unique")
    if attestation.get("reviewer_type") != "human":
        raise ContractError("reviewer_type must be human")
    attested_at = _require_string(attestation.get("attested_at"), "attested_at")
    try:
        datetime.fromisoformat(attested_at.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ContractError("attested_at must be an ISO date-time") from exc
    return attestation


def load_inputs(
    contract_path: Path,
    coverage_path: Path | None,
    attestation_path: Path | None,
) -> LoadedInputs:
    return LoadedInputs(
        contract_path=contract_path,
        contract=load_contract(contract_path),
        coverage_path=coverage_path,
        coverage=load_coverage(coverage_path) if coverage_path else None,
        attestation_path=attestation_path,
        attestation=load_attestation(attestation_path) if attestation_path else None,
    )
