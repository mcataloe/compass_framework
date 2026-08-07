# COMPASS Changelog

All notable framework changes should be documented here.

## vNext 2026-08.2 - Recruiter Fit Brief

Added an optional recruiter-facing derivative to COMPASS Analysis while preserving the complete private analysis and its leakage firewall.

Behavior updates:

- Added `COMPASS Analysis --recruiter-brief` as an explicit generation-only option; ordinary Analysis behavior is unchanged without the flag.
- Added `rules/19-recruiter-fit-brief.md` with eligibility, gap taxonomy, legitimacy, public-safety, disclosure, leakage, format, validation, and action boundaries.
- Added a candidate-neutral strict Recruiter Fit Brief template and acceptance scenarios covering strong fit, defined material gaps, adjacent evidence, hard-screen failure, leakage, sensitive information, and no-flag regression.
- Required the brief to be generated from the same resolved evidence through its own template, never by truncating or redacting the internal analysis.
- Limited external submission postures to `Strong fit` and `Credible fit with defined gaps`; hard-screen failure, `Pass`, and unsafe legitimacy states block default generation.
- Preserved TruthGuard, Human Authenticity, artifact separation, public-disclosure controls, and the rule that generation never attaches, uploads, forwards, or sends the brief.
- Updated the command registry, analysis workflow, artifact rules, launcher, current framework description, README, and active version.
- Advanced the active framework identifier from `vNext 2026-08.1` to `vNext 2026-08.2`.

## vNext 2026-08.1 - Verified Opportunity Search Breadth and Telemetry

Added a measurable search-breadth contract so result limits no longer obscure how broadly a Verified Opportunity Search was executed.

Behavior updates:

- Added `rules/18-opportunity-search-breadth-telemetry.md` with canonical stages for observable source hits, unique normalized discoveries, quick screens, material inspections, live verification, and reported opportunities.
- Clarified that `--max N` and other result limits cap reporting rather than ordinary discovery, screening, material inspection, duplicate or prior-display reconciliation, or live-verification effort.
- Added user-configurable breadth floors, source and title-family coverage, expansion-pass tracking, consecutive no-yield stopping thresholds, and explicit stop reasons.
- Required one canonical run record and exactly one terminal disposition for every materially inspected opportunity.
- Added reconciliation invariants so stage counts, terminal dispositions, duplicate and prior-display counts, and reported results derive from canonical records rather than manual narrative estimates.
- Expanded the opportunity-search run template with targets, actual stage counts, coverage summaries, expansion passes, breadth status, stop reason, limitations, and reconciliation results.
- Preserved the persistence boundary: aggregate telemetry may be stored, but raw snippets and weak discovery noise remain transient.
- Preserved historical run files as append-only and defined missing historical telemetry as unavailable rather than zero.
- Updated the command registry, launcher, current framework description, template documentation, and active version.
- Advanced the active framework identifier from `vNext 2026-07.7` to `vNext 2026-08.1`.

## vNext 2026-07.7 - Pending Delivery and Resume-Class Format Reconciliation

Reconciled generic resume-release assurance with more specific user-owned Source of Truth policies without weakening validated release status.

Behavior updates:

- Preserved aggregate `PASS` as the only authority for final, official, validated, or publication-ready resume status.
- Allowed a user-owned Source of Truth to authorize aggregate `UNKNOWN` delivery only as `Generated — Release Validation Pending`, with the exact limitation disclosed.
- Kept aggregate `FAIL` delivery-blocking and prohibited candidate-specific policy from converting `FAIL` or `UNKNOWN` into `PASS`.
- Required pending outputs to remain separate from validated final outputs and prohibited staging-link workarounds.
- Required Comprehensive Career CV generation to resolve user-owned artifact-format policy before generation.
- Made DOCX mandatory for Comprehensive Career CV when the user-owned resume-class policy requires it; Markdown remains companion-only in that case.
- Updated the command registry and Comprehensive Career CV rule to use the reconciled status and format behavior.
- Advanced the active framework identifier from `vNext 2026-07.6` to `vNext 2026-07.7`.

