# COMPASS Intake Artifact Templates

These templates provide copy-ready shapes for COMPASS Intake checkpoint artifacts.

The durable behavior source is `rules/07-compass-intake.md`. If a template must be adapted, preserve the Intake rule, source priority, TruthGuard, coverage gate, do-not-claim behavior, and storage-honesty requirements.

## Checkpoint Markdown Record

```markdown
# COMPASS Intake Checkpoint - [Round ID] - [Topic] - [YYYY-MM-DD]

## Checkpoint Status

- Framework: COMPASS
- Workflow: COMPASS Intake - Verified Source-of-Truth Onboarding
- Checkpoint ID: [compass-intake-YYYY-MM-DD-###]
- Round ID: [Round## or Round#A]
- Current stage: [setup / source harvesting / cross-examination / ledger update / pause bookmark]
- Source set covered: [source document, folder, role, project, or claim group]
- Intake completeness for current source set: [partial / complete]

## Storage Status

- Storage status: [one approved storage-status label]
- Direct-write availability: [true / false / unknown]
- Target datastore: [Google Drive folder / GitHub repo / local folder / other]
- Datastore visibility verified: [yes / no / not applicable]
- Files generated or updated:
  - [checkpoints/COMPASS_Intake_Round##_Topic_YYYY-MM-DD.md]
  - [ledgers/Approved_Claim_Ledger.md]
  - [ledgers/Do_Not_Claim_Register.md]
  - [ledgers/Coverage_Register.md]
- Next safe action: [upload files / verify files / resume from next claim group]

## Round Summary

- Confirmed facts:
  - [fact or none]
- Source-extracted claims reviewed:
  - [claim or none]
- Inferred claims asked as questions:
  - [question or none]
- Contradictions resolved:
  - [resolution or none]
- Contradictions still open:
  - [open issue or none]
- Unresolved questions:
  - [question or none]

## Materiality Gate Decisions

- Questions asked:
  - Question: [question or none]
  - Materiality reason: [source-of-truth construction / claim approval / claim-depth boundary / evidence requirement / metric requirement / scope clarification / downstream-safe wording / contradiction]
  - Source basis: [approved ledger / do-not-claim register / coverage register / checkpoint / canonical source record / source artifact / user statement / none]
- Questions not asked:
  - Potential question: [question or none]
  - Decision: [already resolved by approved source / non-material detail / discoverable from sources / safe assumption]
  - Source basis or assumption: [source or assumption]
- Resolved from sources:
  - [claim or question resolved from approved ledger, checkpoint, coverage register, canonical source record, or source artifact]
  - Status: [approved / source-extracted unconfirmed / user-confirmed / narrowed / do-not-claim boundary / other coverage status]
- Deferred or next-batch questions:
  - [question or none]
  - Deferral reason: [lower priority than current material batch / awaiting evidence / awaiting metric / awaiting scope clarification / user pause]
- Contradictions or conflicts:
  - [conflict or none]
  - Handling: [blocked by do-not-claim / ask targeted question / defer / needs evidence / needs metric / needs scope clarification]

## Ledger Changes

- Approved claims:
  - [claim ID and approved wording or none]
- Approved with narrowed wording:
  - [claim ID and wording or none]
- Approved with claim-depth boundary:
  - [claim ID, boundary, and wording or none]
- Rejected / do-not-claim:
  - [claim ID and rejected wording or none]
- Needs evidence:
  - [claim ID or none]
- Needs metric:
  - [claim ID or none]
- Needs scope clarification:
  - [claim ID or none]
- Deferred intentionally:
  - [claim ID or none]
- Not material / excluded with reason:
  - [claim ID or none]

## Coverage Changes

| Coverage ID | Source / section | Material claim | Status | Resolution or next action |
| --- | --- | --- | --- | --- |
| [COV-###] | [source] | [claim] | [status] | [note] |

## Resume Point

- Next uncovered source section, role, project, or claim group: [next item]
- Next questions to ask:
  - [question]
```

