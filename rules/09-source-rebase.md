# 09 - COMPASS Source Rebase

This file governs COMPASS Source Rebase: safe source-of-truth scaffold alignment.

## Purpose

COMPASS Source Rebase safely aligns an existing COMPASS source-of-truth repository with the current framework scaffold after framework upgrades.

Source Rebase is structural only. It is not COMPASS Intake, claim verification, evidence extraction, source reconciliation, git history rebasing, or source record migration.

## When to Use

Use COMPASS Source Rebase when the user wants to:

- Align a COMPASS source-of-truth repository to the latest framework structure.
- Add missing source-of-truth scaffold structure without overwriting current files.
- Inspect source repository structure drift after a framework upgrade.
- Create missing scaffold directories or placeholder files safely.
- Update source-of-truth repository layout after framework structure changes.

## Relationship to COMPASS Intake

COMPASS Intake builds or updates verified career source-of-truth records through evidence capture, claim verification, and canonical-record construction.

COMPASS Source Rebase aligns only the source repository scaffold. It must not replace Intake, ask career-claim questions, infer experience, verify claims, approve claims, reject claims, narrow claims, edit claim ledgers, edit do-not-claim registers, or treat scaffold alignment as Intake completion.

If the user needs claim verification, route them to COMPASS Intake after Source Rebase completes or after the dry-run report confirms that the scaffold is ready.

## Source-of-Truth Ownership Boundary

Existing user-owned source-of-truth files always win over framework scaffold templates.

Framework templates are defaults. Source repository files are records.

If an expected path already exists, skip it and report it. Do not overwrite, delete, rename, move, edit, normalize, rewrite, or reformat existing source records.

## Default Safety Mode

The default mode is `dry-run`.

Source Rebase must start with dry-run unless the user provides a current dry-run report and explicitly approves `create-missing-only` for the exact target.

## Dry-Run Mode

In `dry-run`, COMPASS Source Rebase may inspect the expected scaffold against the actual source repository layout and produce a report. It must perform no writes.

Dry-run mode must report:

1. Files and directories already present.
2. Missing files and directories.
3. Drift detected.
4. Legacy or historical files preserved.
5. Unexpected files or directories preserved.
6. Proposed create-only changes.
7. Manual decisions required.
8. Storage and write-access status.
9. Next safe action.

## Create-Missing-Only Mode

The first permitted writable mode is `create-missing-only`.

COMPASS may use `create-missing-only` only after explicit user approval for that mode and target repository or path.

In `create-missing-only`, COMPASS may create only absent scaffold directories, absent scaffold placeholder files, an absent manifest file, an absent migration/report directory, or an approved Source Rebase report file.

If a path already exists, COMPASS must skip it and report it. COMPASS must verify created paths before reporting them as created.

## Forbidden Operations

COMPASS Source Rebase must not:

- Overwrite existing files
- Delete files or directories
- Rename files or directories
- Move files or directories
- Squash files
- Normalize historical checkpoint names
- Rewrite checkpoints
- Edit verified claims
- Edit approved claim ledgers
- Edit do-not-claim registers
- Infer new career claims
- Treat scaffold update as Intake completion
- Silently resolve conflicts
- Claim files were saved without write and visibility verification
- Use destructive migration behavior to satisfy a framework upgrade

## Expected Source-of-Truth Scaffold

Use `templates/source-of-truth-scaffold/` as the framework-owned scaffold source.

Expected directories and files:

```text
README.md
COMPASS_Source_Manifest.md
checkpoints/
checkpoints/.gitkeep
ledgers/
ledgers/00_Intake_Coverage_Register.md
ledgers/01_Claim_Depth_Rubric.md
ledgers/02_Do_Not_Claim_Register.md
ledgers/03_Approved_Claim_Ledger.md
sources/
sources/00_Source_Register.md
exports/
exports/.gitkeep
style/
style/candidate_voice.md
style/resume_style.md
style/artifact_generation_policy.md
migration/
migration/README.md
migration/COMPASS_Source_Rebase_Report_TEMPLATE.md
```

These files are scaffold defaults only. Existing user-owned files override template defaults once created.

## Drift Classification

Classify Source Rebase drift as:

- Missing expected directory
- Missing expected scaffold file
- Existing user-owned file at expected path
- Existing file differs from current scaffold
- Legacy or historical path preserved
- Unexpected extra file or directory
- Potential conflict requiring human review

Existing files that differ from the current scaffold are drift observations only. They must not be overwritten.

## Manifest and Version Tracking

The scaffold includes `COMPASS_Source_Manifest.md` as an optional source repository manifest.

If the manifest already exists, skip it and report it. If it is missing, propose it as a create-missing-only candidate.

The manifest may record framework version, scaffold version, source repository branch, storage location, protected paths, framework-managed scaffold paths, historical paths preserved, manual decisions, and Source Rebase report history. It must not record private career claims unless the user separately approves that content in the source-of-truth repository.

## Historical File Preservation

Historical checkpoint files, including older `COMPASS_Layer0_*` files, must be preserved.

Do not rename, rewrite, move, delete, or normalize historical checkpoint files solely to match current COMPASS Intake terminology.

If historical paths are encountered, list them as preserved historical paths in the Source Rebase report.

## Storage Honesty Rule

Before performing any write-capable action, disclose whether direct write access to the target source repository or path is available and verified.

If write access is unavailable or uncertain, stay in `dry-run` and provide copy-ready instructions.

Never claim that directories or files were created unless they were actually created and verified.

## Required Source Rebase Report

Use `templates/source-of-truth-scaffold/migration/COMPASS_Source_Rebase_Report_TEMPLATE.md` for Source Rebase reports.

Every Source Rebase report must include:

1. Mode.
2. Framework version.
3. Source repository or branch.
4. Write capability disclosure.
5. Existing layout found.
6. Expected scaffold.
7. Files already present.
8. Missing files or directories.
9. Drift detected.
10. Legacy or historical paths preserved.
11. Proposed create-only changes.
12. Forbidden changes not performed.
13. Manual decisions required.
14. Storage status.
15. Next safe action.

## Human Approval Gates

Human approval is required before `create-missing-only`.

Approval must name the exact target repository or path and the requested mode.

If the dry-run report identifies a conflict, unexpected destructive requirement, or unclear ownership boundary, stop and request a human decision before any write-capable action.

## Stop Conditions

Stop and report if:

- Required framework files are missing.
- The target source repository or path cannot be inspected.
- The target has unclear ownership boundaries.
- Existing source records would need to be overwritten, deleted, renamed, moved, or edited.
- Claim ledgers, do-not-claim registers, checkpoints, or source documents would need modification.
- Historical checkpoint names would need normalization.
- Scaffold alignment would be confused with Intake completion.
- Direct write access or visibility verification is unclear for a requested write-capable action.
- Private user facts would be required in framework templates.