## vNext 2026-07.6 - Resume Release Hardening and End-to-End Artifact-Name Integrity

Closed gaps where a Word-incompatible OOXML package could pass validation and where a correct staged filename could become an incorrectly encoded delivered or downloaded filename.

Behavior updates:

- Validated declared XML encoding against actual bytes for every OOXML XML and relationship part.
- Validated markup-compatibility namespace prefixes and rejected undeclared prefixes referenced by compatibility attributes or `mc:Choice Requires`.
- Preserved atomic-publication durability checks on Windows by syncing publication temporaries through a writable file descriptor.
- Required one decoded canonical filename to control filesystem creation, publication, attachment, display, manifest, archive, metadata, completion, and browser-download naming surfaces.
- Added post-publication `artifact.name_integrity` verification with `PASS`, `FAIL`, and release-blocking `UNKNOWN` behavior.
- Added artifact-name integrity receipt and report schemas covering staged/final files, objects, attachments, downloads, controlled `Content-Disposition`, storage labels, links, manifests, ZIPs, generated metadata, and copied variants.
- Added `python -m tools.resume_release verify-name-integrity` and preserved opaque transport encoding only for an explicitly required transport target; encoded display or downloaded names still fail.
- Added candidate-neutral regression tests for OOXML encoding and compatibility-prefix defects plus literal spaces, encoded and double-encoded spaces, delivery metadata, manifests, ZIP names and entries, and transport leakage.
- Advanced the validator from `1.0.0` to `1.1.0` and the active framework identifier from `vNext 2026-07.5` to `vNext 2026-07.6`; existing release-contract, employment-coverage, visual-attestation, and release-manifest schema versions remain compatible.

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
- Clarified that fit-calibrated positioning changes emphasis, sequence, and salience only and cannot hide hard requirements, obscure material limitations, imply missing experience, inflate transferability, or override TruthGuard.
- Advanced the active framework identifier from `vNext 2026-06.1` to `vNext 2026-06.2`.

## vNext 2026-06.1 - Conversational Handoff Gate

Added a reusable conversational-output gate so short-form external messages continue an existing exchange rather than reproducing analysis or behaving like standalone career artifacts.

Behavior updates:

- Extended `rules/08-human-authenticity.md` with a required Conversational Handoff Gate for recruiter replies, networking responses, application follow-ups, scheduling notes, and negotiation messages.
- Required short-form messages to continue from shared context, preserve information gain, ask only the minimum useful questions, state each point once, and move toward one clear next action.
- Prohibited analysis leakage, requirement recitals, compressed-resume phrasing, known-answer questions, generic interest-signaling filler, and unnecessary information requests.
- Added a natural-turn test that evaluates whether the message plausibly belongs at that point in the conversation.
- Preserved user-specific Source of Truth authority so channel-specific voice, sequence, and deletion rules override generic framework defaults within their documented scope.
- Advanced the active framework identifier from `vNext 2026-05.11` to `vNext 2026-06.1`.

## vNext 2026-05.11 - Private Experience Sync Routing

Moved actual Source of Truth and downstream target repository mapping into private Source of Truth configuration.

Behavior updates:

- Added `templates/source-of-truth-scaffold/sync/COMPASS_Experience_Targets.yaml` as the generic private routing-map template.
- Added `templates/source-of-truth-scaffold/sync/README.md` to define the source-side privacy and ownership boundary.
- Updated Source Rebase to recognize `/sync/` as an optional scaffold path and to create only generic missing placeholders after explicit approval.
- Required actual source and target links, target IDs, branches, publication defaults, and protected paths to live in the Source of Truth routing map rather than the public target manifest.
- Sanitized the target `COMPASS_Experience_Manifest.yaml` template so it contains a stable source ID and reconciliation metadata without exposing the private Source of Truth repository location.
- Added deterministic target resolution, override-conflict handling, enabled-target checks, and missing-routing-map behavior.
- Updated Experience Sync dry-run and full-audit behavior to detect public source-location exposure.
- Updated the reconciliation report to record routing-map access, selected target ID, target-resolution basis, and public-manifest sanitization.
- Preserved the one-way projection boundary: Experience Sync reads but never modifies the Source of Truth or routing map.
- Advanced the active framework identifier from `vNext 2026-05.10` to `vNext 2026-05.11`.

