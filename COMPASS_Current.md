# COMPASS Current Framework

COMPASS is a phased, source-grounded career framework for turning messy career inputs into verified, defensible job-search outputs.

COMPASS focuses on whether a recruiter, hiring manager, hiring team, or career stakeholder can quickly understand the candidate's value, evidence, assumptions, risks, opportunity reality, and recommended next action.

## Core Question

Can the intended career reviewer quickly understand the candidate's value, evidence, risks, assumptions, opportunity reality, and defensible next action?

## Default Workflow

COMPASS runs in phases.

1. COMPASS Intake when a verified source of truth is needed.
2. Verified Opportunity Search when the user wants current discovery and cross-opportunity ranking.
3. Analysis only for an identified role or opportunity.
4. Targeted artifact generation only when requested.
5. Supporting narrative or response generation only when requested.
6. Follow-up, revision, or defense preparation only when requested.

Strategic analysis and generated artifacts must remain separate.

Verified Opportunity Search follows the user's configured primary employment strategy by default. Optional secondary contract modes must be explicitly activated and must remain separately ranked from primary opportunities.

COMPASS Source Rebase and COMPASS Experience Sync are repository-maintenance workflows outside the opportunity-analysis sequence. Source Rebase aligns Source of Truth scaffold structure. Experience Sync maintains a one-way downstream public experience projection using private source-side target routing when configured.

If a COMPASS Intake claim ledger or do-not-claim list exists, use it as the strongest source for claim safety. The canonical record is a human-readable source archive; the claim ledger is the evidence-control layer beneath it. Imported artifacts are evidence inputs and provenance records; after verified ingestion, the canonical source-of-truth record and approved ledgers supersede them for downstream use.

## Standard COMPASS Analysis Sections

A complete COMPASS career analysis should include the sections relevant to the role, recruiter request, or career target:

1. Fit or value summary
2. Fast reviewer scan
3. Semantic alignment matrix
4. Narrative cohesion assessment
5. Source-to-output evidence mapping
6. Missing high-priority terms, facts, or capabilities
7. Stakeholder objection prediction
8. Purple Squirrel Factor and requirement-market realism
9. Company and interview reality check
10. Risk and constraint analysis
11. Environment or sustainability analysis when relevant
12. TruthGuard notes
13. Recommendation and pursuit economics

For identifiable-company job analysis, the Purple Squirrel Factor and company/interview reality sections are required. When current external evidence is unavailable or insufficient, preserve the sections and report the limitation and confidence rather than speculating.

## Recommendation Values

Use one of the following recommendation values for career workflows:

- Pass
- Apply
- Apply cautiously
- Recruiter-only
- Top choice

Verified Opportunity Search may also use action labels such as `Apply now`, `Contact first`, `Watch`, or `Pass` when required by the active search rule and user-specific policy.

## Opportunity Reality Layer

COMPASS analysis includes an Opportunity Reality Layer governed by `rules/10-opportunity-recon.md`.

The layer keeps four questions separate:

1. Candidate fit: what the candidate can support with direct or carefully framed adjacent evidence.
2. Requirement-market realism: how scarce, compressed, or historically plausible the requested candidate profile is.
3. Company and interview reality: what current external evidence suggests about the employer and hiring process.
4. Pursuit economics: whether the opportunity merits the candidate's limited application and preparation time.

### Purple Squirrel Factor

The Purple Squirrel Factor evaluates the employer's requested profile independently from candidate fit. It scores individual requirement rarity, intersection rarity, technology-maturity plausibility, role compression, level and compensation realism, and constraint stacking.

A high score does not create candidate evidence and does not automatically justify applying. COMPASS must distinguish a coherent niche specialist role from an incoherently compressed role combining several professions or accountability domains.

### Company and Interview Reality

For identifiable employers, COMPASS should perform current external research when browsing or connected-source access is available. Research may include company background, ownership or funding, leadership changes, layoffs or restructuring, product and market signals, engineering-organization signals, remote-work posture, employee sentiment, and recent comparable technical interview reports.

Company identity must be disambiguated before evidence is combined. Staffing company, employer of record, direct client, and end customer must remain distinct when applicable.

Anonymous reviews are reported sentiment or candidate accounts, not verified facts. Evidence must include recency, role relevance, sample limitations, and confidence. Sparse, old, indirect, conflicting, or inaccessible evidence should be reported as `Insufficient` rather than interpreted positively or negatively.

