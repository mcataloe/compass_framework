"""Post-publication artifact-name integrity verification."""

from __future__ import annotations

import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import unquote, urlsplit

from .constants import (
    EXIT_FAIL,
    EXIT_PASS,
    EXIT_UNKNOWN,
    NAME_INTEGRITY_RECEIPT_SCHEMA_VERSION,
    NAME_INTEGRITY_REPORT_SCHEMA_VERSION,
)
from .contracts import ContractError, load_contract, load_json


CHECK_ID = "artifact.name_integrity"

SURFACES = (
    "staged_filesystem_filename",
    "final_filesystem_filename",
    "published_object_name",
    "attachment_name",
    "browser_download_filename",
    "content_disposition_filename",
    "storage_display_name",
    "markdown_link_label",
    "user_visible_link_text",
    "user_visible_link_target",
    "completion_message_artifact_name",
    "manifest_filename_field",
    "manifest_path_field",
    "zip_filename",
    "zip_entry_name",
    "generated_metadata_name",
    "copied_variant_name",
)

PATH_SURFACES = {
    "manifest_path_field",
    "zip_entry_name",
    "user_visible_link_target",
}

PERCENT_ESCAPE = re.compile(r"%[0-9a-fA-F]{2}")
NESTED_PERCENT_ESCAPE = re.compile(r"%25", re.IGNORECASE)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _canonical_basename(value: str) -> str:
    parsed = urlsplit(value)
    candidate = parsed.path if parsed.scheme or parsed.netloc else value
    return PurePosixPath(candidate.replace("\\", "/")).name


def _validate_receipt(receipt: dict[str, Any]) -> None:
    if receipt.get("schema_version") != NAME_INTEGRITY_RECEIPT_SCHEMA_VERSION:
        raise ContractError(
            "unsupported artifact-name receipt schema_version; "
            f"expected {NAME_INTEGRITY_RECEIPT_SCHEMA_VERSION}"
        )
    if not isinstance(receipt.get("artifact_id"), str) or not receipt["artifact_id"]:
        raise ContractError("artifact-name receipt artifact_id must be a non-empty string")
    canonical = receipt.get("canonical_filename")
    if not isinstance(canonical, str) or not canonical:
        raise ContractError("artifact-name receipt canonical_filename must be a non-empty string")
    if canonical != _canonical_basename(canonical):
        raise ContractError("canonical_filename must be a filename, not a path or URI")
    observations = receipt.get("observations")
    if not isinstance(observations, list):
        raise ContractError("artifact-name receipt observations must be an array")
    seen: set[str] = set()
    statuses_by_surface: dict[str, set[str]] = {}
    for index, observation in enumerate(observations):
        if not isinstance(observation, dict):
            raise ContractError(f"observations[{index}] must be an object")
        surface = observation.get("surface")
        if surface not in SURFACES:
            raise ContractError(f"observations[{index}].surface is unsupported")
        seen.add(surface)
        status = observation.get("status")
        if status not in {"observed", "not_applicable", "uninspectable"}:
            raise ContractError(f"observations[{index}].status is invalid")
        statuses_by_surface.setdefault(surface, set()).add(status)
        if status == "observed":
            for key in ("expected", "actual"):
                if not isinstance(observation.get(key), str) or not observation[key]:
                    raise ContractError(f"observations[{index}].{key} must be a non-empty string")
        if "transport_encoding_required" in observation and not isinstance(
            observation["transport_encoding_required"], bool
        ):
            raise ContractError(
                f"observations[{index}].transport_encoding_required must be a boolean"
            )
    for surface, statuses in statuses_by_surface.items():
        if len(statuses) > 1:
            raise ContractError(
                f"artifact-name receipt mixes applicability statuses for surface: {surface}"
            )


