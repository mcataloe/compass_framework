# COMPASS Source Rebase Report - Example

This generic example shows a safe dry-run report. It does not describe an actual user source-of-truth repository.

## 1. Mode

- Requested mode: dry-run
- Effective mode: dry-run
- Writes performed: no
- Reason: Dry-run is the default Source Rebase mode.

## 2. Framework Version

- COMPASS framework repo: example framework source
- Framework branch/tag/commit: example-main
- COMPASS version: vNext 2026-05.6
- Source scaffold version, if known: templates/source-of-truth-scaffold

## 3. Source Repo / Branch

- Source repo: example source-of-truth repo
- Source branch: example-branch
- Repo access status: read-only example
- Write capability: false
- Visibility verification capability: false

## 4. Write Capability Disclosure

- Direct write available: false
- Visibility verification available: false
- Storage status label: Storage status: copy-ready only / not yet persisted

## 5. Existing Layout Found

- `/sources/`
- `/ledgers/03_Approved_Claim_Ledger.md`

## 6. Expected Scaffold

- `README.md`
- `COMPASS_Source_Manifest.md`
- `checkpoints/`
- `ledgers/`
- `sources/`
- `sources/seed/`
- `sources/seed/README.md`
- `sources/seed/SEED_ARTIFACTS_MANIFEST.md`
- `exports/`
- `style/`
- `migration/`

## 7. Files Already Present

- `/sources/` - skipped
- `/ledgers/03_Approved_Claim_Ledger.md` - skipped

## 8. Missing Files / Directories

- `/checkpoints/`
- `/exports/`
- `/style/`
- `/migration/`
- `/COMPASS_Source_Manifest.md`
- `/sources/seed/`
- `/sources/seed/README.md`
- `/sources/seed/SEED_ARTIFACTS_MANIFEST.md`

## 9. Drift Detected

- Missing expected directory: `/checkpoints/`
- Missing expected directory: `/exports/`
- Missing expected directory: `/sources/seed/`
- Existing user-owned file at expected path: `/ledgers/03_Approved_Claim_Ledger.md`

## 10. Legacy / Historical Paths Preserved

- Example historical `checkpoints/COMPASS_Layer0_Round##_Example_YYYY-MM-DD.md` paths would be preserved and not renamed if encountered.

## 11. Proposed Create-Only Changes

- Create `/checkpoints/`
- Create `/exports/`
- Create `/style/`
- Create `/migration/`
- Create `/COMPASS_Source_Manifest.md`
- Create `/sources/seed/`
- Create `/sources/seed/README.md`
- Create `/sources/seed/SEED_ARTIFACTS_MANIFEST.md`

## 12. Forbidden Changes Not Performed

- No overwrites
- No deletes
- No renames
- No moves
- No checkpoint rewrites
- No claim-ledger edits
- No do-not-claim edits
- No automatic movement of existing resumes, CVs, or source files into `/sources/seed/`

## 13. Manual Decisions Required

- User must explicitly approve `create-missing-only` before any proposed paths are created.

## 14. Storage Status

- Storage status: copy-ready only / not yet persisted

## 15. Next Safe Action

Review this dry-run report. If the proposed missing scaffold paths are correct, explicitly approve `create-missing-only` for this exact target.
