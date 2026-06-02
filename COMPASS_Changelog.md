# COMPASS Changelog

All notable framework changes should be documented here.

## vNext 2026-05.7 - Initial Seed Artifacts

Added first-class Initial Seed Artifact support for provisional career source materials under `/sources/seed/`.

Behavior updates:

- Added `/sources/seed/` as the recommended source-of-truth scaffold location for seed resumes, comprehensive resumes, master CVs, LinkedIn exports, cover letters, portfolio summaries, achievement lists, and similar career evidence.
- Added Provisional Resume / CV Mode for using seed resumes and CVs while verified COMPASS Intake records are incomplete.
- Clarified that seed artifacts are seed, provisional, evidence, and not canonical.
- Clarified that verified Intake claim ledgers, do-not-claim ledgers, and canonical career records supersede seed artifacts for downstream authority.
- Distinguished shortened or tailored resumes from comprehensive resumes and master CVs as provisional baselines.
- Updated Source Rebase so missing seed scaffold paths may be created only in approved `create-missing-only` mode, without moving, renaming, overwriting, or normalizing existing user-owned source files.
- Added seed scaffold templates and a fictional seed artifact manifest example.
- Bumped the active framework version from `vNext 2026-05.6` to `vNext 2026-05.7` because seed artifact handling materially changes source-priority and scaffold behavior.

## vNext 2026-05.6 - COMPASS Source Rebase

Added `COMPASS Source Rebase` as a first-class safe scaffold-alignment command.

Behavior updates:

- Added `rules/09-source-rebase.md` as the durable rule for dry-run and create-missing-only source-of-truth scaffold alignment.
- Added `prompts/compass-source-rebase.md` as the launcher prompt.
- Added framework-owned source-of-truth scaffold templates under `templates/source-of-truth-scaffold/`.
- Added a generic Source Rebase report example.
- Bumped the active framework version from `vNext 2026-05.5` to `vNext 2026-05.6` because the new command materially changes framework behavior.
- Clarified that existing user-owned source-of-truth files always win over framework scaffold templates.
- Clarified that historical checkpoints, including `COMPASS_Layer0_*` paths, are preserved and not renamed.
- Clarified that Source Rebase is not COMPASS Intake and must not verify, extract, reconcile, approve, reject, overwrite, delete, rename, move, or modify source records.

## vNext 2026-05.5 - Human Authenticity Artifact Rules

Added Human Authenticity behavior for external career artifacts without changing the active framework version identifier.

Behavior updates:

- Added `rules/08-human-authenticity.md` as the durable rule for truthful, specific, natural, reviewer-readable, ATS-safe, and interview-defensible external artifacts.
- Integrated Human Authenticity with operating principles, resume generation, cover letter generation, artifact rules, and TruthGuard.
- Updated external artifact prompt launchers and command required-file lists to load the new rule.
- Clarified that AI-assisted drafting is allowed only for clarity, organization, role alignment, concision, reviewer readability, and truthful presentation of verified or source-backed experience.
- Prohibited fake humanization, hidden formatting tricks, unsupported claim smoothing, and AI-detector evasion tactics.

## vNext 2026-05.5 - Intake Artifact Templates

Made COMPASS Intake checkpoint artifact output more concrete without changing the active framework version identifier.

Behavior updates:

- Added stable Intake artifact template requirements for checkpoint records, claim-ledger entries, do-not-claim entries, coverage-register entries, storage-status blocks, and optional ZIP bundle manifests.
- Added `examples/compass-intake-artifact-templates.md` with copy-ready generic skeletons.
- Updated the checkpoint example to include coverage-register output and datastore visibility status.
- Clarified that prompts should reference the reusable template pack while `rules/07-compass-intake.md` remains the durable policy source.

## vNext 2026-05.5 - Command Registry

Added `COMPASS_COMMANDS.md` as the canonical user-facing command registry.

Behavior updates:

- Documented current first-class COMPASS commands: Intake, Analysis, Tailored Resume, Recruiter-Targeted Resume, and Cover Letter.
- Clarified supported artifact requests that are governed by artifact rules but do not yet have first-class launcher prompts.
- Clarified that `COMPASS Charter` is not currently an active first-class command unless explicitly added later with supporting prompt/rule files.
- Updated `README.md` to surface the command registry and active command list.

## vNext 2026-05.5 - Intake Coverage Gate and Artifact Supersession

Clarified COMPASS Intake coverage requirements and downstream source authority without changing the active framework version identifier.

Behavior updates:

