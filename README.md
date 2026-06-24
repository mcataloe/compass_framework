# COMPASS Framework

COMPASS is a career-focused, source-grounded framework for turning messy career inputs into verified, defensible job-search outputs.

COMPASS stands for:

> Capture, Organize, Map, Probe, Approve, Synthesize, Store

The framework is designed to answer a reusable career question:

> Can a recruiter or hiring team quickly understand the candidate's value, evidence, risks, assumptions, opportunity reality, and defensible next action?

COMPASS is the canonical framework. New work should use COMPASS terminology and canonical files.

## Canonical Source Files

Use these files as the active source of truth:

- `VERSION.md` — current framework version and status
- `COMPASS_Current.md` — canonical active framework definition
- `COMPASS_COMMANDS.md` — canonical user-facing command registry
- `COMPASS_Changelog.md` — framework change history
- `rules/` — durable behavior rules
- `rules/07-compass-intake.md` — COMPASS Intake source-of-truth onboarding and claim verification rules
- `rules/08-human-authenticity.md` - truthful human-authenticity and reviewer-signal rules for external artifacts
- `rules/09-source-rebase.md` - safe source-of-truth scaffold alignment rules
- `rules/10-opportunity-recon.md` - Purple Squirrel Factor, company and interview reality, external-evidence handling, and pursuit economics
- `rules/11-experience-sync.md` - one-way Source of Truth reconciliation into a public or externally shareable experience repository
- `prompts/` — reusable prompt templates
- `prompts/compass-intake.md` — reusable COMPASS Intake launcher prompt
- `prompts/compass-source-rebase.md` - reusable COMPASS Source Rebase launcher prompt
- `prompts/compass-experience-sync.md` - reusable COMPASS Experience Sync launcher prompt
- `prompts/compass-analysis.md` — reusable COMPASS analysis launcher prompt
- `prompts/compass-tailored-resume.md` — reusable tailored resume launcher prompt
- `prompts/recruiter-targeted-resume.md` — reusable recruiter-targeted resume launcher prompt
- `prompts/compass-cover-letter.md` — reusable cover letter launcher prompt
- `prompts/compass-recruiter-response.md` — reusable recruiter response launcher prompt
- `prompts/compass-application-answer.md` — reusable application answer launcher prompt
- `prompts/compass-follow-up-message.md` — reusable follow-up message launcher prompt
- `prompts/compass-interview-prep.md` — reusable interview preparation launcher prompt
- `prompts/compass-compensation-note.md` — reusable compensation and remote-work note launcher prompt
- `examples/` — example output patterns
- `examples/compass-intake-artifact-templates.md` - copy-ready COMPASS Intake artifact skeletons
- `examples/seed-artifacts/SEED_ARTIFACTS_MANIFEST_EXAMPLE.md` - fictional seed artifact manifest example
- `templates/source-of-truth-scaffold/` - framework-owned source-of-truth scaffold and report templates
- `templates/source-of-truth-scaffold/sources/seed/` - recommended scaffold location for Initial Seed Artifacts
- `templates/source-of-truth-scaffold/sync/` - private Source of Truth routing templates for downstream experience targets
- `templates/experience-sync/` - sanitized target manifest, reconciliation report, and public claim provenance templates

Compatibility shims for earlier naming have been removed. Prompt templates and rule files should use COMPASS terminology only.

## COMPASS Commands

The active user-facing command surface is defined in `COMPASS_COMMANDS.md`.

Current first-class commands:

- COMPASS Intake
- COMPASS Source Rebase
- COMPASS Experience Sync
- COMPASS Analysis
- COMPASS Tailored Resume
- COMPASS Recruiter-Targeted Resume
- COMPASS Cover Letter

Additional supported artifact requests are governed by `rules/06-artifact-rules.md` and the relevant framework rules.

## COMPASS Analysis and Opportunity Reality

COMPASS Analysis evaluates candidate fit and opportunity reality as related but separate questions.

For identifiable-company role analysis, the strict analysis report includes:

- candidate evidence and material gaps;
- the Purple Squirrel Factor and requirement-market realism;
- company background and employee-sentiment research when current external access is available;
- recent comparable technical interview reports and interview-realism assessment;
- risk, constraints, and sustainability;
- recommendation and pursuit economics.

The Purple Squirrel Factor evaluates how rare, compressed, or historically implausible the employer's requested profile is. It does not make the candidate more qualified and does not automatically justify applying.

Company and interview research must preserve entity identity, source type, recency, role relevance, sample limitations, and confidence. Anonymous reviews are reported sentiment, not verified facts. Sparse or inaccessible evidence should be reported as `Insufficient` rather than guessed.

