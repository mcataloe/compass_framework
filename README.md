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
- `COMPASS_Changelog.md` — framework change history
- `rules/` — durable behavior rules
- `rules/07-source-of-truth-onboarding.md` — Layer 0 source-of-truth onboarding and claim verification rules
- `prompts/` — reusable prompt templates
- `prompts/compass-layer0-source-of-truth.md` — reusable Layer 0 onboarding launcher prompt
- `examples/` — example output patterns

Compatibility shims for earlier naming have been removed. Prompt templates and rule files should use COMPASS terminology only.

## Layer 0 Source-of-Truth Onboarding

Layer 0 is COMPASS's verified source-of-truth onboarding workflow.

Use Layer 0 when a career record, job-search profile, resume source set, recruiter positioning file, interview-prep record, or other career source needs a durable source of truth.

Layer 0 accepts source documents such as prior resumes, cover letters, LinkedIn exports, performance reviews, certification records, portfolio notes, recruiter notes, interview notes, job descriptions, achievement lists, project summaries, or other career reference material. These sources are treated as evidence leads, not automatic truth.

Default setup for non-technical users:

1. Create a Google Drive folder named `COMPASS Source of Truth`.
2. Add useful source documents to that folder.
3. Copy the folder link.
4. Add the folder link to the ChatGPT Project sources.
5. Start Layer 0 using `prompts/compass-layer0-source-of-truth.md`.

GitHub remains optional for end users. Technical users may fork this repository or maintain their own optimized COMPASS framework source.

Layer 0 must support pause/resume behavior. Users may say `I need a break`, `pause`, `bookmark this`, or `let's continue later`; COMPASS should stop asking new questions and emit a checkpoint that can be resumed later.

Layer 0 storage behavior must be honest:

- Before asking setup questions, disclose whether direct write/update access to the requested datastore is available.
- If direct Google Drive write/update access is available, save or update the Layer 0 source-of-truth files in the user's selected folder.
- If direct write/update access is unavailable or uncertain, produce downloadable or copy-ready checkpoint files and clearly tell the user what to save where.
- When practical, package changed checkpoint files into a downloadable ZIP bundle for upload to the target datastore.
- Never claim that files were saved when they were only generated in chat, generated locally, or offered for download.

## Career Profile

COMPASS is career-focused. The active profile is the careers / job-search profile: role evaluation, hiring-manager scan optimization, ATS and semantic alignment, master CV claim-ledger construction, truth-preserving resume tailoring, cover letters, recruiter-specific positioning, compensation and remote-work risk analysis, interview objection prediction, and evidence mapping from source records to job descriptions.

## Branch Policy

The `main` branch is canonical.

Anything merged to `main` is considered the active COMPASS framework unless an instruction explicitly points to another branch, tag, or commit.

## Memory and Context Policy

ChatGPT memory may contain user preferences, but this repository should override memory for COMPASS behavior when there is a conflict.

If repository access fails, the assistant should say so clearly and should not reconstruct COMPASS rules from memory unless explicitly authorized.

## Source-of-Truth Policy

COMPASS outputs must use the latest approved source-of-truth record, verified Layer 0 claim ledger when available, do-not-claim list when available, or user-provided source material for the session.

COMPASS must not invent technologies, ownership, certifications, credentials, metrics, employers, responsibilities, project history, career achievements, or other career claims.