def _observation_status(
    observation: dict[str, Any], canonical: str
) -> tuple[str, str]:
    status = observation["status"]
    surface = observation["surface"]
    if status == "not_applicable":
        return "PASS", "surface.not_applicable"
    if status == "uninspectable":
        return "UNKNOWN", "surface.uninspectable"

    expected = observation["expected"]
    actual = observation["actual"]
    if PERCENT_ESCAPE.search(expected):
        return "FAIL", "expected.transport_encoding_leak"

    expected_name = _canonical_basename(expected) if surface in PATH_SURFACES else expected
    if expected_name != canonical:
        return "FAIL", "expected.not_canonical"

    transport_required = observation.get("transport_encoding_required", False)
    if transport_required:
        if surface != "user_visible_link_target":
            return "FAIL", "transport.exception_invalid_surface"
        if NESTED_PERCENT_ESCAPE.search(actual):
            return "FAIL", "transport.double_encoding"
        if unquote(actual) != expected:
            return "FAIL", "transport.decoded_target_mismatch"
        return "PASS", "transport.opaque_only"

    if PERCENT_ESCAPE.search(actual):
        return "FAIL", "actual.transport_encoding_leak"
    if actual != expected:
        return "FAIL", "actual.canonical_mismatch"
    return "PASS", "surface.matches_canonical"


def build_name_integrity_report(
    contract: dict[str, Any], receipt: dict[str, Any]
) -> dict[str, Any]:
    _validate_receipt(receipt)
    required = contract["artifact"].get("require_delivery_name_receipt", False)
    canonical = receipt["canonical_filename"]
    outcomes: list[dict[str, str]] = []
    if PERCENT_ESCAPE.search(canonical):
        outcomes.append(
            {
                "surface": "canonical_filename",
                "status": "FAIL",
                "diagnostic_code": "canonical.transport_encoding_leak",
            }
        )
    else:
        outcomes.append(
            {
                "surface": "canonical_filename",
                "status": "PASS",
                "diagnostic_code": "canonical.literal_name",
            }
        )
    for observation in receipt["observations"]:
        status, code = _observation_status(observation, canonical)
        outcomes.append(
            {"surface": observation["surface"], "status": status, "diagnostic_code": code}
        )

    observed_surfaces = {observation["surface"] for observation in receipt["observations"]}
    for surface in sorted(set(SURFACES) - observed_surfaces):
        outcomes.append(
            {
                "surface": surface,
                "status": "UNKNOWN",
                "diagnostic_code": "surface.observation_missing",
            }
        )

    statuses = {item["status"] for item in outcomes}
    aggregate = "FAIL" if "FAIL" in statuses else "UNKNOWN" if "UNKNOWN" in statuses else "PASS"
    if required is not True:
        if aggregate == "PASS":
            aggregate = "UNKNOWN"
        outcomes.append(
            {
                "surface": "contract",
                "status": "UNKNOWN",
                "diagnostic_code": "contract.delivery_receipt_not_required",
            }
        )
    return {
        "schema_version": NAME_INTEGRITY_REPORT_SCHEMA_VERSION,
        "artifact_id": receipt["artifact_id"],
        "canonical_filename": canonical,
        "verified_at": _utc_now(),
        "check": {
            "id": CHECK_ID,
            "status": aggregate,
            "diagnostic_code": (
                "name_integrity.pass"
                if aggregate == "PASS"
                else "name_integrity.fail"
                if aggregate == "FAIL"
                else "name_integrity.unknown"
            ),
            "surface_results": outcomes,
        },
        "aggregate_status": aggregate,
    }


def _atomic_write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            json.dump(value, stream, indent=2, sort_keys=True)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary_name, path)
    except OSError:
        try:
            Path(temporary_name).unlink()
        except OSError:
            pass
        raise


def verify_name_integrity(contract_path: Path, receipt_path: Path, report_out: Path) -> int:
    contract = load_contract(contract_path)
    receipt = load_json(receipt_path, "artifact-name integrity receipt")
    report = build_name_integrity_report(contract, receipt)
    _atomic_write_json(report_out, report)
    return {
        "PASS": EXIT_PASS,
        "FAIL": EXIT_FAIL,
        "UNKNOWN": EXIT_UNKNOWN,
    }[report["aggregate_status"]]