Pursuit economics evaluates whether the opportunity merits the candidate's application and preparation time based on evidence, gaps, access path, posting signals, compensation, level, remote-work alignment, strategic value, effort, opportunity cost, and stronger alternatives.

Durable behavior is defined in `rules/01-analysis-workflow.md`, `rules/04-truthguard.md`, `rules/06-artifact-rules.md`, and `rules/10-opportunity-recon.md`.

## COMPASS Intake

COMPASS Intake is the verified source-of-truth onboarding workflow for creating or updating a durable career source of truth.

Use Intake when a career record, job-search profile, resume source set, recruiter positioning file, interview-prep record, or other career source needs a durable source of truth.

Intake accepts source documents such as prior resumes, cover letters, LinkedIn exports, performance reviews, certification records, portfolio notes, recruiter notes, interview notes, job descriptions, achievement lists, project summaries, or other career reference material. These sources are treated as evidence leads, not automatic truth. After their material claims are ingested, reconciled, and verified, the canonical source-of-truth record and approved ledgers supersede the imported artifacts for downstream use.

Initial Seed Artifacts are user-provided source materials stored under `/sources/seed/` when the scaffold is available. Seed artifacts may include existing resumes, shortened resumes, comprehensive resumes, master CVs, LinkedIn exports, cover letters, portfolio summaries, achievement lists, or similar career evidence. They are seed, provisional, evidence, and not canonical. They may support Provisional Resume / CV Mode while Intake is incomplete, but verified Intake records, approved claim ledgers, and do-not-claim ledgers supersede them when available.

Intake asks generally 3-5 questions per response or batch. That limit is a pacing rule, not a scope limit; Intake should continue in small batches until material imported claims are covered, intentionally paused, deferred, rejected, excluded as not material, or marked as needing evidence, metrics, or scope clarification.

Before asking Intake questions, Intake runs a Materiality Gate: inspect available approved ledgers, do-not-claim records, coverage registers, checkpoint records, canonical source records, and relevant source artifacts first. Ask only unresolved material questions whose answers would change source-of-truth construction, claim approval, claim depth, evidence requirements, or downstream-safe wording. If context is sufficient, proceed with the source basis and safe assumptions instead of asking redundant questions.

Default setup for non-technical users:

1. Create a Google Drive folder named `COMPASS Source of Truth`.
2. Add useful source documents to that folder.
3. Copy the folder link.
4. Add the folder link to the ChatGPT Project sources.
5. Start Intake using `prompts/compass-intake.md`.

GitHub remains optional for end users. Technical users may fork this repository or maintain their own optimized COMPASS framework source.

COMPASS Intake must support pause/resume behavior. Users may say `I need a break`, `pause`, `bookmark this`, or `let's continue later`; COMPASS should stop asking new questions and emit a checkpoint that can be resumed later.

A checkpoint is a progress commit, not proof of full source coverage. Intake complete means the relevant material imported claims are captured in the coverage register and resolved into approved, narrowed, rejected, evidence-needed, metric-needed, scope-needed, deferred, or excluded status.

Every committed Intake round should use stable artifact templates for the checkpoint Markdown record, claim-ledger entries, do-not-claim entries, coverage-register entries, storage-status block, and optional ZIP bundle manifest. The durable requirements are defined in `rules/07-compass-intake.md`; copy-ready skeletons are available in `examples/compass-intake-artifact-templates.md`.

Intake storage behavior must be honest:

- Before asking setup questions, disclose whether direct write/update access to the requested datastore is available.
- If direct Google Drive write/update access is available, save or update the Intake source-of-truth files in the user's selected folder.
- If direct write/update access is unavailable or uncertain, produce downloadable or copy-ready checkpoint files and clearly tell the user what to save where.
- When practical, package changed checkpoint files into a downloadable ZIP bundle for upload to the target datastore.
- Never claim that files were saved when they were only generated in chat, generated locally, or offered for download.

## COMPASS Source Rebase

COMPASS Source Rebase is the safe scaffold-alignment workflow for existing COMPASS source-of-truth repositories.

Use Source Rebase when a framework upgrade changes the recommended source-of-truth scaffold and the user wants to identify or create missing scaffold directories or placeholder files without disturbing existing source records.

Source Rebase defaults to dry-run mode. It may inspect structure and produce a report, but it must not overwrite, delete, rename, move, edit, or otherwise modify existing user-owned files.

