# Resume Release Tool Interface

This directory contains the candidate-neutral COMPASS resume validator and atomic-release wrapper.

The governing behavior is `rules/16-resume-release-assurance.md`. JSON inputs and outputs must conform to the schemas under `schemas/resume-release/`.

The tool version is `1.0.0` and requires Python 3.10 or newer. It uses only the Python standard library, accepts release-contract and employment-coverage schema version `1.0.0`, and emits manifest schema version `1.0.1`.

## Module and Commands

Run validation without creating or replacing final artifact paths:

```text
python -m tools.resume_release validate \
  --docx STAGED.docx \
  --markdown STAGED.md \
  --contract RESUME_RELEASE_CONTRACT.json \
  --coverage EMPLOYMENT_COVERAGE_PLAN.json \
  --manifest-out STAGING/release-manifest.json \
  --render-dir STAGING/rendered-pages
```

Validation does not create final artifact paths.

```text
python -m tools.resume_release release \
  --docx STAGED.docx \
  --markdown STAGED.md \
  --contract RESUME_RELEASE_CONTRACT.json \
  --coverage EMPLOYMENT_COVERAGE_PLAN.json \
  --visual-attestation EVERY_PAGE_REVIEW.json \
  --manifest-out STAGING/release-manifest.json \
  --render-dir STAGING/rendered-pages \
  --output-docx FINAL.docx \
  --output-markdown FINAL.md
```

Release creates or replaces final artifacts only after every required check is `PASS`.

Use `python -m tools.resume_release --help` or the command-specific `--help` output for the complete argument list. At least one staged artifact is required. A release requires the corresponding final output path.

Validator `1.0.0` requires staged DOCX and accepts optional Markdown. PDF is an internal render product in this version, not a staged or published CLI artifact; a contract requesting staged PDF or omitting DOCX is incompatible and exits `64`.

## Visual-Review Attestation

When `visual_review.required` is true, `--visual-attestation` must reference JSON conforming to `schemas/resume-release/visual-review-attestation.schema.json`:

```json
{
  "schema_version": "1.0.0",
  "artifact_sha256": "64-lowercase-or-uppercase-hexadecimal-characters",
  "page_count": 2,
  "reviewed_pages": [1, 2],
  "reviewer_type": "human",
  "attested_at": "2026-01-01T00:00:00Z"
}
```

The artifact hash, page count, and exact page set must match the current staged DOCX and renderer output. The validator never creates or infers a human attestation.

## Supported Rendering

When rendering is required, version `1.0.0` supports:

- LibreOffice or `soffice` for isolated DOCX-to-PDF conversion;
- Poppler `pdftoppm` for grayscale page bitmaps;
- dependency-free PGM analysis for ink density and bottom-whitespace geometry.

Tools are discovered at runtime and invoked through argument arrays. An unavailable or failed required renderer produces `UNKNOWN` and blocks release. Page bitmaps are written only beneath `--render-dir`.

## Exit Codes

| Code | Meaning |
|---|---|
| `0` | Aggregate `PASS`; requested publication also succeeded. |
| `1` | Aggregate `FAIL`; no final artifact was published. |
| `2` | Aggregate `UNKNOWN`; no final artifact was published. |
| `64` | Invalid invocation or incompatible input contract before validation could start. |

## Interface Requirements

The implementation must:

- use only the Python standard library unless a later approved Prompt changes the dependency boundary;
- treat contract, coverage, renderer, and visual-review unavailability explicitly;
- inspect DOCX as an OOXML ZIP package rather than trusting visual appearance alone;
- invoke render tools through argument arrays rather than constructed shell commands;
- use staging paths and safe temporary directories;
- emit deterministic privacy-safe manifests;
- leave existing final files unchanged on `FAIL`, `UNKNOWN`, or invalid invocation;
- use atomic move/replace semantics after aggregate `PASS`;
- keep candidate-specific values and artifacts outside the public framework repository.

Malformed or incompatible JSON inputs and invalid invocations exit `64`. Malformed artifacts become check results so their release-blocking evidence appears in the manifest.

Validator version `1.0.0` requires all 20 stable check identifiers in the contract. Format- or policy-disabled checks return an explicit non-bypassing `PASS` reason; omitting a stable check is an incompatible contract, not a downgrade mechanism.

Publication uses same-directory temporary files, per-target atomic replacement, and rollback backups for existing final files. A failed or unavailable check never starts publication. A publication error changes `release.atomic_publication` to `UNKNOWN`, rolls back completed replacements where practical, and leaves the failure manifest in staging.

## Tests

Run the candidate-neutral standard-library suite with:

```text
python -m unittest discover -s tests -v
```

Tests should use synthetic fixtures generated at runtime. Do not commit live resumes, employer names, candidate facts, private templates, or generated page images.
