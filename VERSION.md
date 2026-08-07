# COMPASS Version

Current COMPASS Version: vNext 2026-08.2

Canonical Branch: main

Status: Active

Initialized: 2026-05-18

## Version Rule

The version declared here governs the active framework behavior when used from the `main` branch.

When COMPASS changes materially, update this file and `COMPASS_Changelog.md` in the same change set.

## Naming Rule

COMPASS is the only canonical framework name. New rules, prompts, examples, and project instructions must use COMPASS terminology.

## Active Behavior Notes

The active vNext 2026-08.2 framework includes COMPASS-only terminology, career-focused scope, executable Resume Artifact Release Assurance with hardened OOXML validation and post-publication artifact-name integrity, COMPASS Intake checkpoint artifact behavior, COMPASS Source Rebase scaffold alignment, COMPASS Experience Sync public-projection reconciliation with private source-side target routing, COMPASS Comprehensive Career CV, Initial Seed Artifact support, claim-depth-aware Staff / Principal resume positioning, the Opportunity Reality Layer, the Recruiter Legitimacy and Opportunity Fraud Risk Gate, private recruiter-risk intelligence ledger templates, the Conversational Handoff Gate, fit-calibrated positioning and gap salience, the optional Recruiter Fit Brief, COMPASS Verified Opportunity Search with measurable search breadth and reconciled telemetry, and optional persistent opportunity-registry support:

