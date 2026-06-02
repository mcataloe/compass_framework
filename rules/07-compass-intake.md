# 07 — COMPASS Intake

This file governs COMPASS Intake: Verified Source-of-Truth Onboarding.

## Purpose

COMPASS Intake builds a verified source of truth from messy source material and user cross-examination.

Intake is not primarily an artifact-writing workflow. It is an evidence-capture, claim-verification, and canonical-record construction workflow.

## Default Non-Technical Setup

For most users:

1. Create a Google Drive folder named `COMPASS Source of Truth` or another project-specific source-of-truth folder.
2. Add source documents to that folder.
3. Copy the folder link.
4. Add the folder link to the ChatGPT Project sources when available.
5. Start Intake using `prompts/compass-intake.md`.

## Setup Verification and Storage Disclosure

At the beginning of Intake, COMPASS must inspect the available sources and storage capabilities.

Before asking setup questions, COMPASS must clearly tell the user whether it can directly write or update files in the requested datastore.

If direct write access is unavailable or uncertain, COMPASS must explain the fallback workflow:

1. Generate checkpoint artifacts as downloadable or copy-ready files.
2. Ask the user to upload those files into the target datastore.
3. Verify the files are visible in the datastore before treating them as persisted source-of-truth records.

COMPASS must not imply that anything has been saved unless it has actually written the file and verified it is visible in the datastore.

## Source Documents Are Evidence, Not Truth

Prior documents may be useful but imperfect.

COMPASS may harvest from them, but must not automatically trust them.

Imported resumes, CVs, LinkedIn profiles, cover letters, portfolio examples, recruiter resumes, prior generated artifacts, and similar materials are evidence inputs. They are not permanent factual authorities.

Once material claims from an imported artifact are extracted, reconciled, and verified into the canonical source-of-truth record and approved ledgers, the source-of-truth supersedes the imported artifact for downstream use.

Imported artifacts should remain traceable as provenance and history. Downstream artifacts must use the canonical source-of-truth record, approved claim ledger, and do-not-claim register first. Do not re-harvest old resumes, prior generated outputs, or other historical artifacts as if they are current truth after verified ingestion.

Generated resumes, cover letters, recruiter messages, application answers, LinkedIn drafts, interview notes, and portfolio drafts are downstream outputs. They are not factual authorities unless they are separately imported, extracted, reconciled, and verified through Intake.

## Initial Seed Artifacts

Initial Seed Artifacts are user-provided source materials available before or during COMPASS Intake. They should live under `/sources/seed/` in the user's source-of-truth repository when that scaffold is available.

Seed artifacts may include existing resumes, shortened or tailored resumes, comprehensive resumes, master CVs, LinkedIn exports, cover letters, portfolio summaries, achievement lists, or similar career evidence.

Seed artifacts are not COMPASS Intake-generated artifacts. They are seed, provisional, evidence, and not canonical. They may serve as practical pro tempore source material while the verified source of truth is still being built, but they must be labeled honestly and tracked as provenance.

Once relevant claims are extracted, reconciled, and verified into canonical source-of-truth records, approved claim ledgers, and do-not-claim ledgers, those verified Intake outputs supersede seed artifacts for downstream authority. Superseded seed artifacts should remain traceable as provenance and may be marked `archived-provenance`; COMPASS should not recommend deleting them unless the user explicitly chooses to remove them.

COMPASS must not limit the type of resume or CV a user uploads as a seed artifact. A comprehensive resume or master CV may reasonably remain useful for a longer provisional period because it is more likely to preserve career breadth. A shortened or tailored resume is useful evidence, but it is usually incomplete and should be treated more cautiously because it may omit material history or reflect one target role.

Allowed seed artifact status labels:

- `available-provisional`
- `partially-ingested`
- `fully-ingested`
- `superseded`
- `do-not-use`
- `archived-provenance`

Seed artifacts must not override verified claim ledgers, do-not-claim ledgers, canonical source-of-truth records, or the user's current direct instruction.

## Small-Batch Questioning

Ask 3-5 questions at a time unless the user asks for more.

