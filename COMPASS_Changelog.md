# COMPASS Changelog

All notable framework changes should be documented here.

## vNext 2026-05.4 - Career-Focused Scope Correction

Corrected active COMPASS scope back to careers / job-search.

Behavior updates:

- COMPASS is a career-focused framework, not a field-agnostic framework.
- Product, strategy, research, consulting, grant, policy, and personal knowledge workflows are out of scope unless the project owner explicitly reopens scope.
- Updated active docs and rules to describe career source records, job-search analysis, career artifacts, and recruiter / hiring-team review.
- Preserved TruthGuard, source-grounding, phase separation, Layer 0 checkpointing, and COMPASS-only terminology.

## vNext 2026-05.3 - COMPASS-Only Repository Canonicalization

Removed predecessor-name compatibility from active repository files.

Behavior updates:

- COMPASS is the only canonical framework name.
- Removed legacy redirect prompt files.
- Removed legacy compatibility cleanup helper files.
- Updated repository guidance so future work uses COMPASS terminology only.
- Preserved the active source-grounded, TruthGuard-centered behavior.

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

## vNext 2026-05.1 - Generalize Framework (Superseded by vNext 2026-05.4)

COMPASS stands for:

> Capture, Organize, Map, Probe, Approve, Synthesize, Store

Behavior updates:

- Established COMPASS as the canonical framework name.
- Reframed the framework as field-agnostic rather than career-only.
- Added `COMPASS_Current.md` as the canonical active framework definition.
- Added `COMPASS_Changelog.md` as the canonical changelog.
- Updated core documentation, rule files, prompts, and examples to use COMPASS terminology.
- Updated Layer 0 from career-only source-of-truth onboarding to general verified source-of-truth onboarding.
- Preserved career-specific resume, cover letter, recruiter, ATS, compensation, remote-work, and interview-prep rules as the initial careers profile.

Note: The field-agnostic scope from this entry was superseded by `vNext 2026-05.4`; active COMPASS scope is careers / job-search.

## vNext 2026-05 — Layer 0 Verified Career Source-of-Truth Onboarding

Added Layer 0 as the truth-first onboarding workflow for building a verified career source of truth and master CV from user-provided documents and cross-examination.

This behavior was later generalized in `vNext 2026-05.1`, then superseded by the `vNext 2026-05.4` career-focused scope correction.

## vNext 2026-05 — Prompt Authority Governance

Clarified that prompt templates are workflow launchers rather than independent policy sources.

## vNext 2026-05 — DOCX-First Resume Prompt Enforcement

Updated tailored-resume and recruiter-targeted-resume prompt templates so resume generation requires DOCX-first artifact creation when document-generation tools are available.

## vNext 2026-05 — Initial Repository Baseline

Initialized the COMPASS framework repository.

## Change Management Rules

When changing COMPASS:

1. Update the relevant framework or rules file.
2. Update `VERSION.md` if the change materially affects framework behavior.
3. Add a changelog entry explaining what changed and why.
4. Preserve backward compatibility unless the change intentionally supersedes prior behavior.
5. Avoid burying major behavior changes only inside prompt templates.
