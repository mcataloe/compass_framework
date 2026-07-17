# Resume Release Tool Interface

This directory is the approved home for the candidate-neutral COMPASS resume validation and atomic-release tool implemented in the next Build Unit.

The governing behavior is `rules/16-resume-release-assurance.md`. JSON inputs and outputs must conform to the schemas under `schemas/resume-release/`.

No executable validator is included in this Build Unit.

## Planned Module and Command

The implementation should support module execution without requiring a package manager:

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

## Planned Test Location

Candidate-neutral tests should live under:

```text
tests/resume_release/
```

Tests should use synthetic fixtures generated at runtime. Do not commit live resumes, employer names, candidate facts, private templates, or generated page images.