- Imported resumes, CVs, LinkedIn profiles, cover letters, portfolio examples, recruiter resumes, and prior generated artifacts are evidence inputs and provenance records, not permanent factual authorities.
- After material claims are ingested, reconciled, and verified, the canonical source-of-truth record and approved ledgers supersede the imported artifact for downstream use.
- Intake must treat 3-5 questions as a per-response or per-batch pacing rule, not a per-role, per-artifact, or total Intake limit.
- A role, project, artifact, or source file is not Intake-complete until material imported claims are captured in coverage metadata and resolved into an approved, narrowed, rejected, evidence-needed, metric-needed, scope-needed, deferred, or excluded status.
- Checkpoints are progress commits, not proof of full source coverage.
- Generated artifacts are downstream outputs and historical records, not factual authorities, unless separately imported and verified through Intake.

## vNext 2026-05.5 - COMPASS Intake Terminology Migration

Renamed the active source-of-truth onboarding workflow from "Layer 0" to "COMPASS Intake" while preserving the same verified source-of-truth onboarding function.

Behavior updates:

- COMPASS Intake is now the canonical workflow name for verified source-of-truth onboarding.
- The formal descriptor remains "Verified Source-of-Truth Onboarding."
- Renamed the active Intake rule and launcher prompt files to `rules/07-compass-intake.md` and `prompts/compass-intake.md`.
- Updated active checkpoint naming from `COMPASS_Layer0` to `COMPASS_Intake`.
- Preserved truth-first onboarding, source-evidence handling, claim verification, do-not-claim behavior, pause/resume checkpointing, and storage honesty.

## vNext 2026-05.4 - Career-Focused Scope Correction

Corrected active COMPASS scope back to careers / job-search.

Behavior updates:

- COMPASS is a career-focused framework, not a field-agnostic framework.
- Product, strategy, research, consulting, grant, policy, and personal knowledge workflows are out of scope unless the project owner explicitly reopens scope.
- Updated active docs and rules to describe career source records, job-search analysis, career artifacts, and recruiter / hiring-team review.
- Preserved TruthGuard, source-grounding, phase separation, COMPASS Intake checkpointing, and COMPASS-only terminology.

## vNext 2026-05.3 - COMPASS-Only Repository Canonicalization

Removed predecessor-name compatibility from active repository files.

Behavior updates:

- COMPASS is the only canonical framework name.
- Removed legacy redirect prompt files.
- Removed legacy compatibility cleanup helper files.
- Updated repository guidance so future work uses COMPASS terminology only.
- Preserved the active source-grounded, TruthGuard-centered behavior.

## vNext 2026-05.2 — COMPASS Intake Checkpoint Artifact Generation and Storage Disclosure

Updated COMPASS Intake, then named "Layer 0," to make checkpoint artifact generation explicit at every committed round.

Behavior updates:

- COMPASS Intake must produce checkpoint artifacts after each committed verification round.
- Checkpoint artifacts should behave like small git commits: each one captures the verified state and creates a recoverable backup before proceeding.
- At minimum, each committed round should produce a checkpoint Markdown file, updated claim-ledger entries, updated do-not-claim entries when applicable, and a storage-status statement.
- When practical, COMPASS Intake should package changed checkpoint files into a downloadable ZIP bundle for upload to the target datastore.
- Intake setup must disclose whether direct datastore write access is available before asking setup questions.
- If direct write access to Google Drive, GitHub, or another requested datastore is unavailable or uncertain, Intake must say so up front and explain the fallback workflow.
- Intake must not claim files were saved unless they were actually written and verified in the datastore.
- Expanded the Intake checkpoint example to include storage status, generated artifacts, direct-write availability, and next safe action.

## vNext 2026-05.1 - Generalize Framework (Superseded by vNext 2026-05.4)

COMPASS stands for:

> Capture, Organize, Map, Probe, Approve, Synthesize, Store

Behavior updates:

- Established COMPASS as the canonical framework name.
- Reframed the framework as field-agnostic rather than career-only.
- Added `COMPASS_Current.md` as the canonical active framework definition.
- Added `COMPASS_Changelog.md` as the canonical changelog.
- Updated core documentation, rule files, prompts, and examples to use COMPASS terminology.
- Updated COMPASS Intake from career-only source-of-truth onboarding to general verified source-of-truth onboarding.
- Preserved career-specific resume, cover letter, recruiter, ATS, compensation, remote-work, and interview-prep rules as the initial careers profile.

Note: The field-agnostic scope from this entry was superseded by `vNext 2026-05.4`; active COMPASS scope is careers / job-search.

## vNext 2026-05 — COMPASS Intake Verified Career Source-of-Truth Onboarding

Added COMPASS Intake, then named "Layer 0," as the truth-first onboarding workflow for building a verified career source of truth and master CV from user-provided documents and cross-examination.

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
