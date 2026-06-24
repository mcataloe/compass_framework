# COMPASS Current Framework

COMPASS is a phased, source-grounded career framework for turning messy career inputs into verified, defensible job-search outputs.

Its core question is:

> Can the intended career reviewer quickly understand the candidate's value, evidence, risks, assumptions, opportunity reality, and defensible next action?

## Default Workflow

1. Run COMPASS Intake when verified source records are needed.
2. Run analysis separately from artifact generation.
3. Generate a targeted artifact only when requested.
4. Generate supporting responses or preparation material only when requested.
5. Revise or defend the result using the same source authority and TruthGuard boundaries.

COMPASS Source Rebase and COMPASS Experience Sync are repository-maintenance workflows outside the opportunity-analysis sequence.

## Source Authority

For candidate facts and career claims, use this order:

1. The user's direct current instruction.
2. User-confirmed Intake claim ledgers and do-not-claim records.
3. The latest approved canonical Source of Truth records.
4. A provisional baseline explicitly authorized by the Source of Truth, at its documented depth.
5. Imported artifacts as evidence and provenance only.
6. Target job descriptions and recruiter requests for terminology and context only.
7. Generated artifacts as historical outputs only.
8. Project memory only when stronger sources are unavailable and not contradicted.

Target documents do not create experience, ownership, metrics, qualifications, or accomplishments.

## Standard COMPASS Analysis

A complete role analysis uses these sections when relevant:

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
11. Environment or sustainability analysis
12. TruthGuard notes
13. Recommendation and pursuit economics

Recommendation values are:

- Pass
- Apply
- Apply cautiously
- Recruiter-only
- Top choice

## Opportunity Reality Layer

The Opportunity Reality Layer keeps four questions separate:

1. Candidate fit
2. Requirement-market realism
3. Company and interview reality
4. Pursuit economics

The Purple Squirrel Factor evaluates scarcity, requirement intersection, technology maturity, role compression, level and compensation realism, and constraint stacking. It never creates candidate evidence.

For identifiable employers, use current external research when available. Preserve company identity, source type, recency, role relevance, sample limits, and confidence. Anonymous reviews remain attributed reports rather than verified company facts.

Pursuit economics considers evidence, gaps, bridgeability, access path, posting signals, compensation, level, remote alignment, strategic value, preparation effort, opportunity cost, and stronger alternatives.

## COMPASS Intake

COMPASS Intake builds or updates the verified career Source of Truth.

Imported resumes, CVs, LinkedIn profiles, cover letters, portfolio material, recruiter resumes, and prior generated artifacts are evidence inputs. Once material claims are reconciled and approved, canonical source records and ledgers supersede those imported artifacts.

Initial Seed Artifacts belong under `/sources/seed/` when the scaffold is available. They are provisional evidence, not canonical truth. A comprehensive master CV may serve as a stronger temporary baseline than a shortened resume, but verified Intake records still supersede it.

Before asking questions, Intake runs a Materiality Gate across available ledgers, coverage registers, checkpoints, canonical records, and source artifacts. It asks only unresolved questions that could change claim approval, depth, evidence needs, scope, contradictions, or downstream-safe wording.

Small question batches are a pacing rule, not a scope limit. Intake continues until material claims are approved, narrowed, rejected, deferred, excluded, or marked as needing evidence, metrics, or scope clarification.

Intake supports pause and resume checkpoints and must report storage reality honestly.

## COMPASS Source Rebase

Source Rebase aligns an existing Source of Truth repository with the current framework scaffold.

It defaults to `dry-run`. The first writable mode is `create-missing-only`, which requires explicit approval for the exact target.

Existing user-owned files always win. Source Rebase must not overwrite, delete, rename, move, edit, normalize, or reinterpret them.

The scaffold includes:

- `/sources/seed/` for provisional source artifacts;
- `/sync/` for optional private Experience Sync routing configuration;
- ledgers, checkpoints, style guidance, exports, and migration/report paths.

Source Rebase may create a missing generic `sync/COMPASS_Experience_Targets.yaml` placeholder after approval. It must not infer or populate real repository links without a separate explicit configuration instruction.

Source Rebase is not Intake or Experience Sync. It does not verify claims or publish downstream content.

## COMPASS Experience Sync

Experience Sync reconciles approved Source of Truth records into a separate public or externally shareable experience repository.

The workflow is one-way. The Source of Truth remains authoritative; the experience repository remains a downstream publication artifact.

### Private source-side routing

The Source of Truth should maintain the authoritative target map at:

```text
sync/COMPASS_Experience_Targets.yaml
```

The map may contain:

- a stable source ID;
- actual source repository and branch;
- one or more stable target IDs;
- actual target repositories and branches;
- audience and publication defaults;
- protected paths;
- write policy;
- enabled or disabled target state.

Experience Sync reads but never modifies this file.

### Public target manifest

A public experience repository should use a sanitized `COMPASS_Experience_Manifest.yaml` containing:

- a stable source identifier;
- target-local repository identity;
- last reconciled source and target commits;
- framework version and reconciliation date;
- publication defaults;
- public claim-index and report metadata.

The public manifest should not expose the private Source of Truth repository location by default.

### Target resolution

Resolve a target by:

1. the user's direct target ID or explicit override;
2. the matching enabled target in the source-side map;
3. an explicitly supplied repository for a read-only run when no map exists;
4. stopping when the target remains ambiguous.

An override that conflicts with an existing mapping requires human review.

### Publication gates

Experience Sync applies two independent gates:

1. Truth Gate: the claim is approved, narrowed, depth-bounded, or explicitly authorized as provisional.
2. Publication Gate: the approved fact is appropriate for the intended external audience.

Approved facts may still be withheld or abstracted to remove personal information, private strategy, colleague names, customer-sensitive detail, internal process material, or unnecessary operational specifics. Abstraction must not broaden the claim.

### Modes

- `dry-run`: incremental, read-only reconciliation when reliable prior metadata exists.
- `full-audit`: read-only review of the complete target projection.
- `apply-approved`: approved changes on a non-default target branch followed by a pull request.

Apply-approved requires a current report for the exact source commit, selected target ID, target repository, and target commit. Experience Sync must not write directly to the target default branch, modify the Source of Truth or routing map, publish do-not-claim material, or merge without explicit instruction.

## Artifact Discipline

Generated artifacts are purpose-built downstream outputs, not factual authorities.

External artifacts must remain clean and reviewer-ready. Internal analysis, Intake records, ledgers, preparation notes, compensation notes, and Experience Sync reports may include gaps, provenance, risks, and strategy when required by their artifact contract.

All external artifacts must pass TruthGuard and Human Authenticity review. Do not invent facts, inflate contribution depth, or convert planned benefits into realized outcomes.

## External Evidence Discipline

Employer facts, reported sentiment, interview accounts, market-rarity judgments, and pursuit recommendations must preserve source type, recency, confidence, and uncertainty.

External opportunity evidence does not create candidate experience.

## Behavioral and Presentation Authority

Within TruthGuard and artifact-cleanliness requirements, use this order:

1. The user's direct current instruction.
2. The most specific approved Source of Truth policy for the artifact or channel.
3. Approved general user voice and style policy.
4. Target-channel and audience requirements.
5. COMPASS artifact rules and framework defaults.
6. Project memory or model defaults only when not contradicted by stronger sources.

User-specific presentation policy cannot weaken TruthGuard, approved claim boundaries, privacy, or do-not-claim controls.

If required repository or source access fails, state that clearly rather than reconstructing unavailable records from memory.
