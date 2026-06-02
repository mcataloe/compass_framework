# Initial Seed Artifacts

This folder is the recommended COMPASS location for Initial Seed Artifacts.

Seed artifacts are user-provided career source materials available before or during COMPASS Intake. They are seed, provisional, evidence, and not canonical. Verified Intake records, approved claim ledgers, do-not-claim ledgers, and canonical source-of-truth records supersede seed artifacts for downstream authority when available.

## What Belongs Here

- Existing resumes
- Shortened or tailored resumes
- Comprehensive resumes
- Master CVs
- LinkedIn exports
- Prior cover letters
- Portfolio summaries
- Achievement lists
- Other career evidence supplied by the user

## What Does Not Belong Here

- Final generated downstream artifacts unless the user intentionally imports them as source evidence
- Private tactical notes that are not intended for the source-of-truth repository
- Unsupported claims invented to satisfy a target role
- Files that should be excluded by a do-not-use decision

## Recommended Folders

```text
/sources/seed/resumes/
/sources/seed/cvs/
/sources/seed/linkedin/
/sources/seed/cover-letters/
/sources/seed/portfolio/
/sources/seed/other/
```

## Resume and CV Guidance

A comprehensive resume or master CV may remain useful for a longer provisional period because it is more likely to preserve career breadth.

A shortened or tailored resume is useful seed evidence, but it is usually incomplete and should be treated more cautiously because it may omit material history or reflect one target role.

Neither a shortened resume nor a master CV becomes permanent canonical truth merely by being stored under `/sources/seed/`.

## Status Labels

Use one of these status labels in `SEED_ARTIFACTS_MANIFEST.md`:

- `available-provisional`
- `partially-ingested`
- `fully-ingested`
- `superseded`
- `do-not-use`
- `archived-provenance`

## Supersession

After relevant claims are extracted, reconciled, and verified through COMPASS Intake, the verified source-of-truth records and ledgers supersede the seed artifact for downstream use. Keep the seed artifact traceable as provenance unless the user explicitly removes it.
