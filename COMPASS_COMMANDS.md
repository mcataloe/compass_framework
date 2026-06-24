# COMPASS Command Registry

This registry summarizes the active COMPASS command surface. Detailed behavior remains in the referenced rule and prompt files.

## Shared Source Priority

Candidate facts are resolved from current user instruction, verified Intake ledgers, approved canonical Source of Truth records, explicitly authorized provisional baselines, and then imported evidence. Target job descriptions and generated artifacts are contextual inputs rather than factual authorities.

## COMPASS Intake

**Launcher:** `prompts/compass-intake.md`

Creates or updates verified career Source of Truth records through evidence capture, Materiality Gate review, coverage tracking, claim decisions, and checkpoints.

Key files:

- `rules/07-compass-intake.md`
- `prompts/compass-intake.md`

## COMPASS Source Rebase

**Launcher:** `prompts/compass-source-rebase.md`

Compares an existing Source of Truth repository with the framework scaffold. It supports read-only dry-run and approved create-missing-only modes.

Key files:

- `rules/09-source-rebase.md`
- `templates/source-of-truth-scaffold/README.md`
- `templates/source-of-truth-scaffold/sources/seed/`
- `templates/source-of-truth-scaffold/sync/`
- `templates/source-of-truth-scaffold/migration/COMPASS_Source_Rebase_Report_TEMPLATE.md`
- `prompts/compass-source-rebase.md`

The `/sync/` scaffold contains the Source of Truth target-routing template used by Experience Sync.

## COMPASS Experience Sync

**Launcher:** `prompts/compass-experience-sync.md`

Reconciles approved Source of Truth records into a separate public or externally shareable experience repository.

Key files:

- `rules/11-experience-sync.md`
- `templates/source-of-truth-scaffold/sync/COMPASS_Experience_Targets.yaml`
- `templates/experience-sync/COMPASS_Experience_Manifest_TEMPLATE.yaml`
- `templates/experience-sync/COMPASS_Experience_Sync_Report_TEMPLATE.md`
- `templates/experience-sync/COMPASS_Public_Claim_TEMPLATE.yaml`
- `prompts/compass-experience-sync.md`

Modes:

- `dry-run` — incremental read-only reconciliation
- `full-audit` — complete read-only projection review
- `apply-approved` — approved target-branch changes followed by a pull request

Source-side routing maps stable target IDs to repository locations. Public target manifests use a stable source ID and sanitized reconciliation metadata.

Example triggers:

```text
Run COMPASS Experience Sync for public-experience.
Run COMPASS Experience Sync --full-audit.
Apply the approved COMPASS Experience Sync.
```

## COMPASS Analysis

**Launcher:** `prompts/compass-analysis.md`

Evaluates candidate fit, requirement-market realism, company and interview reality, risk, and pursuit economics.

Key files:

- `rules/01-analysis-workflow.md`
- `rules/04-truthguard.md`
- `rules/06-artifact-rules.md`
- `rules/10-opportunity-recon.md`
- `prompts/compass-analysis.md`

## COMPASS Tailored Resume

**Launcher:** `prompts/compass-tailored-resume.md`

Generates a role-specific resume from verified source records.

Key files:

- `rules/02-resume-generation.md`
- `rules/04-truthguard.md`
- `rules/06-artifact-rules.md`
- `rules/08-human-authenticity.md`

## COMPASS Recruiter-Targeted Resume

**Launcher:** `prompts/recruiter-targeted-resume.md`

Generates a broader recruiter-facing resume for related senior opportunities using the same resume, TruthGuard, artifact, and Human Authenticity rules.

## COMPASS Cover Letter

**Launcher:** `prompts/compass-cover-letter.md`

Generates a source-grounded cover letter using cover-letter rules, TruthGuard, artifact rules, and Human Authenticity rules.

## Additional Supported Artifacts

Supported outputs also include canonical records, claim ledgers, coverage registers, Experience Sync reports, public claim indexes, recruiter responses, application answers, follow-up messages, interview preparation, and compensation notes.

## Maintenance

Command changes should update this registry, the corresponding launcher and durable rules, the framework README, changelog, and version when behavior changes materially.
