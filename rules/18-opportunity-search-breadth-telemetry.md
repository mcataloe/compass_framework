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
- required source, named-roster, rotation-window, query-bundle, and title-family coverage;
- controlled source-attempt statuses and approved substitution methods;
- a minimum actionable-result objective and the exact result class that satisfies it;
- staged discovery and material-inspection escalation targets;
- hard search ceilings for unique discoveries, material inspections, expansion passes, or another bounded effort measure;
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

The search may stop before configured numeric breadth targets when the requested number of fully qualified opportunities has already been found and the active user-specific policy permits early success. Early success may bypass only the numeric breadth gate. It must not bypass applicable source coverage, query-bundle or title-family coverage, or telemetry reconciliation. The run must record that stop reason.

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
- viability-threshold result when configured;
- actionable-result class and count eligibility when configured;
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

## Minimum Actionable-Result Objectives

A user's Source of Truth may configure a minimum actionable-result objective separately from a reporting cap. The policy must define:

- the result class that counts, such as fully qualified, application-safe, `Apply now`, or another controlled user-specific class;
- the minimum count;
- the baseline breadth checkpoint;
- the staged expansion plan;
- the hard search ceiling;
- the viability threshold used for no-yield evaluation.

The minimum is an outcome objective, not a quota that can be satisfied by weakening eligibility, evidence, live-verification, work-mode, compensation, legitimacy, duplicate, prior-display, or utility gates.

When the baseline breadth checkpoint is reached but the configured minimum has not been satisfied, `breadth_targets_satisfied` is a checkpoint rather than a stop condition. Continue through the configured expansion stages until the minimum is satisfied or another bounded stop condition applies.

The workflow must be allowed to return fewer than the minimum after bounded exhaustion. It must never search indefinitely or promote a borderline opportunity merely to satisfy the count.

## Source Attempts and Coverage Gates

When a Source of Truth configures named sources, mandatory surfaces, tiers, or rotation windows, completion means mandatory attempt with an approved substitution path when blocked. It does not mean that every site must be scraped successfully or yield an opportunity.

Maintain one source-attempt record for every applicable required source and every selected rotating source. At minimum, each record must include:

- `source_id`;
- `lane`;
- `status`;
- `access_method`;
- `query_bundles`;
- `unique_opportunities_added`;
- `materially_inspected_added`;
- `substitute_source_id`;
- `limitation`.

Use only these source-attempt statuses:

- `completed` — the configured source or surface was attempted through its normal accountable path, including valid zero-yield attempts;
- `completed_via_substitution` — the normal path was blocked and an approved substitution was completed and recorded;
- `blocked_unsubstituted` — the normal path was blocked and no approved substitution was completed;
- `skipped` — the applicable source was not attempted;
- `not_applicable` — the active policy explicitly permits non-applicability for that source in this run.

A blocked source does not satisfy coverage merely because the limitation is disclosed. It satisfies coverage only through `completed_via_substitution` under the active policy. `blocked_unsubstituted` and `skipped` fail the applicable source requirement. `not_applicable` satisfies a requirement only when the user-specific policy defines the exact non-applicability condition.

Evaluate four gates independently:

1. `numeric_breadth` — configured unique-discovery and material-inspection targets;
2. `source_coverage` — mandatory surfaces, named sources, tier minimums, substitutions, and rolling rotation windows;
3. `title_family_coverage` — configured title families or query bundles;
4. `telemetry_reconciliation` — source attempts, stages, dispositions, and reported results reconcile.

Gate statuses are `PASS`, `FAIL`, `NOT_CONFIGURED`, or `UNKNOWN`. Overall `breadth_status: complete` requires every applicable gate to be `PASS`, except that an explicitly allowed early-success stop may satisfy the numeric breadth gate below its numeric floor. `FAIL` or `UNKNOWN` on source coverage, title-family coverage, or telemetry reconciliation prevents verified completion.

A policy may require bundled queries. Cover the configured bundles across the run; do not infer a source-by-title Cartesian product unless the policy explicitly requires one.

Derive rolling rotation state from append-only completed search-run history. Do not use the current opportunity registry as rotation authority, because opportunity state and source-attempt history are different concerns. Missing historical attempt telemetry remains unavailable and must not be backfilled from memory.

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
- actionable results added under the configured minimum-result class;
- whether the pass was a no-yield pass.

A no-yield pass adds no new opportunity that reaches the configured viability threshold. When no stricter threshold is configured, material inspection remains the default. A policy may instead define viability as passing hard eligibility, work-mode, and known economic floors while remaining eligible for application or qualification review.

## Stop Conditions

A run may stop when one of the following is true:

1. `requested_result_count_satisfied` — the configured minimum actionable-result count or requested fully qualified result count has been found and user-specific policy permits success.
2. `breadth_targets_satisfied` — configured discovery and inspection targets plus required source/title coverage have been satisfied, and no unmet minimum actionable-result objective requires continued expansion.
3. `configured_search_ceiling_reached` — the run reached its configured bounded ceiling before satisfying the minimum actionable-result objective.
4. `consecutive_no_yield_passes` — the configured number of expansion passes produced no new opportunity at the configured viability threshold.
5. `source_exhaustion` — the practical approved search space was exhausted before targets or the actionable-result objective were reached.
6. `source_access_blocked` — material search surfaces were inaccessible or unavailable.
7. `safety_or_policy_block` — continuing would violate tool, privacy, legal, security, or user-specific policy.
8. `user_requested_stop` — the user explicitly stopped or narrowed the run.

