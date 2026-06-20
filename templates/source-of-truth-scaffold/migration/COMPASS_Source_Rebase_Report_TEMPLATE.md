# COMPASS Source Rebase Report - YYYY-MM-DD

## 1. Mode

- Requested mode:
- Effective mode:
- Writes performed: yes/no
- Reason:

## 2. Framework Version

- COMPASS framework repo:
- Framework branch/tag/commit:
- COMPASS version:
- Source scaffold version, if known:

## 3. Source Repo / Branch

- Source repo:
- Source branch:
- Repo access status:
- Write capability:
- Visibility verification capability:

## 4. Write Capability Disclosure

- Direct write available: true/false/unknown
- Visibility verification available: true/false/unknown
- Storage status label:

## 5. Existing Layout Found

List directories/files detected.

## 6. Expected Scaffold

List expected directories/files from the current framework scaffold, including `/sources/seed/` Initial Seed Artifact paths when applicable.

## 7. Files Already Present

List expected files that already exist and were skipped.

## 8. Missing Files / Directories

List scaffold files/directories that are missing.

## 9. Drift Detected

Classify drift as:

- Missing expected directory
- Missing expected scaffold file
- Existing user-owned file at expected path
- Existing file differs from current scaffold
- Legacy/historical path preserved
- Unexpected extra file/directory
- Potential conflict requiring human review

## 10. Legacy / Historical Paths Preserved

List historical paths such as older `COMPASS_Layer0_*` checkpoints.

State that they were preserved and not renamed.

## 11. Proposed Create-Only Changes

List changes that may be created in `create-missing-only` mode after approval. Missing seed scaffold directories and seed placeholder/template files may be proposed, but existing resumes, CVs, or source files must not be moved into `/sources/seed/`.

## 12. Forbidden Changes Not Performed

Confirm:

- No overwrites
- No deletes
- No renames
- No moves
- No checkpoint rewrites
- No claim-ledger edits
- No do-not-claim edits
- No automatic movement of existing resumes, CVs, or source files into `/sources/seed/`

## 13. Manual Decisions Required

List unresolved decisions.

## 14. Storage Status

Use one approved label:

- Storage status: verified in datastore
- Storage status: generated locally / ready for upload
- Storage status: copy-ready only / not yet persisted
- Storage status: storage unavailable / manual save required

## 15. Next Safe Action

Recommend one:

- remain in dry-run
- approve create-missing-only
- resolve conflicts first
- continue COMPASS Intake separately
