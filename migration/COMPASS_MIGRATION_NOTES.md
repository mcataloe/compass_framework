# COMPASS Canonicalization Notes

**Status: Historical migration record.** This file describes the completed May 2026 canonicalization and Intake rename. It remains at its existing path for traceability; it is not a current implementation plan, version declaration, or independent policy source.

For current behavior, use [`../VERSION.md`](../VERSION.md), [`../COMPASS_Current.md`](../COMPASS_Current.md), [`../COMPASS_COMMANDS.md`](../COMPASS_COMMANDS.md), and the relevant [`../rules/`](../rules/) files. [`../COMPASS_Changelog.md`](../COMPASS_Changelog.md) records subsequent changes.

## Historical goal

The migration aligned the repository around COMPASS-only terminology and source-of-truth behavior.

## Files affected by the migration

- `COMPASS_Current.md`
- `COMPASS_Changelog.md`
- `prompts/compass-intake.md`
- `prompts/compass-analysis.md`
- `prompts/compass-tailored-resume.md`
- `prompts/compass-cover-letter.md`

## Historical compatibility decision

The migration removed predecessor-name redirect files rather than maintaining a parallel compatibility policy. Current naming and compatibility requirements are governed by `VERSION.md` and the active rules, not this record.

## Scope correction

COMPASS active scope was corrected back to careers / job-search in `vNext 2026-05.4`.

That correction removed the broader product, strategy, research, consulting, grant, policy, and personal-knowledge scope. Current scope is defined in `COMPASS_Current.md`.

## Completed version bump

Updated to `vNext 2026-05.5`.

## Intake terminology migration

The former "Layer 0" source-of-truth onboarding workflow was renamed to "COMPASS Intake" in `vNext 2026-05.5`.

The migration changed active terminology to "COMPASS Intake" on first mention and "Intake" thereafter. Historical changelog and migration notes retained "Layer 0" only to explain the rename.

Updated active file names:

- `rules/07-compass-intake.md`
- `prompts/compass-intake.md`
- `examples/compass-intake-checkpoint-example.md`

## Historical PR title

The recorded PR-title recommendation was "Rename Layer 0 to COMPASS Intake"; it is retained as historical context, not a pending PR recommendation.
