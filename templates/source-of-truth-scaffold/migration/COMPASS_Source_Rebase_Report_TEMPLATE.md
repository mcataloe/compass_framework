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

## 5. Manifest Policy Resolution

- Current Source Manifest found: yes/no
- Manifest path:
- Persistence/lifecycle policy found: yes/no
- Retired-path policy found: yes/no
- Policy ambiguity or conflict:

Do not infer retired paths from absence, naming, age, or apparent non-use.

## 6. Existing Layout Found

List directories/files detected.

## 7. Generic Expected Scaffold

List directories/files from the current generic framework scaffold, including `/sources/seed/` Initial Seed Artifact paths and `/sync/` routing paths when applicable.

## 8. Manifest-Retired Active-Tree Paths

List paths or path classes explicitly retired by current user-owned manifest policy.

For each path, state whether it is:

- absent as intended; or
- still present and left untouched.

An absent explicitly retired path is not missing drift.

## 9. Repository-Specific Expected Scaffold

List the generic expected scaffold after applying explicit current manifest retirement policy.

Only this repository-specific expected scaffold is eligible for missing-path classification or `create-missing-only` proposals.

## 10. Files Already Present

List expected files that already exist and were skipped.

## 11. Missing Non-Retired Files / Directories

List repository-specific expected scaffold files/directories that are missing.

Do not include manifest-retired paths.

## 12. Drift Detected

Classify findings as:

- Missing expected directory
- Missing expected scaffold file
- Existing user-owned file at expected path
- Existing file differs from current scaffold
- Legacy/historical path preserved by current policy
- Manifest-retired path absent as intended
- Manifest-retired path still present and untouched
- Unexpected extra file/directory
- Potential conflict requiring human review

## 13. Legacy / Historical Paths Preserved

List historical paths that remain active under current repository policy, such as older `COMPASS_Layer0_*` checkpoints.

State that Source Rebase preserved and did not rename them.

Historical preservation is the generic default when current user-owned policy does not explicitly retire the path.

## 14. Proposed Create-Only Changes

List changes that may be created in `create-missing-only` mode after approval.

Only absent non-retired paths may be proposed. Missing seed scaffold directories and seed placeholder/template files may be proposed only when they remain part of the repository-specific expected scaffold. Existing resumes, CVs, or source files must not be moved into `/sources/seed/`.

## 15. Forbidden Changes Not Performed

Confirm:

- No overwrites
- No deletes
- No renames
- No moves
- No checkpoint rewrites
- No claim-control edits
- No do-not-claim edits
- No automatic movement of existing resumes, CVs, or source files into `/sources/seed/`
- No recreation of manifest-retired paths
- No lifecycle deletion of existing retired paths

## 16. Manual Decisions Required

List unresolved decisions, including ambiguous retirement declarations or ownership conflicts.

## 17. Storage Status

Use one approved label:

- Storage status: verified in datastore
- Storage status: generated locally / ready for upload
- Storage status: copy-ready only / not yet persisted
- Storage status: storage unavailable / manual save required

## 18. Next Safe Action

Recommend one:

- remain in dry-run
- approve create-missing-only for the exact non-retired path set
- resolve manifest ambiguity or conflicts first
- continue COMPASS Intake separately
- perform separately authorized lifecycle cleanup outside Source Rebase
