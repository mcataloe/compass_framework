# COMPASS Changelog

All notable framework changes should be documented here.

## vNext 2026-05.2 — Layer 0 Checkpoint Artifact Generation and Storage Disclosure

Updated COMPASS Layer 0 to make checkpoint artifact generation explicit at every committed round.

Behavior updates:

- Layer 0 must produce checkpoint artifacts after each committed verification round.
- Checkpoint artifacts should behave like small git commits: each one captures the verified state and creates a recoverable backup before proceeding.
- At minimum, each committed round should produce a checkpoint Markdown file, updated claim-ledger entries, updated do-not-claim entries when applicable, and a storage-status statement.
- When practical, Layer 0 should package changed checkpoint files into a downloadable ZIP bundle for upload to the target datastore.
- Layer 0 setup must disclose whether direct datastore write access is available before asking setup questions.
- If direct write access to Google Drive, GitHub, or another requested datastore is unavailable or uncertain, Layer 0 must say so up front and explain the fallback workflow.
- Layer 0 must not claim files were saved unless they were actually written and verified in the datastore.
- Expanded the Layer 0 checkpoint example to include storage status, generated artifacts, direct-write availability, and next safe action.

## vNext 2026-05.1 — Rename STRIDE to COMPASS and Generalize Framework

Renamed the framework from STRIDE to COMPASS.

COMPASS stands for:

> Capture, Organize, Map, Probe, Approve, Synthesize, Store

Behavior updates:

- Established COMPASS as the canonical framework name.
- Reframed the framework as field-agnostic rather than career-only.
- Preserved STRIDE as the legacy career-domain profile during migration.
- Added `COMPASS_Current.md` as the canonical active framework definition.
- Added `COMPASS_Changelog.md` as the canonical changelog.
- Updated core documentation, rule files, prompts, and examples to use COMPASS terminology.
- Updated Layer 0 from career-only source-of-truth onboarding to general verified source-of-truth onboarding.
- Preserved career-specific resume, cover letter, recruiter, ATS, compensation, remote-work, and interview-prep rules as the initial careers profile.
- Added migration guidance for legacy STRIDE file names and prompt references.
- Added compatibility stubs for `STRIDE_Current.md` and `STRIDE_Changelog.md` so old launch prompts do not silently use stale behavior.

## vNext 2026-05 — Layer 0 Verified Career Source-of-Truth Onboarding

Added Layer 0 as the original STRIDE truth-first onboarding workflow for building a verified career source of truth and master CV from user-provided documents and cross-examination.

This behavior is now generalized under COMPASS Layer 0.

## vNext 2026-05 — Prompt Authority Governance

Clarified that prompt templates are workflow launchers rather than independent policy sources.

## vNext 2026-05 — DOCX-First Resume Prompt Enforcement

Updated tailored-resume and recruiter-targeted-resume prompt templates so resume generation requires DOCX-first artifact creation when document-generation tools are available.

## vNext 2026-05 — Initial Repository Baseline

Initialized the STRIDE framework repository.

## Change Management Rules

When changing COMPASS:

1. Update the relevant framework or rules file.
2. Update `VERSION.md` if the change materially affects framework behavior.
3. Add a changelog entry explaining what changed and why.
4. Preserve backward compatibility unless the change intentionally supersedes prior behavior.
5. Avoid burying major behavior changes only inside prompt templates.