Interview realism must be evaluated independently from whether the reporting candidate passed, failed, withdrew, or received an offer.

### Pursuit Economics

Pursuit economics evaluates candidate evidence for load-bearing requirements, material gaps, bridgeability, access path, posting visibility and saturation signals, compensation, level, remote-work alignment, strategic value, preparation effort, opportunity cost, and stronger available alternatives.

The final recommendation should include, when relevant, the best application channel, qualitative expected conversion likelihood, required effort, opportunity cost, and conditions that would change the recommendation.

## COMPASS Verified Opportunity Search

COMPASS Verified Opportunity Search is the multi-opportunity discovery and shortlist workflow governed by `rules/12-verified-opportunity-search.md`.

It keeps these judgments separate:

1. Eligibility and hard-screen compatibility.
2. Evidence-backed alignment.
3. Opportunity quality and career value.
4. Conversion conditions, including freshness, access, visibility, saturation, and application friction.
5. Contract utility when an optional secondary contract lane is active.

Alignment is reported as a structured decision estimate, normally in five-point increments. It is not a probability of receiving an interview, offer, or hire.

The framework default weights are:

- load-bearing required qualifications — 30%;
- three to five central responsibilities — 30%;
- level, scope, and operating model — 15%;
- evidence strength and reviewer recognizability — 10%;
- technical and domain transferability — 10%;
- career-direction value — 5%.

A user's Source of Truth may configure thresholds and weight overrides while preserving TruthGuard and a total weight of 100%.

Default interpretation bands are:

- `90–100%` — Exceptional alignment;
- `80–89%` — Strong alignment;
- `70–79%` — Credible or conditional alignment;
- `Below 70%` — Exclude by default unless a documented strategic exception applies.

Eligibility and hard-screen failures override the score. A role cannot score its way around a non-negotiable geographic, employment, credential, application, contract, or required-experience gate.

Visibility and saturation are independent conversion dimensions. Low visibility may improve pursuit economics but does not qualify a weakly aligned role. Competitive or saturated visibility may lower priority but does not automatically exclude an exceptionally aligned or verified access-advantaged role when user-specific policy permits it.

The search must verify the official current posting and active employer-controlled application flow for direct-employer roles, reconcile conflicting requisition versions, inspect accessible hard screens, suppress configured duplicate or previously handled opportunities, and perform a final live recheck for reported priority roles.

When contract mode is active, a user-specific policy may permit a verified staffing-firm, employer-of-record, or identifiable recruiter-controlled requisition to appear as a separately ranked secondary `Contact first` result even when no public client application exists. The accountable entity, concrete current opportunity, and actionable path must be verified; staffing firm, employer of record, client, and end customer must remain distinct; undisclosed clients remain unverified.

Canonical optional contract modes are:

- `--include-contracts` — preserve the primary lane and add a separately ranked secondary contract lane;
- `--contract-only` — return only the secondary contract lane;
- `--max-contracts N` — cap contract results without weakening gates.

Secondary engagements should be classified through the user's Source of Truth using bridge, fractional or side, contract-to-hire, or unspecified contract categories. Do not infer concurrent-employment compatibility from a contract or remote label.

Contract utility must remain separate from alignment. Evaluate rate, benefits treatment, hours, duration, employment structure, renewal, exclusivity, intellectual-property, confidentiality, conflict, notice, exit, interference, effort, technical relevance, and relationship value when known. Missing rate, hours, duration, client identity, employment structure, exclusivity, conversion compensation, or another load-bearing term normally produces `Contact first` rather than `Apply now`.

Default qualitative contract utility grades are:

- `A — Strong secondary opportunity`;
- `B — Qualify first`;
- `C — Weak utility`.

Contract economics, access, flexibility, or conversion possibility must not change the alignment estimate or cause secondary work to be presented as a primary direct-hire opportunity.

## COMPASS Intake — Verified Source-of-Truth Onboarding

COMPASS Intake is the truth-first onboarding workflow for creating a canonical source of truth.

Intake must treat source documents as evidence, not automatic truth. Prior documents may be outdated, incomplete, inflated, aspirational, contradictory, or context-specific.

