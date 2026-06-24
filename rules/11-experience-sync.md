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

Source Rebase aligns Source of Truth scaffold structure, including the optional private Experience Sync routing scaffold. Experience Sync reads that configuration but must not create or modify it during a sync run.

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

## Repository Routing Model

The private Source of Truth should contain the authoritative source-to-target routing map at:

```text
sync/COMPASS_Experience_Targets.yaml
```

Use `templates/source-of-truth-scaffold/sync/COMPASS_Experience_Targets.yaml` as the default scaffold shape.

The routing map may contain:

- stable source ID;
- actual Source of Truth repository and branch;
- one or more target IDs;
- actual target repository and branch;
- target manifest path;
- intended audience;
- publication defaults;
- protected target paths;
- write policy;
- enabled or disabled target status.

This file is private Source of Truth configuration. Do not copy it into a public experience repository.

### Target resolution order

Resolve the target in this order:

1. A direct current user instruction naming a target ID or explicit target repository.
2. A matching enabled target ID in `sync/COMPASS_Experience_Targets.yaml`.
3. An explicit target repository supplied for the current dry-run when no source-side map exists.
4. A stop condition when the target remains ambiguous.

A direct repository override must not silently replace an existing mapped target. If the override conflicts with the source-side map, report the conflict and require a human decision.

When a source-side map is absent but the user explicitly supplies both repositories, Experience Sync may perform a dry-run or full audit. The report must identify the missing routing configuration and recommend adding it through Source Rebase or a separately approved Source of Truth configuration change.

Experience Sync must not write the source-side routing map because Experience Sync never modifies the Source of Truth.

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
- claims needing evidence, metrics, scope clarification, or material conflict resolution;
- the actual private Source of Truth repository name or URL in a public target manifest.

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

In dry-run, Experience Sync may inspect the framework, Source of Truth repository, source-side routing map, experience repository, target manifest, commit history, ledgers, records, and target files. It may produce a reconciliation report. It must perform no writes.

Dry-run must report:

1. framework version and governing files;
2. source repository, branch, and inspected commit;
3. selected target ID and target-resolution basis;
4. target repository, branch, and inspected commit;
5. previous reconciliation state, if available;
6. source changes or full-audit scope examined;
7. claim authority and coverage classifications;
8. proposed public additions, updates, narrowings, removals, and provisional markers;
9. disclosure abstractions and withheld content;
10. conflicts or decisions requiring human review;
11. target files that would change;
12. write and visibility-verification capability;
13. forbidden actions not performed;
14. next safe action.

### Full Audit

`full-audit` is a read-only dry-run variant that rechecks the entire target experience repository against the current Source of Truth rather than relying only on changes since the last reconciled commit.

Use full audit for:

- first-time Experience Sync setup;
- suspected drift;
- manual edits to the experience repository;
- changes to publication policy;
- major framework or claim-depth changes;
- missing or unreliable sync-manifest history;
- migration from a target manifest that exposed the private source repository location.

### Apply Approved

`apply-approved` is the only write-capable mode.

It requires:

- a current dry-run or full-audit report for the exact source commit, selected target ID, target repository, and target commit;
- explicit user approval to apply that report;
- verified write access to the target repository;
- no unresolved `requires-human-decision` items affecting the requested changes.

In apply-approved mode, COMPASS may:

- create a target branch;
- create, update, or remove approved public-projection files on that branch;
- update the sanitized target Experience Manifest and public claim provenance;
- create a reconciliation report in the target repository when approved;
- open a pull request from the sync branch into the target base branch configured by the source-side map or current instruction.

Experience Sync must not write directly to the target default branch or modify the source-side routing map.

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
4. update target-local reconciliation metadata;
5. open a pull request;
6. summarize source commit, selected target ID, target base commit, changed claims, disclosure actions, and unresolved follow-ups.

Do not merge the pull request unless the user explicitly asks.

## Source-Side Target Map

The authoritative routing file is private and belongs in the Source of Truth:

```text
sync/COMPASS_Experience_Targets.yaml
```

A Source of Truth may define multiple downstream targets, including a public experience repository, personal website, recruiter-facing evidence repository, internal portfolio, or future retrieval service.

Each target must have a stable `id`. Target IDs should remain stable even when repository names or hosting locations change.

Experience Sync reads this map. Source Rebase may create the missing scaffold placeholder after explicit approval. Neither workflow may overwrite an existing user-owned map.

