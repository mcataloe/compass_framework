# 11 - COMPASS Experience Sync

## Purpose

COMPASS Experience Sync reconciles an approved career Source of Truth into a separate public or externally shareable experience repository.

Experience Sync is a one-way projection workflow:

```text
COMPASS Source of Truth
          ↓
approved public projection
          ↓
Experience Repository
```

The Source of Truth remains the factual authority. The experience repository is a downstream publication artifact and must never update, override, or become factual authority for the Source of Truth.

## When to Use

Use COMPASS Experience Sync when the user wants to:

- compare a public experience repository with the latest approved COMPASS Source of Truth;
- publish newly approved Intake claims into an experience repository;
- narrow, replace, or remove public claims after Source of Truth corrections;
- distinguish COMPASS-reconciled content from provisional CV-derived content;
- audit public career content for factual drift, claim-depth drift, or disclosure risk;
- create a review branch and pull request containing approved public-projection changes.

## Relationship to Other COMPASS Workflows

### COMPASS Intake

COMPASS Intake verifies, approves, narrows, rejects, and records career claims. Experience Sync consumes those results. It must not replace Intake or silently resolve unresolved career facts.

If the Source of Truth contains unresolved material conflicts, missing claim-depth boundaries, or unverified claims whose resolution would affect publication, stop and route the user to COMPASS Intake.

### COMPASS Source Rebase

Source Rebase aligns Source of Truth scaffold structure. Experience Sync reconciles approved source records into a downstream experience repository. Do not combine the two workflows.

### COMPASS Analysis and Artifact Generation

Experience Sync is not role analysis, resume tailoring, cover-letter generation, recruiter messaging, or interview preparation. It maintains a broad public experience projection rather than a target-specific application artifact.

## Source Authority

Use the active COMPASS candidate-factual-authority order:

1. The user's direct current instruction.
2. User-confirmed COMPASS Intake claim ledgers and do-not-claim records.
3. Latest approved canonical Source of Truth records.
4. A provisional baseline explicitly authorized by the Source of Truth, used only at its documented source-stated depth.
5. Imported artifacts as evidence and provenance only.
6. Generated artifacts as historical outputs only.
7. Project memory only when not contradicted by stronger sources and never as a substitute for available records.

Do-not-claim entries override all downstream publication pressure.

## Public-Projection Gate

Factual approval and public suitability are separate decisions.

Every candidate claim must pass both gates:

1. **Truth gate:** Is the claim approved, narrowed, claim-depth-bounded, or explicitly authorized for provisional use?
2. **Publication gate:** Is the claim appropriate and useful for the intended public or external audience?

A fact may be canonical but still unsuitable for public release because it contains personal information, private strategy, internal names, colleague names, customer-sensitive detail, security-sensitive detail, evidence inventories, or unnecessary operational specifics.

## Publication Exclusions

Unless the user explicitly approves otherwise, exclude or abstract:

- personal phone numbers, home addresses, and personal email addresses;
- compensation targets, negotiation strategy, and private job-search constraints;
- recruiter communications, interview notes, and private tactical analysis;
- raw Intake questions, checkpoints, internal deliberation, and evidence inventories;
- private access material, private URLs, customer data, and internal source code;
- names of individual colleagues or private stakeholders;
- non-public customer names, project names, implementation topology, endpoints, account identifiers, and security configurations;
- do-not-claim rationale whose publication would reveal private or sensitive context;
- claims needing evidence, metrics, scope clarification, or material conflict resolution.

Abstraction must preserve the approved claim's meaning and depth. It must not make the claim broader, stronger, or more impressive.

## Coverage-Status Handling

Apply these default publication behaviors:

