from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.resume_release.cli import main as cli_main
from tools.resume_release.name_integrity import SURFACES, build_name_integrity_report

from test_resume_release import base_contract


CANONICAL = "Candidate Name - Example Company - Staff Software Engineer (Time Management) - 07-2026 - Resume.docx"


def receipt() -> dict:
    return {
        "schema_version": "1.0.0",
        "artifact_id": "synthetic-name-integrity",
        "canonical_filename": CANONICAL,
        "observations": [
            {
                "surface": surface,
                "status": "observed",
                "expected": CANONICAL,
                "actual": CANONICAL,
            }
            for surface in SURFACES
        ],
    }


def contract() -> dict:
    value = base_contract()
    value["artifact"]["require_delivery_name_receipt"] = True
    return value


class ArtifactNameIntegrityTests(unittest.TestCase):
    def assert_surface_failure(self, surface: str, actual: str) -> None:
        value = receipt()
        item = next(entry for entry in value["observations"] if entry["surface"] == surface)
        item["actual"] = actual
        report = build_name_integrity_report(contract(), value)
        self.assertEqual(report["aggregate_status"], "FAIL")
        result = next(
            entry for entry in report["check"]["surface_results"] if entry["surface"] == surface
        )
        self.assertEqual(result["status"], "FAIL")

    def test_valid_filename_with_spaces_parentheses_and_hyphens_passes(self) -> None:
        report = build_name_integrity_report(contract(), receipt())
        self.assertEqual(report["aggregate_status"], "PASS")

    def test_staged_filename_with_encoded_space_fails(self) -> None:
        self.assert_surface_failure(
            "staged_filesystem_filename", CANONICAL.replace(" ", "%20")
        )

    def test_final_filename_with_encoded_space_fails(self) -> None:
        self.assert_surface_failure("final_filesystem_filename", CANONICAL.replace(" ", "%20"))

    def test_double_encoded_filename_fails(self) -> None:
        self.assert_surface_failure(
            "final_filesystem_filename", "Candidate%2520Name%2520-%2520Example%2520Company.docx"
        )

    def test_link_label_with_encoded_space_fails(self) -> None:
        self.assert_surface_failure("markdown_link_label", CANONICAL.replace(" ", "%20"))

    def test_attachment_and_download_metadata_with_encoded_space_fail(self) -> None:
        for surface in (
            "attachment_name",
            "browser_download_filename",
            "content_disposition_filename",
        ):
            with self.subTest(surface=surface):
                self.assert_surface_failure(surface, CANONICAL.replace(" ", "%20"))

    def test_manifest_filename_and_path_fields_with_encoded_space_fail(self) -> None:
        for surface in ("manifest_filename_field", "manifest_path_field"):
            with self.subTest(surface=surface):
                self.assert_surface_failure(surface, CANONICAL.replace(" ", "%20"))

    def test_zip_filename_and_entry_with_encoded_space_fail(self) -> None:
        for surface in ("zip_filename", "zip_entry_name"):
            with self.subTest(surface=surface):
                self.assert_surface_failure(surface, CANONICAL.replace(" ", "%20"))

    def test_valid_name_survives_publication_and_download_unchanged(self) -> None:
        value = receipt()
        report = build_name_integrity_report(contract(), value)
        self.assertEqual(report["aggregate_status"], "PASS")
        for surface in ("published_object_name", "browser_download_filename"):
            item = next(
                result for result in report["check"]["surface_results"] if result["surface"] == surface
            )
            self.assertEqual(item["status"], "PASS")

    def test_transport_encoding_leak_into_downloaded_filename_fails(self) -> None:
        value = receipt()
        target = next(
            entry for entry in value["observations"] if entry["surface"] == "user_visible_link_target"
        )
        target["expected"] = "/downloads/" + CANONICAL
        target["actual"] = "/downloads/" + CANONICAL.replace(" ", "%20")
        target["transport_encoding_required"] = True
        download = next(
            entry for entry in value["observations"] if entry["surface"] == "browser_download_filename"
        )
        download["actual"] = CANONICAL.replace(" ", "%20")
        report = build_name_integrity_report(contract(), value)
        self.assertEqual(report["aggregate_status"], "FAIL")
        target_result = next(
            result for result in report["check"]["surface_results"]
            if result["surface"] == "user_visible_link_target"
        )
        self.assertEqual(target_result["status"], "PASS")

    def test_uninspectable_download_is_unknown_and_blocks_final_presentation(self) -> None:
        value = receipt()
        download = next(
            entry for entry in value["observations"] if entry["surface"] == "browser_download_filename"
        )
        download.clear()
        download.update({"surface": "browser_download_filename", "status": "uninspectable"})
        report = build_name_integrity_report(contract(), value)
        self.assertEqual(report["aggregate_status"], "UNKNOWN")

    def test_missing_surface_observation_is_unknown(self) -> None:
        value = receipt()
        value["observations"] = [
            item
            for item in value["observations"]
            if item["surface"] != "browser_download_filename"
        ]
        report = build_name_integrity_report(contract(), value)
        self.assertEqual(report["aggregate_status"], "UNKNOWN")

    def test_multiple_zip_entries_are_all_validated(self) -> None:
        value = receipt()
        value["observations"].append(
            {
                "surface": "zip_entry_name",
                "status": "observed",
                "expected": CANONICAL,
                "actual": CANONICAL.replace(" ", "%20"),
            }
        )
        report = build_name_integrity_report(contract(), value)
        self.assertEqual(report["aggregate_status"], "FAIL")

    def test_cli_writes_passing_post_publication_report(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            contract_path = root / "contract.json"
            receipt_path = root / "receipt.json"
            report_path = root / "report.json"
            contract_path.write_text(json.dumps(contract()), encoding="utf-8")
            receipt_path.write_text(json.dumps(receipt()), encoding="utf-8")
            code = cli_main(
                [
                    "verify-name-integrity",
                    "--contract",
                    str(contract_path),
                    "--receipt",
                    str(receipt_path),
                    "--report-out",
                    str(report_path),
                ]
            )
            self.assertEqual(code, 0)
            report = json.loads(report_path.read_text(encoding="utf-8"))
            self.assertEqual(report["aggregate_status"], "PASS")

    def test_cli_returns_failure_when_download_name_leaks_transport_encoding(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            contract_path = root / "contract.json"
            receipt_path = root / "receipt.json"
            report_path = root / "report.json"
            value = receipt()
            download = next(
                entry
                for entry in value["observations"]
                if entry["surface"] == "browser_download_filename"
            )
            download["actual"] = CANONICAL.replace(" ", "%20")
            contract_path.write_text(json.dumps(contract()), encoding="utf-8")
            receipt_path.write_text(json.dumps(value), encoding="utf-8")
            code = cli_main(
                [
                    "verify-name-integrity",
                    "--contract",
                    str(contract_path),
                    "--receipt",
                    str(receipt_path),
                    "--report-out",
                    str(report_path),
                ]
            )
            self.assertEqual(code, 1)
            report = json.loads(report_path.read_text(encoding="utf-8"))
            self.assertEqual(report["aggregate_status"], "FAIL")


if __name__ == "__main__":
    unittest.main()
