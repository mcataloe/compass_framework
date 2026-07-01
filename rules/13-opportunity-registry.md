# 13 — Opportunity Registry and Search-Run Persistence

This rule governs durable cross-run opportunity history for `COMPASS Verified Opportunity Search`.

It supplements `rules/12-verified-opportunity-search.md`. Rule 12 continues to govern discovery, verification, eligibility, alignment, opportunity quality, conversion conditions, contract utility, and result structure. This rule owns observational persistence, registry identity, run provenance, recovery, and the boundary between opportunity observations and candidate-confirmed status.

## Purpose

A Verified Opportunity Search must not repeatedly present an unchanged role as new merely because the current conversation cannot remember a prior run.

When a user's Source of Truth configures an opportunity registry, the search workflow should maintain:

1. a canonical current-state opportunity registry;
2. append-only search-run records;
3. conservative duplicate and repost relationships;
4. material-change history;
5. explicit persistence success or failure.

The registry is not a candidate-tracking inference engine. Observed posting facts and user-confirmed candidate status must remain separate.

## Authority and repository ownership

The COMPASS framework owns the reusable schema, identity rules, persistence method, failure behavior, and safety boundaries.

The user's Source of Truth owns:

- the actual registry and run-log paths;
- candidate-confirmed statuses;
- suppression and reconsideration policy;
- user-specific result thresholds;
- repository write permissions;
- protected-path and review requirements.

A registry write must never create candidate facts, career claims, application answers, commercial terms, or employer facts unsupported by current evidence.

## Activation

Observational persistence is active only when all of the following are true:

- the user's Source of Truth explicitly configures a registry and search-run path;
- the current command is `COMPASS Verified Opportunity Search` or an explicitly authorized registry-maintenance action;
- repository write capability is available;
- the write is limited to configured opportunity-registry and run-log paths;
- the workflow reports persistence status in the same response.

Running a configured Verified Opportunity Search authorizes observational persistence for that run. It does not authorize candidate-status inference or unrelated Source of Truth edits.

When no registry is configured or write capability is unavailable, continue the search, disclose that cross-run persistence was not updated, and produce a copy-ready registry delta when practical.

## Persistence threshold

Do not store every raw snippet, aggregator result, or weak discovery lead.

Persist an opportunity when at least one condition is true:

- it is reported in the user-facing output;
- it reaches current employer-controlled or accountable-source verification;
- it is excluded for a durable reason, including verified closure, hard-screen mismatch, or duplicate identity;
- it is recognized as previously handled;
- it represents a material change to an existing registry record.

Low-confidence discovery noise may remain only in transient working notes.

## Required state separation

Each opportunity record must keep these concerns distinct:

### Identity

Stable identifiers, employer or accountable entity, ATS provider, requisition ID, canonical and alternate URLs, duplicate relationships, and repost relationships.

### Observation

First seen, last seen, last verified, posting state, verification strength, location and remote facts, and material signature.

### Reporting

First reported, last reported, report count, and the last run that reported the role.

### Candidate status

User-confirmed or explicitly authorized state such as applied, interviewing, rejected, withdrawn, contacted, represented, accepted, or do not pursue.

### Suppression

Whether the role is suppressed by default, why, and what permits reconsideration.

### Provenance

Source records, run IDs, and evidence notes sufficient to explain the current state.

Do not flatten these into one ambiguous `status` field.

## Candidate-status boundary

Verified Opportunity Search must not infer or automatically write any of the following:

- `applied`;
- `interviewing`;
- `rejected`;
- `withdrawn`;
- `contacted`;
- `representation_accepted`;
- `offer_accepted`;
- `do_not_pursue`;
- an equivalent candidate-action or employer-outcome status.

Resume generation, cover-letter generation, application-form inspection, application-answer preparation, recruiter-message drafting, qualification-question preparation, or opening an application page does not establish one of these statuses.