The 3-5 question limit is a user-experience throttle per response or batch. It is not a limit of 3-5 questions per role, 3-5 questions per source artifact, or 3-5 questions total.

Intake must continue in small batches until the relevant imported source coverage is complete, intentionally paused, deferred, rejected, or marked as needing evidence, metrics, or scope clarification.

After each round, summarize confirmed facts, source-extracted claims, candidate inferred claims, contradictions, clarifying questions, approved claims, rejected claims, and claims needing evidence, metrics, or scope.

## Coverage Gate Rule

A role, project, artifact, or source file is not Intake-complete until every material imported claim has been captured in a coverage register or equivalent checkpoint metadata with one of these statuses:

- Imported / unreviewed
- Source-extracted / unconfirmed
- User-confirmed
- Approved
- Approved with narrowed wording
- Approved with claim-depth boundary
- Rejected / do-not-claim
- Needs evidence
- Needs metric
- Needs scope clarification
- Deferred intentionally
- Not material / excluded with reason

COMPASS must not imply that a source, role, project, or artifact has been fully ingested unless coverage has been verified.

## Canonical Source Priority

When Intake or downstream artifact generation must resolve conflicting sources, use this order:

1. User's current direct instruction
2. User-confirmed claim ledger and do-not-claim ledger
3. Canonical source-of-truth record
4. Imported artifacts as evidence and provenance only
5. Target job description, recruiter request, or opportunity record for terminology and context only
6. Generated artifacts as historical outputs only
7. Framework defaults and project memory only when not contradicted by stronger sources

Target job descriptions, recruiter requests, and opportunity records may identify useful terminology, selection criteria, and gaps. They must not create experience, skills, ownership, metrics, credentials, or facts the user does not have.

## Intake Completion Definition

Intake complete means all material claims from the relevant imported source set have been captured in the coverage register and resolved into approved, narrowed, rejected, evidence-needed, metric-needed, scope-needed, deferred, or excluded status.

Checkpoint created does not mean Intake complete. A checkpoint is a progress commit, not proof of full source coverage.

## Checkpoint Artifact Rule

Every committed Intake round must produce checkpoint artifacts.

A committed round means the user has resolved a batch of claims sufficiently for COMPASS to record a checkpoint.

Checkpoint artifacts should be treated like small git commits: each checkpoint captures the verified state at that moment and creates a recoverable backup before the workflow proceeds.

At minimum, each committed round should produce:

1. A checkpoint Markdown file for the round.
2. Any updated claim-ledger entries.
3. Any updated do-not-claim entries.
4. Any updated coverage-register entries or equivalent coverage metadata.
5. A storage-status statement.

When practical, COMPASS should also package changed checkpoint files into a downloadable ZIP bundle so the user can upload them into the datastore as a batch.

## Required Intake Artifact Templates

Every committed Intake round should use a stable artifact shape so checkpoints, ledgers, and coverage metadata can be resumed and reviewed without reconstructing context from chat.

Use `examples/compass-intake-artifact-templates.md` as the copy-ready example pack. The rule in this file remains the durable source of truth if an example needs adaptation.

### Checkpoint Markdown Record

Each checkpoint Markdown record should include:

1. Checkpoint status: workflow, checkpoint ID, round ID, date, current stage, source set covered, and whether the current source set is partial or complete.
2. Storage status: one approved storage-status label, direct-write availability, target datastore, generated or updated artifacts, and next save or verification action.
3. Round summary: confirmed facts, source-extracted claims reviewed, inferred claims asked as questions, contradictions resolved or still open, and unresolved questions.
4. Ledger changes: approved claims, narrowed claims, claim-depth boundaries, rejected or do-not-claim items, and claims needing evidence, metrics, scope clarification, deferral, or exclusion.
5. Coverage changes: each material imported claim reviewed in the round with source/provenance, current status, and next action.
6. Resume point: where Intake should continue next, including the next uncovered source section, role, project, or claim group.

### Claim Ledger Entries

Each claim-ledger entry should include:

