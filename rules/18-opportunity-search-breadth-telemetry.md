# 18 — Opportunity Search Breadth and Telemetry

This rule supplements `rules/12-verified-opportunity-search.md` and `rules/13-opportunity-registry.md`.

Rule 12 continues to govern discovery, live verification, eligibility, alignment, opportunity quality, conversion conditions, recruiter-legitimacy handling, and optional contract utility. Rule 13 continues to govern durable opportunity identity, reporting history, run provenance, registry persistence, and candidate-status boundaries. This rule owns measurable search breadth, stage definitions, stopping behavior, telemetry reconciliation, and breadth-status reporting.

## Purpose

A result limit must not silently become a discovery limit.

Verified Opportunity Search must distinguish:

- how broadly the market was searched;
- how many unique opportunities were discovered after normalization;
- how many received a quick screen;
- how many were materially inspected;
- how many reached live verification;
- how many were reported.

The workflow must also explain why it stopped when fewer than the requested number of qualified opportunities are returned.

## Applicability

Apply this rule whenever COMPASS discovers, refreshes, ranks, or shortlists multiple opportunities under `COMPASS Verified Opportunity Search`.

A user's Source of Truth may configure:

- minimum unique-opportunity discovery targets;
- minimum material-inspection targets;
- required source and title-family coverage;
- expansion-pass limits;
- no-yield stopping thresholds;
- additional telemetry fields;
- stricter reconciliation requirements.

User-specific configuration may tighten breadth expectations. It must not lower eligibility, live-verification, alignment, TruthGuard, duplicate, prior-display, or persistence-honesty gates.

## Result Limits Are Not Search Limits

`--max N`, a default result limit, or another primary-result cap controls the maximum number of opportunities displayed in the applicable result lane.

It does not ordinarily cap:

- discovery queries;
- search sources;
- title families;
- unique opportunities discovered;
- quick screens;
- material inspections;
- duplicate or prior-display reconciliation;
- live-verification attempts.

The search may stop before configured breadth targets when the requested number of fully qualified opportunities has already been found and the active user-specific policy permits early success. The run must record that stop reason.

## Canonical Search Stages

Each run uses the following stage definitions.

### `source_hits_observed`

Raw result entries observed across search engines, ATS indexes, employer pages, directories, recruiter sources, or other discovery surfaces before opportunity normalization.

This count is optional because some tools do not expose complete or stable result totals. When unavailable, record `null` or `not_observable`; do not estimate it.

### `unique_opportunities_discovered`

Distinct opportunity candidates after removing obvious tracking variants, repeated syndications, exact ATS duplicates, and exact requisition duplicates.

This is the preferred breadth-floor metric. A repeated copy of one requisition must not increase this count.

At this stage, a record may still fail a later gate and need not be persisted as a durable opportunity.

### `quick_screened`

Unique opportunities reviewed sufficiently to assess readily visible title, level, work mode, geography, employment structure, compensation when exposed, and obvious hard-screen mismatches.

A quick screen does not require opening or fully reading the official posting when the role can be safely rejected from already authoritative identity or policy evidence, such as an exact previously reported requisition or an explicit fixed hybrid location in a current employer-controlled source.

### `materially_inspected`

Opportunities for which the current run inspected enough accountable content to assign a defensible terminal disposition.

Material inspection normally requires opening the official employer-controlled posting or accountable current source and reviewing the role's material responsibilities, qualifications, work-mode constraints, and current-state evidence. An exact previously reported role counts as materially inspected only when the current posting is opened for material-change review or another substantive current-state determination.

Every materially inspected opportunity must appear exactly once in the run's canonical material-inspection records with one terminal disposition.

### `live_verified`

Materially inspected opportunities whose active posting or accountable opportunity state and actionable application or qualification path were verified under Rule 12.

A role may be materially inspected but not live verified, for example when the employer page is inaccessible or the application path cannot be confirmed.

### `reported`

Opportunities displayed to the user as recommended, conditional, watchlist, excluded/deferred, previously displayed, duplicate/repost, unverified, or otherwise required by the active output contract.

Reporting is not equivalent to recommendation. A run may report notable exclusions while recommending zero roles.

## Canonical Material-Inspection Record

Maintain one canonical working record for each materially inspected opportunity. At minimum, each record should include:

- stable run-local opportunity key;
- employer or accountable entity;
- title;
- ATS provider and requisition identifier when known;
- canonical URL when known;
- whether the opportunity was previously displayed;
- whether it is a duplicate or related repost;
- live-verification result;
- terminal disposition;
- concise disposition reason.

Allowed terminal dispositions are supplied by Rule 12 and user-specific policy. A disposition must be mutually exclusive within a run.

Do not derive telemetry by manually counting prose after the report has been drafted. Generate both counts and narrative result sections from the canonical working records.

## Breadth Targets

When the user's Source of Truth configures breadth targets, record both target and actual values.

A target is an effort and coverage contract, not permission to weaken quality gates. Reaching a numeric floor does not make the search successful if source or title-family coverage is materially narrow.

A run may finish below a target only under an allowed stop condition. It must then record `breadth_status: incomplete` and the exact reason.

Do not inflate breadth by:

- counting duplicate syndications as unique opportunities;
- counting tracking-parameter variants separately;
- counting the same requisition once per search source;
- counting broad employer career pages as opportunities;
- counting generic talent networks or role-family pages as concrete opportunities;
- counting unidentifiable snippets that cannot be reconciled to a role.

## Expansion Passes

An expansion pass deliberately broadens at least one dimension after the initial search pass, such as:

