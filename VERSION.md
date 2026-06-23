# COMPASS Version

Current COMPASS Version: vNext 2026-05.9

Canonical Branch: main

Status: Active

Initialized: 2026-05-18

## Version Rule

The version declared here governs the active framework behavior when used from the `main` branch.

When COMPASS changes materially, update this file and `COMPASS_Changelog.md` in the same change set.

## Naming Rule

COMPASS is the only canonical framework name. New rules, prompts, examples, and project instructions must use COMPASS terminology.

## Active Behavior Notes

The active vNext 2026-05.9 framework includes COMPASS-only terminology, career-focused scope, COMPASS Intake checkpoint artifact behavior, COMPASS Source Rebase scaffold alignment, Initial Seed Artifact support, claim-depth-aware Staff / Principal resume positioning, and the Opportunity Reality Layer:

- COMPASS is a career-focused, source-grounded framework for turning messy career inputs into verified, defensible job-search outputs.
- COMPASS supports the careers / job-search profile. Product, strategy, research, consulting, grant, policy, and personal knowledge workflows are out of scope unless the project owner explicitly reopens scope.
- Core behavior remains truth-first, source-grounded, checkpointed, and claim-ledger-driven.
- COMPASS Analysis uses a strict 13-section report contract that separates candidate fit, requested-candidate rarity, company and interview reality, risk, TruthGuard, and pursuit economics.
- The Opportunity Reality Layer evaluates the Purple Squirrel Factor independently from candidate fit.
- Purple Squirrel scoring considers individual requirement rarity, intersection rarity, technology-maturity plausibility, role compression, level and compensation realism, and constraint stacking.
- Candidate scarcity or role compression never substitutes for candidate evidence and does not automatically justify applying.
- Identifiable-company analysis requires current company and interview research when external access is available, with entity disambiguation, source-tier handling, recency labels, role relevance, sample limitations, and confidence.
- Anonymous employee and candidate reviews remain attributed sentiment or reported accounts, not verified company facts.
- Pursuit economics considers evidence, material gaps, bridgeability, access path, posting signals, compensation, level, remote alignment, strategic value, effort, opportunity cost, and stronger alternatives.
- COMPASS Intake requires checkpoint artifact generation at every committed round.
- COMPASS Intake uses stable artifact templates for checkpoint records, claim-ledger entries, do-not-claim entries, coverage-register entries, storage-status blocks, and optional ZIP bundle manifests.
- COMPASS Intake requires coverage tracking for material imported claims; checkpoints are progress commits, not proof of full source ingestion.
- COMPASS Intake runs a Materiality Gate before asking questions: it inspects available approved ledgers, do-not-claim records, coverage registers, checkpoint records, canonical source records, and relevant source artifacts, then asks only unresolved material questions.
- COMPASS Source Rebase supports safe dry-run and explicitly approved create-missing-only scaffold alignment for source-of-truth repositories without overwriting, deleting, renaming, moving, or modifying existing user-owned records.
- COMPASS Source Rebase recognizes `/sources/seed/` as the recommended scaffold path for Initial Seed Artifacts and may create missing seed scaffold paths only in approved `create-missing-only` mode.
- COMPASS Source Rebase preserves historical checkpoint files such as older `COMPASS_Layer0_*` paths as historical records rather than normalizing names.
- Imported resumes, CVs, LinkedIn profiles, cover letters, portfolio examples, recruiter resumes, and prior generated artifacts are evidence inputs until their material claims are verified into the canonical source of truth.
- Initial Seed Artifacts under `/sources/seed/` are seed, provisional, evidence, and not canonical. They may support Provisional Resume / CV Mode while Intake is incomplete.
- Comprehensive resumes and master CVs may be stronger provisional baselines than shortened or tailored resumes, but neither becomes permanent canonical truth merely by being stored as a seed artifact.
- After verified ingestion, the canonical source-of-truth record, approved claim ledger, and do-not-claim register supersede imported artifacts for downstream use.
- Generated artifacts are downstream outputs, not factual authorities, unless separately imported and verified through Intake.
- Generated artifact types use strict output templates from `rules/06-artifact-rules.md` unless the user explicitly requests a different format.
- External career artifacts use `rules/08-human-authenticity.md` to preserve truthful specificity, reviewer readability, candidate-specific voice, ATS-safe structure, and interview-defensible claims without fake humanization or AI-detector evasion tactics.
- Senior-IC resumes use claim-depth-aware wording, preserve official employment titles, prioritize verified Staff / Principal evidence, and distinguish intended benefits from realized outcomes.
- Resume review should preserve useful technical depth while revising repeated architecture-taxonomy lists that obscure the candidate's action, decision, or consequence.
- Intake setup must disclose whether direct datastore writes are available before asking setup questions.
- If direct writes are unavailable, Intake must generate downloadable or copy-ready files and clearly instruct the user where to upload them.

## Compatibility Rule

Future COMPASS changes should preserve the core operating principles unless explicitly superseded:

- Truthful source-grounded output
- Phased workflow
- No fabricated technologies, metrics, credentials, employment history, project ownership, career achievements, business outcomes, market statistics, or company facts
- Separate strategic analysis from clean external generated artifacts
- Strict artifact output templates preserved unless the user explicitly requests a different format
- Career-profile rules may add specialized output rules without weakening source-grounding or TruthGuard
- Prompt templates remain workflow launchers and must defer to active rule files for workflow behavior
- External employer and interview evidence must preserve attribution, recency, confidence, and uncertainty
- COMPASS Intake remains the default process for building a canonical source record from unverified documents or a new user's history
- COMPASS Source Rebase remains scaffold alignment only and must not perform Intake, claim verification, or destructive source-record migration
- Initial Seed Artifacts remain provisional evidence and provenance until superseded by verified source-of-truth records and ledgers
