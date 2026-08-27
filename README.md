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
- `rules/07-compass-intake.md` — COMPASS Intake source-of-truth onboarding, persistence-contract resolution, and claim verification rules
- `rules/08-human-authenticity.md` — truthful human-authenticity and reviewer-signal rules for external artifacts
- `rules/09-source-rebase.md` — safe source-of-truth scaffold alignment and retired-path rules
- `rules/10-opportunity-recon.md` — Purple Squirrel Factor, company and interview reality, external-evidence handling, and pursuit economics
- `rules/11-experience-sync.md` — one-way Source of Truth reconciliation into a public or externally shareable experience repository
- `rules/12-verified-opportunity-search.md` — current-opportunity discovery, live verification, alignment scoring, conversion-condition ranking, and optional secondary contract search
- `rules/13-opportunity-registry.md` — optional persistent opportunity registry and append-only search-run records
- `rules/14-recruiter-legitimacy-risk.md` — recruiter, company, entity-chain, application-path, process-safety, and information-sharing risk gate
- `rules/15-opportunity-unique-questions.md` — opportunity-specific interview question design grounded in unresolved decision value
- `rules/16-resume-release-assurance.md` — deterministic resume staging, validation, manifest, and atomic-release assurance
- `rules/17-comprehensive-career-cv.md` — comprehensive approved career-history compilation, role coverage, audience variants, disclosure, and publication boundaries
- `rules/18-opportunity-search-breadth-telemetry.md` — measurable search breadth, named-source attempts, substitutions, coverage gates, rotation, and reconciled telemetry
- `rules/19-recruiter-fit-brief.md` — optional recruiter-facing fit brief generation, disclosure, leakage, safety, and action boundaries
- `schemas/resume-release/` — machine-readable resume release, manifest, employment-coverage, and visual-review-attestation contracts
- `tools/resume_release/` — executable standard-library resume validator and atomic-release interface
- `prompts/` — reusable prompt templates
- `prompts/compass-intake.md` — reusable COMPASS Intake launcher prompt
- `prompts/compass-source-rebase.md` — reusable COMPASS Source Rebase launcher prompt
- `prompts/compass-experience-sync.md` — reusable COMPASS Experience Sync launcher prompt
- `prompts/compass-analysis.md` — reusable COMPASS analysis launcher prompt
- `prompts/compass-verified-opportunity-search.md` — reusable verified opportunity-search launcher prompt
- `prompts/compass-tailored-resume.md` — reusable tailored resume launcher prompt
- `prompts/recruiter-targeted-resume.md` — reusable recruiter-targeted resume launcher prompt
- `prompts/compass-comprehensive-career-cv.md` — reusable comprehensive career CV launcher prompt
- `prompts/compass-cover-letter.md` — reusable cover letter launcher prompt
- `prompts/compass-recruiter-response.md` — reusable recruiter response launcher prompt
- `prompts/compass-application-answer.md` — reusable application answer launcher prompt
- `prompts/compass-follow-up-message.md` — reusable follow-up message launcher prompt
- `prompts/compass-interview-prep.md` — reusable interview preparation launcher prompt
- `prompts/compass-compensation-note.md` — reusable compensation and remote-work note launcher prompt
- `examples/` — example output patterns
- `examples/compass-intake-artifact-templates.md` — copy-ready COMPASS default Intake artifact skeletons
- `examples/seed-artifacts/SEED_ARTIFACTS_MANIFEST_EXAMPLE.md` — fictional seed artifact manifest example
- `templates/source-of-truth-scaffold/` — framework-owned generic source-of-truth scaffold and report templates
- `templates/source-of-truth-scaffold/sources/seed/` — generic recommended scaffold location for Initial Seed Artifacts
- `templates/source-of-truth-scaffold/sync/` — private Source of Truth routing templates for downstream experience targets
- `templates/experience-sync/` — sanitized target manifest, reconciliation report, and public claim provenance templates
- `templates/comprehensive-career-cv/` — candidate-neutral comprehensive career CV template
- `templates/opportunity-registry/` — opportunity registry and append-only search-run templates
- `templates/recruiter-fit-brief/` — candidate-neutral strict Recruiter Fit Brief template
- `examples/recruiter-fit-brief-acceptance-scenarios.md` — candidate-neutral acceptance and regression scenarios

Compatibility shims for earlier naming have been removed. Prompt templates and rule files should use COMPASS terminology only.

