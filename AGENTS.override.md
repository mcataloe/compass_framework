# COMPASS Framework — Repository Agent Override

This repository-level override supersedes the editable repository section in the root `AGENTS.md` for current repository facts and project-specific operating guidance. The locked global LEAP section in `AGENTS.md` remains unchanged and is not being revised by this initiative.

## Current Repository State

- Project: `COMPASS Framework`
- Canonical branch: `main`
- Active framework version: `vNext 2026-08.5`
- Primary formats: Markdown and Python
- Executable runtime: `python -m tools.resume_release`
- Automated regression tests: Python standard-library `unittest`

Use `VERSION.md`, `COMPASS_Current.md`, `COMPASS_Changelog.md`, the applicable `rules/`, and current launcher prompts as the active framework sources.

## LEAP and Change Discipline

- Ground changes in current repository files before editing.
- Keep durable behavior in `rules/` and canonical framework docs rather than only in launcher prompts or examples.
- Keep prompt launchers deferential to active rules.
- Preserve TruthGuard, phase separation, artifact cleanliness, privacy, and storage honesty.
- When COMPASS behavior changes materially, update `VERSION.md` and `COMPASS_Changelog.md` in the same change set.
- Do not add candidate-specific data to this public framework repository.
- Prefer bounded, reviewable commits and targeted validation.

## Intake Persistence Contract

COMPASS Intake must resolve the active Source-of-Truth persistence contract before committed writes.

- If no current user-owned persistence override exists, the generic checkpoint, approved-claim, do-not-claim, coverage-register, and storage-status artifact model remains the default.
- A current user-owned Source of Truth may explicitly declare repository-defined canonical persistence.
- An override changes storage shape only. It must preserve equivalent claim approval/rejection state, claim depth, do-not-claim boundaries, coverage, unresolved state, pause/resume continuity, historical retention, conflict handling, privacy, and storage honesty.
- Do not infer a persistence override from dossiers, Git history, missing legacy folders, or a nonstandard layout.
- Git history may serve as the recoverable historical checkpoint only when current user-owned policy explicitly declares Git-backed retention.

Do not treat default checkpoint or ledger artifacts as universally mandatory when an explicit current repository persistence contract has replaced them with equivalent governing current state.

## Source Rebase Contract

COMPASS Source Rebase remains non-destructive scaffold alignment.

Before drift classification:

1. Inspect the current user-owned Source Manifest when available.
2. Resolve protected paths, current persistence/lifecycle policy, and explicitly retired active-tree paths.
3. Derive the repository-specific expected scaffold from the generic framework scaffold.

An explicitly retired path:

- is not missing drift when absent;
- must not be proposed or recreated by `create-missing-only`;
- remains untouched when it still exists;
- may be deleted only through a separately authorized repository-maintenance workflow outside Source Rebase.

Historical preservation remains the generic default when no explicit current user-owned retirement policy exists.

## Source and Claim Safety

- Source documents and seed artifacts are evidence, not automatic truth.
- Current verified Source-of-Truth authorities govern downstream candidate facts.
- Treat the current claim-control and do-not-claim authorities required by the active persistence contract as evidence-control data. Under default persistence these are commonly ledgers; under repository-defined canonical persistence the governing canonical record may own the same boundaries.
- Inferred claims are questions only until confirmed.
- Never fabricate technologies, credentials, dates, metrics, responsibilities, ownership, implementation stage, leadership scope, outcomes, or other material career facts.

## Validation Commands

Run practical checks for the changed area. For framework-wide behavior changes, use at minimum when the repository is locally available:

```bash
python -m compileall -q tools/resume_release tests/resume_release tests/framework_policy deployments/chatgpt-custom-gpt/tests
python -m unittest discover -s tests -v
python -m unittest discover -s deployments/chatgpt-custom-gpt/tests -v
```

Also use targeted repository searches for stale or contradictory framework behavior.

Do not claim a test passed unless it actually ran.

## Stop Conditions

Stop rather than silently weaken or reinterpret:

- TruthGuard or no-fabrication behavior;
- current Source-of-Truth authority;
- active persistence-contract guarantees;
- claim-depth or do-not-claim controls;
- coverage completeness;
- storage honesty;
- privacy or candidate-neutral boundaries;
- non-destructive Source Rebase behavior;
- a material framework version/alignment requirement.

Do not restore retired scaffold paths merely because older generic COMPASS behavior expected them.
