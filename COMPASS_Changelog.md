# COMPASS Changelog

All notable framework changes should be documented here.

## vNext 2026-05.11 - Private Experience Sync Routing

Moved actual Source of Truth and downstream target repository mapping into private Source of Truth configuration.

Behavior updates:

- Added `templates/source-of-truth-scaffold/sync/COMPASS_Experience_Targets.yaml` as the generic private routing-map template.
- Added `templates/source-of-truth-scaffold/sync/README.md` to define the source-side privacy and ownership boundary.
- Updated Source Rebase to recognize `/sync/` as an optional scaffold path and to create only generic missing placeholders after explicit approval.
- Required actual source and target links, target IDs, branches, publication defaults, protected paths, and write policy to live in the Source of Truth routing map rather than the public target manifest.
- Sanitized the target `COMPASS_Experience_Manifest.yaml` template so it contains a stable source ID and reconciliation metadata without exposing the private Source of Truth repository location.
- Added deterministic target resolution, override-conflict handling, enabled-target checks, and missing-routing-map behavior.
- Updated Experience Sync dry-run and full-audit behavior to detect public source-location exposure.
- Updated the reconciliation report to record routing-map access, selected target ID, target-resolution basis, and public-manifest sanitization.
- Preserved the one-way projection boundary: Experience Sync reads but never modifies the Source of Truth or routing map.
- Advanced the active framework identifier from `vNext 2026-05.10` to `vNext 2026-05.11`.

## vNext 2026-05.10 - COMPASS Experience Sync

Added `COMPASS Experience Sync` as a first-class command for reconciling an approved career Source of Truth into a separate public or externally shareable experience repository.

Key updates:

- Added `rules/11-experience-sync.md` and `prompts/compass-experience-sync.md`.
- Added `dry-run`, `full-audit`, and explicitly approved `apply-approved` modes.
- Required a current matching report before target writes.
- Required target changes through a non-default branch and pull request.
- Separated factual approval from public suitability.
- Added Experience Manifest, reconciliation report, and public claim templates.
- Preserved TruthGuard, claim-depth, provisional-source, do-not-claim, privacy, and storage-honesty controls.

## vNext 2026-05.9 - Opportunity Reality Layer

Added the Opportunity Reality Layer to COMPASS Analysis.

Key updates:

- Added `rules/10-opportunity-recon.md`.
- Added Purple Squirrel Factor scoring and role-compression analysis.
- Added current company, employee-sentiment, and interview research requirements when external access is available.
- Added interview-realism classifications and pursuit economics.
- Expanded the strict analysis report from 11 to 13 sections.
- Preserved separation between internal opportunity analysis and clean external artifacts.

## vNext 2026-05.8 - Initial Seed Artifacts and Release Hygiene

Added `/sources/seed/` as the recommended location for provisional career source material.

Key updates:

- Added Provisional Resume / CV Mode.
- Clarified that seed artifacts are evidence, not canonical truth.
- Distinguished comprehensive master CVs from shortened or tailored resumes as provisional baselines.
- Updated Source Rebase to create missing seed scaffold paths only after approval.

## vNext 2026-05.7 - Staff / Principal Positioning

Added claim-depth-aware senior individual-contributor positioning.

Key updates:

- Prioritized verified architecture ownership, technical direction, cross-team influence, organizational leverage, operational accountability, mentoring, and implementation.
- Preserved official titles while communicating operating level through evidence.
- Added claim-depth-aware wording and transition/shared-ownership handling.
- Recognized evidence-grounded qualitative impact without inventing metrics.

## vNext 2026-05.6 - Intake Materiality Gate

Added a Materiality Gate to COMPASS Intake.

Key updates:

- Required inspection of ledgers, coverage registers, checkpoints, canonical records, and source artifacts before asking questions.
- Limited questions to unresolved material issues.
- Preserved small-batch pacing without treating it as a total scope limit.

## vNext 2026-05.6 - COMPASS Source Rebase

Added Source Rebase as a first-class scaffold-alignment command.

Key updates:

- Added dry-run and approved create-missing-only behavior.
- Added framework-owned Source of Truth scaffold templates.
- Preserved existing user-owned files and historical checkpoints.
- Kept claim verification and source-record migration out of scope.

## vNext 2026-05.5 - Human Authenticity

Added `rules/08-human-authenticity.md` for truthful, specific, natural, reviewer-readable, and interview-defensible external artifacts.

Prohibited unsupported claim smoothing, hidden formatting tricks, fake humanization, and detector-evasion tactics.

## vNext 2026-05.5 - Intake Artifact Templates

Added stable templates for checkpoints, claim ledgers, do-not-claim entries, coverage entries, storage status, and optional ZIP bundle manifests.

## vNext 2026-05.5 - Command Registry

Added `COMPASS_COMMANDS.md` as the canonical user-facing command registry.

## vNext 2026-05.5 - Intake Coverage and Artifact Supersession

Clarified that imported career artifacts are evidence and provenance until material claims are verified into canonical records and ledgers.

Checkpoints remain progress commits rather than proof of complete source coverage.

## vNext 2026-05.5 - COMPASS Intake Terminology

Renamed the active verified onboarding workflow to `COMPASS Intake` and updated active file and checkpoint naming while preserving truth-first behavior.

## vNext 2026-05.4 - Career-Focused Scope Correction

Restored COMPASS to careers and job-search scope while preserving TruthGuard, source-grounding, phase separation, and checkpointing.

## vNext 2026-05.3 - COMPASS-Only Canonicalization

Removed predecessor-name compatibility from active framework files and established COMPASS as the sole canonical framework name.

## vNext 2026-05.2 - Checkpoint Generation and Storage Disclosure

Required checkpoint artifacts at every committed Intake round and honest disclosure of datastore write capability.

## vNext 2026-05.1 - Generalization Experiment

Temporarily reframed COMPASS as field-agnostic. This behavior was superseded by the career-focused scope correction in vNext 2026-05.4.

## vNext 2026-05 - Intake Onboarding Baseline

Established the truth-first verified Source of Truth onboarding workflow, prompt-authority governance, DOCX-first resume behavior, and the initial repository baseline.

## Change Management Rules

When changing COMPASS:

1. Update the relevant framework or rule file.
2. Update `VERSION.md` when behavior changes materially.
3. Add a changelog entry explaining the change.
4. Preserve backward compatibility unless intentionally superseded.
5. Do not bury major behavior changes only inside launcher prompts.
