# COMPASS Experience Sync Templates

These templates support `COMPASS Experience Sync`, the one-way reconciliation workflow from an approved career Source of Truth into a separate public or externally shareable experience repository.

## Templates

- `COMPASS_Experience_Manifest_TEMPLATE.yaml` — declares sanitized target-local identity, source ID, prior reconciliation state, publication defaults, protected paths, and write policy.
- `COMPASS_Experience_Sync_Report_TEMPLATE.md` — records dry-run, full-audit, or apply-approved reconciliation findings and validation.
- `COMPASS_Public_Claim_TEMPLATE.yaml` — provides a generic provenance shape for structured public claims.

The authoritative source-to-target routing map belongs in the private Source of Truth at `sync/COMPASS_Experience_Targets.yaml`, using the scaffold template under `templates/source-of-truth-scaffold/sync/`.

## Ownership boundary

These are framework defaults. A target experience repository may adapt paths and add fields, but repository-specific configuration must not weaken:

- Source of Truth authority;
- TruthGuard and do-not-claim controls;
- claim-depth and contribution boundaries;
- public-disclosure filtering;
- dry-run default behavior;
- branch-and-pull-request-only writes;
- the prohibition on Source of Truth modification.

The experience repository is a downstream publication artifact. It is not a canonical factual source.

## Public manifest privacy

A public Experience Manifest should not expose the private Source of Truth repository name or URL. It should use a stable source identifier plus reconciliation metadata. The private source-side target map resolves that identifier to the actual repository and target configuration.