## COMPASS Commands

The active user-facing command surface is defined in `COMPASS_COMMANDS.md`.

Current first-class commands:

- COMPASS Intake
- COMPASS Source Rebase
- COMPASS Experience Sync
- COMPASS Analysis
- COMPASS Verified Opportunity Search
- COMPASS Tailored Resume
- COMPASS Recruiter-Targeted Resume
- COMPASS Comprehensive Career CV
- COMPASS Cover Letter

Additional supported artifact requests are governed by `rules/06-artifact-rules.md` and the relevant framework rules. Recruiter-legitimacy risk reports are supported artifacts when the user asks whether a recruiter, company, role, application path, staffing chain, or requested next action is safe enough to continue.

## COMPASS Analysis and Opportunity Reality

COMPASS Analysis evaluates candidate fit and opportunity reality as related but separate questions for an identified role. The optional `--recruiter-brief` flag requests a separate recruiter-facing derivative after the complete private analysis.

For identifiable-company role analysis, the strict analysis report includes:

- candidate evidence and material gaps;
- the Purple Squirrel Factor and requirement-market realism;
- company background and employee-sentiment research when current external access is available;
- recent comparable technical interview reports and interview-realism assessment;
- recruiter-legitimacy, entity-chain, domain, application-path, sensitive-work, and process-safety review when applicable;
- risk, constraints, and sustainability;
- recommendation and pursuit economics.

The Purple Squirrel Factor evaluates how rare, compressed, or historically implausible the employer's requested profile is. It does not make the candidate more qualified and does not automatically justify applying.

Company and interview research must preserve entity identity, source type, recency, role relevance, sample limitations, and confidence. Anonymous reviews are reported sentiment, not verified facts. Sparse or inaccessible evidence should be reported as `Insufficient` rather than guessed.

Recruiter Legitimacy and Opportunity Risk evaluates whether the recruiter, staffing firm, employer of record, direct employer, client, end customer, domain, application path, communication channel, and requested next action are verified enough to continue safely. Legitimacy concerns do not alter candidate-fit scoring; they change the recommended action, verification boundary, and information-sharing boundary.

Pursuit economics evaluates whether the opportunity merits the candidate's application and preparation time based on evidence, gaps, access path, posting signals, compensation, level, remote-work alignment, strategic value, effort, opportunity cost, and stronger alternatives.

With `--recruiter-brief`, COMPASS may generate a 300–500 word external brief that leads with supported value, separates direct from adjacent evidence, names material gaps precisely, and states an accurate submission posture. The brief excludes internal scores, ATS notes, research, risk analysis, strategy, and evidence-control mechanics. It is created through its own template, never by shortening the analysis, and generation never sends or attaches it.

Durable behavior is defined in `rules/01-analysis-workflow.md`, `rules/04-truthguard.md`, `rules/06-artifact-rules.md`, `rules/10-opportunity-recon.md`, `rules/14-recruiter-legitimacy-risk.md` when applicable, and `rules/19-recruiter-fit-brief.md` when the flag is active.

## COMPASS Verified Opportunity Search

COMPASS Verified Opportunity Search discovers and ranks multiple current opportunities.

The workflow separates:

1. eligibility and hard-screen compatibility;
2. evidence-backed alignment;
3. opportunity quality and career value;
4. conversion conditions such as freshness, access, visibility, saturation, and application friction;
5. recruiter-legitimacy risk when applicable;
6. contract utility when an optional secondary contract lane is active.

Alignment is a structured decision estimate, not a probability of interview, offer, or hire. A failed location, employment, credential, application, contract, or required-experience hard screen overrides the score.

Low visibility may improve pursuit economics, but it cannot qualify a weakly aligned role. Mainstream visibility may lower priority, but it does not automatically exclude an exceptionally aligned or verified access-advantaged role when the user's Source of Truth permits that exception.

The workflow verifies the official current posting and employer-controlled application flow for direct-employer roles, reconciles conflicting requisition versions, inspects accessible screening questions, suppresses configured duplicate or previously handled opportunities, and rechecks priority roles before reporting them. When user-specific policy configures named sources, it records one controlled-status attempt per applicable required or selected rotating source, uses approved substitutions for blocked paths, and evaluates numeric breadth, source coverage, title-family coverage, and telemetry reconciliation as independent gates.

Optional secondary contract modes are explicit:

