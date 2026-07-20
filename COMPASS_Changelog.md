# COMPASS Changelog

All notable framework changes should be documented here.

## vNext 2026-07.5 - Comprehensive Career CV

Added a first-class workflow for compiling approved career evidence into a broad, human-readable and ATS-readable career document without creating a second Source of Truth.

Behavior updates:

- Added `COMPASS Comprehensive Career CV` to the canonical command registry.
- Added `rules/17-comprehensive-career-cv.md` for source resolution, compilation rather than dossier concatenation, per-role coverage dispositions, implementation-stage preservation, audience variants, disclosure boundaries, and output separation.
- Added `prompts/compass-comprehensive-career-cv.md` with `--recruiter`, `--public`, and `--both` modes.
- Added a candidate-neutral comprehensive-CV Markdown template.
- Required public comprehensive-CV publication to use the existing Experience Sync truth and publication gates, target routing, branch-and-pull-request policy, and no-provisional-claim behavior when configured.
- Clarified that targeted resumes remain the default application artifact and that ATS readability is not equivalent to role-specific optimization.
- Classified downloadable comprehensive-CV DOCX files as resume-class artifacts that require an applicable executable release contract; a conventional resume filename or section contract may not be bypassed through relabeling.
- Preserved generated CVs and public experience repositories as downstream publication artifacts rather than factual authorities.
- Advanced the active framework identifier from `vNext 2026-07.4` to `vNext 2026-07.5`.

## vNext 2026-07.4 - Resume Release Validator

Implemented the candidate-neutral validation and atomic-release engine defined by Resume Artifact Release Assurance.

Behavior updates:

- Added `python -m tools.resume_release validate` and `release` with stable exit codes `0`, `1`, `2`, and `64`.
- Enforced all 20 stable version `1.0.0` check identifiers so a private contract cannot silently remove a release gate.
- Added dependency-free contract loading, deterministic check aggregation, privacy-safe manifests, DOCX ZIP/OOXML inspection, configured style/list/indentation/margin/break/keep-next checks, normalized anchor and coverage validation, and overlap-safe experience-duration calculation.
- Added isolated LibreOffice rendering, Poppler page rasterization, dependency-free PGM ink and bottom-whitespace measurement, and blocking `UNKNOWN` behavior for missing or failed required rendering.
- Added `schemas/resume-release/visual-review-attestation.schema.json` for separately supplied human every-page review evidence. The validator does not generate or infer this attestation.
- Added staged atomic publication with rollback backups and regression proof that `FAIL`, `UNKNOWN`, and publication errors do not replace an existing final artifact.
- Corrected a Prompt 1 manifest defect so an attempted publication that is rolled back may be recorded with aggregate `UNKNOWN`; advanced only the release-manifest schema from `1.0.0` to `1.0.1`.
- Added candidate-neutral generated-fixture tests under `tests/resume_release/` covering structural, content, rendering, visual-review, filename, and publication behavior.
- Preserved release-contract and employment-coverage schema version `1.0.0` and introduced validator and visual-attestation version `1.0.0`.
- Advanced the active framework identifier from `vNext 2026-07.3` to `vNext 2026-07.4`.

## vNext 2026-07.3 - Resume Artifact Release Assurance

Added the framework contract and machine-readable schemas for deterministic resume artifact staging, validation, and publication.

Behavior updates:

- Added `rules/16-resume-release-assurance.md` to define the candidate-neutral `generate -> stage -> validate -> render -> manifest -> atomically release` lifecycle.
- Added `PASS`, `FAIL`, and `UNKNOWN` validation semantics. Every required check must be `PASS`; either `FAIL` or `UNKNOWN` blocks final publication.
- Added release-contract, release-manifest, and employment-coverage-plan schemas under `schemas/resume-release/`.
- Added stable check identifiers covering current policy and profile inputs, actual filenames, DOCX structure and pagination controls, Markdown/DOCX parity, employment coverage, experience-duration calculation, rendered pages and whitespace, blank pages, every-page visual review, and atomic publication.
- Required explicit detailed, compressed, or excluded disposition for each in-scope employment role and union-of-calendar-intervals experience calculation.
- Required generated outputs to remain staged and untrusted until validation succeeds and a matching manifest authorizes atomic publication.
- Preserved the public/private boundary: generic contracts live in the framework, while candidate-specific profiles, coverage plans, claims, and artifacts remain outside this repository.
- Added `tools/resume_release/README.md` as the stable command, result, check-ID, and exit-code interface. This build unit defines the interface; the executable validator and tests follow in the next resume-assurance build unit.
- Updated the canonical framework definition, command registry, artifact and resume rules, both resume launchers, repository guidance, and README navigation to load the release contract.
- Advanced the active framework identifier from `vNext 2026-07.2` to `vNext 2026-07.3`.

