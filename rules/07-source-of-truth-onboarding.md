# 07 — Layer 0 Source-of-Truth Onboarding

This file governs COMPASS Layer 0.

## Purpose

Layer 0 builds a verified source of truth from messy source material and user cross-examination.

Layer 0 is not primarily an artifact-writing workflow. It is an evidence-capture, claim-verification, and canonical-record construction workflow.

## Default Non-Technical Setup

For most users:

1. Create a Google Drive folder named `COMPASS Source of Truth`.
2. Add source documents to that folder.
3. Copy the folder link.
4. Add the folder link to the ChatGPT Project sources.
5. Start Layer 0 using `prompts/compass-layer0-source-of-truth.md`.

## Source Documents Are Evidence, Not Truth

Prior documents may be useful but imperfect.

COMPASS may harvest from them, but must not automatically trust them.

## Small-Batch Questioning

Ask 3-5 questions at a time unless the user asks for more.

After each round, summarize confirmed facts, source-extracted claims, candidate inferred claims, contradictions, clarifying questions, approved claims, rejected claims, and claims needing evidence, metrics, or scope.

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

For non-career domains, adapt this ladder to claim confidence, ownership, implementation depth, or source certainty.

## Do-Not-Claim Rule

If the user rejects a claim, add it to the do-not-claim list.

Do-not-claim items must block downstream artifacts from reintroducing the rejected claim.

## Pause / Resume Rule

If the user says `I need a break`, `pause`, `bookmark this`, or `let's continue later`, stop asking new questions and produce a checkpoint.

## Storage Honesty Rule

If direct save/update access is available, save or update the source-of-truth files.

If direct save/update access is unavailable, produce copy-ready files and clearly tell the user what to save where.

Never claim files were saved when they were only generated in chat.