```text
Run COMPASS Verified Opportunity Search --include-contracts.
Run COMPASS Verified Opportunity Search --contract-only.
Run COMPASS Verified Opportunity Search --include-contracts --max-contracts 3.
```

- `--include-contracts` preserves the user's configured primary search and adds a separately ranked secondary contract lane.
- `--contract-only` returns only the secondary contract lane.
- `--max-contracts N` caps contract results without weakening eligibility, alignment, verification, legitimacy, or utility gates.

Contract results must not be blended into the primary shortlist. Candidate alignment remains the evidence-backed fit estimate; contract utility separately evaluates structure-aware economics, hours, duration, continuity, flexibility, exclusivity, intellectual-property, conflict, notice, exit, interference, effort, technical relevance, and relationship value.

When user-specific policy permits it, a verified staffing-firm, employer-of-record, or identifiable recruiter-controlled requisition may support a secondary `Contact first` result even when no public client application exists. The accountable entity and current opportunity must be verified. Staffing firm, employer of record, direct client, and end customer remain distinct, and an undisclosed client remains unverified.

The reusable contract classifications are bridge, fractional / side, contract-to-hire, and unspecified contract structure. The default utility grades are `A — Strong secondary opportunity`, `B — Qualify first`, and `C — Weak utility`.

COMPASS does not infer contract rate, hours, duration, client identity, conversion value, exclusivity, or concurrent-employment compatibility. It separates application-stage readiness from agreement-stage review: missing pre-application terms may produce `Contact first`, while ordinary missing IP, confidentiality, termination, notice, non-solicitation, or comparable agreement language remains a later-stage review item unless the user's policy makes the exact term pre-application load-bearing.

User-specific policy may configure a minimum actionable-result objective separately from reporting caps. In that mode, baseline breadth is a checkpoint and the search continues through bounded adaptive expansion until the objective is satisfied or a configured ceiling, viability no-yield threshold, source exhaustion, access block, or safety boundary applies. Bounded exhaustion returns fewer results rather than weakening gates or searching indefinitely.

Recruiter-legitimacy concerns may require verification-first handling even when candidate alignment is strong.

Durable behavior is defined in `rules/12-verified-opportunity-search.md`, `rules/13-opportunity-registry.md`, `rules/18-opportunity-search-breadth-telemetry.md`, and `rules/14-recruiter-legitimacy-risk.md` when applicable. The launcher is `prompts/compass-verified-opportunity-search.md`.

## COMPASS Comprehensive Career CV

COMPASS Comprehensive Career CV compiles the currently approved career Source of Truth into one broad document for reviewers who need more depth than a targeted resume but do not want to navigate a repository.

The workflow:

- resolves every material role and project scope;
- assigns each canonical employment role an internal `detailed`, `compressed`, or `excluded` disposition;
- compiles rather than concatenates dossiers;
- preserves official titles, contribution depth, implementation stage, collaborator transitions, and outcome boundaries;
- supports `--recruiter`, `--public`, and `--both` audience modes;
- applies Experience Sync publication controls to public variants;
- keeps source records, claim statuses, evidence inventories, and private strategy outside the clean CV;
- preserves the generated CV as a downstream publication artifact rather than factual authority.

A comprehensive CV may be longer than a normal resume and can be ATS-readable without being role-optimized. Targeted resumes remain the default application artifact.

A downloadable comprehensive-CV DOCX is resume-class output and requires an applicable executable release contract. A conventional resume filename or section contract cannot be bypassed merely by relabeling the artifact.

Durable behavior is defined in `rules/17-comprehensive-career-cv.md`. The launcher is `prompts/compass-comprehensive-career-cv.md`.

## COMPASS Intake

COMPASS Intake is the verified Source-of-Truth onboarding workflow for creating or updating a durable career source of truth.

Use Intake when a career record, job-search profile, resume source set, recruiter positioning file, interview-prep record, or other career source needs a durable source of truth.

Intake accepts source documents such as prior resumes, cover letters, LinkedIn exports, performance reviews, certification records, portfolio notes, recruiter notes, interview notes, job descriptions, achievement lists, project summaries, or other career reference material. These sources are treated as evidence leads, not automatic truth. After their material claims are ingested, reconciled, and verified, the governing current Source-of-Truth authority supersedes the imported artifact for downstream use. Under the generic default persistence model, separate approved-claim and do-not-claim ledgers remain current controls when present; an explicit repository-defined canonical persistence contract may instead place equivalent controls in the governing current record.

