# COMPASS Source Manifest

Scaffold placeholder. Existing manifests override this template.

## Repository Identity

- Source repo:
- Branch:
- Owner/user:

## Framework Alignment

- Last aligned COMPASS framework version:
- Framework branch/tag/commit:
- Source scaffold version:
- Last Source Rebase date:

## Persistence and Lifecycle Policy

This section is optional for repositories that intentionally diverge from generic COMPASS persistence or scaffold defaults.

- Intake persistence mode: `default_artifact_persistence` | `repository_defined_canonical_persistence`
- Current canonical authority summary:
- Historical retention: `active_tree` | `git_history` | `other explicitly defined user-owned retention`
- Retired active-tree paths / path classes:
  - none
- Source Rebase rule for retired paths: do not classify absent retired paths as drift and do not recreate them.

If this section is omitted, COMPASS uses the generic default Intake persistence and scaffold behavior.

A repository-defined persistence mode may change storage shape but may not weaken TruthGuard, claim depth, do-not-claim boundaries, coverage completeness, pause/resume state, source-conflict handling, or storage honesty.

## Protected User-Owned Paths

List paths that Source Rebase must not touch.

## Framework-Managed Scaffold Paths

List active scaffold paths created or tracked through Source Rebase.

## Legacy / Historical Paths Preserved

List historical paths that remain intentionally active, including older `COMPASS_Layer0_*` checkpoint files when encountered and not explicitly retired.

## Manual Decisions Pending

List unresolved scaffold-alignment decisions.

## Storage Status

Use one approved storage-status label.

## Notes

Do not add private career claims to this manifest unless the user explicitly approves storing that content in the Source-of-Truth repository.