1. Claim ID.
2. Claim text as extracted or proposed.
3. Source or provenance.
4. Status from the coverage gate status set.
5. Approved wording when applicable.
6. Claim-depth boundary when applicable.
7. Evidence, metric, scope, deferral, or exclusion note when applicable.
8. Last reviewed date or checkpoint ID.

Approved, narrowed, and claim-depth-bounded entries may support downstream artifacts. Needs-evidence, needs-metric, needs-scope, deferred, excluded, rejected, and do-not-claim entries must not be used as output-ready claims.

### Do-Not-Claim Entries

Each do-not-claim entry should include:

1. Rejected claim or prohibited wording.
2. Source or provenance that introduced the claim.
3. Reason for rejection or boundary.
4. Downstream block instruction.
5. Last reviewed date or checkpoint ID.

Do-not-claim entries must override target-document keyword pressure and must block downstream artifacts from reintroducing the rejected claim.

### Coverage-Register Entries

Each coverage-register entry should include:

1. Coverage ID.
2. Source artifact, source section, role, project, or claim group.
3. Material claim text or summary.
4. Provenance note.
5. Current status from the coverage gate status set.
6. Resolution note or next action.
7. Last reviewed date or checkpoint ID.

Every material imported claim should have one coverage-register entry or equivalent checkpoint metadata before the source, role, project, or artifact is treated as Intake-complete.

### Storage-Status Block

Each checkpoint response and checkpoint Markdown record should include:

1. One approved storage-status label.
2. Direct-write availability: true, false, or unknown.
3. Target datastore.
4. Files generated or updated.
5. Whether datastore visibility was verified.
6. Next safe action.

COMPASS must not state or imply that a checkpoint, ledger, register, or source-of-truth record was saved unless it was actually written and verified in the target datastore.

### Optional ZIP Bundle Manifest

When changed checkpoint artifacts are packaged into a ZIP bundle, include a manifest with:

1. Bundle filename.
2. Included files.
3. Checkpoint ID and round ID.
4. Storage status.
5. Upload destination.
6. Verification instruction.

## Recommended Checkpoint File Pattern

Use stable, sortable filenames.

```text
COMPASS_Intake_Round##_Topic_YYYY-MM-DD.md
```

Examples:

```text
COMPASS_Intake_Round00_Setup_2026-05-26.md
COMPASS_Intake_Round1A_Improvix_IntakeAtState_2026-05-26.md
COMPASS_Intake_Round1B_Improvix_MetricsPlatform_2026-05-26.md
```

## Recommended Datastore Layout

For folder-based storage, use a simple structure:

```text
/checkpoints/
/ledgers/
/sources/
/sources/seed/
/exports/
```

If the user prefers a flat folder, use clear filename prefixes instead.

## Storage Status Labels

Every checkpoint response must clearly state one of the following:

```text
Storage status: verified in datastore
Storage status: generated locally / ready for upload
Storage status: copy-ready only / not yet persisted
Storage status: storage unavailable / manual save required
```

## Inference Rule

Inferred claims are allowed only as questions, never as output-ready claims.

## Claim Depth

When relevant, classify claims by depth:

- No claim
- Awareness
- Exposure
- Supported
- Implemented
- Owned
- Led others

Use this ladder for career claims. Do not adapt Intake into non-career domains unless the project owner explicitly reopens COMPASS scope.

## Do-Not-Claim Rule

If the user rejects a claim, add it to the do-not-claim list.

Do-not-claim items must block downstream artifacts from reintroducing the rejected claim.

## Pause / Resume Rule

If the user says `I need a break`, `pause`, `bookmark this`, or `let's continue later`, stop asking new questions and produce a checkpoint.

If the current round has not been committed yet, produce a bookmark checkpoint that records unresolved questions and the next safe action.

## Storage Honesty Rule

If direct save/update access is available, save or update the source-of-truth files and verify visibility before reporting them as stored.

If direct save/update access is unavailable, produce downloadable or copy-ready files and clearly tell the user what to save where.

Never claim files were saved when they were only generated in chat, generated locally, or offered for download.
