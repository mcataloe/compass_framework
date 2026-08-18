# 09 - COMPASS Source Rebase

This file governs COMPASS Source Rebase: safe source-of-truth scaffold alignment.

## Purpose

COMPASS Source Rebase safely aligns an existing COMPASS Source-of-Truth repository with the current framework scaffold after framework upgrades.

Source Rebase is structural only. It is not COMPASS Intake, claim verification, evidence extraction, source reconciliation, Git-history rebasing, destructive source-record migration, or lifecycle cleanup.

## When to Use

Use COMPASS Source Rebase when the user wants to:

- align a COMPASS Source-of-Truth repository to the current framework structure;
- add missing scaffold structure without overwriting current files;
- inspect source-repository structure drift after a framework upgrade;
- create missing scaffold directories or placeholder files safely;
- update source-of-truth repository layout after framework structure changes;
- add the optional private Experience Sync routing scaffold.

## Relationship to COMPASS Intake

COMPASS Intake builds or updates verified career Source-of-Truth records through evidence capture, claim verification, coverage, and canonical-record construction.

COMPASS Source Rebase aligns repository scaffold only. It must not replace Intake, ask career-claim questions, infer experience, verify claims, approve claims, reject claims, narrow claims, edit current career authorities, or treat scaffold alignment as Intake completion.

If the user needs claim verification, route them to COMPASS Intake after Source Rebase completes or after the dry-run report confirms that the scaffold is ready.

## Source-of-Truth Ownership Boundary

Existing user-owned Source-of-Truth files always win over framework scaffold templates.

Framework templates are defaults. Source repository files are records and policy.

If an expected path already exists, Source Rebase skips it and reports it. Source Rebase does not overwrite, delete, rename, move, edit, normalize, rewrite, or reformat existing user-owned records.

A current user-owned Source Manifest may also declare that one or more generic scaffold paths have been retired from the repository's active architecture. That retirement declaration changes what Source Rebase considers expected; it does not authorize Source Rebase itself to delete an existing file.

## Manifest Policy Resolution

Before comparing the target repository with the generic scaffold, inspect the current user-owned `COMPASS_Source_Manifest.md` when one exists.

The manifest may define repository-specific structural policy such as:

- active Intake persistence mode;
- protected current paths;
- framework-managed current scaffold paths;
- historical-retention policy;
- explicitly retired active-tree paths or path classes;
- Source Rebase behavior for retired paths.

Use a repository-specific retirement rule only when it is explicit in the current user-owned manifest or another current user-owned repository policy that the manifest identifies as controlling.

Do not infer retirement merely because a path is absent, empty, old, named `legacy`, historical in Git, or not used by one current workflow.

If the manifest is missing or does not declare retired paths, use the generic scaffold and historical-preservation behavior as the default.

## Retired Active-Tree Paths

When a current user-owned manifest explicitly retires a generic scaffold path or path class:

- remove that path from the repository-specific expected scaffold for the current Source Rebase run;
- do not classify its absence as missing drift;
- do not propose it for `create-missing-only`;
- do not recreate it from a framework template;
- do not require it merely because older COMPASS versions expected it;
- if the path still exists, report it as an existing manifest-retired path and leave it untouched;
- do not interpret retirement as permission for Source Rebase to delete, move, rename, or rewrite the existing path.

Deletion or lifecycle cleanup of an existing retired path is a separate explicitly authorized repository-maintenance operation outside COMPASS Source Rebase.

A repository may therefore use Git history or another explicit retention mechanism for retired records without Source Rebase continuously attempting to restore those records to the active tree.

## Default Safety Mode

The default mode is `dry-run`.

Source Rebase must start with dry-run unless the user provides a current dry-run report and explicitly approves `create-missing-only` for the exact target.

## Dry-Run Mode

In `dry-run`, COMPASS Source Rebase may inspect the generic scaffold, current manifest policy, and actual source repository layout and produce a report. It must perform no writes.

Dry-run mode must report:

