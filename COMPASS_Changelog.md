# COMPASS Changelog

All notable framework changes should be documented here.

## vNext 2026-06.3 - COMPASS Verified Opportunity Search

Added a first-class multi-opportunity discovery and shortlist workflow centered on evidence-backed alignment rather than hiddenness alone.

Behavior updates:

- Added `rules/12-verified-opportunity-search.md` as the durable rule for current-opportunity discovery, live-posting verification, requisition reconciliation, ordered eligibility and hard-screen gates, alignment scoring, opportunity-quality review, conversion-condition ranking, application-stage inspection, and duplicate suppression.
- Added `prompts/compass-verified-opportunity-search.md` as the reusable launcher prompt.
- Added `COMPASS Verified Opportunity Search` to `COMPASS_COMMANDS.md` with required framework and user-specific source inputs.
- Separated eligibility and hard screens, evidence-backed alignment, opportunity quality, and conversion conditions so one dimension cannot silently substitute for another.
- Added a default alignment model weighted across load-bearing qualifications, central responsibilities, level and operating scope, evidence recognizability, transferability, and career-direction value.
- Required alignment estimates to use decision bands and ordinary five-point increments rather than false precision or implied interview probability.
- Clarified that a hard eligibility or application-screen failure overrides an otherwise high alignment score.
- Reclassified freshness, access, visibility, saturation, and application friction as conversion conditions and ranking factors rather than universal fit gates.
- Clarified that low visibility cannot qualify a weakly aligned role and that mainstream visibility does not automatically exclude an exceptionally aligned or access-advantaged role when user-specific policy permits it.
- Added untrusted-external-content controls for job descriptions, ATS pages, application forms, recruiter posts, HTML, and metadata.
- Required current employer-controlled job and application verification, conflict reconciliation, application-stage visibility disclosure, and an immediate final recheck for reported priority roles.
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
- Required actual source and target links, target IDs, branches, publication defaults, protected paths, and write policy to live in the Source of Truth routing map rather than the public target manifest.
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