## vNext 2026-05.10 - COMPASS Experience Sync

Added `COMPASS Experience Sync` as a first-class command for reconciling an approved career Source of Truth into a separate public or externally shareable experience repository.

Behavior updates:

- Added `rules/11-experience-sync.md` as the durable rule for one-way Source of Truth publication, reconciliation classifications, disclosure gating, drift detection, protected-path handling, and branch-and-pull-request-only writes.
- Added `prompts/compass-experience-sync.md` as the reusable launcher prompt.
- Added `dry-run`, `full-audit`, and explicitly approved `apply-approved` modes.
- Required a current matching reconciliation report and explicit approval before any target-repository write.
- Prohibited Source of Truth writes, direct target-default-branch writes, implicit pull-request merges, and use of the public experience repository as factual authority.
- Separated factual approval from public suitability through independent Truth and Publication gates.
- Added coverage-status handling for approved, narrowed, claim-depth-bounded, rejected, unresolved, deferred, and provisionally authorized claims.
- Added reconciliation classifications for additions, wording updates, narrowing, approved strengthening, public-claim removal, provisional replacement, withholding, and human-decision conflicts.
- Added generic Experience Manifest, Experience Sync Report, and public claim provenance templates under `templates/experience-sync/`.
- Added Experience Sync report and public claim index contracts to `rules/06-artifact-rules.md`.
- Updated `COMPASS_Current.md`, `COMPASS_COMMANDS.md`, and `README.md` to expose the command and its relationship to Intake and Source Rebase.
- Preserved TruthGuard, claim-depth boundaries, do-not-claim precedence, provisional-source controls, privacy, confidentiality, and storage honesty.
- Advanced the active framework identifier from `vNext 2026-05.9` to `vNext 2026-05.10`.

## vNext 2026-05.9 - Opportunity Reality Layer

Added an Opportunity Reality Layer to COMPASS Analysis so role evaluation covers not only candidate fit, but also requested-candidate scarcity, employer and interview reality, and whether pursuing the opportunity is worth the candidate's limited time.

Behavior updates:

- Added `rules/10-opportunity-recon.md` as the durable rule for Purple Squirrel Factor scoring, role-compression analysis, company background research, employee sentiment, technical interview research, interview realism, external-evidence handling, and pursuit economics.
- Added Purple Squirrel scoring across individual requirement rarity, intersection rarity, technology-maturity plausibility, role compression, level and compensation realism, and constraint stacking.
- Clarified that a coherent niche specialist role is different from an incoherently compressed role and that candidate scarcity does not create candidate evidence.
- Added pursuit-economics analysis covering load-bearing evidence, material gaps, bridgeability, access path, posting visibility and saturation signals, compensation, level, remote-work alignment, strategic value, effort, opportunity cost, and stronger alternatives.
- Required current company and interview research for identifiable employers when browsing or connected-source access is available.
- Added entity-disambiguation rules for similarly named companies and for staffing company, employer of record, direct client, and end customer relationships.
- Added employee-sentiment handling with engineering-specific analysis, repeated-theme detection, recency, sample limitations, and High / Medium / Low / Insufficient confidence.
- Added technical-interview research priorities for recent, comparable, role-relevant reports and separated interview difficulty from interview realism.
- Added interview-realism classifications ranging from role-aligned through potentially exploitative, with an Insufficient evidence option.
- Extended TruthGuard so anonymous reviews remain attributed accounts, isolated allegations are not generalized, historical evidence is not presented as current without corroboration, and missing evidence remains unknown.
- Expanded the strict COMPASS Analysis report from 11 to 13 sections, adding Purple Squirrel Factor and requirement-market realism, company and interview reality, and recommendation and pursuit economics.
- Updated the analysis launcher and command registry to require `rules/06-artifact-rules.md` and `rules/10-opportunity-recon.md`.
- Preserved analysis / artifact separation so company research, employee sentiment, opportunity scoring, interview-risk findings, and pursuit economics do not leak into clean resumes, cover letters, recruiter responses, application answers, or follow-up messages.
- Advanced the active framework identifier from `vNext 2026-05.8` to `vNext 2026-05.9`.