1. Files and directories already present.
2. Generic expected scaffold.
3. Manifest-retired paths excluded from the repository-specific expected scaffold.
4. Missing non-retired files and directories.
5. Drift detected.
6. Legacy or historical paths preserved by current policy.
7. Existing manifest-retired paths left untouched.
8. Unexpected files or directories preserved.
9. Proposed create-only changes.
10. Manual decisions required.
11. Storage and write-access status.
12. Next safe action.

## Create-Missing-Only Mode

The first permitted writable mode is `create-missing-only`.

COMPASS may use `create-missing-only` only after explicit user approval for that mode and target repository or path.

In `create-missing-only`, COMPASS may create only absent, non-retired scaffold directories or placeholder files, an absent manifest file, an absent migration/report directory when still part of the repository-specific expected scaffold, an absent Experience Sync routing placeholder, or an approved Source Rebase report file.

If a path already exists, skip it and report it.

If a path is explicitly retired by the current manifest, skip it even when the generic framework scaffold contains it.

COMPASS must verify created paths before reporting them as created.

## Forbidden Operations

COMPASS Source Rebase must not:

- overwrite existing files;
- delete files or directories;
- rename files or directories;
- move files or directories;
- squash files;
- normalize historical checkpoint names;
- rewrite checkpoints;
- edit verified claims;
- edit approved claim controls;
- edit do-not-claim controls;
- infer new career claims;
- treat scaffold update as Intake completion;
- silently resolve conflicts;
- claim files were saved without write and visibility verification;
- use destructive migration behavior to satisfy a framework upgrade;
- populate user-specific repository mappings without explicit user instruction;
- recreate a path explicitly retired by the current user-owned manifest.

## Generic Expected Source-of-Truth Scaffold

Use `templates/source-of-truth-scaffold/` as the framework-owned generic scaffold source.

