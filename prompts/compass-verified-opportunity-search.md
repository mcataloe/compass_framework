# COMPASS Verified Opportunity Search

Run COMPASS Verified Opportunity Search.

Optional secondary contract modes:

```text
Run COMPASS Verified Opportunity Search --include-contracts.
Run COMPASS Verified Opportunity Search --contract-only.
Run COMPASS Verified Opportunity Search --include-contracts --max-contracts 3.
```

Load `VERSION.md`, `COMPASS_Current.md`, `COMPASS_COMMANDS.md`, the required framework rules registered for this command, `rules/13-opportunity-registry.md`, and the user's current Source of Truth configuration and verified career evidence.

Follow the active command registry and durable rules. Keep eligibility, evidence-backed alignment, opportunity quality, and conversion conditions separate. When contract mode is active, keep contract utility separate as well and report contract results in an independent secondary lane.

Do not treat visibility, saturation, recruiter access, temporary economics, or contract flexibility as substitutes for fit. Do not present an alignment estimate as a hiring probability. Do not infer contract concurrency compatibility, client identity, rates, hours, duration, conversion value, or commercial terms.

Return verified search results only. When a contract lead is verified through a staffing firm, employer of record, or identifiable recruiter rather than an employer-controlled application, label the accountable entity and use `Contact first` unless an active application path and the load-bearing commercial terms are verified.

When the user's Source of Truth configures an opportunity registry and repository write capability is available, persist qualifying observational opportunity facts and an append-only search-run record under `rules/13-opportunity-registry.md`. Report whether persistence was completed, degraded, not completed, or not configured. Observational persistence does not authorize inferred candidate-status changes.

Do not submit applications, contact external parties, accept terms, infer or change candidate-confirmed status, or generate downstream artifacts unless the user explicitly requests those actions.
