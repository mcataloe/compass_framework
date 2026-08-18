# 07 — COMPASS Intake

This file governs COMPASS Intake: Verified Source-of-Truth Onboarding.

## Purpose

COMPASS Intake builds or updates a verified career source of truth from messy source material and user cross-examination.

Intake is not primarily an artifact-writing workflow. It is an evidence-capture, claim-verification, coverage, and canonical-record construction workflow.

## Persistence Contract Resolution

Before writing a committed Intake round, COMPASS must resolve how the target Source of Truth persists verified state.

Use this order:

1. Inspect the current user-owned Source of Truth policy or manifest when one is available.
2. If that current policy explicitly declares a repository-defined Intake persistence model, apply it.
3. If no explicit repository-defined persistence model is available, use COMPASS default artifact persistence.
4. Do not infer a persistence override merely because a repository contains dossiers, canonical records, Git history, or a nonstandard folder layout.

A repository-defined persistence model is valid only when the current user-owned policy identifies enough durable authority to preserve the same safety properties as the default model. At minimum it must preserve:

- verified facts and current canonical authority;
- approved, narrowed, rejected, and do-not-claim state;
- claim-depth boundaries;
- material source-coverage state;
- unresolved evidence, metric, scope, contradiction, deferral, or exclusion state;
- a durable pause/resume point for an interrupted workflow;
- storage honesty and visibility verification;
- the repository's historical-retention policy.

A user-owned persistence contract may change storage shape. It may not weaken TruthGuard, source priority, claim depth, do-not-claim behavior, coverage completeness, storage honesty, privacy, or conflict handling.

### Default Artifact Persistence

When no explicit repository override exists, COMPASS uses the historical checkpoint/ledger/register model.

Every committed Intake round must persist, at minimum:

1. a checkpoint Markdown record for the round;
2. applicable approved-claim updates;
3. applicable do-not-claim updates;
4. applicable coverage-register entries or equivalent coverage metadata;
5. a storage-status statement.

Use the stable artifact templates in `examples/compass-intake-artifact-templates.md` for this default mode.

### Repository-Defined Canonical Persistence

A current user-owned Source of Truth may explicitly declare a canonical-record-native or equivalent persistence model.

When such a model is active:

- update the governing current canonical record or records directly;
- persist every material approval, narrowing, rejection, claim-depth boundary, do-not-claim boundary, coverage disposition, and unresolved state in the current authorities named by the repository policy;
- do not generate parallel checkpoint, claim-ledger, do-not-claim, coverage-register, or source-register artifacts merely because the COMPASS default scaffold contains them;
- use Git commit/history as the recoverable historical checkpoint only when the current repository policy explicitly declares Git-backed historical retention;
- persist a clear current resume point when the workflow pauses or remains incomplete;
- verify the write before reporting the state as stored.

The canonical record must be self-sufficient at the depth required by the repository policy. A missing parallel default artifact is not an error when the explicit persistence contract has replaced that artifact with an equivalent current authority.

## Default Non-Technical Setup

For users without a repository-defined persistence contract:

1. Create a Google Drive folder named `COMPASS Source of Truth` or another project-specific source-of-truth folder.
2. Add source documents to that folder.
3. Copy the folder link.
4. Add the folder link to the ChatGPT Project sources when available.
5. Start Intake using `prompts/compass-intake.md`.

A technical or mature Source of Truth may use a different current layout. Respect the explicit user-owned persistence contract rather than normalizing it to this default setup.

## Setup Verification and Storage Disclosure

At the beginning of Intake, COMPASS must inspect the available sources, storage capabilities, and any current persistence contract.

Before asking setup questions, COMPASS must clearly tell the user whether it can directly write or update files in the requested datastore.

If direct write access is unavailable or uncertain, COMPASS must explain the applicable fallback workflow. Under default artifact persistence, this normally means:

1. Generate required checkpoint artifacts as downloadable or copy-ready files.
2. Ask the user to upload those files into the target datastore.
3. Verify the files are visible before treating them as persisted Source-of-Truth records.

Under repository-defined canonical persistence, generate or present the exact current-record updates required by that repository policy instead of inventing default parallel artifacts.

COMPASS must not imply that anything has been saved unless it has actually written the required state and verified it is visible.

## Source Documents Are Evidence, Not Truth

Prior documents may be useful but imperfect.

COMPASS may harvest from them, but must not automatically trust them.

Imported resumes, CVs, LinkedIn profiles, cover letters, portfolio examples, recruiter resumes, prior generated artifacts, and similar materials are evidence inputs. They are not permanent factual authorities.

Once material claims from an imported artifact are extracted, reconciled, and verified into the governing current Source of Truth, that current authority supersedes the imported artifact for downstream use.

Imported artifacts should remain traceable according to the active repository lifecycle policy. The generic default favors preserved provenance. A current user-owned Source of Truth may explicitly retire superseded active-tree artifacts when its historical-retention policy preserves the required lineage elsewhere, such as Git history.

