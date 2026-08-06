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
- the below-floor discovery and inspection counts are not treated as failure because the allowed early-success condition was satisfied

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
