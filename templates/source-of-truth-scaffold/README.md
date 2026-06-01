# COMPASS Source-of-Truth Scaffold

This is a generic COMPASS source-of-truth scaffold.

Existing source repository files are user-owned records and must not be overwritten. Use COMPASS Intake to verify claims. Use COMPASS Source Rebase to align structure.

## Baseline Directories

```text
checkpoints/
ledgers/
sources/
exports/
style/
migration/
```

## Safety

Source Rebase may create missing scaffold files only in `create-missing-only` mode after explicit approval.

If a path already exists, skip it and report it. Do not overwrite, delete, rename, move, or modify existing source records.
