# COMPASS Framework

COMPASS is a career-focused, source-grounded framework for turning messy career inputs into verified, defensible job-search outputs.

COMPASS stands for:

> Capture, Organize, Map, Probe, Approve, Synthesize, Store

The framework is designed to answer a reusable career question:

> Can a recruiter or hiring team quickly understand the candidate's value, evidence, risks, assumptions, and defensible next action?

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
- `prompts/` — reusable prompt templates
- `prompts/compass-intake.md` — reusable COMPASS Intake launcher prompt
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

Compatibility shims for earlier naming have been removed. Prompt templates and rule files should use COMPASS terminology only.

## COMPASS Commands

The active user-facing command surface is defined in `COMPASS_COMMANDS.md`.

Current first-class commands:

- COMPASS Intake
- COMPASS Analysis
- COMPASS Tailored Resume
- COMPASS Recruiter-Targeted Resume
- COMPASS Cover Letter

Additional supported artifact requests are governed by `rules/06-artifact-rules.md` and the relevant framework rules.

## COMPASS Intake

COMPASS Intake is the verified source-of-truth onboarding workflow for creating or updating a durable career source of truth.

Use Intake when a career record, job-search profile, resume source set, recruiter positioning file, interview-prep record, or other career source needs a durable source of truth.

Intake accepts source documents such as prior resumes, cover letters, LinkedIn exports, performance reviews, certification records, portfolio notes, recruiter notes, interview notes, job descriptions, achievement lists, project summaries, or other career reference material. These sources are treated as evidence leads, not automatic truth. After their material claims are ingested, reconciled, and verified, the canonical source-of-truth record and approved ledgers supersede the imported artifacts for downstream use.

Intake asks generally 3-5 questions per response or batch. That limit is a pacing rule, not a scope limit; Intake should continue in small batches until material imported claims are covered, intentionally paused, deferred, rejected, excluded as not material, or marked as needing evidence, metrics, or scope clarification.

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

## Career Profile

COMPASS is career-focused. The active profile is the careers / job-search profile: role evaluation, hiring-manager scan optimization, ATS and semantic alignment, master CV claim-ledger construction, truth-preserving resume tailoring, cover letters, recruiter-specific positioning, compensation and remote-work risk analysis, interview objection prediction, and evidence mapping from source records to job descriptions.

Generated artifacts must follow the strict output templates in `rules/06-artifact-rules.md` unless the user explicitly requests a different format. Prompt templates are launchers and must defer to the active rule files for artifact section order, source priority, TruthGuard, and clean-deliverable requirements.

External career artifacts should also follow `rules/08-human-authenticity.md` so resumes, cover letters, recruiter responses, application answers, follow-up messages, and similar deliverables remain specific, source-grounded, natural, reviewer-readable, and interview-defensible without using fake humanization or AI-detector evasion tactics.

## Branch Policy

The `main` branch is canonical.

Anything merged to `main` is considered the active COMPASS framework unless an instruction explicitly points to another branch, tag, or commit.

## Memory and Context Policy

ChatGPT memory may contain user preferences, but this repository should override memory for COMPASS behavior when there is a conflict.

If repository access fails, the assistant should say so clearly and should not reconstruct COMPASS rules from memory unless explicitly authorized.

## Source-of-Truth Policy

COMPASS outputs must use the user's current direct instruction, verified Intake claim ledger, do-not-claim list, and latest approved source-of-truth record before relying on imported artifacts as evidence. Target job descriptions and recruiter requests provide terminology and context only; they do not create experience the user does not have. Generated artifacts are downstream outputs, not factual authorities, unless separately imported and verified through Intake.

COMPASS must not invent technologies, ownership, certifications, credentials, metrics, employers, responsibilities, project history, career achievements, or other career claims.
