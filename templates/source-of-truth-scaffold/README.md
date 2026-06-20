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
migration/
```

## Initial Seed Artifacts

Use `sources/seed/` for Initial Seed Artifacts such as existing resumes, comprehensive resumes, master CVs, LinkedIn exports, prior cover letters, portfolio summaries, achievement lists, and similar career evidence.

Seed artifacts are seed, provisional, evidence, and not canonical. Verified COMPASS Intake records and ledgers supersede them for downstream authority when available.

## Safety

Source Rebase may create missing scaffold files only in `create-missing-only` mode after explicit approval.

If a path already exists, skip it and report it. Do not overwrite, delete, rename, move, or modify existing source records.