## Claim Ledger Entry

```markdown
## [CLAIM-###] [Short Claim Label]

- Claim text: [source-extracted or user-confirmed claim]
- Source or provenance: [source file, user statement, checkpoint ID, or other provenance]
- Status: [Imported / unreviewed | Source-extracted / unconfirmed | User-confirmed | Approved | Approved with narrowed wording | Approved with claim-depth boundary | Rejected / do-not-claim | Needs evidence | Needs metric | Needs scope clarification | Deferred intentionally | Not material / excluded with reason]
- Approved wording: [exact approved wording or not applicable]
- Claim-depth boundary: [No claim / Awareness / Exposure / Supported / Implemented / Owned / Led others / not applicable]
- Evidence, metric, scope, deferral, or exclusion note: [note or not applicable]
- Last reviewed: [YYYY-MM-DD or checkpoint ID]
```

## Do-Not-Claim Entry

```markdown
## [DNC-###] [Short Rejected Claim Label]

- Rejected claim or prohibited wording: [wording that must not be used]
- Source or provenance: [where the claim appeared or how it was proposed]
- Reason for rejection or boundary: [user rejected / unsupported / overstated / wrong timeline / wrong ownership / other]
- Downstream block instruction: Do not include this claim or equivalent wording in resumes, cover letters, recruiter messages, application answers, interview prep, or other downstream artifacts unless the user explicitly reopens and approves it through Intake.
- Last reviewed: [YYYY-MM-DD or checkpoint ID]
```

## Coverage-Register Entry

```markdown
## [COV-###] [Source / Claim Group Label]

- Source artifact, section, role, project, or claim group: [source area]
- Material claim text or summary: [claim summary]
- Provenance note: [source file, user statement, or checkpoint ID]
- Current status: [Imported / unreviewed | Source-extracted / unconfirmed | User-confirmed | Approved | Approved with narrowed wording | Approved with claim-depth boundary | Rejected / do-not-claim | Needs evidence | Needs metric | Needs scope clarification | Deferred intentionally | Not material / excluded with reason]
- Resolution note or next action: [what changed or what remains]
- Last reviewed: [YYYY-MM-DD or checkpoint ID]
```

## Storage-Status Block

```yaml
storage_status:
  label: "generated locally / ready for upload"
  direct_write_available: false
  target_datastore: "[target datastore]"
  files_generated_or_updated:
    - "checkpoints/COMPASS_Intake_Round##_Topic_YYYY-MM-DD.md"
    - "ledgers/Approved_Claim_Ledger.md"
    - "ledgers/Do_Not_Claim_Register.md"
    - "ledgers/Coverage_Register.md"
  datastore_visibility_verified: false
  next_safe_action: "Upload the generated files to the target datastore, verify visibility, then resume Intake from the checkpoint resume point."
```

Approved storage-status labels:

- `verified in datastore`
- `generated locally / ready for upload`
- `copy-ready only / not yet persisted`
- `storage unavailable / manual save required`

## Optional ZIP Bundle Manifest

```yaml
zip_bundle_manifest:
  bundle_filename: "COMPASS_Intake_Round##_Topic_YYYY-MM-DD.zip"
  checkpoint_id: "compass-intake-YYYY-MM-DD-###"
  round_id: "[Round##]"
  included_files:
    - "checkpoints/COMPASS_Intake_Round##_Topic_YYYY-MM-DD.md"
    - "ledgers/Approved_Claim_Ledger.md"
    - "ledgers/Do_Not_Claim_Register.md"
    - "ledgers/Coverage_Register.md"
  storage_status: "generated locally / ready for upload"
  upload_destination: "[target datastore folder or repo path]"
  verification_instruction: "After upload, verify the files are visible in the target datastore before treating them as persisted source-of-truth records."
```