- adjacent approved title families;
- additional accountable ATS platforms;
- additional employer career sites;
- specialist or venture-portfolio sources;
- remote-first directories;
- approved industry or domain adjacencies;
- alternative technology terminology that remains directionally aligned.

Each pass must record:

- pass number;
- sources or title families added;
- unique opportunities added;
- materially inspected opportunities added;
- viable opportunities added;
- whether the pass was a no-yield pass.

A no-yield pass adds no new opportunity that reaches material inspection or another stricter user-configured viability threshold.

## Stop Conditions

A run may stop when one of the following is true:

1. `requested_result_count_satisfied` — the requested number of fully qualified reportable opportunities has been found and user-specific policy permits early success.
2. `breadth_targets_satisfied` — configured discovery and inspection targets plus required source/title coverage have been satisfied.
3. `consecutive_no_yield_passes` — the configured number of expansion passes produced no new material inspection or other configured viable candidate.
4. `source_exhaustion` — the practical approved search space was exhausted before targets were reached.
5. `source_access_blocked` — material search surfaces were inaccessible or unavailable.
6. `safety_or_policy_block` — continuing would violate tool, privacy, legal, security, or user-specific policy.
7. `user_requested_stop` — the user explicitly stopped or narrowed the run.

Record exactly one primary stop reason and any secondary limitations.

Do not use `--max N` itself as a stop reason unless the requested qualified result count was actually satisfied.

## Breadth Status

Use one of:

- `complete` — configured breadth targets and coverage requirements were satisfied, or an allowed early-success condition was satisfied.
- `incomplete` — one or more configured targets or coverage requirements were not satisfied.
- `not_configured` — no user-specific breadth targets exist; stage telemetry and stop reason are still required.
- `unverified` — required telemetry could not be reconstructed or validated.

Do not claim comprehensive market coverage merely because `breadth_status` is `complete`. It means the configured search contract was completed, not that every possible role on the market was found.

## Required Run Telemetry

A search-run record should include:

- configured result limits;
- breadth targets;
- stage counts;
- source and title-family coverage;
- expansion-pass records;
- primary stop reason;
- secondary limitations;
- breadth status;
- canonical material-inspection records or a privacy-safe durable subset;
- reconciliation checks.

Recommended stage-count fields are:

```yaml
telemetry:
  targets:
    unique_opportunities_discovered: null
    materially_inspected: null
    consecutive_no_yield_passes: null
  actual:
    source_hits_observed: null
    unique_opportunities_discovered: 0
    quick_screened: 0
    materially_inspected: 0
    live_verified: 0
    reported: 0
  breadth_status: not_configured
  stop_reason: null
  limitations: []
```

A Source of Truth may add fields but should preserve these meanings.

## Reconciliation Invariants

Before final reporting and persistence, validate at least:

1. `materially_inspected` equals the number of canonical material-inspection records.
2. Every canonical material-inspection record has exactly one terminal disposition.
3. The sum of terminal-disposition counts equals `materially_inspected`.
4. `live_verified` is less than or equal to `materially_inspected`.
5. `reported` is derived from the actual user-facing opportunity records and does not exceed the number of records eligible for reporting under the active output contract.
6. `unique_opportunities_discovered` is greater than or equal to `quick_screened` when every quick screen derives from the current run's discovery set; record an explicit carry-forward exception otherwise.
7. `quick_screened` is greater than or equal to `materially_inspected` unless the run documents a current-source direct-to-material-inspection path.
8. Duplicate and prior-display counts match the applicable canonical records rather than prose estimates.
9. Every reported recommendation has a corresponding materially inspected record and live-verification result required by Rule 12.
10. `--max N` limits reported primary recommendations, not discovery-stage counts.

Record reconciliation as `PASS`, `FAIL`, or `UNKNOWN` with concise diagnostics. `FAIL` or `UNKNOWN` blocks a claim that telemetry or breadth was successfully verified. It does not erase otherwise valid opportunity findings, but the limitation must be disclosed.

## Persistence Boundary

Rule 13's persistence threshold still applies.

Do not persist every raw hit or weak discovery lead merely to support telemetry. Persist:

- aggregate stage counts;
- breadth targets and status;
- source/title coverage summaries;
- expansion-pass summaries;
- stop reason and limitations;
- canonical records that independently meet Rule 13's durable persistence threshold.

Transient low-confidence discovery details may be discarded after aggregate counts and reconciliation are complete.

## Backward Compatibility

Historical run records are append-only and must not be rewritten solely to add new telemetry fields.

When reconciling older runs:

- treat missing telemetry as unavailable, not zero;
- do not reconstruct exact discovery or inspection counts from memory;
- preserve existing reported-opportunity and prior-display evidence;
- label historical breadth as `unverified` when the old record cannot support the new contract.

The new fields are additive for schema-version compatibility unless a future executable schema explicitly requires a version migration.

## Required Pressure Tests

Before activating an implementation, test at least:

- a normal broad run that reaches configured targets;
- early success with the requested qualified result count reached before the floor;
- heavy prior-display suppression;
- duplicate syndication collapsing many raw hits into fewer unique opportunities;
- market or source exhaustion below the floor;
- consecutive no-yield expansion passes;
- stale registry with successful run-history reconciliation;
- materially inspected roles whose application paths remain unverified;
- arithmetic reconciliation across all stage and terminal-disposition counts;
- `--max N` limiting reporting without limiting discovery.

## Action Boundary

This rule changes search breadth, telemetry, and reporting semantics only.

It does not authorize:

- weaker opportunity gates;
- application submission;
- recruiter contact;
- candidate-status changes;
- historical run rewriting;
- registry reconstruction;
- persistence of raw search noise;
- generation of downstream artifacts unless separately authorized.
