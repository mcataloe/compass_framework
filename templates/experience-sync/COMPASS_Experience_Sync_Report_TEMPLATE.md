# COMPASS Experience Sync Report - YYYY-MM-DD

## 1. Mode and Date

- Requested mode:
- Effective mode:
- Report date:
- Writes performed: yes/no
- Reason:

## 2. Framework Version

- COMPASS framework repository:
- Framework branch/tag/commit:
- COMPASS version:
- Experience Sync rule version, if tracked:

## 3. Source Repository and Target Resolution

- Source repository:
- Source branch:
- Source commit inspected:
- Source read access:
- Source records inspected:
- Routing map path:
- Routing map access:
- Requested target ID or override:
- Selected target ID:
- Resolution basis: direct instruction / source-side map / explicit unmapped override
- Target enabled status:
- Mapping conflict detected: yes/no
- Public source-location exposure detected: yes/no

## 4. Target Repository

- Target repository:
- Target branch:
- Target commit inspected:
- Target read access:
- Target write access:
- Branch-creation capability:
- Pull-request capability:
- Visibility-verification capability:

## 5. Previous Reconciliation State

- Experience Manifest path:
- Public manifest uses stable source ID: yes/no
- Previous source commit:
- Previous target commit:
- Previous reconciliation date:
- Previous mode:
- Previous report path:
- Manifest reliability:

## 6. Source Scope Examined

List changed source records for incremental dry-run, or the complete source scope for full-audit.

Include:

- approved claim ledgers;
- do-not-claim records;
- coverage-register entries;
- canonical role and project records;
- authorized provisional baselines;
- user instructions that affect publication.

## 7. Authority and Coverage Findings

For each affected claim or content block, record:

| Claim/content ID | Source authority | Coverage status | Claim depth | Current target state | Reconciliation classification |
|---|---|---|---|---|---|
| | | | | | |

Allowed reconciliation classifications:

- `unchanged`
- `add-public-claim`
- `update-wording`
- `narrow-claim`
- `strengthen-with-approved-evidence`
- `remove-public-claim`
- `mark-provisional`
- `replace-provisional`
- `withhold-from-publication`
- `requires-human-decision`

`remove-public-claim` removes or corrects public wording that conflicts with stronger source authority or an approved do-not-claim boundary. It does not remove the do-not-claim control.

## 8. Proposed Public Additions

List new claims, pages, sections, or provenance records eligible for publication.

For each addition, include:

- source basis;
- approved public wording;
- claim-depth boundary;
- publication-gate result;
- target file;
- limitations.

## 9. Proposed Wording Updates and Narrowings

List stale, inaccurate, overly broad, or newly supportable target wording.

Separate:

- ordinary wording updates;
- narrowed claims;
- approved strengthening;
- collaborator or transition corrections;
- outcome or metric corrections.

## 10. Proposed Removals and Do-Not-Claim Corrections

List public claims or wording that must be removed, blocked, or corrected because they are rejected, superseded, unsupported, or inconsistent with approved claim depth.

## 11. Provisional Claims

### Retained

List provisional claims that remain authorized at source-stated depth.

### Replaced

List provisional claims now superseded by approved canonical records.

### Withheld

List unreviewed or unconfirmed material that must not be published.

## 12. Disclosure Abstractions and Withheld Content

Record publication-gate actions such as:

- direct PII removed;
- colleague names omitted;
- customer or project names abstracted;
- security-sensitive details reduced;
- evidence inventories withheld;
- private job-search strategy excluded;
- internal Intake detail excluded;
- private Source of Truth repository location removed from public target metadata.

State whether each abstraction preserves the approved claim meaning and depth.

## 13. Conflicts and Manual Decisions

List every `requires-human-decision` item.

Include:

- conflicting source records;
- unsafe or meaning-changing abstraction;
- unsupported manual target wording;
- unclear removal authority;
- target override conflicting with the source-side map;
- protected-path conflict;
- publication-audience ambiguity;
- source or target commit drift.

## 14. Target Files That Would Change

| Target path | Change type | Claims/content affected | Protected-path status |
|---|---|---|---|
| | | | |

## 15. Forbidden Actions Not Performed

Confirm:

- No Source of Truth files modified
- No source-side routing map modified
- No Intake checkpoints modified
- No claim ledgers modified
- No do-not-claim records modified
- No new career claims inferred or approved
- No unresolved claims published
- No protected target paths overwritten
- No direct target default-branch writes
- No pull request merged
- No private source archive copied into the target
- No private Source of Truth repository location added to public target metadata

## 16. Validation Performed

Record results for:

- routing-map syntax;
- unique and enabled target ID;
- target manifest syntax;
- sanitized source identifier;
- structured claim syntax;
- unique public claim IDs;
- relative links;
- source references;
- PII and private-content scan;
- private source-location scan;
- claim-depth comparison;
- do-not-claim scan;
- branch-policy check;
- pull-request diff review, when applicable.

List checks not run and why.

## 17. Storage Status

Use one status:

- Storage status: dry-run only / no writes
- Storage status: generated locally / ready for upload
- Storage status: copy-ready only / not yet persisted
- Storage status: target branch written / visibility verified
- Storage status: pull request opened / visibility verified
- Storage status: write unavailable / manual application required

## 18. Applied Change Metadata

Complete only for `apply-approved`:

- Approved report path or ID:
- Selected target ID:
- Target sync branch:
- Target branch base commit:
- Resulting head commit:
- Pull request URL or number:
- Files changed:
- Public manifest sanitized: yes/no
- Manifest updated: yes/no
- Post-write verification result:

## 19. Next Safe Action

Recommend one:

- remain in dry-run;
- run full-audit;
- add or repair the source-side target map through an approved Source of Truth configuration change;
- resolve Intake questions first;
- resolve publication decisions first;
- approve apply-approved for the exact report and target;
- review the opened pull request;
- merge only after explicit user review and instruction;
- repair target manifest or provenance metadata first.
