# COMPASS Opportunity Registry Templates

These templates define the reusable persistence contract for `COMPASS Verified Opportunity Search`.

The registry is a current materialized view of opportunities that reached a durable search state. Search-run files are append-only provenance records describing what a specific run considered, reported, excluded, suppressed, consolidated, recognized as materially changed, and how broadly the search was executed.

## Files

- `COMPASS_Opportunity_Registry_TEMPLATE.yaml` — canonical current-state registry template.
- `COMPASS_Opportunity_Search_Run_TEMPLATE.yaml` — append-only per-run record template.

## Repository boundary

The COMPASS framework owns the generic schema and behavior. A user's Source of Truth owns the actual registry, run logs, candidate-confirmed statuses, suppression configuration, search-breadth targets, and repository write policy.

A configured Source of Truth may authorize a Verified Opportunity Search run to persist observational facts without a second instruction. This does not authorize inferred candidate-status changes.

## Search breadth and telemetry

`rules/18-opportunity-search-breadth-telemetry.md` defines the reusable stage and reconciliation contract.

The run template separates:

- `source_hits_observed` — optional raw result count when the discovery tool exposes a reliable total;
- `unique_opportunities_discovered` — normalized opportunity candidates after exact duplicate and syndication collapse;
- `quick_screened` — unique roles checked for visible title, level, location, work mode, structure, compensation, and obvious hard screens;
- `materially_inspected` — roles inspected deeply enough to receive a defensible terminal disposition;
- `live_verified` — materially inspected roles whose active posting and actionable application or qualification path were verified;
- `reported` — opportunity records actually shown to the user under the active output contract.

A user's Source of Truth may set numeric targets and required source or title-family coverage. `--max N` limits reported results; it does not ordinarily limit discovery, quick screening, material inspection, or duplicate and prior-display reconciliation.

Every materially inspected opportunity must have one canonical run record and exactly one terminal disposition. Counts must be derived from those records rather than estimated from the narrative after drafting.

The telemetry block records:

- configured targets;
- actual stage counts;
- source and title-family coverage;
- expansion-pass summaries;
- breadth status;
- stop reason and limitations;
- reconciliation checks.

Use these breadth statuses:

- `complete` — configured targets and coverage were satisfied, or an allowed early-success condition was satisfied;
- `incomplete` — one or more configured targets or coverage requirements were not satisfied;
- `not_configured` — no user-specific floors exist, though stage telemetry and stop reason remain required;
- `unverified` — required telemetry could not be reconstructed or validated.

A complete configured search contract is not a claim that every possible market opportunity was found.

## Observational persistence

A search may persist an opportunity when at least one condition is met:

- it is reported to the user;
- it reaches official employer-controlled or accountable-source verification;
- it is excluded for a durable reason such as closure, hard-screen mismatch, or duplicate identity;
- it is recognized as previously handled.

Do not persist raw snippets or low-confidence discovery noise merely because it appeared in search results.

Aggregate breadth telemetry, expansion-pass summaries, source/title coverage, stop reason, and reconciliation results may be persisted even though transient weak discovery leads are not.

Permitted observational fields include identity, source URLs, posting state, dates seen or verified, duplicate relationships, reporting history, material changes, run provenance, search telemetry, and persistence results.

## Candidate-status boundary

Do not infer or automatically write candidate statuses such as `applied`, `interviewing`, `rejected`, `withdrawn`, `contacted`, `represented`, `accepted`, or `do_not_pursue` from resume generation, form inspection, answer preparation, recruiter-response drafting, or search activity.

Candidate status requires direct user confirmation, an explicitly authorized status update, or another source explicitly approved by the user's Source of Truth.

## Identity and duplicate handling

Identity priority is:

1. exact ATS provider and provider job ID;
2. exact employer requisition ID;
3. exact accountable entity and requisition ID;
4. canonical employer-controlled URL resolving to the same requisition;
5. high-confidence semantic identity;
6. conservative `possible_duplicate_of` relationship.

A new requisition ID is not automatically a duplicate. Use `related_repost_of` when a materially identical role appears under a new requisition but evidence supports a repost rather than an unrelated opening.

Tracking parameters, fragments, redirect variants, and alternate ATS paths do not create separate opportunities.

## Reconciliation expectations

Before persistence, validate at least:

- `materially_inspected` equals the number of canonical considered records;
- every canonical considered record has exactly one terminal disposition;
- terminal-disposition totals equal `materially_inspected`;
- `live_verified` does not exceed `materially_inspected`;
- reported recommendations have corresponding material-inspection and live-verification records;
- duplicate and prior-display totals match canonical records;
- `--max N` constrains reporting rather than discovery-stage counts.

Record reconciliation as `PASS`, `FAIL`, or `UNKNOWN` with concise diagnostics.

## Write and recovery order

1. Read and validate the current registry.
2. Assign a stable run ID.
3. Compute the registry delta in memory.
4. Create the append-only run record.
5. Update the registry using the current file revision.
6. Re-read both files and verify persistence.
7. Report persistence status to the user.

If the run record succeeds but the registry update fails, report `Persistence degraded` and preserve the run record as recovery evidence. If neither write succeeds, return the verified search results with an explicit disclosure and a copy-ready registry delta; do not claim future suppression is active.

## Schema evolution

- Preserve `schema_version` in both files.
- Additive fields should remain backward compatible.
- Breaking changes require a documented migration.
- Do not silently delete unknown user-owned fields.
- Source Rebase must not overwrite or normalize populated opportunity registries or run logs.
- Historical completed run records remain append-only and are not rewritten merely to add telemetry fields.
- Missing historical telemetry means unavailable, not zero.
