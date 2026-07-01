# COMPASS Opportunity Registry Templates

These templates define the reusable persistence contract for `COMPASS Verified Opportunity Search`.

The registry is a current materialized view of opportunities that reached a durable search state. Search-run files are append-only provenance records describing what a specific run considered, reported, excluded, suppressed, consolidated, or recognized as materially changed.

## Files

- `COMPASS_Opportunity_Registry_TEMPLATE.yaml` — canonical current-state registry template.
- `COMPASS_Opportunity_Search_Run_TEMPLATE.yaml` — append-only per-run record template.

## Repository boundary

The COMPASS framework owns the generic schema and behavior. A user's Source of Truth owns the actual registry, run logs, candidate-confirmed statuses, suppression configuration, and repository write policy.

A configured Source of Truth may authorize a Verified Opportunity Search run to persist observational facts without a second instruction. This does not authorize inferred candidate-status changes.

## Observational persistence

A search may persist an opportunity when at least one condition is met:

- it is reported to the user;
- it reaches official employer-controlled or accountable-source verification;
- it is excluded for a durable reason such as closure, hard-screen mismatch, or duplicate identity;
- it is recognized as previously handled.

Do not persist raw snippets or low-confidence discovery noise merely because it appeared in search results.

Permitted observational fields include identity, source URLs, posting state, dates seen or verified, duplicate relationships, reporting history, material changes, run provenance, and persistence results.

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
