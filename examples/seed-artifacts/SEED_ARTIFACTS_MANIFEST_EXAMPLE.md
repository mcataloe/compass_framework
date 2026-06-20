# Seed Artifacts Manifest - Example

This fictional example shows how Initial Seed Artifacts can be tracked. It does not describe a real person.

Required trust labels used by this manifest:

- seed
- provisional
- evidence
- not canonical
- superseded by verified source-of-truth when available

## Artifact Entry

- Artifact ID: SEED-001
- File path: `/sources/seed/resumes/Jordan_Lee_Product_Platform_Tailored_Resume_2026-04.pdf`
- Original filename: `Jordan_Lee_Product_Platform_Tailored_Resume_2026-04.pdf`
- Artifact type: `resume`
- Artifact subtype: shortened tailored resume
- Date added: 2026-06-02
- Added by: candidate
- Source format: PDF
- Intended use: Provisional Resume / CV Mode for one product-platform target role while Intake is incomplete.
- Provisional downstream use allowed: yes, with caution
- Current status: `partially-ingested`
- Intake coverage status: summary and two role bullets reviewed; project metrics still need confirmation
- Supersession status: partially superseded by `ledgers/03_Approved_Claim_Ledger.md`
- Superseded by: `CLAIM-014`, `CLAIM-018`, `COV-022`
- Known limitations: Tailored to one target role and may omit earlier career history.
- Known conflicts: One ownership phrase is broader than the approved claim-depth boundary.
- Do-not-use notes: Do not use the phrase "owned the full AI roadmap" unless reopened and approved through Intake.
- Last reviewed: 2026-06-02
- Notes: Useful as seed evidence, but not canonical.

## Artifact Entry

- Artifact ID: SEED-002
- File path: `/sources/seed/cvs/Jordan_Lee_Master_CV_2026-05.docx`
- Original filename: `Jordan_Lee_Master_CV_2026-05.docx`
- Artifact type: `master-cv`
- Artifact subtype: comprehensive career archive
- Date added: 2026-06-02
- Added by: candidate
- Source format: DOCX
- Intended use: Broader provisional baseline for Intake coverage and Provisional Resume / CV Mode.
- Provisional downstream use allowed: yes, with source limitations
- Current status: `available-provisional`
- Intake coverage status: not fully ingested; employment timeline and project inventory pending review
- Supersession status: not yet superseded
- Superseded by: not applicable
- Known limitations: Contains older project descriptions that may need date and scope confirmation.
- Known conflicts: None recorded.
- Do-not-use notes: None recorded.
- Last reviewed: 2026-06-02
- Notes: More complete than the shortened resume, but still provisional evidence and not canonical.

## Artifact Entry

- Artifact ID: SEED-003
- File path: `/sources/seed/cover-letters/Jordan_Lee_Old_Cover_Letter_2024-11.docx`
- Original filename: `Jordan_Lee_Old_Cover_Letter_2024-11.docx`
- Artifact type: `cover-letter`
- Artifact subtype: prior application artifact
- Date added: 2026-06-02
- Added by: candidate
- Source format: DOCX
- Intended use: Provenance only.
- Provisional downstream use allowed: no
- Current status: `do-not-use`
- Intake coverage status: excluded as not material
- Supersession status: archived for provenance
- Superseded by: not applicable
- Known limitations: Written for a past company and not suitable as current source material.
- Known conflicts: Contains an unsupported industry claim.
- Do-not-use notes: Do not reuse the unsupported industry claim or company-specific motivation language.
- Last reviewed: 2026-06-02
- Notes: Kept only to preserve source history.

## Artifact Entry

- Artifact ID: SEED-004
- File path: `/sources/seed/linkedin/Jordan_Lee_LinkedIn_Export_2026-05.zip`
- Original filename: `Jordan_Lee_LinkedIn_Export_2026-05.zip`
- Artifact type: `linkedin-export`
- Artifact subtype: profile export
- Date added: 2026-06-02
- Added by: candidate
- Source format: ZIP
- Intended use: Provenance for profile language and employment-date comparison.
- Provisional downstream use allowed: no
- Current status: `archived-provenance`
- Intake coverage status: fully ingested for profile headline and employment dates
- Supersession status: superseded
- Superseded by: `COV-031`, `CLAIM-027`
- Known limitations: Public profile wording was abbreviated.
- Known conflicts: None remaining after Intake review.
- Do-not-use notes: None recorded.
- Last reviewed: 2026-06-02
- Notes: Retained for traceability after verified source-of-truth records superseded it.