- COMPASS is a career-focused, source-grounded framework for turning messy career inputs into verified, defensible job-search outputs.
- COMPASS supports the careers / job-search profile. Product, strategy, research, consulting, grant, policy, and personal knowledge workflows are out of scope unless the project owner explicitly reopens scope.
- Core behavior remains truth-first, source-grounded, checkpointed, and claim-ledger-driven.
- COMPASS Comprehensive Career CV is a first-class command for compiling the currently approved career Source of Truth into a broad human-readable and ATS-readable document without turning the CV into a second factual authority.
- Comprehensive-CV generation requires per-role coverage dispositions, implementation-stage preservation, recruiter/public publication envelopes, and Experience Sync for public repository publication.
- Targeted resumes remain the default application artifact; a comprehensive CV is a broad review and evidence-depth artifact rather than automatic role optimization.
- Downloadable comprehensive-CV DOCX files remain resume-class artifacts and require an applicable executable release contract; an ordinary resume contract must not be bypassed through relabeling.
- `rules/16-resume-release-assurance.md` defines a candidate-neutral `generate -> stage -> validate -> render -> manifest -> atomically release` lifecycle for downloadable resume artifacts.
- Resume release checks use `PASS`, `FAIL`, and `UNKNOWN`; every required check must be `PASS`, while `FAIL` and `UNKNOWN` block final publication.
- A more specific user-owned Source of Truth may authorize delivery on aggregate `UNKNOWN` only as `Generated — Release Validation Pending`; this preserves `UNKNOWN`, never authorizes pending delivery on `FAIL`, and never permits final or official release language without aggregate `PASS`.
- Resume-class artifact-format policy is resolved before Comprehensive Career CV generation; when the user-owned policy requires DOCX, Markdown is companion-only and cannot substitute.
- Machine-readable contracts under `schemas/resume-release/` bind releases to current inputs, the actual staged filename, an explicit employment-coverage plan, structural and content checks, rendered-page checks, every-page visual review, privacy boundaries, and atomic publication.
- User-specific release profiles and coverage plans remain private inputs. They may tighten but cannot weaken the public framework contract, and candidate data must not be stored in this repository.
- `python -m tools.resume_release` implements version `1.1.0` validation, atomic local release, and post-publication artifact-name verification using only the Python standard library, with blocking `FAIL` or `UNKNOWN` behavior when required rendering or delivery-name verification is unavailable or invalid.
- Release contract and employment coverage schemas remain at `1.0.0`; the validator emits release manifest schema `1.0.1`, accepts every-page human visual attestations at schema `1.0.0`, and consumes/emits artifact-name integrity receipt/report schema `1.0.0`.
- COMPASS Analysis uses a strict 13-section report contract that separates candidate fit, requested-candidate rarity, company and interview reality, risk, TruthGuard, and pursuit economics.
- `COMPASS Analysis --recruiter-brief` preserves that complete private analysis and may generate a separate externally shareable Recruiter Fit Brief under `rules/19-recruiter-fit-brief.md`.
- The Recruiter Fit Brief is generated from the same resolved evidence through its own template, never by shortening or redacting the analysis; it leads with supported value, separates direct and adjacent evidence, and discloses only material gaps with exact boundaries.
- Hard-screen failure, `Pass`, `Do not share sensitive info yet`, or `Likely scam / disengage` blocks default brief generation; `Proceed cautiously` requires explicit post-analysis approval.
- The flag authorizes generation only. It never authorizes attachment, upload, forwarding, sending, or weakening of TruthGuard, public-safety, Human Authenticity, or analysis-leakage controls.
- COMPASS Analysis applies the Recruiter Legitimacy and Opportunity Fraud Risk Gate when recruiter, staffing, consulting, unclear-entity, suspicious-domain, sensitive-work, or unsafe-process signals are present.
- The Recruiter Legitimacy and Opportunity Fraud Risk Gate evaluates entity identity, domain integrity, application path, recruiter authority, process safety, staffing-firm/client separation, clearance-sensitive risk, and safe next action without changing candidate-fit scoring.
- A configured private recruiter-risk intelligence ledger may be used as a defensive cache for prior sourced observations, but stale, name-only, contradicted, or high-risk matches require current verification before changing the recommended action.
- Public COMPASS framework files define the private-ledger schema, template, and update launcher; they must not store live lists of named recruiters, people, companies, clients, domains, or alleged bad actors.
- Legitimacy ratings are `Verified enough to proceed`, `Proceed cautiously`, `Do not share sensitive info yet`, and `Likely scam / disengage`.
- Legitimacy gaps should change the recommended action, verification boundary, and information-sharing boundary rather than inflate or reduce evidence-backed alignment.
- COMPASS Verified Opportunity Search is a first-class discovery and shortlist workflow for finding active opportunities across multiple employers and, when explicitly activated, a separately ranked secondary contract lane.
- Verified Opportunity Search separates eligibility and hard screens, evidence-backed alignment, opportunity quality, conversion conditions, recruiter-legitimacy risk where applicable, private-ledger matches when configured, and optional contract utility.
- Alignment is a structured decision estimate rather than a probability of interview, offer, or hiring success.
- Freshness, access, visibility, saturation, and application friction are conversion conditions and ranking factors; they do not substitute for fit.
- Low visibility does not qualify a weakly aligned role, and mainstream visibility does not automatically exclude an exceptionally aligned or access-advantaged role when user-specific policy permits it.
- `rules/18-opportunity-search-breadth-telemetry.md` defines canonical discovery stages, configurable breadth targets, expansion-pass tracking, explicit stop conditions, and reconciled run telemetry.
- `--max N` and other result limits cap reporting rather than ordinary discovery, screening, material inspection, duplicate or prior-display reconciliation, or live-verification effort.
- Every materially inspected opportunity must have one canonical run record and exactly one terminal disposition; stage counts and report sections must derive from those records.
- Search-run records may persist aggregate breadth targets, actual stage counts, source and title-family coverage, expansion-pass summaries, breadth status, stop reason, limitations, and reconciliation results without persisting every raw hit or weak discovery lead.
- Historical completed run records remain append-only and missing historical telemetry is unavailable rather than zero.
- Optional contract modes use `--include-contracts`, `--contract-only`, and `--max-contracts N`; contract results remain separate from primary rankings.
- Contract utility evaluates structure-aware economics, hours, duration, flexibility, continuity, exclusivity, intellectual-property, conflict, exit, interference, effort, technical relevance, and relationship value without changing candidate alignment.
- Verified staffing-firm, employer-of-record, or identifiable recruiter-controlled requisitions may support a secondary `Contact first` result when user-specific policy permits it, but accountable entities must remain distinct and undisclosed clients remain unverified.
- The framework does not infer contract rates, hours, duration, client identity, conversion value, exclusivity, or concurrent-work compatibility.
- `rules/13-opportunity-registry.md` defines optional durable cross-run opportunity history using a schema-versioned current registry and append-only search-run records.
- A configured Source of Truth may authorize Verified Opportunity Search to persist observational opportunity facts, duplicate relationships, material changes, reporting history, and persistence outcomes without a second instruction.
- Observational opportunity persistence remains separate from candidate-confirmed status. Applied, interviewing, rejected, withdrawn, contacted, represented, accepted, and do-not-pursue states must not be inferred from search, artifact preparation, or application inspection.
- Opportunity identity prioritizes ATS and requisition identifiers, treats URL variation conservatively, distinguishes reposts from exact duplicates, and uses `possible_duplicate_of` when semantic evidence is insufficient for an automatic merge.
- Search-run persistence must be revision-aware, append-only for completed run records, recoverable after partial failure, and explicitly reported as persisted, degraded, not persisted, or not configured.
- The Opportunity Reality Layer evaluates the Purple Squirrel Factor independently from candidate fit.
- Purple Squirrel scoring considers individual requirement rarity, intersection rarity, technology-maturity plausibility, role compression, level and compensation realism, and constraint stacking.
- Candidate scarcity or role compression never substitutes for candidate evidence and does not automatically justify applying.
- Identifiable-company analysis requires current company and interview research when external access is available, with entity disambiguation, source-tier handling, recency labels, role relevance, sample limitations, and confidence.
- Anonymous employee and candidate reviews remain attributed sentiment or reported accounts, not verified company facts.
- Pursuit economics considers evidence, material gaps, bridgeability, access path, posting signals, compensation, level, remote alignment, strategic value, effort, opportunity cost, and stronger alternatives.
- COMPASS Intake requires checkpoint artifact generation at every committed round.
- COMPASS Intake uses stable artifact templates for checkpoint records, claim-ledger entries, do-not-claim entries, coverage-register entries, storage-status blocks, and optional ZIP bundle manifests.
- COMPASS Intake requires coverage tracking for material imported claims; checkpoints are progress commits, not proof of full source ingestion.
- COMPASS Intake runs a Materiality Gate before asking questions: it inspects available approved ledgers, do-not-claim records, coverage registers, checkpoint records, canonical source records, and relevant source artifacts, then asks only unresolved material questions.
- COMPASS Source Rebase supports safe dry-run and explicitly approved create-missing-only scaffold alignment for source-of-truth repositories without overwriting, deleting, renaming, moving, or modifying existing user-owned records.
- COMPASS Source Rebase recognizes `/sources/seed/` as the recommended scaffold path for Initial Seed Artifacts and `/sync/` as the optional private scaffold path for Experience Sync target routing.
- COMPASS Source Rebase preserves historical checkpoint files such as older `COMPASS_Layer0_*` paths as historical records rather than normalizing names.
- COMPASS Experience Sync reconciles an approved Source of Truth into a separate public or externally shareable experience repository as a one-way downstream projection.
- COMPASS Experience Sync resolves downstream targets from the private Source of Truth routing map at `sync/COMPASS_Experience_Targets.yaml` when available.
- Public Experience Manifests use a stable source identifier and reconciliation metadata rather than exposing the private Source of Truth repository location.
- COMPASS Experience Sync defaults to dry-run, supports full-audit, and permits writes only in explicitly approved `apply-approved` mode through a non-default target branch and pull request.
- COMPASS Experience Sync applies factual approval and public-disclosure suitability as separate gates, preserves claim-depth and do-not-claim boundaries, and never modifies the Source of Truth or routing map.
- Imported resumes, CVs, LinkedIn profiles, cover letters, portfolio examples, recruiter resumes, and prior generated artifacts are evidence inputs until their material claims are verified into the canonical source of truth.
- Initial Seed Artifacts under `/sources/seed/` are seed, provisional, evidence, and not canonical. They may support Provisional Resume / CV Mode while Intake is incomplete.
- Comprehensive resumes and master CVs may be stronger provisional baselines than shortened or tailored resumes, but neither becomes permanent canonical truth merely by being stored as a seed artifact.
- After verified ingestion, the canonical source-of-truth record, approved claim ledger, and do-not-claim register supersede imported artifacts for downstream use.
- Generated artifacts are downstream outputs, not factual authorities, unless separately imported and verified through Intake.
- Generated artifact types use strict output templates from `rules/06-artifact-rules.md` unless the user explicitly requests a different format.
- Downloadable resume artifacts remain staged and untrusted until a matching release manifest records `PASS` for every required check; missing validation capability is `UNKNOWN`, not an unchecked fallback.
- External career artifacts use `rules/08-human-authenticity.md` to preserve truthful specificity, reviewer readability, candidate-specific voice, ATS-safe structure, and interview-defensible claims without fake humanization or AI-detector evasion tactics.
- Fit-calibrated positioning preserves comprehensive internal gap analysis while ordering external evidence according to actual role alignment, leading with source-backed value in highly aligned opportunities and surfacing material gaps proportionately in moderate- or low-alignment opportunities.
- Short-form external messages use the Conversational Handoff Gate in `rules/08-human-authenticity.md` to continue from shared context, preserve information gain, ask only the minimum useful questions, keep internal analysis out of the message, state each point once, and move toward one clear next action.
- Conversational message drafting must identify established context, the remaining necessary answer or boundary, unresolved gating information, and the single next action before producing sendable text.
- Conversational message revision must run a deletion pass that removes resume-summary phrasing, analysis leakage, repeated known context, generic interest signaling, and social filler that adds no answer, boundary, question, or action.
- Senior-IC resumes use claim-depth-aware wording, preserve official employment titles, prioritize verified Staff / Principal evidence, and distinguish intended benefits from realized outcomes.
- Resume review should preserve useful technical depth while revising repeated architecture-taxonomy lists that obscure the candidate's action, decision, or consequence.
- Intake setup must disclose whether direct datastore writes are available before asking setup questions.
- If direct writes are unavailable, Intake must generate downloadable or copy-ready files and clearly instruct the user where to upload them.