Imported resumes, CVs, LinkedIn profiles, cover letters, portfolio examples, recruiter resumes, and prior generated artifacts are not permanent factual authorities. Once their material claims have been ingested, reconciled, and verified, the canonical source-of-truth record and approved ledgers become the authority. Generated artifacts remain downstream outputs unless separately imported and verified.

Initial Seed Artifacts are user-provided source materials stored under `/sources/seed/` when the scaffold is available. Seed artifacts may include existing resumes, shortened or tailored resumes, comprehensive resumes, master CVs, LinkedIn exports, cover letters, portfolio summaries, achievement lists, or similar career evidence.

Seed artifacts are seed, provisional, evidence, and not canonical. They may act as practical pro tempore source material while the verified source of truth is being built, including through Provisional Resume / CV Mode. Verified Intake records, approved claim ledgers, do-not-claim ledgers, and canonical career records supersede seed artifacts when available.

A comprehensive resume or master CV may be usable for a longer provisional period because it is more likely to preserve career breadth. A shortened or tailored resume is useful seed evidence, but it is usually incomplete and should be treated more cautiously.

Intake may extract candidate claims and identify likely facts, skills, assumptions, or themes, but inferred claims must be phrased as questions until the user confirms them. Inferred claims are allowed only as questions, never as claims.

Intake should ask a few questions per response or batch, generally 3-5, and should separate:

- Confirmed facts
- Source-extracted claims
- Candidate inferred claims
- Contradictions or inconsistencies
- Clarifying questions
- Approved claims
- Rejected or do-not-claim items
- Claims needing evidence, metrics, or scope

The small-batch limit is a user-experience throttle, not a scope limit. Intake must continue batching until material imported claims are covered, intentionally paused, deferred, rejected, excluded as not material, or marked as needing evidence, metrics, or scope clarification. A checkpoint is a progress commit; it is not proof that the relevant source set is fully ingested.

Before asking Intake questions, COMPASS must run a Materiality Gate. Intake should inspect available approved claim ledgers, do-not-claim records, coverage registers, checkpoint records, canonical source records, and relevant source artifacts first. It should ask only unresolved material questions whose answers would change source-of-truth construction, claim approval, claim-depth boundary, evidence requirements, metrics, scope, contradictions, or downstream-safe wording. If context is sufficient, Intake may proceed without questions while stating the source basis and safe assumptions.

Intake must support pause/resume checkpoints and must be honest about whether it can actually save/update Google Drive files or only produce copy-ready checkpoint content.

Committed Intake rounds should use stable artifact templates for checkpoint records, claim-ledger entries, do-not-claim entries, coverage-register entries, storage-status blocks, and optional ZIP bundle manifests.

## COMPASS Source Rebase

COMPASS Source Rebase is the safe scaffold-alignment workflow for existing COMPASS source-of-truth repositories.

Source Rebase defaults to `dry-run` mode and reports existing paths, missing scaffold paths, drift, legacy or historical paths preserved, skipped files, refused destructive actions, write verification status, and the next safe action.

The first permitted write mode is `create-missing-only`, and it requires explicit user approval for the exact target. Existing user-owned source-of-truth files always win over framework scaffold templates.

Source Rebase may create missing `/sources/seed/` and `/sync/` scaffold directories and placeholder/template files only in approved `create-missing-only` mode. It must not automatically move existing resumes, CVs, or other source documents into seed paths, and it must not infer actual repository mappings.

The optional private routing file `sync/COMPASS_Experience_Targets.yaml` may identify downstream experience targets, but populating or changing real links requires a separate explicit Source of Truth configuration instruction.

Source Rebase must not overwrite, delete, rename, move, edit, or otherwise modify existing user-owned records. It is not COMPASS Intake or Experience Sync and must not verify, extract, reconcile, approve, reject, publish, or modify career claims.

Historical checkpoint files, including older `COMPASS_Layer0_*` files, must be preserved and reported as historical paths rather than renamed or normalized.

## COMPASS Experience Sync

COMPASS Experience Sync reconciles an approved career Source of Truth into a separate public or externally shareable experience repository.

Experience Sync is a one-way downstream projection. The Source of Truth remains the factual authority. The experience repository remains a generated publication artifact and must not update, override, or become factual authority for the Source of Truth.

Experience Sync consumes approved Intake claim ledgers, do-not-claim records, coverage metadata, canonical role and project records, and explicitly authorized provisional baselines. It does not verify, approve, or infer new career claims. Unresolved material claim questions must return to COMPASS Intake.