| Source status | Experience repository behavior |
|---|---|
| Approved | Eligible for publication after the publication gate |
| Approved with narrowed wording | Use only the approved narrowed wording |
| Approved with claim-depth boundary | Preserve the approved contribution boundary |
| Rejected / do-not-claim | Remove, block, or correct the public claim |
| Needs evidence | Do not publish as established fact |
| Needs metric | Do not publish the unsupported metric; retain safe qualitative wording only when separately approved |
| Needs scope clarification | Do not publish as settled |
| Deferred intentionally | Preserve existing approved wording or omit; do not strengthen |
| Not material / excluded | Omit unless a separate public-use rationale is approved |
| Imported / unreviewed | Publish only when provisional public use is explicitly authorized |
| Source-extracted / unconfirmed | Do not publish as established fact |
| User-confirmed but not approved | Treat as unresolved unless the active Source of Truth explicitly authorizes downstream use |

## Reconciliation Classifications

Classify each affected claim or content block as one of:

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

`remove-public-claim` means removing or correcting a public claim because it conflicts with an approved do-not-claim boundary or stronger source authority. It never means removing the do-not-claim guardrail itself.

Strengthening is permitted only when stronger wording is explicitly approved by the Source of Truth and passes the publication gate.

## Modes

### Dry-Run

`dry-run` is the default mode.

In dry-run, Experience Sync may inspect the framework, Source of Truth repository, experience repository, manifests, commit history, ledgers, records, and target files. It may produce a reconciliation report. It must perform no writes.

Dry-run must report:

1. framework version and governing files;
2. source repository, branch, and inspected commit;
3. target repository, branch, and inspected commit;
4. previous reconciliation state, if available;
5. source changes or full-audit scope examined;
6. claim authority and coverage classifications;
7. proposed public additions, updates, narrowings, removals, and provisional markers;
8. disclosure abstractions and withheld content;
9. conflicts or decisions requiring human review;
10. target files that would change;
11. write and visibility-verification capability;
12. forbidden actions not performed;
13. next safe action.

### Full Audit

`full-audit` is a read-only dry-run variant that rechecks the entire target experience repository against the current Source of Truth rather than relying only on changes since the last reconciled commit.

Use full audit for:

- first-time Experience Sync setup;
- suspected drift;
- manual edits to the experience repository;
- changes to publication policy;
- major framework or claim-depth changes;
- missing or unreliable sync-manifest history.

### Apply Approved

`apply-approved` is the only write-capable mode.

It requires:

- a current dry-run or full-audit report for the exact source and target repositories;
- explicit user approval to apply that report;
- verified write access to the target repository;
- no unresolved `requires-human-decision` items affecting the requested changes.

In apply-approved mode, COMPASS may:

- create a target branch;
- create, update, or remove approved public-projection files on that branch;
- update the target Experience Manifest and public claim provenance;
- create a reconciliation report in the target repository when approved;
- open a pull request from the sync branch into the target base branch configured by the manifest or current instruction.

Experience Sync must not write directly to the target default branch.

## Branch and Pull-Request Policy

Default branch naming:

```text
experience-sync/YYYY-MM-DD
```

If that branch already exists, append a short descriptive suffix or sequence number.

Every apply-approved run must:

1. create or use an explicitly approved non-default target branch;
2. apply only changes covered by the approved report;
3. verify changed files when the connector supports verification;
4. update reconciliation metadata;
5. open a pull request;
6. summarize source commit, target base commit, changed claims, disclosure actions, and unresolved follow-ups.

Do not merge the pull request unless the user explicitly asks.

## Experience Manifest

Use `templates/experience-sync/COMPASS_Experience_Manifest_TEMPLATE.yaml` as the default target-repository manifest shape.

The target manifest should record:

- schema version;
- repository role;
- source repository and branch;
- target repository and branch;
- last reconciled source and target commits;
- last reconciliation date and mode;
- publication defaults;
- write policy;
- protected paths;
- public claim index path, if used;
- report history or latest report path.

Repository-specific manifests may extend the template, but they must not weaken TruthGuard, source priority, public-disclosure controls, or branch-and-PR-only writes.

## Public Claim Provenance

Public structured claims should record, when practical:

