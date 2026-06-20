# Seed Artifacts Manifest

Use this manifest to track Initial Seed Artifacts stored under `/sources/seed/`.

Required trust labels for seed artifacts:

- seed
- provisional
- evidence
- not canonical
- superseded by verified source-of-truth when available

Allowed status values:

- `available-provisional`
- `partially-ingested`
- `fully-ingested`
- `superseded`
- `do-not-use`
- `archived-provenance`

Artifact type examples:

- `resume`
- `comprehensive-resume`
- `master-cv`
- `linkedin-export`
- `cover-letter`
- `portfolio-summary`
- `achievement-list`
- `other`

## Artifact Entry

- Artifact ID:
- File path:
- Original filename:
- Artifact type:
- Artifact subtype:
- Date added:
- Added by:
- Source format:
- Intended use:
- Provisional downstream use allowed:
- Current status:
- Intake coverage status:
- Supersession status:
- Superseded by:
- Known limitations:
- Known conflicts:
- Do-not-use notes:
- Last reviewed:
- Notes:

## Notes

Seed artifacts may support Provisional Resume / CV Mode while Intake is incomplete. They must not override verified Intake claim ledgers, do-not-claim ledgers, or canonical career records.