Candidate status may change only when:

- the user directly confirms it;
- the user explicitly authorizes a status update;
- another source and write policy explicitly approved by the user's Source of Truth provides it.

Observational posting state such as active, closed, unavailable, reopened, or unverified remains separate from candidate status.

## Canonical identity precedence

Use identity evidence in this order:

1. exact ATS provider plus provider job ID;
2. exact employer requisition ID;
3. exact accountable entity plus requisition ID;
4. canonical employer-controlled URL resolving to the same requisition;
5. high-confidence semantic identity;
6. conservative `possible_duplicate_of` relationship.

A URL alone is not sufficient identity. Remove or ignore tracking parameters, fragments, source tags, and redirect-only variation when comparing URLs.

## Semantic identity

High-confidence semantic identity requires several matching load-bearing facts, including when available:

- employer or accountable entity;
- normalized title;
- team or functional area;
- location, remote scope, or timezone;
- employment structure;
- level and central responsibilities;
- materially identical qualification content;
- compensation;
- verified client identity for contract roles;
- duration, hours, and rate for contract roles.

Title and company alone must not trigger automatic merging.

When semantic evidence is incomplete, preserve both records and use `possible_duplicate_of`. Possible duplicates must not be silently suppressed as exact duplicates unless user-specific policy explicitly allows it and evidence is recorded.

## Requisitions and reposts

A new requisition ID is not automatically a duplicate.

Classify it as:

- `distinct` when team, scope, level, location, employment structure, or material description differs;
- `related_repost_of` when the content is materially identical and evidence supports a repost or new hiring cycle;
- `possible_duplicate_of` when current evidence cannot resolve the relationship.

A related repost enters material-change review rather than automatically appearing as a completely new opportunity.

## Contract and staffing identity

For staffing, employer-of-record, recruiter-controlled, and contract opportunities:

- keep staffing firm, employer of record, direct client, and end customer distinct;
- preserve each accountable source or contact path;
- do not infer an undisclosed client;
- consolidate agency paths only when client, requisition, title, location, structure, duration, hours, rate, and materially identical description support the relationship;
- prefer the strongest current accountable path in user-facing results;
- preserve materially different verified commercial terms rather than discarding them.

## Material changes

A previously reported or suppressed role may be reconsidered when current evidence establishes a material change, including:

- reopening after verified closure;
- a new requisition representing a credible new hiring cycle;
- compensation added or materially changed;
- remote, location, timezone, travel, or eligibility changed;
- employment structure changed;
- level, decision scope, or central responsibilities changed;
- required credentials, domain experience, or other hard screens changed;
- a blocking hard screen was removed;
- verified recruiter, referral, hiring-leader, or equivalent access was discovered;
- contract rate, duration, hours, client identity, structure, exclusivity, conversion terms, notice, or exit constraints materially changed.

State the exact change when resurfacing the opportunity.

The following are normally non-material:

- tracking or source parameters;
- formatting, punctuation, or section-order changes;
- minor title variation under the same requisition;
- an aggregator rediscovering the role;
- a refreshed posting date without material content change;
- an application redirect change that still resolves to the same requisition.

Non-material refreshes may update `last_seen_at` or source aliases but must not reset previous-report suppression.

## Material signatures

A registry may store a deterministic material signature built from normalized load-bearing fields. The signature is a comparison aid, not independent evidence.

Do not include volatile tracking parameters, formatting, timestamps, or source-order noise in the signature.

A signature change must still be interpreted. It does not automatically prove that the change is material or beneficial.

## Run ID and run-log contract

Each persisted run must have a stable, unique run ID. Recommended shape:

```text
vos-YYYYMMDD-HHMMSS-zone
```

The run record should include:

- command and mode;
- start and completion timestamps;
- framework version;
- registry revision before and after;
- considered opportunities;
- reported opportunities;
- exclusions;
- previously handled suppressions;
- duplicate consolidations;
- material changes;
- intended registry delta;
- persistence results and errors.

