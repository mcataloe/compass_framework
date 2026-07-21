"""Stable public constants for the resume release interface."""

VALIDATOR_NAME = "compass-resume-release"
VALIDATOR_VERSION = "1.1.0"
CONTRACT_SCHEMA_VERSION = "1.0.0"
MANIFEST_SCHEMA_VERSION = "1.0.1"
COVERAGE_SCHEMA_VERSION = "1.0.0"
ATTESTATION_SCHEMA_VERSION = "1.0.0"
NAME_INTEGRITY_RECEIPT_SCHEMA_VERSION = "1.0.0"
NAME_INTEGRITY_REPORT_SCHEMA_VERSION = "1.0.0"

PASS = "PASS"
FAIL = "FAIL"
UNKNOWN = "UNKNOWN"

CHECK_IDS = (
    "policy.current",
    "profile.current",
    "input.hashes",
    "filename.actual",
    "docx.package",
    "docx.styles",
    "docx.native_lists",
    "docx.indentation",
    "docx.margins",
    "docx.breaks",
    "docx.keep_next",
    "content.markdown_docx_parity",
    "content.employment_coverage",
    "content.experience_duration",
    "render.available",
    "render.pages",
    "render.whitespace",
    "render.blank_pages",
    "visual.every_page_review",
    "release.atomic_publication",
)

EXIT_PASS = 0
EXIT_FAIL = 1
EXIT_UNKNOWN = 2
EXIT_INVALID = 64