## vNext 2026-07.2 - Recruiter Risk Intel Ledger Templates

Added framework-owned templates and a maintenance launcher for a private recruiter-risk intelligence ledger.

Behavior updates:

- Added `templates/recruiter-risk-intel/README.md` to define the public-framework / private-ledger boundary.
- Added `templates/recruiter-risk-intel/RECRUITER_RISK_INTEL_LEDGER_TEMPLATE.yaml` as the reusable private-ledger scaffold.
- Added `prompts/compass-recruiter-risk-intel-update.md` as a supported maintenance launcher, not a first-class command.
- Updated `rules/14-recruiter-legitimacy-risk.md` so a configured private ledger may be used as a defensive cache while stale, name-only, contradicted, or high-risk matches still require current verification.
- Updated `COMPASS_COMMANDS.md` to expose recruiter-risk intel updates as a supported maintenance artifact and to keep private-ledger matches separate from candidate fit, opportunity quality, and contract utility.
- Updated `VERSION.md` to expose the active behavior.
- Preserved the rule that the public COMPASS Framework repository must not store live lists of named recruiters, people, companies, clients, domains, or alleged bad actors.
- Advanced the active framework identifier from `vNext 2026-07.1` to `vNext 2026-07.2`.

## vNext 2026-07.1 - Recruiter Legitimacy Risk Gate

Added a durable recruiter-legitimacy and opportunity-risk gate for recruiter-presented, staffing, consulting, employer-of-record, unclear-entity, sensitive-work, and process-safety concerns.

Behavior updates:

- Added `rules/14-recruiter-legitimacy-risk.md` as the durable rule for entity-chain separation, recruiter authority, domain and application-path integrity, process-safety review, information-sharing boundaries, and verification-first actions.
- Added legitimacy ratings: `Verified enough to proceed`, `Proceed cautiously`, `Do not share sensitive info yet`, and `Likely scam / disengage`.
- Clarified that legitimacy findings do not change evidence-backed candidate alignment; they change recommended action, verification requirements, and information-sharing boundaries.
- Updated COMPASS Analysis behavior so recruiter, staffing, consulting, unclear-entity, suspicious-domain, sensitive-work, or unsafe-process signals load the new gate.
- Updated Verified Opportunity Search behavior so recruiter-legitimacy risk remains separate from eligibility, alignment, opportunity quality, conversion conditions, and contract utility.
- Updated recruiter-response behavior so unresolved legitimacy concerns produce verification-first responses rather than normal interest responses.
- Updated `VERSION.md`, `COMPASS_Current.md`, `COMPASS_COMMANDS.md`, `README.md`, and relevant launcher prompts to expose the active behavior.
- Advanced the active framework identifier from `vNext 2026-06.5` to `vNext 2026-07.1`.

## vNext 2026-06.5 - Persistent Opportunity Registry

Added optional durable cross-run opportunity history for COMPASS Verified Opportunity Search.

Behavior updates:

- Added `rules/13-opportunity-registry.md` as the durable contract for schema-versioned opportunity registries, append-only search-run records, revision-aware writes, partial-failure recovery, idempotency, and persistence reporting.
- Added generic registry and search-run templates under `templates/opportunity-registry/`.
- Separated opportunity identity, observation, reporting history, candidate-confirmed status, suppression, and provenance so search observations cannot silently become candidate actions or employer outcomes.
- Authorized configured Verified Opportunity Search runs to persist observational opportunity facts without a second instruction when the user's Source of Truth defines the paths and write policy.
- Preserved explicit user authority for candidate statuses including applied, interviewing, rejected, withdrawn, contacted, represented, accepted, and do-not-pursue.
- Added exact-identifier precedence, conservative semantic duplicate handling, `possible_duplicate_of`, and `related_repost_of` behavior.
- Added material-change rules for reopenings, new hiring cycles, compensation, eligibility, scope, hard screens, access, and contract terms.
- Added persistence outcomes: `Persisted`, `Persistence degraded`, `Not persisted`, and `Persistence not configured`.
- Added recovery behavior for malformed registries, concurrent revision conflicts, and run-log-success / registry-failure cases.
- Updated the Verified Opportunity Search launcher and `VERSION.md` to load and expose the new contract.
- Advanced the active framework identifier from `vNext 2026-06.4` to `vNext 2026-06.5`.

## vNext 2026-06.4 - Conversational Handoff Refinement

Folded branch-only Conversational Handoff guidance into the active Human Authenticity rule.

Behavior updates:

- Extended `rules/08-human-authenticity.md` with the required pre-draft handoff sequence: established context, remaining answer or boundary, unresolved gating information, and one next action.
- Added conversation-specific evidence compression so candidate evidence appears only when it answers, corrects, distinguishes, repositions, supports negotiation, or resolves ambiguity.
- Added explicit interest-signaling and deletion-pass controls for short-form sendable messages.
- Updated `COMPASS_Current.md` and `VERSION.md` to expose the active behavior.
- Advanced the active framework identifier from `vNext 2026-06.3` to `vNext 2026-06.4`.