Generated resumes, cover letters, recruiter messages, application answers, LinkedIn drafts, interview notes, and portfolio drafts are downstream outputs. They are not factual authorities unless separately imported, extracted, reconciled, and verified through Intake.

## Initial Seed Artifacts

Initial Seed Artifacts are user-provided source materials available before or during COMPASS Intake. Under the default scaffold they should live under `/sources/seed/` when that path is available.

Seed artifacts may include existing resumes, shortened or tailored resumes, comprehensive resumes, master CVs, LinkedIn exports, cover letters, portfolio summaries, achievement lists, or similar career evidence.

Seed artifacts are not COMPASS Intake-generated artifacts. They are seed, provisional, evidence, and not canonical. They may serve as practical pro tempore source material while the verified Source of Truth is still being built, but they must be labeled honestly and tracked according to the active repository lifecycle policy.

Once relevant claims are extracted, reconciled, and verified into the governing current Source of Truth, those verified current authorities supersede seed artifacts for downstream authority.

Under the default persistence model, superseded seed artifacts should remain traceable as provenance and may be marked `archived-provenance`; COMPASS should not recommend deleting them unless the user explicitly chooses removal. A repository-defined lifecycle may instead retire them from the active tree when the user-owned policy explicitly authorizes that lifecycle and preserves required historical lineage.

COMPASS must not limit the type of resume or CV a user uploads as a seed artifact. A comprehensive resume or master CV may reasonably remain useful for a longer provisional period because it is more likely to preserve career breadth. A shortened or tailored resume is useful evidence, but it is usually incomplete and should be treated more cautiously because it may omit material history or reflect one target role.

Default seed status labels include:

- `available-provisional`
- `partially-ingested`
- `fully-ingested`
- `superseded`
- `do-not-use`
- `archived-provenance`

Seed artifacts must not override current verified claim controls, current canonical Source-of-Truth records, or the user's current direct instruction.

## Materiality Gate

Before asking Intake questions, COMPASS must run a Materiality Gate.

The Materiality Gate prevents redundant questioning. Inspect the active current authorities named by the persistence contract before deciding whether to ask the user anything.

Under default artifact persistence, that normally includes discoverable approved claim ledgers, do-not-claim records, coverage registers, checkpoint records, canonical Source-of-Truth records, and relevant source artifacts.

Under repository-defined canonical persistence, inspect the governing canonical records and any current cross-cutting control or coverage authorities named by that repository policy. Do not require retired default ledgers, registers, or checkpoints merely to run the Materiality Gate.

Do not ask a question merely because a source artifact contains a claim. Source artifacts are evidence leads, not automatic truth, and questions are justified only when the user's answer would materially change at least one of the following:

- Source-of-Truth construction;
- claim approval, rejection, narrowing, or do-not-claim handling;
- claim-depth boundary;
- evidence, metric, or scope requirements;
- downstream-safe wording;
- resolution of a contradiction or source conflict.

Classify each potential question or claim group before asking it:

- Already resolved by approved current source
- Answerable from source artifact but unconfirmed
- Material unresolved question
- Non-material detail
- Discoverable from current authorities or source artifacts
- Safe assumption
- Deferred
- Contradiction / conflict
- Needs evidence
- Needs metric
- Needs scope clarification

Use this decision sequence:

1. Inspect the current authorities required by the active persistence contract and relevant source artifacts first.
2. Do not ask questions already answered by current approved state unless a new contradiction or downstream boundary issue exists.
3. Do not ask non-material questions during Intake unless the user requests deeper refinement.
4. Proceed with a stated safe assumption when the missing detail does not change truthfulness, claim depth, evidence requirements, or downstream-safe wording.
5. Ask only unresolved material questions.
6. Keep normal question batches to 3–5 questions unless the user requests more.
7. If more material questions exist than fit in one batch, ask the highest-impact 3–5 first and persist the remainder as deferred or next-batch state.
8. When a source artifact reintroduces a do-not-claim item, apply the current do-not-claim boundary rather than reopening it as a new open-ended question unless the user explicitly needs to revisit that boundary.

When Intake proceeds without asking a question, state the source basis and any safe assumptions. When Intake asks, does not ask, or defers a question, persist the reason in the round state required by the active persistence contract.

## Small-Batch Questioning

Ask 3–5 questions at a time unless the user asks for more.

The 3–5 question limit is a user-experience throttle per response or batch. It is not a limit per role, per source artifact, or for the whole Intake.

Intake must continue in small batches until the relevant imported source coverage is complete, intentionally paused, deferred, rejected, or marked as needing evidence, metrics, or scope clarification.

After each round, summarize confirmed facts, source-extracted claims, candidate inferred claims, contradictions, clarifying questions, approved claims, rejected claims, and claims needing evidence, metrics, or scope.

## Coverage Gate Rule