The first permitted write mode is `create-missing-only`, and it requires explicit user approval for the exact target. In that mode, COMPASS may create only absent scaffold directories or absent framework placeholder files, including missing `/sources/seed/` and `/sync/` scaffold paths. Existing paths are always skipped and reported.

The optional `/sync/COMPASS_Experience_Targets.yaml` file belongs in the private Source of Truth and stores actual downstream target locations and publication defaults. Source Rebase may create only the generic missing scaffold; populating real repository mappings requires a separate explicit configuration instruction.

Historical checkpoint files, including older `COMPASS_Layer0_*` files, must be preserved and reported as historical paths. Source Rebase must not rename or normalize them for terminology cleanliness.

Source Rebase is not COMPASS Intake or Experience Sync. It does not verify, extract, reconcile, approve, reject, publish, or modify career claims.

## COMPASS Experience Sync

COMPASS Experience Sync reconciles an approved COMPASS Source of Truth into a separate public or externally shareable experience repository.

The workflow is one-way: the Source of Truth remains authoritative, while the experience repository is a downstream publication artifact. Experience Sync never modifies the Source of Truth and never uses the public repository as factual authority.

The private Source of Truth should maintain the authoritative routing map at `sync/COMPASS_Experience_Targets.yaml`. That file may contain actual source and target repository locations, stable target IDs, branches, publication defaults, protected paths, and write policy.

The public experience repository should use a sanitized `COMPASS_Experience_Manifest.yaml` containing a stable source identifier and reconciliation metadata rather than the private Source of Truth repository name or URL.

Experience Sync defaults to `dry-run`. It may compare source records, claim ledgers, do-not-claim controls, coverage status, source-side routing, public files, structured claims, and prior reconciliation metadata, but it performs no writes.

`full-audit` rechecks the entire public projection and is appropriate for first-time setup, suspected drift, manual target edits, missing manifest history, publication-policy changes, major framework changes, or migration away from a public manifest that exposed private source routing.

`apply-approved` requires a current matching dry-run or full-audit report and explicit user approval. It writes only to a non-default target branch, updates sanitized reconciliation metadata, opens a pull request, and does not merge unless explicitly instructed.

Truth approval and public suitability are separate gates. Approved facts may still be withheld or abstracted when they contain personal information, private strategy, colleague names, customer-sensitive details, security-sensitive details, raw Intake material, or unnecessary operational specifics.

Durable behavior is defined in `rules/11-experience-sync.md`. The launcher is `prompts/compass-experience-sync.md`. Private routing templates are under `templates/source-of-truth-scaffold/sync/`, and sanitized target-repository templates are under `templates/experience-sync/`.

## Career Profile

COMPASS is career-focused. The active profile is the careers / job-search profile: role evaluation, hiring-manager scan optimization, ATS and semantic alignment, requirement-market realism, company and interview research, pursuit economics, master CV claim-ledger construction, truth-preserving resume tailoring, cover letters, recruiter-specific positioning, compensation and remote-work risk analysis, interview objection prediction, and evidence mapping from source records to job descriptions.

Generated artifacts must follow the strict output templates in `rules/06-artifact-rules.md` unless the user explicitly requests a different format. Prompt templates are launchers and must defer to the active rule files for artifact section order, source priority, TruthGuard, Opportunity Reality Layer behavior, and clean-deliverable requirements.

External career artifacts should also follow `rules/08-human-authenticity.md` so resumes, cover letters, recruiter responses, application answers, follow-up messages, and similar deliverables remain specific, source-grounded, natural, reviewer-readable, and interview-defensible without using fake humanization or AI-detector evasion tactics.

## Branch Policy

The `main` branch is canonical.

Anything merged to `main` is considered the active COMPASS framework unless an instruction explicitly points to another branch, tag, or commit.

## Memory and Context Policy

ChatGPT memory may contain user preferences, but this repository should override memory for COMPASS behavior when there is a conflict.

If repository access fails, the assistant should say so clearly and should not reconstruct COMPASS rules from memory unless explicitly authorized.

## Source-of-Truth Policy

COMPASS outputs must use the user's current direct instruction, verified Intake claim ledger, do-not-claim list, and latest approved source-of-truth record before relying on imported artifacts, including Initial Seed Artifacts, as evidence. Target job descriptions and recruiter requests provide terminology and context only; they do not create experience the user does not have. Generated artifacts are downstream outputs, not factual authorities, unless separately imported and verified through Intake.

COMPASS must not invent technologies, ownership, certifications, credentials, metrics, employers, responsibilities, project history, career achievements, market statistics, company facts, or other material claims.
