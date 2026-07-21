# 16 — Resume Artifact Release Assurance

This rule defines the generic COMPASS release contract for generated resume artifacts.

## Purpose

Resume style, content, pagination, rendering, and source-grounding requirements are release conditions, not optional review suggestions.

The required lifecycle is:

```text
generate -> stage -> validate -> render -> manifest -> atomically release -> publish/attach -> verify delivered name -> present
```

A staged resume is an untrusted internal artifact. It must not be copied, uploaded, presented, linked as final, or used as a factual authority until the local release gate passes. A locally released file is publication-ready, not delivery-verified: after upload or attachment it must remain unpresented until the actual delivered-name verification passes.

## Applicability

Apply this rule to tailored and recruiter-targeted resume workflows that produce DOCX, PDF, Markdown, or another configured resume format.

The configured Source of Truth supplies candidate-specific facts, style values, coverage requirements, filename rules, template identity, thresholds, and allowed variants. This public rule supplies the candidate-neutral validation behavior and release semantics.

This rule does not authorize resume generation, application submission, candidate-status changes, or changes to career evidence.

## Status Contract

Every required check has exactly one status:

- `PASS` — the check ran against the actual staged artifact and satisfied its current contract.
- `FAIL` — the check ran and found a contract violation.
- `UNKNOWN` — the check could not run completely, its required source or tool was unavailable, its result was indeterminate, or its evidence was missing.

`FAIL` and `UNKNOWN` are both release-blocking. There is no partial, substantial, warning-only, or self-attested substitute for a required `PASS`.

The aggregate status is:

- `PASS` only when every required check is `PASS`;
- `FAIL` when at least one required check is `FAIL`;
- `UNKNOWN` when no required check failed but at least one required check is `UNKNOWN`.

## Required Inputs

The release gate requires:

1. The actual staged artifact files.
2. A current resume release contract conforming to `schemas/resume-release/resume-release-contract.schema.json`.
3. A per-artifact employment coverage plan conforming to `schemas/resume-release/employment-coverage-plan.schema.json` when employment history or an experience-duration claim appears.
4. The current applicable framework and Source of Truth policy identity.
5. The actual filesystem output names and intended final paths.
6. Required render tools and a writable staging location.
7. Every-page visual-review evidence when the contract requires it.
8. After publication or attachment, an artifact-name integrity receipt conforming to `schemas/resume-release/artifact-name-integrity-receipt.schema.json` when the contract requires delivery-name verification.

Missing, unreadable, incompatible, stale, or unverifiable required input produces `UNKNOWN` and blocks release.

## Stable Check Identifiers

Implementations and private profiles use these candidate-neutral identifiers:

| Check ID | Purpose |
|---|---|
| `policy.current` | Confirms the governing framework and Source of Truth policy identities. |
| `profile.current` | Confirms the configured style/profile contract identity and version. |
| `input.hashes` | Records and validates staged input hashes. |
| `filename.actual` | Validates actual filesystem names rather than viewer or URL-encoded labels. |
| `docx.package` | Validates DOCX/OOXML package integrity and required parts. |
| `docx.styles` | Validates configured styles, typography, and paragraph behavior. |
| `docx.native_lists` | Validates native Word list relationships and configured list semantics. |
| `docx.indentation` | Validates configured bullet and wrapped-line indentation. |
| `docx.margins` | Validates configured section and page margins. |
| `docx.breaks` | Detects and validates manual and forced page-break behavior. |
| `docx.keep_next` | Validates configured keep-with-next and orphan-control structure. |
| `content.markdown_docx_parity` | Validates configured cross-format sections and anchors. |
| `content.employment_coverage` | Accounts for every required canonical role. |
| `content.experience_duration` | Validates configured experience-duration wording and interval calculation. |
| `render.available` | Confirms that the required renderer completed successfully. |
| `render.pages` | Confirms expected page production and page-image generation. |
| `render.whitespace` | Validates configured page-density and bottom-whitespace thresholds. |
| `render.blank_pages` | Detects empty or nearly blank pages. |
| `visual.every_page_review` | Records a distinct review of every rendered page. |
| `release.atomic_publication` | Confirms final paths were published only after aggregate `PASS`. |

A private profile must not rename, weaken, or silently omit an applicable required check from this table. Validator version `1.1.0` preserves all 20 stable local-release identifiers. Post-publication delivery uses the separate candidate-neutral `artifact.name_integrity` verification because its evidence does not exist until after upload or attachment.

## Post-Publication Artifact-Name Integrity

The canonical filename must be resolved once as a decoded filename and reused without URL encoding before file creation, upload, attachment, or presentation. A literal space in a filename is the normal space character. Percent-encoded or nested percent-encoded values used in place of filename characters are forbidden naming values.

Checking the intended filename or local staged path alone is insufficient. After publication or attachment, record and verify every applicable actual naming surface defined by the artifact-name receipt schema, including filesystem and object names, attachment and browser-download metadata, controlled `Content-Disposition` filename values, storage display names, link labels and visible text, raw-space link targets where supported, completion listings, manifest fields, ZIP names and entries, generated metadata, and copied variants.

An underlying transport may percent-encode an opaque URI only when the transport requires it. That exception applies only to the transport target: the decoded canonical filename must still control the displayed name, attachment metadata, persisted name fields, and browser-saved filename. Double encoding is never acceptable.

Run `python -m tools.resume_release verify-name-integrity` against the actual observations after publication or attachment. The resulting `artifact.name_integrity` status must be `PASS` before the artifact link or attachment is presented as final. A mismatch or encoding leak is `FAIL`; a required platform-controlled surface that cannot be inspected is `UNKNOWN`. Either blocks presentation and triggers correction plus complete re-verification.

