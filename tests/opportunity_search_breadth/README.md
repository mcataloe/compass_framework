# Verified Opportunity Search Breadth and Telemetry Pressure Tests

These candidate-neutral cases pressure-test `rules/18-opportunity-search-breadth-telemetry.md` and the opportunity-search run template.

They are specification-level regression cases. An executable implementation may encode the same cases in another test framework while preserving the inputs, expected classifications, and invariants.

## Shared invariants

Every case must validate:

1. `materially_inspected` equals the canonical material-inspection record count.
2. Every material-inspection record has exactly one terminal disposition.
3. Terminal-disposition totals equal `materially_inspected`.
4. `live_verified <= materially_inspected`.
5. Every reported recommendation has a material-inspection record and the required live-verification result.
6. Duplicate and prior-display counts derive from canonical records.
7. `--max N` limits reporting rather than ordinary discovery-stage counts.
8. Raw weak discovery leads are not persisted as durable opportunity records.
9. Every applicable required or selected rotating source has exactly one source-attempt record using a controlled status.
10. A blocked source satisfies coverage only through an approved recorded substitution.
11. Numeric breadth, source coverage, title-family coverage, and telemetry reconciliation are evaluated independently.
12. Rotation state derives from append-only completed run history, not the current opportunity registry.
13. A configured minimum actionable-result objective is separate from the reporting cap.
14. Baseline breadth is a checkpoint rather than a stop while the minimum remains unmet and expansion capacity remains.
15. Search ceilings and no-yield rules bound effort without weakening result gates.

## Case 1 — Normal broad run

Configuration:

```yaml
targets:
  unique_opportunities_discovered: 40
  materially_inspected: 15
  consecutive_no_yield_passes: 2
max_primary_results: 5
```

Actual:

```yaml
source_hits_observed: 83
unique_opportunities_discovered: 46
quick_screened: 23
materially_inspected: 15
live_verified: 9
reported: 6
```

Expected:

- `breadth_status: complete`
- `stop_reason: breadth_targets_satisfied`
- one role may be `Apply now`; notable exclusions may also be reported
- reconciliation `PASS`

## Case 2 — Early success

Actual:

```yaml
unique_opportunities_discovered: 31
quick_screened: 18
materially_inspected: 12
live_verified: 7
primary_qualified_results: 5
```

Expected:

- `breadth_status: complete`
- `stop_reason: requested_result_count_satisfied`
- five primary recommendations maximum
- the below-floor discovery and inspection counts are not treated as failure because the allowed early-success condition satisfied the numeric gate
- applicable source coverage, title-family coverage, and telemetry reconciliation still pass

## Case 3 — Heavy prior-display suppression

Discovery includes 54 unique opportunities. Twenty-eight are exact previously reported requisitions and are suppressed during quick screening without reopening. Six are reopened for material-change review.

Expected:

- all 54 count as unique discoveries
- exact suppressions checked only against durable identity do not count as materially inspected
- the six reopened for substantive material-change review do count as materially inspected
- prior-display counts reconcile to canonical records

## Case 4 — Duplicate syndication collapse

Actual source results contain 70 hits representing 38 unique requisitions after tracking-parameter, ATS-copy, and syndication collapse.

Expected:

```yaml
source_hits_observed: 70
unique_opportunities_discovered: 38
```

- breadth target of 40 is not satisfied merely because raw hits exceed 40
- duplicate copies do not create durable opportunity records

## Case 5 — Source exhaustion below floor

Only 27 unique aligned-title opportunities can be found after all approved source and title-family expansion.

Expected:

- valid opportunity findings are retained
- `breadth_status: incomplete`
- `stop_reason: source_exhaustion`
- target and actual values are reported
- no claim of comprehensive coverage

## Case 6 — Consecutive no-yield passes

Initial pass produces 33 unique discoveries and 12 material inspections. Expansion pass 1 and expansion pass 2 each add unique roles but add zero new material inspections.

Expected:

- both passes are recorded as no-yield
- `breadth_status: incomplete`
- `stop_reason: consecutive_no_yield_passes`
- unique-discovery additions do not erase the no-yield classification when the configured threshold is material inspection

## Case 7 — Stale registry with run-history reconciliation

The canonical registry is stale, but completed run records permit conservative prior-display reconciliation.

Expected:

- search and telemetry may complete
- prior-display status follows conservative suppression
- run record persists intended registry delta
- persistence may be `Persistence degraded`
- breadth reconciliation remains separate from registry-write success

## Case 8 — Material inspection without live verification

Fifteen roles are materially inspected. Four official pages or application endpoints are inaccessible.

Expected:

```yaml
materially_inspected: 15
live_verified: 11
```

- inaccessible roles receive an unverified terminal disposition
- they do not enter `Apply now`
- reconciliation may still `PASS`

## Case 9 — Arithmetic mismatch

The draft telemetry says `materially_inspected: 10`, but eleven canonical material records exist.

Expected:

- reconciliation `FAIL`
- breadth status cannot be represented as verified
- the implementation must recalculate from canonical records or correct the record before final release

## Case 10 — Result cap does not constrain discovery

Configuration uses `--max 5`. The first pass finds one qualified result. The search continues to configured breadth or another valid stop condition.

Expected:

