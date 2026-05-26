# COMPASS Version

Current COMPASS Version: vNext 2026-05.2

Former Name: STRIDE

Canonical Branch: main

Status: Active

Initialized: 2026-05-18 as STRIDE

Renamed: 2026-05-22 to COMPASS

## Version Rule

The version declared here governs the active framework behavior when used from the `main` branch.

When COMPASS changes materially, update this file and `COMPASS_Changelog.md` in the same change set.

## Rename Rule

COMPASS supersedes STRIDE as the canonical framework name.

Legacy STRIDE references are allowed only for migration, backward compatibility, historical changelog context, or career-domain compatibility. New rules, prompts, examples, and project instructions should use COMPASS.

If a prompt references STRIDE after this migration, interpret it as COMPASS unless the user explicitly asks for historical STRIDE behavior.

## Active Behavior Notes

The active vNext 2026-05.2 framework includes the STRIDE-to-COMPASS rename, generalization, and Layer 0 checkpoint artifact behavior:

- COMPASS is a field-agnostic, source-grounded framework for turning messy inputs into verified, defensible outputs.
- STRIDE is now the legacy name and may be treated as the career/job-search domain profile of COMPASS during migration.
- COMPASS preserves the Layer 0 verified source-of-truth onboarding workflow added under STRIDE.
- COMPASS may support multiple domain profiles, including careers, software/product planning, consulting deliverables, business strategy, research planning, grants, policy documents, and personal knowledge systems.
- Core behavior remains truth-first, source-grounded, checkpointed, and claim-ledger-driven.
- Layer 0 now requires checkpoint artifact generation at every committed round.
- Layer 0 setup must disclose whether direct datastore writes are available before asking setup questions.
- If direct writes are unavailable, Layer 0 must generate downloadable or copy-ready files and clearly instruct the user where to upload them.

## Compatibility Rule

Future COMPASS changes should preserve the core operating principles unless explicitly superseded:

- Truthful source-grounded output
- Phased workflow
- No fabricated technologies, metrics, credentials, employment history, project ownership, product claims, research findings, or business outcomes
- Separate strategic analysis from clean generated artifacts
- Domain profiles may add specialized output rules without weakening source-grounding or TruthGuard
- Prompt templates remain workflow launchers and must defer to active rule files for workflow behavior
- Layer 0 source-of-truth onboarding remains the default process for building a canonical source record from unverified documents or a new user's history
