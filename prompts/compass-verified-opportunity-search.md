# COMPASS Verified Opportunity Search

Run COMPASS Verified Opportunity Search.

Optional secondary contract modes:

```text
Run COMPASS Verified Opportunity Search --include-contracts.
Run COMPASS Verified Opportunity Search --contract-only.
Run COMPASS Verified Opportunity Search --include-contracts --max-contracts 3.
```

Load `VERSION.md`, `COMPASS_Current.md`, `COMPASS_COMMANDS.md`, the required framework rules registered for this command, `rules/13-opportunity-registry.md`, `rules/18-opportunity-search-breadth-telemetry.md`, `rules/15-opportunity-unique-questions.md`, `rules/14-recruiter-legitimacy-risk.md` when recruiter-controlled or unclear-entity paths are present, and the user's current Source of Truth configuration and verified career evidence.

Follow the active command registry and durable rules. Keep eligibility, evidence-backed alignment, opportunity quality, conversion conditions, recruiter-legitimacy risk, and opportunity-unique application-question handling separate. When contract mode is active, keep contract utility separate as well and report contract results in an independent secondary lane.

Treat `--max N` and other result limits as reporting caps, not ordinary discovery or inspection caps. Follow the user's configured search-breadth targets and source-coverage profile. Record one attempt for every applicable required or selected rotating source using only the controlled statuses; complete an approved recorded substitution when a normal source path is blocked. Track query bundles and rotation windows without inferring a source-by-title Cartesian product. Evaluate numeric breadth, source coverage, title-family coverage, and telemetry reconciliation independently. Early success may bypass only numeric floors. Reconcile every materially inspected opportunity to exactly one terminal disposition before reporting breadth as verified.

Do not treat visibility, saturation, recruiter access, temporary economics, contract flexibility, recruiter legitimacy signals, or an easily answerable application question as substitutes for fit. Do not present an alignment estimate as a hiring probability. Do not infer contract concurrency compatibility, client identity, rates, hours, duration, conversion value, or commercial terms.

Return verified search results only. When a contract lead is verified through a staffing firm, employer of record, or identifiable recruiter rather than an employer-controlled application, label the accountable entity and use `Contact first` unless an active application path and the load-bearing commercial terms are verified. If legitimacy, impersonation, domain, entity-chain, unsafe-process, or sensitive-information concerns are present, apply `rules/14-recruiter-legitimacy-risk.md` and prefer verification before sensitive engagement.

Inspect accessible application or qualification flows for role-specific, employer-specific, portfolio, public-artifact, technical-narrative, or work-sample questions when safe to do so without submitting an application or accepting terms. Classify visible questions under `rules/15-opportunity-unique-questions.md` as `Verified answer`, `Draft answer — user review`, `User confirmation required`, `Do not answer automatically`, or `Unsupported / disqualifying`. Prepare draft answers only when source-grounded and useful. Do not answer sensitive voluntary fields or legal/personal attestations automatically.

When the user's Source of Truth configures an opportunity registry and repository write capability is available, persist qualifying observational opportunity facts and an append-only search-run record under `rules/13-opportunity-registry.md`. Persist aggregate breadth telemetry, pass summaries, stop reason, and reconciliation results without storing every raw hit or weak discovery lead. Report whether persistence was completed, degraded, not completed, or not configured. Observational persistence does not authorize inferred candidate-status changes.

Do not submit applications, contact external parties, accept terms, infer or change candidate-confirmed status, share sensitive information, or generate downstream artifacts unless the user explicitly requests those actions.