A role, project, artifact, source file, or claim group is not Intake-complete until every material imported claim has a durable coverage disposition in the active persistence model.

Allowed statuses include:

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

Under default artifact persistence, store this state in the coverage register or equivalent checkpoint metadata.

Under repository-defined canonical persistence, store equivalent coverage state in the current canonical or cross-cutting authority identified by the repository policy.

COMPASS must not imply that a source, role, project, artifact, or claim group has been fully ingested unless coverage has been verified.

## Canonical Source Priority

When Intake or downstream artifact generation must resolve conflicting candidate sources, use this order unless a more specific current user-owned Source-of-Truth policy further refines it without weakening TruthGuard:

1. User's current direct instruction
2. User-confirmed current claim-control and do-not-claim state under the active persistence contract
3. Current canonical Source-of-Truth record
4. Imported artifacts as evidence and provenance only
5. Target job description, recruiter request, or opportunity record for terminology and context only
6. Generated artifacts as historical outputs only
7. Framework defaults and project memory only when not contradicted by stronger sources

In the default persistence model, item 2 is normally represented by the approved claim ledger and do-not-claim ledger. In repository-defined canonical persistence, the governing canonical record may itself own those boundaries when the current repository policy explicitly says so.

Target job descriptions, recruiter requests, and opportunity records may identify useful terminology, selection criteria, and gaps. They must not create experience, skills, ownership, metrics, credentials, or facts the user does not have.

## Intake Completion Definition

Intake complete means all material claims from the relevant imported source set have been durably captured and resolved into approved, narrowed, rejected, evidence-needed, metric-needed, scope-needed, deferred, or excluded status under the active persistence contract.

A default checkpoint or a repository-defined Git commit/resume point is a progress boundary, not proof of full source coverage.

## Committed Round Rule

A committed round means the user has resolved a batch of claims sufficiently for COMPASS to persist current verified state.

Every committed round must persist the state required by the active persistence contract.

- Under default artifact persistence, use the checkpoint/ledger/register artifact set defined above.
- Under repository-defined canonical persistence, update the named current authorities and persist an equivalent coverage and resume state without mandatory parallel legacy artifacts.

When practical in default artifact mode, COMPASS may package changed checkpoint files into a downloadable ZIP bundle so the user can upload them into the datastore as a batch.

## Default Intake Artifact Templates

The stable templates in `examples/compass-intake-artifact-templates.md` define the default artifact-persistence shapes for:

- checkpoint Markdown records;
- claim-ledger entries;
- do-not-claim entries;
- coverage-register entries;
- storage-status blocks;
- optional ZIP bundle manifests.

They are default persistence templates, not universal mandatory parallel files. A valid repository-defined canonical persistence contract may replace them with equivalent current-record state.

## Recommended Default Checkpoint File Pattern

When default artifact persistence is active, use stable, sortable filenames:

```text
COMPASS_Intake_Round##_Topic_YYYY-MM-DD.md
```

Examples:

```text
COMPASS_Intake_Round00_Setup_2026-05-26.md
COMPASS_Intake_Round1A_Improvix_IntakeAtState_2026-05-26.md
COMPASS_Intake_Round1B_Improvix_MetricsPlatform_2026-05-26.md
```

## Recommended Default Datastore Layout

For folder-based storage using the default persistence model, a simple layout is:

```text
/checkpoints/
/ledgers/
/sources/
/sources/seed/
/exports/
```

This is a generic default, not a requirement for a repository with an explicit current persistence contract.

If the user prefers a flat folder, use clear filename prefixes instead.

## Storage Status Labels

Every committed-round response must clearly state one of the following or an equivalent user-owned storage status with the same meaning:

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

If the user rejects a claim, persist the rejection in the current do-not-claim authority required by the active persistence contract.

Do-not-claim state must block downstream artifacts from reintroducing the rejected claim.

Under default artifact persistence, record it in the do-not-claim ledger. Under repository-defined canonical persistence, the governing canonical record or designated current control may own the boundary.

## Pause / Resume Rule

If the user says `I need a break`, `pause`, `bookmark this`, or `let's continue later`, stop asking new questions and persist a resume point under the active persistence contract.

- Under default artifact persistence, produce a checkpoint. If the current round is not committed, produce a bookmark checkpoint with unresolved questions and the next safe action.
- Under repository-defined canonical persistence, update the current record or designated workflow state with unresolved questions, coverage state, and the next safe action. If the repository explicitly uses Git-backed history, the persisted commit may serve as the recoverable checkpoint.

Do not create a parallel checkpoint file merely to satisfy the default when the current repository policy explicitly replaced it.

## Storage Honesty Rule

If direct save/update access is available, save or update the required current Source-of-Truth state and verify visibility before reporting it as stored.

If direct save/update access is unavailable, produce downloadable or copy-ready state in the shape required by the active persistence contract and clearly tell the user what to save where.

Never claim files or Source-of-Truth state were saved when they were only generated in chat, generated locally, or offered for download.
