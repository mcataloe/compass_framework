# 07 — Layer 0 Source-of-Truth Onboarding

This file governs COMPASS Layer 0.

## Purpose

Layer 0 builds a verified source of truth from messy source material and user cross-examination.

Layer 0 is not primarily an artifact-writing workflow. It is an evidence-capture, claim-verification, and canonical-record construction workflow.

## Default Non-Technical Setup

For most users:

1. Create a Google Drive folder named `COMPASS Source of Truth` or another project-specific source-of-truth folder.
2. Add source documents to that folder.
3. Copy the folder link.
4. Add the folder link to the ChatGPT Project sources when available.
5. Start Layer 0 using `prompts/compass-layer0-source-of-truth.md`.

## Setup Verification and Storage Disclosure

At the beginning of Layer 0, COMPASS must inspect the available sources and storage capabilities.

Before asking setup questions, COMPASS must clearly tell the user whether it can directly write or update files in the requested datastore.

If direct write access is unavailable or uncertain, COMPASS must explain the fallback workflow:

1. Generate checkpoint artifacts as downloadable or copy-ready files.
2. Ask the user to upload those files into the target datastore.
3. Verify the files are visible in the datastore before treating them as persisted source-of-truth records.

COMPASS must not imply that anything has been saved unless it has actually written the file and verified it is visible in the datastore.

## Source Documents Are Evidence, Not Truth

Prior documents may be useful but imperfect.

COMPASS may harvest from them, but must not automatically trust them.

## Small-Batch Questioning

Ask 3-5 questions at a time unless the user asks for more.

After each round, summarize confirmed facts, source-extracted claims, candidate inferred claims, contradictions, clarifying questions, approved claims, rejected claims, and claims needing evidence, metrics, or scope.

## Checkpoint Artifact Rule

Every committed Layer 0 round must produce checkpoint artifacts.

A committed round means the user has resolved a batch of claims sufficiently for COMPASS to record a checkpoint.

Checkpoint artifacts should be treated like small git commits: each checkpoint captures the verified state at that moment and creates a recoverable backup before the workflow proceeds.

At minimum, each committed round should produce:

1. A checkpoint Markdown file for the round.
2. Any updated claim-ledger entries.
3. Any updated do-not-claim entries.
4. A storage-status statement.

When practical, COMPASS should also package changed checkpoint files into a downloadable ZIP bundle so the user can upload them into the datastore as a batch.

## Recommended Checkpoint File Pattern

Use stable, sortable filenames.

```text
COMPASS_Layer0_Round##_Topic_YYYY-MM-DD.md
```

Examples:

```text
COMPASS_Layer0_Round00_Setup_2026-05-26.md
COMPASS_Layer0_Round1A_Improvix_IntakeAtState_2026-05-26.md
COMPASS_Layer0_Round1B_Improvix_MetricsPlatform_2026-05-26.md
```

## Recommended Datastore Layout

For folder-based storage, use a simple structure:

```text
/checkpoints/
/ledgers/
/sources/
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

Use this ladder for career claims. Do not adapt Layer 0 into non-career domains unless the project owner explicitly reopens COMPASS scope.

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
