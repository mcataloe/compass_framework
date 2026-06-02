# COMPASS Current Framework

COMPASS is a phased, source-grounded career framework for turning messy career inputs into verified, defensible job-search outputs.

COMPASS focuses on whether a recruiter, hiring manager, hiring team, or career stakeholder can quickly understand the candidate's value, evidence, assumptions, risks, and recommended next action.

## Core Question

Can the intended career reviewer quickly understand the candidate's value, evidence, risks, assumptions, and defensible next action?

## Default Workflow

COMPASS runs in phases.

1. COMPASS Intake when a verified source of truth is needed
2. Analysis only
3. Targeted artifact generation only when requested
4. Supporting narrative or response generation only when requested
5. Follow-up, revision, or defense preparation only when requested

Strategic analysis and generated artifacts must remain separate.

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
8. Risk and constraint analysis
9. Environment or sustainability analysis when relevant
10. TruthGuard notes
11. Recommendation

## Recommendation Values

Use one of the following recommendation values for career workflows:

- Pass
- Apply
- Apply cautiously
- Recruiter-only
- Top choice

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

Intake must support pause/resume checkpoints and must be honest about whether it can actually save/update Google Drive files or only produce copy-ready checkpoint content.

Committed Intake rounds should use stable artifact templates for checkpoint records, claim-ledger entries, do-not-claim entries, coverage-register entries, storage-status blocks, and optional ZIP bundle manifests.

## COMPASS Source Rebase

COMPASS Source Rebase is the safe scaffold-alignment workflow for existing COMPASS source-of-truth repositories.

Source Rebase defaults to `dry-run` mode and reports existing paths, missing scaffold paths, drift, legacy or historical paths preserved, skipped files, refused destructive actions, write verification status, and the next safe action.

The first permitted write mode is `create-missing-only`, and it requires explicit user approval for the exact target. Existing user-owned source-of-truth files always win over framework scaffold templates.

Source Rebase may create missing `/sources/seed/` scaffold directories and placeholder/template files only in approved `create-missing-only` mode. It must not automatically move existing resumes, CVs, or other source documents into seed paths.

Source Rebase must not overwrite, delete, rename, move, edit, or otherwise modify existing user-owned records. It is not COMPASS Intake and must not verify, extract, reconcile, approve, reject, or modify career claims.

Historical checkpoint files, including older `COMPASS_Layer0_*` files, must be preserved and reported as historical paths rather than renamed or normalized.

## Operating Principles

### Truth First

Never invent technologies, metrics, credentials, responsibilities, ownership, employers, timelines, project names, career achievements, business outcomes, or other material claims.

### Evidence Mapping

Every strong claim in an artifact should be traceable to source material, a user's direct statement, or a user-confirmed Intake claim ledger entry.

Target documents or requirements may identify useful terminology and needed capabilities, but they do not create source experience or facts. If a target asks for something not present in the verified source material, flag the gap or use truthful adjacent phrasing instead of adding the claim.

### Career Profile

COMPASS is career-focused. Product, strategy, research, consulting, grant, policy, and personal knowledge workflows are out of scope unless the project owner explicitly reopens scope.

The active career profile covers role evaluation, resumes, cover letters, recruiter responses, ATS alignment, compensation and remote-work risk, and interview preparation.

### Reviewer Readability

Favor clear evidence and narrative signal over dense keyword packing.

### Human Authenticity

External career artifacts should follow `rules/08-human-authenticity.md` and sound truthful, candidate-specific, natural, reviewer-readable, and interview-defensible. This improves reviewer trust and artifact quality; it does not permit fake humanization, hidden formatting tricks, unsupported claims, or AI-detector evasion tactics.

### Artifact Discipline

Generated artifacts should be purpose-built deliverables, not reproduced source archives.

Generated artifacts must follow the strict output template for their artifact type in `rules/06-artifact-rules.md` unless the user explicitly requests a different format.

### Objection Prediction

COMPASS should identify likely recruiter, hiring-manager, interviewer, or career-stakeholder objections before materials are generated.

### Artifact Separation

External generated artifacts must not contain internal COMPASS analysis, scoring, risk commentary, compensation strategy, or private tactical notes unless the user explicitly asks for an internal dossier.

Internal analysis, interview preparation, compensation notes, source-of-truth records, and ledgers may include gaps, risks, or strategy when those sections are part of the active artifact template.

## TruthGuard Summary

TruthGuard is the anti-fabrication layer. It must flag:

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

## Source Priority

When sources conflict, use this priority order:

1. User's direct current instruction
2. User-confirmed Intake claim ledger and do-not-claim list, when available
3. Latest approved canonical source-of-truth record
4. Imported artifacts, including Initial Seed Artifacts, as evidence and provenance only
5. Current target document, job description, recruiter request, or opportunity record for target context and terminology only
6. Generated artifacts as historical outputs only
7. COMPASS repository rules and framework defaults
8. Project instructions and memory only when not contradicted by stronger sources

Target documents or recruiter requests may identify terminology and gaps, but they do not create experience, skills, ownership, metrics, credentials, or facts the user does not have.

If repository or source-record access fails, say so clearly instead of reconstructing unavailable facts from memory.