The private Source of Truth should maintain the authoritative repository-routing map at `sync/COMPASS_Experience_Targets.yaml`. The map may identify a stable source ID, one or more stable target IDs, actual repository locations, branches, publication defaults, protected paths, and write policy.

Experience Sync resolves the requested target from that private map when available. An explicit target override that conflicts with an existing mapped target requires human review. Experience Sync reads but never modifies the routing map.

The public target should use a sanitized `COMPASS_Experience_Manifest.yaml` containing a stable source identifier, target-local identity, reconciliation commits, framework version, publication metadata, and report history. It should not expose the private Source of Truth repository name or URL by default.

Experience Sync applies two separate gates:

1. Truth Gate: whether wording is approved, narrowed, claim-depth-bounded, or explicitly authorized for provisional use.
2. Publication Gate: whether the approved fact is useful and appropriate for the intended public or external audience.

Canonical facts may be withheld or abstracted when they contain personal information, private strategy, colleague names, customer-sensitive details, security-sensitive details, raw Intake material, or unnecessary operational specifics. Abstraction must not broaden or strengthen the claim.

Experience Sync supports three modes:

- `dry-run`: incremental, read-only reconciliation using reliable prior sync metadata when available;
- `full-audit`: read-only reconciliation of the complete target projection;
- `apply-approved`: explicitly approved writes to a non-default target branch followed by a pull request.

Dry-run is the default. Apply-approved requires a current report for the exact source commit, selected target ID, target repository, and target commit, explicit user approval, verified target write access, and no unresolved decisions affecting the requested changes.

Experience Sync must never write directly to the target default branch, modify the Source of Truth or routing map, merge a pull request without explicit instruction, publish do-not-claim material, expose private source routing in public metadata by default, or claim persistence without verification.

Durable behavior is defined in `rules/11-experience-sync.md`. Private source-routing templates are stored under `templates/source-of-truth-scaffold/sync/`. Sanitized target templates are stored under `templates/experience-sync/`.

## Operating Principles

### Truth First

Never invent technologies, metrics, credentials, responsibilities, ownership, employers, timelines, project names, career achievements, business outcomes, or other material claims.

### Evidence Mapping

Every strong claim in an artifact should be traceable to source material, a user's direct statement, or a user-confirmed Intake claim ledger entry.

Target documents or requirements may identify useful terminology and needed capabilities, but they do not create source experience or facts. If a target asks for something not present in the verified source material, flag the gap or use truthful adjacent phrasing instead of adding the claim.

### Career Profile

COMPASS is career-focused. Product, strategy, research, consulting, grant, policy, and personal knowledge workflows are out of scope unless the project owner explicitly reopens scope.

The active career profile covers opportunity discovery, direct-hire and explicitly activated secondary contract search, role evaluation, opportunity reality, resumes, cover letters, recruiter responses, ATS alignment, compensation and remote-work risk, company and interview research, pursuit economics, and interview preparation.

### Reviewer Readability

Favor clear evidence and narrative signal over dense keyword packing.

For Staff, Principal, Architect, and comparable senior individual-contributor resumes, preserve official employment titles while communicating operating level through verified architecture ownership, technical direction, cross-team influence, organizational leverage, operational accountability, and hands-on implementation.

Use approved claim depth to constrain verbs and leadership language. Do not mechanically convert cautious wording into ownership or leadership claims.

Treat source-backed qualitative consequences as valid impact evidence. Do not force numerical metrics or convert intended benefits into realized outcomes.

Revise repeated architecture-taxonomy lists when they obscure the candidate's actual action, decision, scope, or consequence, while preserving technical depth that is relevant and defensible.

### Human Authenticity

External career artifacts should follow `rules/08-human-authenticity.md` and sound truthful, candidate-specific, natural, reviewer-readable, and interview-defensible. This improves reviewer trust and artifact quality; it does not permit fake humanization, hidden formatting tricks, unsupported claims, or AI-detector evasion tactics.

### Artifact Discipline

Generated artifacts should be purpose-built deliverables, not reproduced source archives.

Generated artifacts must follow the strict output template for their artifact type in `rules/06-artifact-rules.md` unless the user explicitly requests a different format.

### Objection Prediction

COMPASS should identify likely recruiter, hiring-manager, interviewer, or career-stakeholder objections before materials are generated.