## vNext 2026-05.8 - Initial Seed Artifacts and Release Hygiene

Added first-class Initial Seed Artifact support for provisional career source materials under `/sources/seed/` and normalized the active release identifier so distinct material behavior changes no longer share the same version heading.

Behavior updates:

- Added `/sources/seed/` as the recommended source-of-truth scaffold location for seed resumes, comprehensive resumes, master CVs, LinkedIn exports, cover letters, portfolio summaries, achievement lists, and similar career evidence.
- Added Provisional Resume / CV Mode for using seed resumes and CVs while verified COMPASS Intake records are incomplete.
- Clarified that seed artifacts are seed, provisional, evidence, and not canonical.
- Clarified that verified Intake claim ledgers, do-not-claim ledgers, and canonical career records supersede seed artifacts for downstream authority.
- Distinguished shortened or tailored resumes from comprehensive resumes and master CVs as provisional baselines.
- Updated Source Rebase so missing seed scaffold paths may be created only in approved `create-missing-only` mode, without moving, renaming, overwriting, or normalizing existing user-owned source files.
- Added seed scaffold templates and a fictional seed artifact manifest example.
- Advanced the active framework identifier to `vNext 2026-05.8` to distinguish Initial Seed Artifact behavior from the Staff / Principal positioning release.

## vNext 2026-05.7 - Staff / Principal Positioning and Claim-Depth-Aware Resume Language

Added explicit downstream resume rules for senior individual-contributor positioning without changing Source of Truth authority or claim-depth boundaries.

Behavior updates:

- Added Staff / Principal evidence-prioritization rules so verified architecture ownership, technical direction, cross-team influence, organizational leverage, operational accountability, mentoring or enablement, and hands-on implementation are surfaced before lower-signal detail.
- Clarified that official employment titles must remain intact and operating level must be communicated through verified evidence rather than title inflation.
- Added a non-exhaustive claim-depth-aware wording map for Awareness, Exposure, Supported, Implemented, Owned, and Led others.
- Clarified that the wording map is not a mechanical verb-replacement system and that mixed-depth claims must preserve separate architecture, implementation, ownership, leadership, and formal-management boundaries.
- Added TruthGuard checks preventing Supported from becoming Owned or Led, Implemented from implying architecture ownership, Owned from implying people leadership, and Led others from implying sole contribution.
- Added explicit handling for shared ownership, initial leadership followed by transition, Technical Product Owner and primary-technical-contact context, mentoring without formal management, and formal management outside conventional engineering titles.
- Recognized evidence-grounded qualitative consequences as valid impact while preserving the prohibition on invented numerical metrics and unsupported realized outcomes.
- Added bullet-construction guidance around problem, action or decision, technical mechanism, scope or stakeholders, and consequence without forcing every bullet into a rigid formula.
- Added a technical-density and architecture-taxonomy review to preserve useful technical depth while consolidating repeated pattern inventories that obscure the candidate's actual contribution.
- Updated `COMPASS_Current.md` and `VERSION.md` to surface the active behavior.

## vNext 2026-05.6 - Intake Materiality Gate

Added a durable Materiality Gate to COMPASS Intake without changing the active framework version identifier.

Behavior updates:

- Added a Materiality Gate to `rules/07-compass-intake.md` so Intake inspects approved ledgers, do-not-claim records, coverage registers, checkpoint records, canonical source records, and relevant source artifacts before asking questions.
- Clarified that Intake should ask only unresolved material questions whose answers would change source-of-truth construction, claim approval, claim depth, evidence requirements, metrics, scope, contradictions, or downstream-safe wording.
- Preserved the 3-5 question rule as a pacing throttle, not a logic gate or total question limit.
- Clarified that Intake may proceed without questions when context is sufficient, while stating the source basis and safe assumptions.
- Updated the Intake launcher and checkpoint templates to record why questions were asked, not asked, resolved from sources, deferred, or escalated as conflicts or gaps.
- Preserved imported artifacts as evidence leads, not automatic truth, and preserved approved claim ledger, do-not-claim, coverage register, checkpoint, and storage-honesty behavior.