The generic scaffold currently includes:

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
sources/seed/
sources/seed/README.md
sources/seed/SEED_ARTIFACTS_MANIFEST.md
sources/seed/resumes/
sources/seed/resumes/.gitkeep
sources/seed/cvs/
sources/seed/cvs/.gitkeep
sources/seed/linkedin/
sources/seed/linkedin/.gitkeep
sources/seed/cover-letters/
sources/seed/cover-letters/.gitkeep
sources/seed/portfolio/
sources/seed/portfolio/.gitkeep
sources/seed/other/
sources/seed/other/.gitkeep
exports/
exports/.gitkeep
style/
style/candidate_voice.md
style/resume_style.md
style/artifact_generation_policy.md
sync/
sync/README.md
sync/COMPASS_Experience_Targets.yaml
migration/
migration/README.md
migration/COMPASS_Source_Rebase_Report_TEMPLATE.md
```

These are generic defaults only.

For an existing repository, derive the repository-specific expected scaffold by applying the current user-owned manifest's protected paths, active structure, and explicit retired-path declarations to this generic baseline.

Existing user-owned files control over template defaults once created.

## Initial Seed Artifact Scaffold

Source Rebase recognizes `/sources/seed/` as the generic recommended scaffold location for Initial Seed Artifacts.

In `dry-run`, Source Rebase may report missing seed scaffold directories and missing seed placeholder/template files only when those paths remain part of the repository-specific expected scaffold.

In approved `create-missing-only` mode, Source Rebase may create only missing, non-retired seed scaffold directories and absent framework placeholder/template files. It must not overwrite, delete, rename, move, normalize, or modify existing user-owned files.

Source Rebase must not automatically move existing resumes, CVs, LinkedIn exports, cover letters, portfolio files, or other source documents into `/sources/seed/`.

Existing nonstandard source folders must be preserved and reported as existing user structure, not renamed or normalized.

If the current manifest explicitly retires `/sources/seed/` after ingestion under a repository-defined lifecycle, Source Rebase must not recreate it.

## Experience Sync Routing Scaffold

Source Rebase recognizes `/sync/` as the generic recommended location for private Experience Sync routing configuration.

The framework-owned scaffold includes:

```text
sync/README.md
sync/COMPASS_Experience_Targets.yaml
```

The routing file may contain actual Source of Truth and downstream target repository locations. It belongs in the private Source of Truth and must not be copied into a public experience repository.

In `dry-run`, Source Rebase may report the routing scaffold as missing when it remains part of the repository-specific expected scaffold.

In approved `create-missing-only` mode, Source Rebase may create only the absent non-retired scaffold file with generic placeholder values. It must not overwrite an existing routing file or infer user-specific repository mappings.

Populating or changing actual source and target links is a separate explicitly approved Source-of-Truth configuration change. Experience Sync itself may read but must never modify this file.

## Drift Classification

Classify Source Rebase findings as:

- Missing expected directory
- Missing expected scaffold file
- Existing user-owned file at expected path
- Existing file differs from current scaffold
- Legacy or historical path preserved by current policy
- Manifest-retired path absent as intended
- Manifest-retired path still present and left untouched
- Unexpected extra file or directory
- Potential conflict requiring human review

A manifest-retired path absent as intended is not missing drift.

Existing files that differ from the current scaffold are drift observations only. They must not be overwritten.

## Manifest and Version Tracking

The generic scaffold includes `COMPASS_Source_Manifest.md` as an optional source-repository manifest.

If the manifest already exists, read it as current user-owned repository policy and skip template replacement.

If it is missing, propose it as a `create-missing-only` candidate.

The manifest may record framework version, scaffold version, source repository branch, storage location, protected paths, framework-managed scaffold paths, persistence mode, historical-retention policy, retired active-tree paths, manual decisions, and Source Rebase report history. It must not record private career claims unless the user separately approves that content in the Source-of-Truth repository.

The actual source-to-target Experience Sync routing map belongs in `sync/COMPASS_Experience_Targets.yaml`, not in a public experience repository.

## Historical File Preservation

Historical file preservation remains the generic default.

Historical checkpoint files, including older `COMPASS_Layer0_*` files, must not be renamed, rewritten, moved, deleted, or normalized solely to match current COMPASS terminology.

When no current user-owned lifecycle policy retires a historical path, list it as preserved historical state in the Source Rebase report.

When a current user-owned manifest explicitly retires a historical path from the active tree, Source Rebase must respect that retirement for scaffold comparison and non-recreation. Source Rebase still must not delete an existing file; deletion remains a separate maintenance operation.

## Storage Honesty Rule

Before performing any write-capable action, disclose whether direct write access to the target source repository or path is available and verified.

If write access is unavailable or uncertain, stay in `dry-run` and provide copy-ready instructions.

Never claim that directories or files were created unless they were actually created and verified.

## Required Source Rebase Report

Use `templates/source-of-truth-scaffold/migration/COMPASS_Source_Rebase_Report_TEMPLATE.md` for Source Rebase reports when that report scaffold remains active for the target repository.

Every Source Rebase report must include:

1. Mode.
2. Framework version.
3. Source repository or branch.
4. Write capability disclosure.
5. Manifest policy resolution.
6. Existing layout found.
7. Generic expected scaffold.
8. Manifest-retired paths.
9. Repository-specific expected scaffold.
10. Files already present.
11. Missing non-retired files or directories.
12. Drift detected.
13. Legacy or historical paths preserved.
14. Existing retired paths left untouched.
15. Proposed create-only changes.
16. Forbidden changes not performed.
17. Manual decisions required.
18. Storage status.
19. Next safe action.

If the target repository explicitly retires the migration/report scaffold itself, Source Rebase may return the report conversationally or at another explicitly approved current path rather than recreating the retired report directory.

## Human Approval Gates

Human approval is required before `create-missing-only`.

Approval must name the exact target repository or path and requested mode.

If the dry-run report identifies a conflict, unexpected destructive requirement, unclear ownership boundary, or ambiguous retirement declaration, stop and request a human decision before any write-capable action.

## Stop Conditions

Stop and report if:

- Required framework files are missing.
- The target Source-of-Truth repository or path cannot be inspected.
- The target has unclear ownership boundaries.
- A claimed retirement rule is not explicit in current user-owned policy.
- Existing source records would need to be overwritten, deleted, renamed, moved, or edited.
- Claim controls, current canonical records, checkpoints, or source documents would need modification.
- Historical checkpoint names would need normalization.
- Scaffold alignment would be confused with Intake completion.
- Direct write access or visibility verification is unclear for a requested write-capable action.
- Private user facts would be required in framework templates.
