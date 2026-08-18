# COMPASS Intake Checkpoint Example — Default Artifact Persistence

This example demonstrates the generic default Intake persistence model. Use it only when the active Source-of-Truth persistence contract resolves to default artifact persistence.

Use `examples/compass-intake-artifact-templates.md` for copy-ready checkpoint, claim-ledger, do-not-claim, coverage-register, storage-status, and ZIP manifest skeletons. The durable rule source remains `rules/07-compass-intake.md`.

A current user-owned Source of Truth may explicitly declare repository-defined canonical persistence. In that mode, update the governing current authorities according to the active policy and do not generate this parallel checkpoint/ledger set merely because this example exists.

```yaml
checkpoint:
  framework: COMPASS
  workflow: "COMPASS Intake — Verified Source-of-Truth Onboarding"
  persistence_mode: "default_artifact_persistence"
  checkpoint_id: "compass-intake-YYYY-MM-DD-001"
  round_id: "Round1A"
  current_stage: "Source harvesting / cross-examination"
  storage_status: "generated locally / ready for upload"
  direct_write_available: false
  target_datastore: "Google Drive folder supplied by user"
  generated_artifacts:
    - "checkpoints/COMPASS_Intake_Round1A_Example_YYYY-MM-DD.md"
    - "ledgers/Approved_Claim_Ledger.md"
    - "ledgers/Do_Not_Claim_Register.md"
    - "ledgers/Coverage_Register.md"
    - "exports/COMPASS_Intake_Round1A_Example_YYYY-MM-DD.zip"
  datastore_visibility_verified: false
  completed_sections:
    - source_document_inventory
    - preliminary_timeline
  partially_completed_sections:
    - claim_verification
    - capability_depth_classification
  coverage_register_entries:
    - coverage_id: "COV-001"
      source_or_section: "Example source document"
      material_claim: "Example extracted claim requiring user verification."
      status: "Source-extracted / unconfirmed"
      next_action: "Ask the user to confirm, narrow, reject, defer, or mark the claim as needing evidence."
  approved_claims_count: 12
  rejected_claims_count: 3
  unresolved_claims_count: 18
  next_questions:
    - "Confirm the actual depth of involvement for the next extracted claim."
    - "Resolve the contradiction between two source documents."
    - "Confirm whether a real metric exists or if non-quantified phrasing is required."
  next_safe_action: "Upload generated checkpoint artifacts to the datastore, verify visibility, then resume Intake from unresolved claims."
```

## Artifact Expectations

Under default artifact persistence, every committed Intake round should produce at least one checkpoint Markdown artifact.

When applicable, it should also produce updated default control artifacts:

- Approved claim ledger
- Do-not-claim register
- Coverage register
- Source register updates when applicable
- Claim-depth boundary updates when applicable

If direct datastore write access is unavailable, the assistant should generate downloadable or copy-ready files and clearly state that the files still need to be uploaded by the user.

These expectations do not apply as mandatory parallel files when an explicit current repository-defined canonical persistence contract supplies equivalent governing state.