Run records are append-only. Do not overwrite a completed run record. A replay or recovery attempt must use a new run record or an explicitly documented recovery record.

## Idempotency

Replaying the same completed run must not:

- increment report counts twice;
- append the same run ID twice;
- create duplicate opportunity records;
- overwrite newer candidate status;
- discard aliases or provenance;
- reset suppression without material evidence.

Use the run ID and current registry revision to detect duplicate or stale writes.

## Write order

Use this order when direct writes are available:

1. read and validate the current registry;
2. capture its current revision or content SHA;
3. assign the run ID;
4. complete search, identity reconciliation, and registry delta in memory;
5. create the append-only run record containing the intended delta;
6. update the registry against the current revision;
7. re-read both records;
8. verify the persisted content;
9. report persistence status.

Do not blindly overwrite a registry whose revision changed after it was read. Re-read and reconcile first.

## Failure and recovery behavior

### Run record succeeds, registry update fails

- report `Persistence degraded`;
- do not claim cross-run suppression was updated;
- preserve the run record and intended delta as recovery evidence;
- recommend or perform an explicitly authorized replay against the latest registry revision.

### Neither write succeeds

- return otherwise valid search results;
- disclose that results were not durably recorded;
- provide a copy-ready registry delta when practical;
- do not claim that future searches will suppress the roles.

### Registry is malformed or schema-incompatible

- stop registry mutation;
- do not replace the file with a blank or newly generated registry;
- report the parsing or schema problem;
- preserve the search result separately;
- require reconciliation or migration before the next write.

### Concurrent update conflict

- re-read the latest registry;
- reconcile non-conflicting observational additions;
- preserve newer candidate status and user-owned fields;
- stop for human review when the same field has conflicting material values.

## Persistence reporting

Every search using configured persistence must report one status:

- `Persisted` — run record and registry were written and re-read successfully;
- `Persistence degraded` — run record exists but registry update or verification failed;
- `Not persisted` — no durable write was completed;
- `Persistence not configured` — no registry or write policy is configured.

Do not hide persistence failure inside general search caveats.

## Schema evolution

Both registry and run records must contain `schema_version`.

- Additive fields should remain backward compatible.
- Breaking changes require a documented migration.
- Unknown user-owned fields must be preserved.
- Source Rebase must not overwrite, normalize, move, or delete populated registries or run logs.
- A framework version change does not itself require rewriting historical run files.

## Privacy and content limits

Store opportunity facts, search provenance, and candidate status only at the depth required for job-search workflow control.

Do not store secrets, credentials, voluntary demographic answers, sensitive application answers, legal attestations, or unnecessary personal data in opportunity registry files.

## Required validation

Before treating the registry feature as active, test at least:

- tracking-parameter URL variants;
- two official URLs for one requisition;
- same company and title with different requisition IDs;
- same title on different teams;
- a related repost;
- unchanged previously reported suppression;
- unchanged applied suppression;
- material compensation or eligibility changes;
- reopening after closure;
- removal of a hard screen;
- agency duplicate consolidation;
- unresolved possible duplicates;
- candidate status remaining unknown after artifact preparation;
- partial persistence failure;
- same-run replay idempotency;
- malformed registry handling;
- concurrent revision conflict.

## Action boundary

Configured observational registry and run-log persistence is part of the authorized Verified Opportunity Search execution.

The workflow must still not, without separate explicit user instruction:

- change candidate-confirmed status;
- submit applications;
- contact external parties;
- accept representation, compensation, commercial, legal, exclusivity, confidentiality, intellectual-property, conversion, or employment terms;
- generate downstream resumes or cover letters unless separately requested;
- merge repository pull requests or perform destructive migration.

Follow `rules/04-truthguard.md` and `rules/12-verified-opportunity-search.md` everywhere their controls apply.