## vNext 2026-05.6 - COMPASS Source Rebase

Added `COMPASS Source Rebase` as a first-class safe scaffold-alignment command.

Behavior updates:

- Added `rules/09-source-rebase.md` as the durable rule for dry-run and create-missing-only source-of-truth scaffold alignment.
- Added `prompts/compass-source-rebase.md` as the launcher prompt.
- Added framework-owned source-of-truth scaffold templates under `templates/source-of-truth-scaffold/`.
- Added a generic Source Rebase report example.
- Bumped the active framework version from `vNext 2026-05.5` to `vNext 2026-05.6` because the new command materially changes framework behavior.
- Clarified that existing user-owned source-of-truth files always win over framework scaffold templates.
- Clarified that historical checkpoints, including `COMPASS_Layer0_*` paths, are preserved and not renamed.
- Clarified that Source Rebase is not COMPASS Intake and must not verify, extract, reconcile, approve, reject, overwrite, delete, rename, move, or modify source records.

## vNext 2026-05.5 - Human Authenticity Artifact Rules

Added Human Authenticity behavior for external career artifacts without changing the active framework version identifier.

Behavior updates:

- Added `rules/08-human-authenticity.md` as the durable rule for truthful, specific, natural, reviewer-readable, ATS-safe, and interview-defensible external artifacts.
- Integrated Human Authenticity with operating principles, resume generation, cover letter generation, artifact rules, and TruthGuard.
- Updated external artifact prompt launchers and command required-file lists to load the new rule.
- Clarified that AI-assisted drafting is allowed only for clarity, organization, role alignment, concision, reviewer readability, and truthful presentation of verified or source-backed experience.
- Prohibited fake humanization, hidden formatting tricks, unsupported claim smoothing, and AI-detector evasion tactics.

## vNext 2026-05.5 - Intake Artifact Templates

Made COMPASS Intake checkpoint artifact output more concrete without changing the active framework version identifier.

Behavior updates:

- Added stable Intake artifact template requirements for checkpoint records, claim-ledger entries, do-not-claim entries, coverage-register entries, storage-status blocks, and optional ZIP bundle manifests.
- Added `examples/compass-intake-artifact-templates.md` with copy-ready generic skeletons.
- Updated the checkpoint example to include coverage-register output and datastore visibility status.
- Clarified that prompts should reference the reusable template pack while `rules/07-compass-intake.md` remains the durable policy source.

## vNext 2026-05.5 - Command Registry

Added `COMPASS_COMMANDS.md` as the canonical user-facing command registry.

Behavior updates:

- Documented current first-class COMPASS commands: Intake, Analysis, Tailored Resume, Recruiter-Targeted Resume, and Cover Letter.
- Clarified supported artifact requests that are governed by artifact rules but do not yet have first-class launcher prompts.
- Clarified that `COMPASS Charter` is not currently an active first-class command unless explicitly added later with supporting prompt/rule files.
- Updated `README.md` to surface the command registry and active command list.

## vNext 2026-05.5 - Intake Coverage Gate and Artifact Supersession

Clarified COMPASS Intake coverage requirements and downstream source authority without changing the active framework version identifier.

Behavior updates:

- Imported resumes, CVs, LinkedIn profiles, cover letters, portfolio examples, recruiter resumes, and prior generated artifacts are evidence inputs and provenance records, not permanent factual authorities.
- After material claims are ingested, reconciled, and verified, the canonical source-of-truth record and approved ledgers supersede the imported artifact for downstream use.
- Intake must treat 3-5 questions as a per-response or per-batch pacing rule, not a per-role, per-artifact, or total Intake limit.
- A role, project, artifact, or source file is not Intake-complete until material imported claims are captured in coverage metadata and resolved into an approved, narrowed, rejected, evidence-needed, metric-needed, scope-needed, deferred, or excluded status.
- Checkpoints are progress commits, not proof of full source coverage.