## Public Experience Manifest

Use `templates/experience-sync/COMPASS_Experience_Manifest_TEMPLATE.yaml` as the default target-repository manifest shape.

The public target manifest should record:

- schema version;
- repository role;
- stable source ID, but not the private source repository location;
- target repository and branch;
- last reconciled source and target commits;
- last reconciliation date and mode;
- framework version;
- publication defaults;
- write policy;
- protected paths;
- public claim index path, if used;
- report history or latest report path.

The target manifest must not expose the private Source of Truth repository name or URL unless the user explicitly approves publication and the source repository is itself intended to be public.

Repository-specific manifests may extend the template, but they must not weaken TruthGuard, source priority, public-disclosure controls, source-location privacy, or branch-and-PR-only writes.

## Public Claim Provenance

Public structured claims should record, when practical:

- stable public claim ID;
- approved public wording;
- source status such as `compass-reconciled` or `provisional-baseline`;
- stable source record or ledger references that do not reveal private repository location;
- source commit;
- claim-depth or contribution boundary;
- public-projection status;
- disclosure abstraction note, when applicable;
- limitations;
- last reconciled date.

Do not expose private Source of Truth content or repository location merely to provide provenance. Stable record IDs and repository-relative source paths are preferable to public URLs.

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
- missing or stale manifest metadata;
- target manifests that expose a private Source of Truth repository location;
- source-side target mappings that disagree with target-local identity or branch metadata.

Manual target edits are not automatically wrong. Classify them and reconcile them against source authority rather than overwriting them blindly.

## Conflict Handling

Stop and require human review when:

- Source of Truth records conflict materially;
- a public claim cannot be safely abstracted without changing its meaning;
- target edits introduce useful wording not clearly supported by source records;
- removal would materially change public positioning and the governing do-not-claim or approval status is unclear;
- a direct target override conflicts with the source-side routing map;
- repository ownership, target branch, protected paths, target ID, or publication audience is unclear;
- the current dry-run report no longer matches the inspected source or target commits;
- apply-approved would require changes outside the approved report.

Do not silently choose the more favorable wording or repository target.

## Forbidden Operations

COMPASS Experience Sync must not:

- modify the Source of Truth repository;
- create or edit `sync/COMPASS_Experience_Targets.yaml` during a sync run;
- modify Intake checkpoints, claim ledgers, do-not-claim records, source registers, or canonical career records;
- treat the experience repository as factual authority;
- infer or approve new career claims;
- publish unresolved or rejected claims;
- weaken privacy, confidentiality, security, or disclosure boundaries;
- copy the complete Source of Truth into the public repository;
- expose the private Source of Truth repository location in a public manifest by default;
- expose raw evidence merely to make a public claim appear stronger;
- overwrite protected target paths;
- write directly to the target default branch;
- merge a pull request without explicit user instruction;
- claim files were changed, persisted, or verified when they were not.

## Storage and Access Honesty

Before any write-capable action, disclose:

- source read access;
- source-side routing-map access;
- selected target ID and resolution basis;
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
4. selected target ID and target-resolution basis;
5. target repository, branch, and commit;
6. access and write-capability disclosure;
7. previous reconciliation state;
8. source scope examined;
9. authority and coverage findings;
10. proposed additions;
11. proposed wording updates and narrowings;
12. proposed removals and do-not-claim corrections;
13. provisional claims retained or replaced;
14. disclosure abstractions and withheld content;
15. conflicts and manual decisions;
16. files that would change;
17. forbidden actions not performed;
18. validation performed;
19. storage status;
20. next safe action.

## Validation

Before completing dry-run or apply-approved, validate as applicable:

- source-side routing-map syntax;
- selected target ID uniqueness and enabled status;
- target manifest syntax;
- structured claim syntax and unique IDs;
- relative links and referenced target files;
- source references and commit metadata;
- no direct PII or prohibited private content in changed public files;
- no private Source of Truth repository location in public target files unless explicitly approved;
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
- target selection is ambiguous;
- a target override conflicts with the source-side map;
- the selected target is disabled;
- unresolved claims materially affect publication;
- protected paths would need modification;
- apply-approved lacks a current matching report;
- the source or target commit changed after approval;
- write or visibility-verification capability is unclear for a requested write;
- a safe public abstraction cannot be produced without user judgment.