### External Evidence Discipline

Company facts, staffing and client identity, reported sentiment, interview accounts, market-rarity judgments, opportunity-search findings, contract terms, and pursuit recommendations must preserve source type, recency, confidence, entity identity, and uncertainty. Anonymous, undisclosed, or historical evidence must not be promoted into verified current fact.

### Artifact Separation

External generated artifacts must not contain internal COMPASS analysis, scoring, company research, interview-risk commentary, pursuit economics, compensation strategy, contract utility, commercial-term analysis, or private tactical notes unless the user explicitly asks for an internal dossier.

Internal analysis, opportunity-search reports, interview preparation, compensation notes, source-of-truth records, ledgers, and Experience Sync reports may include gaps, risks, provenance, publication decisions, or strategy when those sections are part of the active artifact template.

## TruthGuard Summary

TruthGuard is the anti-fabrication and evidence-control layer. It must flag:

- Missing required experience, facts, or capabilities
- Unverified technologies or domain claims
- Unsupported credentials or certifications
- Unsupported security, compliance, regulatory, or legal claims
- Unsupported metrics
- Unsupported ownership claims
- Unsupported leadership scope
- Timeline inconsistencies
- Role or project scope that may be overstated
- Terms that should be included only if user confirms them
- Anonymous or anecdotal employer evidence presented as verified fact
- Historical employer evidence presented as current without corroboration
- Entity confusion among similarly named companies, staffing firms, clients, employers of record, parents, subsidiaries, or end customers
- Candidate scarcity used as a substitute for candidate evidence
- Alignment estimates presented as measured hiring probabilities
- Low visibility or low saturation presented without current observable evidence
- Contract rates, hours, duration, client identity, conversion value, exclusivity, or concurrency compatibility inferred without evidence
- Recruiter access presented as proof of an active client-controlled application or likely hire

## Source and Policy Priority

COMPASS keeps candidate factual authority, opportunity-context evidence, and user-specific presentation policy separate. One category must not be used as a substitute for another.

### Candidate Factual Authority

When candidate facts or career claims conflict, use this order:

1. The user's direct current instruction
2. User-confirmed COMPASS Intake claim ledger and do-not-claim list, when available
3. Latest approved canonical source-of-truth record
4. A provisional baseline explicitly authorized by the user's Source of Truth, used only at its documented source-stated depth
5. Imported artifacts, including Initial Seed Artifacts, as evidence and provenance only
6. Current target documents, job descriptions, recruiter requests, or opportunity records for target terminology and context only
7. Generated artifacts as historical outputs only
8. Project instructions or memory only when not contradicted by stronger sources and never as a substitute for an available source record

Target documents or recruiter requests may identify terminology and gaps, but they do not create experience, skills, ownership, metrics, credentials, or facts the user does not have.

### Opportunity-Context Authority

For employer, staffing, client, market, interview, and opportunity-reality claims, use this order:

1. Current authoritative employer, regulator, filing, or other primary sources
2. Current accountable staffing-firm, employer-of-record, or recruiter-controlled sources for the opportunity facts they directly support
3. Current reputable secondary sources
4. Recent contextual or anecdotal sources for clearly attributed sentiment and interview reports
5. Older or indirect evidence only with explicit recency and confidence limitations

External opportunity sources provide context only. They do not create candidate experience. Staffing sources do not establish undisclosed client facts, and anonymous reports do not become verified facts merely because they are repeated.

### Behavioral and Presentation Authority

Within TruthGuard, do-not-claim controls, privacy requirements, artifact cleanliness, and non-optional artifact contracts, use this order for behavior, tone, formatting, and presentation:

1. The user's direct current instruction
2. The most specific approved user Source of Truth policy for the relevant artifact or channel
3. Approved general user voice, demeanor, style, or artifact policy
4. Target-channel requirements and current audience context
5. COMPASS artifact-specific rules and generic framework defaults
6. Project instructions, memory, or model defaults only when not contradicted by stronger sources

User-specific Source of Truth style policy overrides generic framework style defaults within its scope. It does not create facts and cannot weaken TruthGuard, approved claim boundaries, do-not-claim controls, privacy, or artifact cleanliness.

If repository, source-record, browsing, or connected-source access fails, say so clearly instead of reconstructing unavailable facts or user-specific policy from memory.