## Structural DOCX Validation

When DOCX is produced, validate the package rather than relying on a single renderer's appearance.

The configured checks may include:

- required OOXML package parts;
- paragraph and character styles;
- font family, size, color, and spacing;
- native Word numbering and list relationships;
- bullet left and hanging indentation;
- section margins and page settings;
- manual page breaks and `pageBreakBefore` behavior;
- `keepNext` or equivalent heading-group behavior;
- configured section, heading, and text anchors.

A custom paragraph that only resembles a list, a typed bullet glyph used in place of required native list semantics, or an inherited style without the required durable numbering relationship must fail the applicable configured check.

## Content and Coverage Validation

Generated resume content remains subject to source priority and TruthGuard.

When a coverage plan is required:

- every canonical role in scope must have a stable role identifier and source references;
- every role must be classified as `detailed`, `compressed`, or `excluded`;
- an excluded role must include an explicit internal reason;
- the clean resume must not expose internal coverage classifications or exclusion reasoning;
- omission for pagination or convenience must not be treated as an implicit exclusion;
- experience-duration calculations must use the configured calendar-interval method and must not double-count overlapping roles.

Cross-format validation must compare configured anchors and sections from the actual staged files. It must not assume that successfully generating DOCX proves parity with Markdown or another source format.

## Rendered Validation

When rendering is required, the release gate must render the actual staged DOCX/PDF through a supported configured renderer and produce evidence for every page.

Configured rendered checks may include:

- page count;
- page-image creation;
- excessive unused space on non-final pages;
- nearly blank pages;
- configured final-page handling;
- heading-group pagination;
- bullet and wrapped-line alignment;
- unexpected style or density drift.

Missing renderer capability, render failure, incomplete page output, or unavailable page inspection is `UNKNOWN`. Do not claim visual validation when only structural validation ran.

Every-page visual review is a distinct check. A generated manifest, unit test, contact sheet, or automated geometry result does not by itself prove that a reviewer inspected every page.

## Release Manifest

Every run emits a deterministic manifest conforming to `schemas/resume-release/resume-release-manifest.schema.json`.

The manifest must record:

- validator and schema versions;
- contract and policy identity;
- staged input hashes;
- actual filenames;
- every required check and status;
- concise privacy-safe diagnostics and measurements;
- render and visual-review evidence;
- aggregate status;
- publication attempt and outcome;
- final artifact hashes and paths only after successful publication.

Do not include full resume text, private career records, secrets, or unnecessary candidate data in a public log or generic diagnostic.

## Atomic Publication

Final artifact paths are release outputs, not staging paths.

The release implementation must:

1. Generate and validate in a separate staging location.
2. Leave existing final artifacts unchanged on `FAIL` or `UNKNOWN`.
3. Create or replace final artifacts only after aggregate `PASS`.
4. Use atomic move/replace semantics to the practical extent supported by the filesystem.
5. Record published hashes and paths in the successful manifest.
6. Keep failure manifests clearly separated from released deliverables.

Do not upload to a user-facing datastore or present a staging link as a workaround for a blocked final path.

Successful atomic publication does not prove attachment, link, storage-metadata, or browser-download name integrity. Those surfaces are verified only by the post-publication receipt and report.

## Generic CLI Contract

The candidate-neutral version `1.1.0` interface and implementation are documented in `tools/resume_release/README.md`. It validates staged artifacts with `validate`, performs gated local publication with `release`, and verifies post-publication naming surfaces with `verify-name-integrity`.

Validator `1.1.0` consumes release-contract and employment-coverage schema `1.0.0`, consumes visual-review-attestation and artifact-name receipt schema `1.0.0`, emits release-manifest schema `1.0.1`, and emits artifact-name integrity report schema `1.0.0`.

Expected exit-code classes are:

- `0` — aggregate `PASS` and successful requested publication;
- `1` — aggregate `FAIL`;
- `2` — aggregate `UNKNOWN`;
- `64` — invalid invocation or incompatible input contract before artifact validation can start.

An implementation must not return success when publication was requested but did not complete. A successful local `release` command must not be represented as proof of post-publication delivery-name integrity.

Every-page visual review uses `schemas/resume-release/visual-review-attestation.schema.json`. The attestation must identify the current staged artifact hash and exact rendered page set and must be supplied by a human reviewer; the validator must not generate or infer it.

## Privacy and Public/Private Separation

The public COMPASS Framework owns generic schemas, validation behavior, check identifiers, CLI expectations, and candidate-neutral synthetic tests.

A private Source of Truth owns candidate-specific:

- facts and career records;
- style values and template identity;
- employer and role coverage;
- experience-duration claims;
- private reference artifacts;
- private thresholds or permitted variants;
- generated resumes and page images.

Do not commit live candidate artifacts or candidate-specific profile values to the public framework repository.

## Compatibility and Failure Behavior

Resume launchers remain workflow entry points and must defer to this rule.

When a resume workflow cannot retrieve a required contract, cannot run its required checks, cannot produce the required manifest, or cannot verify a required delivered naming surface, stop with a release limitation. Do not silently fall back to unchecked generation, a remembered style profile, or the correctness of the staged filename.

User-specific Source of Truth policy may tighten this rule but may not convert a required `FAIL` or `UNKNOWN` into `PASS`, remove TruthGuard, or weaken privacy and artifact-cleanliness boundaries.