Initial Seed Artifacts are user-provided source materials stored under `/sources/seed/` when the generic scaffold path is active. They are seed, provisional, evidence, and not canonical. They may support Provisional Resume / CV Mode while Intake is incomplete. A current user-owned repository lifecycle may explicitly retire superseded seed paths after complete ingestion when required lineage is preserved elsewhere; Source Rebase must respect that explicit retirement and must not recreate the path.

Intake asks generally 3–5 questions per response or batch. That limit is a pacing rule, not a scope limit; Intake should continue in small batches until material imported claims are covered, intentionally paused, deferred, rejected, excluded as not material, or marked as needing evidence, metrics, or scope clarification.

Before asking Intake questions, Intake resolves the active persistence contract and runs a Materiality Gate against the current authorities required by that contract. Under default artifact persistence, this normally includes approved ledgers, do-not-claim records, coverage registers, checkpoints, canonical source records, and relevant source artifacts. Under explicit repository-defined canonical persistence, use the governing current canonical and cross-cutting authorities identified by current user-owned policy rather than requiring retired default artifacts. Ask only unresolved material questions whose answers would change Source-of-Truth construction, claim approval, claim depth, evidence requirements, or downstream-safe wording.

Default setup for non-technical users:

1. Create a Google Drive folder named `COMPASS Source of Truth`.
2. Add useful source documents to that folder.
3. Copy the folder link.
4. Add the folder link to the ChatGPT Project sources.
5. Start Intake using `prompts/compass-intake.md`.

GitHub remains optional for end users. Technical users may fork this repository or maintain their own optimized COMPASS framework source.

COMPASS Intake must support pause/resume behavior. If the user pauses, persist a resume point under the active persistence contract. Under default artifact persistence, this normally emits a checkpoint. Under explicit repository-defined canonical persistence, the current canonical record or designated workflow state may hold the resume point without an unnecessary parallel checkpoint file.

A persisted round boundary is a progress commit, not proof of full source coverage. Intake complete means the relevant material imported claims have durable coverage dispositions under the active persistence contract and are resolved into approved, narrowed, rejected, evidence-needed, metric-needed, scope-needed, deferred, or excluded status.

Every committed Intake round must persist the state required by the active persistence contract. The generic default uses stable checkpoint, claim-ledger, do-not-claim, coverage-register, storage-status, and optional ZIP-bundle templates defined in `rules/07-compass-intake.md` and `examples/compass-intake-artifact-templates.md`. An explicit repository-defined canonical persistence contract may update governing current authorities directly without mandatory parallel default artifacts, provided equivalent claim safety, coverage, pause/resume, retention, and storage-honesty guarantees remain intact.

Intake storage behavior must be honest:

- Before asking setup questions, disclose whether direct write/update access to the requested datastore is available.
- If direct write/update access is available, save or update the current Source-of-Truth state required by the active persistence contract.
- If direct write/update access is unavailable or uncertain, produce downloadable or copy-ready state in the shape required by the active persistence contract and clearly tell the user what to save where.
- Under the generic default model, changed checkpoint artifacts may be packaged into a ZIP bundle when practical.
- Never claim that files or Source-of-Truth state were saved when they were only generated in chat, generated locally, or offered for download.

## COMPASS Source Rebase

COMPASS Source Rebase is the safe scaffold-alignment workflow for existing COMPASS Source-of-Truth repositories.

Use Source Rebase when a framework upgrade changes the recommended generic scaffold and the user wants to identify or create missing scaffold directories or placeholder files without disturbing existing source records.

Source Rebase defaults to dry-run mode. It resolves the current user-owned Source Manifest when present before classifying drift, then derives a repository-specific expected scaffold from the generic framework scaffold. It must not overwrite, delete, rename, move, edit, or otherwise modify existing user-owned files.

The first permitted write mode is `create-missing-only`, and it requires explicit user approval for the exact target. In that mode, COMPASS may create only absent, non-retired scaffold directories or framework placeholder files. Existing paths are always skipped and reported. A path explicitly retired by current user-owned manifest policy is not missing drift and must not be proposed or recreated.

The optional `/sync/COMPASS_Experience_Targets.yaml` file belongs in the private Source of Truth and stores actual downstream target locations and publication defaults. Source Rebase may create only the generic missing scaffold when that path remains active; populating real repository mappings requires a separate explicit configuration instruction.