- stable public claim ID;
- approved public wording;
- source status such as `compass-reconciled` or `provisional-baseline`;
- source record or ledger references;
- source commit;
- claim-depth or contribution boundary;
- public-projection status;
- disclosure abstraction note, when applicable;
- limitations;
- last reconciled date.

Do not expose private Source of Truth content merely to provide provenance. Repository paths and stable record IDs are preferable to copying private evidence.

## Drift Detection

Experience Sync should detect:

- source-approved claims missing from the target;
- target claims no longer approved;
- target wording stronger than approved source wording;
- target wording weaker or stale after an approved source update;
- provisional claims that now have canonical replacements;
- duplicate claims presented as independent evidence;
- broken or stale source references;
- public files manually edited after the last reconciliation;
- publication-policy drift;
- missing or stale manifest metadata.

Manual target edits are not automatically wrong. Classify them and reconcile them against source authority rather than overwriting them blindly.

## Conflict Handling

Stop and require human review when:

- Source of Truth records conflict materially;
- a public claim cannot be safely abstracted without changing its meaning;
- target edits introduce useful wording not clearly supported by source records;
- removal would materially change public positioning and the governing do-not-claim or approval status is unclear;
- repository ownership, target branch, protected paths, or publication audience is unclear;
- the current dry-run report no longer matches the inspected source or target commits;
- apply-approved would require changes outside the approved report.

Do not silently choose the more favorable wording.

## Forbidden Operations

COMPASS Experience Sync must not:

- modify the Source of Truth repository;
- modify Intake checkpoints, claim ledgers, do-not-claim records, source registers, or canonical career records;
- treat the experience repository as factual authority;
- infer or approve new career claims;
- publish unresolved or rejected claims;
- weaken privacy, confidentiality, security, or disclosure boundaries;
- copy the complete Source of Truth into the public repository;
- expose raw evidence merely to make a public claim appear stronger;
- overwrite protected target paths;
- write directly to the target default branch;
- merge a pull request without explicit user instruction;
- claim files were changed, persisted, or verified when they were not.

## Storage and Access Honesty

Before any write-capable action, disclose:

- source read access;
- target read access;
- target write access;
- branch-creation capability;
- pull-request capability;
- post-write visibility-verification capability.

If target write access or verification is unavailable or uncertain, remain in dry-run and provide copy-ready changes or downloadable files.

## Required Experience Sync Report

Use `templates/experience-sync/COMPASS_Experience_Sync_Report_TEMPLATE.md`.

Every report must include:

1. mode and date;
2. framework version;
3. source repository, branch, and commit;
4. target repository, branch, and commit;
5. access and write-capability disclosure;
6. previous reconciliation state;
7. source scope examined;
8. authority and coverage findings;
9. proposed additions;
10. proposed wording updates and narrowings;
11. proposed removals and do-not-claim corrections;
12. provisional claims retained or replaced;
13. disclosure abstractions and withheld content;
14. conflicts and manual decisions;
15. files that would change;
16. forbidden actions not performed;
17. validation performed;
18. storage status;
19. next safe action.

## Validation

Before completing dry-run or apply-approved, validate as applicable:

- manifest syntax;
- structured claim syntax and unique IDs;
- relative links and referenced target files;
- source references and commit metadata;
- no direct PII or prohibited private content in changed public files;
- no target wording exceeds approved claim depth;
- no do-not-claim item is reintroduced;
- target branch differs from the default branch;
- pull-request diff contains only approved reconciliation changes.

Report checks that could not be run.

## Stop Conditions

Stop and report if:

- required framework files are missing;
- the Source of Truth cannot be inspected;
- the target repository cannot be inspected;
- source authority cannot be determined;
- the target manifest is missing and repository mapping is ambiguous;
- unresolved claims materially affect publication;
- protected paths would need modification;
- apply-approved lacks a current matching report;
- the source or target commit changed after approval;
- write or visibility-verification capability is unclear for a requested write;
- a safe public abstraction cannot be produced without user judgment.
