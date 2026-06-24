# COMPASS Source-of-Truth Scaffold

This is a generic COMPASS source-of-truth scaffold.

Existing source repository files are user-owned records and must not be overwritten. Use COMPASS Intake to verify claims. Use COMPASS Source Rebase to align structure.

## Baseline Directories

```text
checkpoints/
ledgers/
sources/
sources/seed/
exports/
style/
sync/
migration/
```

## Initial Seed Artifacts

Use `sources/seed/` for Initial Seed Artifacts such as existing resumes, comprehensive resumes, master CVs, LinkedIn exports, prior cover letters, portfolio summaries, achievement lists, and similar career evidence.

Seed artifacts are seed, provisional, evidence, and not canonical. Verified COMPASS Intake records and ledgers supersede them for downstream authority when available.

## Experience Sync Configuration

Use `sync/COMPASS_Experience_Targets.yaml` for the private source-to-target routing map used by COMPASS Experience Sync.

This source-side file may contain actual Source of Truth and target repository locations, target IDs, branches, publication defaults, protected paths, and write policy. It must not be copied into a public experience repository.

The public target manifest should use a stable source identifier and reconciliation metadata rather than exposing the private Source of Truth repository location.

## Safety

Source Rebase may create missing scaffold files only in `create-missing-only` mode after explicit approval.

If a path already exists, skip it and report it. Do not overwrite, delete, rename, move, or modify existing source records.