- discovery and material inspection are not stopped at five candidate records
- no more than five primary recommendations are displayed
- `--max 5` is not used as the stop reason unless five qualified results were actually found

## Case 11 — Carry-forward quick screen

A currently active role is supplied directly by a verified user-controlled opportunity record rather than discovered during the current external search pass.

Expected:

- the role may be quick-screened or materially inspected
- `unique_opportunities_discovered` need not include it when it was not discovered in the current run
- the run records a carry-forward exception so stage-order invariants remain interpretable

## Case 12 — Historical telemetry

An older append-only run contains reported and excluded roles but no breadth fields.

Expected:

- no historical rewrite
- missing telemetry is `unavailable` or breadth `unverified`, not zero
- prior reporting history remains usable for suppression

## Case 13 — Named sources complete with zero yield

A configured contract lane requires eight core sources. All eight have one `completed` attempt record; five add zero unique opportunities.

Expected:

- all eight attempts satisfy the named-source requirement
- zero yield does not convert a completed attempt into a failure
- source coverage may be `PASS` when all other applicable requirements pass

## Case 14 — Approved substitution for an access block

One required source is inaccessible through its normal job page. The run completes a configured official-domain search and records `completed_via_substitution`, the substitute identifier, access method, and limitation.

Expected:

- the source requirement is satisfied
- the limitation remains visible
- no claim is made that the normal source was scraped

## Case 15 — Blocked without substitution

One applicable required source records `blocked_unsubstituted`.

Expected:

- `source_coverage: FAIL`
- overall `breadth_status: incomplete` even when numeric floors are reached
- the valid opportunity findings remain reportable with the limitation

## Case 16 — Early success cannot bypass coverage

The requested five qualified results are found before numeric floors. Two required sources were skipped and one required query bundle was not used.

Expected:

- early success may satisfy only `numeric_breadth`
- source coverage and title-family coverage fail
- overall breadth is incomplete rather than complete

## Case 17 — Rolling rotation from run history

The current opportunity registry contains observations from every rotating firm, but the prior two completed contract-run records show attempts for only part of the configured rotation.

Expected:

- rotation state uses the append-only completed run records
- registry observations do not satisfy the rotation window
- missing historical attempt telemetry is `UNKNOWN`, not backfilled

## Case 18 — Controlled status and gate drift

A draft run uses `telemetry_degraded` as a breadth status and `blocked` as a source-attempt status.

Expected:

- reconciliation `FAIL`
- neither value is silently accepted or mapped
- the run must use the controlled breadth and source-attempt status vocabularies before verified release

## Case 19 — Bundled queries without a Cartesian explosion

A policy requires four query bundles across a run and twenty named sources. Each bundle is used on multiple suitable sources, and every source attempt records the bundles it used, but not all eighty source-by-bundle combinations are executed.

Expected:

- title-family coverage may be `PASS` when all four required bundles were used
- source coverage is evaluated from required attempts and rotation cadence
- no Cartesian product is inferred unless the policy explicitly requires it

## Case 20 — Minimum actionable result continues beyond baseline

Configuration requires two `Application-safe` results, with a 40/15 baseline checkpoint and a 150/50 hard ceiling. The baseline pass reaches 46 unique discoveries and 19 material inspections but finds zero actionable results.

Expected:

- the run does not stop with `breadth_targets_satisfied`
- the 40/15 floor is recorded as the completed baseline checkpoint
- expansion continues under the configured stages
- no eligibility, evidence, verification, compensation, or utility gate is weakened

## Case 21 — Objective satisfied during expansion

The baseline finds one application-safe result. Expansion pass 2 finds a second while required source, title-family, and reconciliation gates pass.

Expected:

- `result_objective_status: satisfied`
- `stop_reason: requested_result_count_satisfied`
- both counted results satisfy the configured class and Rule 12 live-verification requirements
- the reporting cap still limits display independently

## Case 22 — Bounded exhaustion below objective

The run reaches 150 unique discoveries, 50 material inspections, and eight expansion passes with only one application-safe result.

Expected:

- `stop_reason: configured_search_ceiling_reached`
- `result_objective_status: unmet_after_bounded_exhaustion`
- target, actual, shortfall, and final viability yield are reported
- the one valid result is retained
- no borderline role is promoted to satisfy the minimum

## Case 23 — Viability-based no-yield threshold

Three consecutive expansion passes add materially inspected exclusions but no role that passes hard eligibility, work mode, and known economic floors for application or qualification review.

Expected:

- each pass records material-inspection additions and zero viable additions
- each pass is no-yield under the configured viability threshold
- `stop_reason: consecutive_no_yield_passes`
- the system does not search indefinitely merely because exclusions continue to accumulate

## Case 24 — Evidence detail unknown is not negative evidence

Current evidence establishes professional use of an AI-assisted engineering workflow, but exact cadence is unresolved. A role requires daily AI-tool fluency.

Expected:

- the unresolved cadence is `User confirmation required`, not affirmative evidence that the candidate lacks AI-tool experience
- the role is not hard-screened solely because the exact cadence is absent from the record
- a current candidate confirmation may resolve the cadence at the exact confirmed depth
- unrelated unsupported mandatory technologies remain eligible for normal hard-screen treatment