Historical preservation remains the generic default. Historical checkpoint files, including older `COMPASS_Layer0_*` files, must not be renamed or normalized merely for terminology cleanliness. When a current user-owned manifest explicitly retires a historical path from the active architecture, Source Rebase treats its absence as intentional and does not recreate it. If an explicitly retired path still exists, Source Rebase reports it and leaves it untouched; deletion is a separate repository-maintenance operation.

Source Rebase is not COMPASS Intake or Experience Sync. It does not verify, extract, reconcile, approve, reject, publish, lifecycle-delete, or modify career claims.

## COMPASS Experience Sync

COMPASS Experience Sync reconciles an approved COMPASS Source of Truth into a separate public or externally shareable experience repository.

The workflow is one-way: the Source of Truth remains authoritative, while the experience repository is a downstream publication artifact. Experience Sync never modifies the Source of Truth and never uses the public repository as factual authority.

The private Source of Truth should maintain the authoritative routing map at `sync/COMPASS_Experience_Targets.yaml`. That file may contain actual source and target repository locations, stable target IDs, branches, publication defaults, protected paths, and write policy.

The public experience repository should use a sanitized `COMPASS_Experience_Manifest.yaml` containing a stable source identifier and reconciliation metadata rather than the private Source of Truth repository name or URL.

Experience Sync defaults to `dry-run`. It may compare current approved source records and controls, coverage status, source-side routing, public files, structured claims, and prior reconciliation metadata, but it performs no writes and does not require a specific legacy persistence shape when the current Source of Truth defines an equivalent canonical model.

`full-audit` rechecks the entire public projection and is appropriate for first-time setup, suspected drift, manual target edits, missing manifest history, publication-policy changes, major framework changes, or migration away from a public manifest that exposed private source routing.

`apply-approved` requires a current matching dry-run or full-audit report and explicit user approval. It writes only to a non-default target branch, updates sanitized reconciliation metadata, opens a pull request, and does not merge unless explicitly instructed.

Truth approval and public suitability are separate gates. Approved facts may still be withheld or abstracted when they contain personal information, private strategy, colleague names, customer-sensitive details, security-sensitive details, raw Intake material, or unnecessary operational specifics.

Durable behavior is defined in `rules/11-experience-sync.md`. The launcher is `prompts/compass-experience-sync.md`. Private routing templates are under `templates/source-of-truth-scaffold/sync/`, and sanitized target-repository templates are under `templates/experience-sync/`.

## Career Profile

COMPASS is career-focused. The active profile is the careers / job-search profile: opportunity discovery, explicitly activated secondary contract search, role evaluation, hiring-manager scan optimization, ATS and semantic alignment, recruiter-legitimacy risk, compensation and remote-work risk, company and interview research, pursuit economics, recruiter responses, application answers, follow-up messages, interview preparation, comprehensive career CV generation, and source-grounded artifact generation.

Generated artifacts must follow the strict output templates in `rules/06-artifact-rules.md` unless the user explicitly requests a different format. Prompt templates are launchers and must defer to the active rule files for artifact section order, source priority, TruthGuard, Opportunity Reality Layer behavior, Verified Opportunity Search behavior, recruiter-legitimacy behavior, and clean-deliverable requirements.

Downloadable resume-class artifacts, including comprehensive career CV DOCX files, must also follow the release lifecycle in `rules/16-resume-release-assurance.md`. Drafts are staged as untrusted outputs and become final only when every required structural, content, rendered, and visual check is `PASS` and a matching manifest is written. Any `FAIL` or `UNKNOWN`, including unavailable rendering or missing current inputs, blocks final delivery.

The candidate-neutral implementation is `python -m tools.resume_release`. It inspects DOCX/OOXML structure, checks configured content and coverage, renders through supported system tools when required, records every-page review separately, emits a privacy-safe manifest, and publishes final paths only after aggregate `PASS`.

External career artifacts should also follow `rules/08-human-authenticity.md` so resumes, comprehensive CVs, cover letters, recruiter responses, application answers, follow-up messages, and similar deliverables remain specific, source-grounded, natural, reviewer-readable, and interview-defensible without using fake humanization or AI-detector evasion tactics.

## Branch Policy

The `main` branch is canonical.

Anything merged to `main` is considered the active COMPASS framework unless an instruction explicitly points to another branch, tag, or commit.

## Memory and Context Policy

ChatGPT memory may contain user preferences, but this repository should override memory for COMPASS behavior when there is a conflict.