Record exactly one primary stop reason and any secondary limitations.

Do not use `--max N` itself as a stop reason unless the requested qualified result count was actually satisfied. Do not use `breadth_targets_satisfied` when a configured minimum actionable-result objective remains unmet and expansion capacity remains.

## Breadth Status

Use one of:

- `complete` — configured numeric breadth, applicable source coverage, applicable title-family or query-bundle coverage, and telemetry reconciliation were satisfied; an allowed early-success condition may satisfy only the numeric breadth gate below its floor.
- `incomplete` — one or more configured targets or coverage requirements were not satisfied.
- `not_configured` — no user-specific breadth targets exist; stage telemetry and stop reason are still required.
- `unverified` — required telemetry could not be reconstructed or validated.

Do not claim comprehensive market coverage merely because `breadth_status` is `complete`. It means the configured search contract was completed, not that every possible role on the market was found.

When a minimum actionable-result objective is configured, also record `result_objective_status` as one of:

- `satisfied` — the configured minimum was reached;
- `unmet_after_bounded_exhaustion` — the run stopped at a configured ceiling, source exhaustion, no-yield threshold, access block, or safety/policy boundary with fewer results;
- `not_configured` — no minimum actionable-result objective applies.

Breadth completion and result-objective satisfaction are separate. A run may have `breadth_status: complete` and `result_objective_status: unmet_after_bounded_exhaustion` when it fully executes the bounded search contract but the market does not supply enough qualified opportunities.

## Required Run Telemetry

A search-run record should include:

- configured result limits;
- breadth targets;
- minimum actionable-result objective, result class, and actual count;
- staged expansion checkpoints and hard search ceilings when configured;
- stage counts;
- source-family, named-source, rotation-window, query-bundle, and title-family coverage;
- per-source attempt records with controlled status, access method, yield, substitution, and limitation fields;
- independent completion-gate statuses;
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
    minimum_actionable_results: null
    actionable_result_class: null
    search_ceiling:
      unique_opportunities_discovered: null
      materially_inspected: null
      expansion_passes: null
  actual:
    source_hits_observed: null
    unique_opportunities_discovered: 0
    quick_screened: 0
    materially_inspected: 0
    live_verified: 0
    reported: 0
    actionable_results: 0
  coverage:
    source_families: []
    title_families: []
    query_bundles: []
    source_attempts: []
    rotation_windows: []
  gates:
    numeric_breadth: NOT_CONFIGURED
    source_coverage: NOT_CONFIGURED
    title_family_coverage: NOT_CONFIGURED
    telemetry_reconciliation: UNKNOWN
  breadth_status: not_configured
  result_objective_status: not_configured
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
11. Every applicable required or selected rotating source has exactly one source-attempt record.
12. Every source-attempt status is in the controlled status set.
13. A blocked source counted as satisfied has an approved substitution and status `completed_via_substitution`.
14. Per-source unique and material-inspection additions are nonnegative and do not exceed the reconciled run totals; they are attribution fields, not an alternative source of stage totals.
15. Rotation-window evaluation derives from append-only completed run history and records unavailable history as `UNKNOWN` rather than assuming coverage.
16. Overall breadth is `complete` only when all applicable gates satisfy the completion rule, including the early-success exception limited to numeric breadth.
17. Every counted actionable result satisfies the configured actionable-result class and has the material inspection and live verification required by Rule 12.
18. `breadth_targets_satisfied` is not used while a configured minimum actionable-result objective remains unmet and unused expansion capacity remains.
19. A run stopped at `configured_search_ceiling_reached` records the configured ceiling, actual effort, actionable-result shortfall, and final viability yield without weakening gates.

Record reconciliation as `PASS`, `FAIL`, or `UNKNOWN` with concise diagnostics. `FAIL` or `UNKNOWN` blocks a claim that telemetry or breadth was successfully verified. It does not erase otherwise valid opportunity findings, but the limitation must be disclosed.

## Persistence Boundary

Rule 13's persistence threshold still applies.

Do not persist every raw hit or weak discovery lead merely to support telemetry. Persist:

- aggregate stage counts;
- breadth targets and status;
- source/title coverage summaries;
- privacy-safe source-attempt records, substitution outcomes, gate statuses, and rotation-window summaries;
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
- label historical breadth as `unverified` when the old record cannot support the new contract;
- do not backfill source attempts, substitutions, or rotation coverage from the opportunity registry or memory.

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
- `--max N` limiting reporting without limiting discovery;
- a required named-source run in which all sources complete, including valid zero-yield attempts;
- an access-blocked source completed through an approved substitution;
- an access-blocked source without a substitution, which leaves source coverage incomplete;
- early success that satisfies numeric breadth but cannot bypass source or title-family coverage;
- rolling rotation derived from append-only completed run history;
- invalid or drifted source-attempt and breadth-status values;
- bundled query coverage without an accidental source-by-title Cartesian requirement.
- a minimum actionable-result objective that continues beyond the baseline breadth checkpoint;
- an objective satisfied during a later expansion stage;
- a configured search ceiling reached with fewer actionable results than requested;
- evidence-detail uncertainty that is routed to confirmation rather than converted into negative evidence.

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