## Compatibility Rule

Future COMPASS changes should preserve the core operating principles unless explicitly superseded:

- Truthful source-grounded output
- Phased workflow
- No fabricated technologies, metrics, credentials, employment history, project ownership, career achievements, business outcomes, market statistics, company facts, client identity, contract terms, opportunity status, or other material claims
- Separate strategic analysis from clean external generated artifacts
- External positioning may calibrate emphasis and gap salience to actual alignment, but must not hide hard requirements, obscure material limitations, or imply unsupported experience
- Short-form conversational outputs continue the established exchange instead of restating shared context or leaking internal analysis
- Strict artifact output templates preserved unless the user explicitly requests a different format
- Career-profile rules may add specialized output rules without weakening source-grounding or TruthGuard
- External employer, staffing, client, interview, contract, and private-ledger evidence must preserve attribution, entity identity, recency, confidence, match strength, and uncertainty
- Verified Opportunity Search must preserve separate eligibility, alignment, opportunity-quality, conversion-condition, recruiter-legitimacy risk where applicable, private-ledger matches when configured, and optional contract-utility judgments
- Verified Opportunity Search must keep result limits separate from search breadth and must not claim reconciled discovery or inspection telemetry without canonical records
- Persistent opportunity history must preserve separate identity, observation, reporting, candidate-status, suppression, and provenance state
- Configured observational registry writes must not be treated as permission to infer candidate actions or employer outcomes
- Primary and secondary opportunity rankings must remain separate
- Staffing, employer-of-record, client, and end-customer identities must not be conflated
- Recruiter-legitimacy concerns must not change evidence-backed candidate-fit scoring; they affect verification, sensitive-information boundaries, and recommended next action
- Private recruiter-risk intelligence ledgers are private Source of Truth records, not public framework data, and stale, weakly matched, or contradicted records must not be treated as current proof
- COMPASS Intake remains the default process for building a canonical source record from unverified documents or a new user's history
- COMPASS Source Rebase remains scaffold alignment only and must not perform Intake, claim verification, destructive source-record migration, or overwrite populated opportunity registries and run logs
- COMPASS Experience Sync remains a one-way downstream public projection and must not modify or supersede Source of Truth records
- Source-side Experience Sync routing remains private Source of Truth configuration and must not be copied into public target metadata
- COMPASS Comprehensive Career CV remains a generated publication, not a source archive or factual authority, and must preserve role coverage, contribution depth, implementation stage, disclosure controls, and resume-release requirements
- Initial Seed Artifacts remain provisional evidence and provenance until superseded by verified source-of-truth records and ledgers