## vNext 2026-06.3 - COMPASS Verified Opportunity Search

Added a first-class multi-opportunity discovery and shortlist workflow centered on evidence-backed alignment rather than hiddenness alone, with explicitly activated secondary contract-search modes.

Behavior updates:

- Added `rules/12-verified-opportunity-search.md` as the durable rule for current-opportunity discovery, live-opportunity verification, requisition reconciliation, ordered eligibility and hard-screen gates, alignment scoring, opportunity-quality review, conversion-condition ranking, application-stage inspection, duplicate suppression, and optional contract-utility assessment.
- Added `prompts/compass-verified-opportunity-search.md` as the reusable launcher prompt.
- Added `COMPASS Verified Opportunity Search` to `COMPASS_COMMANDS.md` with required framework and user-specific source inputs.
- Separated eligibility and hard screens, evidence-backed alignment, opportunity quality, conversion conditions, and optional contract utility so one dimension cannot silently substitute for another.
- Added a default alignment model weighted across load-bearing qualifications, central responsibilities, level and operating scope, evidence recognizability, transferability, and career-direction value.
- Required alignment estimates to use decision bands and ordinary five-point increments rather than false precision or implied interview probability.
- Clarified that a hard eligibility or application-screen failure overrides an otherwise high alignment score.
- Reclassified freshness, access, visibility, saturation, and application friction as conversion conditions and ranking factors rather than universal fit gates.
- Clarified that low visibility cannot qualify a weakly aligned role and that mainstream visibility does not automatically exclude an exceptionally aligned or access-advantaged role when user-specific policy permits it.
- Added `--include-contracts`, `--contract-only`, and `--max-contracts N` as canonical optional secondary-search modes.
- Required primary direct-hire and secondary contract results to remain in separate lanes and rankings.
- Added reusable bridge, fractional / side, contract-to-hire, and unspecified contract classifications.
- Added qualitative contract-utility assessment across structure-aware economics, benefits treatment, hours, duration, continuity, flexibility, exclusivity, intellectual-property, conflict, notice, exit, interference, effort, technical relevance, and relationship value.
- Added `A — Strong secondary opportunity`, `B — Qualify first`, and `C — Weak utility` as default contract-utility grades while preserving user-specific overrides.
- Required missing rate, hours, duration, employment structure, client identity, exclusivity, conversion compensation, or other load-bearing terms to default to `Contact first` rather than `Apply now` unless a stricter Source of Truth policy applies.
- Added controlled verification for staffing-firm, employer-of-record, and identifiable recruiter-controlled contract requisitions when a public client application does not exist.
- Required staffing firm, employer of record, direct client, and end customer to remain distinct; undisclosed clients remain unverified.
- Added agency duplicate reconciliation using known client, accountable entity, title, location, employment structure, duration, hours, rate, requisition identity, and materially identical description.
- Prohibited inference of contract concurrency compatibility, client identity, rate, hours, duration, conversion value, exclusivity, representation rights, or commercial terms.
- Added untrusted-external-content controls for job descriptions, ATS pages, application forms, recruiter posts, staffing pages, direct messages, HTML, and metadata.
- Required current employer-controlled job and application verification for direct-employer roles, conflict reconciliation, application or qualification-stage visibility disclosure, and an immediate final recheck for reported priority roles or leads.
- Updated `COMPASS_Current.md`, `README.md`, and `VERSION.md` to expose the active behavior.
- Advanced the active framework identifier from `vNext 2026-06.2` to `vNext 2026-06.3`.

## vNext 2026-06.2 - Fit-Calibrated Positioning and Gap Salience

Added alignment-aware positioning rules so external career materials lead with source-backed value in highly aligned opportunities while preserving proportionate gap disclosure and full internal diagnostic analysis.

Behavior updates:

- Extended `rules/08-human-authenticity.md` with a Fit-Calibrated Positioning and Gap Salience section governing external artifacts and interview guidance.
- Required highly aligned opportunities to lead with direct fit, contribution depth, transferable scope, and reviewer value instead of opening with non-material absences or negative-first constructions.
- Distinguished company-specific systems, exact internal implementations, tool-specific differences, and normal onboarding from material candidate deficiencies.
- Required moderately aligned opportunities to distinguish direct from adjacent evidence, identify material gaps proportionately, and use credible source-backed ramp-up framing.
- Required weakly aligned opportunities to surface material limitations rather than manufacture a conversion narrative.
- Preserved comprehensive internal analysis while keeping external positioning selective, truthful, role-relevant, and calibrated to materiality.
