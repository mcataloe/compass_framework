# 20 — Professional Effectiveness Evidence

This rule governs how COMPASS captures, derives, matches, and surfaces non-technical professional capabilities such as critical thinking, systems thinking, judgment, communication, influence, ownership, and adaptability.

## Purpose

Employers often describe these capabilities as `soft skills`. COMPASS uses the term **professional effectiveness** because the relevant hiring signal is not personality or self-description; it is evidence that the candidate can turn technical or domain expertise into sound decisions, coordinated action, and useful outcomes.

Professional-effectiveness evidence is career evidence. It is subject to TruthGuard, claim-depth boundaries, do-not-claim controls, source priority, implementation-stage boundaries, collaborator boundaries, and current user-owned Source-of-Truth policy.

## Core Principle

Do not treat professional effectiveness as an adjective inventory.

The preferred evidence shape is:

> context or problem -> candidate action or decision -> constraint or tradeoff -> stakeholders or system boundary -> consequence or outcome

A statement such as `strong critical thinker`, `excellent communicator`, `strategic`, `resilient`, or `great collaborator` is weak evidence by itself and must not become a downstream candidate claim merely because it appears in a target job description, prior generated artifact, personality assessment, or self-description.

## Stable Capability Taxonomy

Use these candidate-neutral capability IDs when classification is useful. The taxonomy is analytical metadata, not a claim that every candidate possesses every capability.

### Cognitive and strategic

- `critical_thinking` — tests assumptions, distinguishes evidence from inference, evaluates competing explanations, and identifies reasoning defects.
- `problem_framing` — identifies the actual problem, decision, invariant, or constraint before selecting a solution.
- `systems_thinking` — reasons across dependencies, interfaces, feedback loops, second-order effects, and cross-system consequences.
- `judgment_under_ambiguity` — makes defensible decisions with incomplete or conflicting information while preserving uncertainty and risk boundaries.
- `prioritization` — allocates attention or effort according to materiality, risk, value, urgency, and opportunity cost.
- `creative_reasoning` — generates materially different viable approaches rather than optimizing only the first apparent solution.
- `learning_agility` — acquires unfamiliar domain or technical context quickly enough to make useful progress without overstating mastery.
- `business_product_judgment` — connects technical or operational choices to user value, cost, risk, delivery, policy, or organizational objectives.

### Interpersonal

- `communication` — conveys complex information accurately at the audience's required level and preserves important nuance.
- `active_listening` — incorporates stakeholder intent, constraints, or new information rather than treating communication as one-way transmission.
- `collaboration` — integrates other contributors' expertise and coordinates work across boundaries.
- `constructive_disagreement` — challenges assumptions or proposals without turning technical disagreement into interpersonal conflict.
- `stakeholder_management` — reconciles competing needs, clarifies ownership, and maintains useful alignment across affected parties.

### Leadership and leverage

- `influence_without_authority` — changes direction, adoption, or decisions through evidence, credibility, facilitation, or technical reasoning without relying on formal reporting authority.
- `technical_leadership` — establishes or guides technical direction, standards, decisions, or implementation across contributors at the verified claim depth.
- `mentoring_enablement` — improves another contributor's ability to execute through mentoring, onboarding, guidance, review, or reusable enablement.
- `decision_leadership` — creates decision clarity, frames tradeoffs, drives convergence, or owns a bounded decision process.
- `organizational_alignment` — connects multiple teams, functions, or stakeholder groups around a shared technical or delivery direction.

### Executional

- `ownership` — follows a problem or responsibility through to the relevant outcome or handoff rather than stopping at a narrow assigned task boundary.
- `adaptability` — changes approach when requirements, evidence, constraints, or technology change.
- `resilience` — continues effective execution through setbacks, uncertainty, failed approaches, or changed conditions without implying invulnerability or a personality trait.
- `reliability` — establishes predictable follow-through, operational discipline, or risk control within the supported scope.
- `ambiguity_navigation` — creates enough structure, evidence, or next-step clarity to make progress when requirements or ownership are not fully defined.

## Evidence Atom Contract

When a Source of Truth supports professional-effectiveness annotations, prefer an evidence atom with these fields or equivalent prose:

- `evidence` — the verified underlying event, action, decision, or outcome.
- `capability_signals` — one or more taxonomy IDs supported by that evidence.
- `signal_strength` — `direct`, `corroborated`, or `indicative`.
- `claim_depth` — the governing contribution depth when relevant.
- `external_use_boundary` — wording, scope, collaborator, outcome, or implementation limits that downstream artifacts must preserve.

Signal strength means:

- `direct` — one approved evidence atom plainly demonstrates the capability behavior.
- `corroborated` — multiple approved facts or episodes support the same capability pattern.
- `indicative` — the approved facts make the signal plausible enough for internal mapping or interview exploration, but not strong enough to support an external trait-style claim.

Signal strength is not a personality score, performance rating, or percentile.

## Source-of-Truth Discipline

The underlying event or behavior remains the factual authority. Capability tags are derived metadata used for retrieval and matching.

- Do not create professional-effectiveness evidence from a target job description.
- Do not create it from generic praise, a generated resume, or a prior COMPASS analysis unless the underlying behavior has been verified into the current Source of Truth.
- Do not infer formal people management from `technical_leadership`, `mentoring_enablement`, `stakeholder_management`, or `influence_without_authority`.
- Do not infer sole ownership from collaboration or decision participation.
- Do not infer realized outcomes from plausible consequences.
- A user-owned Source of Truth may store annotations inside governing dossiers or another explicitly configured current authority, but a standalone competency profile must not displace the factual project/role sources that prove the behavior.

Existing approved Source-of-Truth records remain valid if they do not yet contain capability tags. COMPASS may derive professional-effectiveness signals from approved factual evidence during analysis. Backfill is useful when a capability is materially important to current job-search workflows, but mass rewriting historical records solely to add labels is not required.

## Intake Behavior

During COMPASS Intake:

1. Verify the underlying action, decision, stakeholder context, and outcome first.
2. Add capability tags only after the underlying evidence is approved at the required depth.
3. Treat a proposed capability interpretation as derived metadata, not as a substitute for the factual event.
4. Ask behavior-specific questions only when the answer would materially change downstream-safe capability evidence.
5. Do not ask generic questions such as `Are you a critical thinker?` when a concrete situation, decision, or behavior can be examined instead.
6. Preserve unresolved or merely indicative signals without upgrading them into external claims.

## Target-Signal Mapping

A target role may communicate professional-effectiveness requirements explicitly or implicitly.

Explicit examples include terms such as critical thinking, communication, collaboration, influence, ownership, adaptability, stakeholder management, mentoring, strategic thinking, judgment, or ambiguity.

Implicit signals may arise from responsibilities such as:

- driving cross-team architecture decisions;
- resolving ambiguous incidents or requirements;
- balancing product, risk, delivery, and technical tradeoffs;
- mentoring engineers;
- coordinating with executives, customers, security, product, operations, or other functions;
- leading without formal authority;
- choosing what not to build;
- operating through changing constraints.

When mapping target signals:

- preserve the target's actual wording and importance;
- map it to one or more capability IDs only when that translation is reasonable;
- distinguish explicit requirements from analyst-inferred implicit signals;
- keep professional-effectiveness alignment separate from unrelated technical or credential hard screens;
- do not let strong behavioral evidence erase a material technical gap, and do not let a missing generic adjective erase stronger behavioral evidence.

## COMPASS Analysis

Within the existing strict analysis report contract, professional-effectiveness evidence belongs inside the semantic alignment matrix, source-to-output evidence mapping, missing-capabilities analysis, or stakeholder-objection analysis. Do not create a fourteenth required report section merely for this rule.

For material target signals, show:

- target behavior or requirement;
- mapped capability ID or IDs;
- governing source-backed evidence;
- direct, corroborated, indicative, adjacent, or missing status as appropriate;
- material boundary or likely reviewer objection.

Evaluate these signals as part of candidate fit and differentiation, not as personality diagnosis.

## Resume Behavior

For tailored resumes:

- Treat strong target-relevant professional-effectiveness evidence as a legitimate differentiation signal when the underlying work is already resume-worthy.
- Prefer bullets that naturally show the behavior through the candidate's action, decision, coordination, tradeoff, or consequence.
- Do not add a generic `Soft Skills` section by default.
- Do not fill `Core Skills` with unsupported adjectives such as `critical thinking`, `leadership`, or `communication` merely for ATS matching.
- A professional summary may describe a supported operating pattern such as cross-team technical leadership, decision-making under ambiguity, or stakeholder alignment when the evidence is strong enough and the wording preserves claim depth.
- Qualification remains primary: professional-effectiveness differentiation must not bury a hard screen or load-bearing technical requirement.

For broad recruiter resumes, use recurring corroborated patterns rather than target-specific soft-skill keyword lists.

## Cover Letters, Recruiter Messages, and Application Answers

When professional-effectiveness evidence is material:

- show one or two concrete behaviors or decisions rather than listing traits;
- use the target's language only when the source-backed behavior reasonably maps to it;
- keep the message natural for the channel;
- do not turn an external message into an internal competency matrix.

## Interview Preparation

Interview preparation should build an evidence-backed story bank for material professional-effectiveness capabilities.

For each important capability, identify when available:

1. likely behavioral or scenario question;
2. approved situation or context;
3. candidate action or decision;
4. constraint, tradeoff, or competing hypothesis;
5. stakeholder or system boundary;
6. consequence or verified outcome;
7. claim-depth and do-not-claim boundary;
8. what the story demonstrates without naming a stronger trait than the evidence supports.

Prefer stories that demonstrate multiple naturally connected signals, such as `critical_thinking + problem_framing + judgment_under_ambiguity`, when those signals arise from the same work. Do not splice unrelated experiences into a synthetic story.

## Evidence Prioritization

When two evidence items are otherwise comparable, prefer the one that:

1. proves a load-bearing target requirement;
2. demonstrates stronger verified contribution depth;
3. shows a consequential decision or tradeoff;
4. crosses meaningful stakeholder or system boundaries;
5. produces a verified outcome or decision consequence;
6. provides a target-relevant professional-effectiveness signal;
7. is more recent or reviewer-recognizable.

This ordering is contextual rather than a numeric score. Do not manufacture a universal professional-effectiveness percentage.

## Anti-Patterns

Do not:

- create a personality scorecard;
- claim a candidate is a `strong critical thinker` because a job description asks for critical thinking;
- infer communication strength merely because a role involved meetings;
- infer influence because a candidate was senior;
- infer ownership because the candidate participated;
- infer resilience from hardship without evidence of effective action;
- use generic soft-skill keywords to compensate for missing technical evidence;
- duplicate the same underlying event across many capability labels merely to inflate coverage;
- create a standalone candidate competency ledger that overrides or bypasses governing factual sources;
- convert `indicative` evidence into a confident external claim.

## Compatibility

This rule is additive. It does not change the strict analysis section count, the resume release contract, claim-depth semantics, recommendation values, eligibility gates, or TruthGuard hierarchy.

A Source of Truth that has not yet adopted explicit professional-effectiveness annotations remains compatible. The framework may derive signals from approved factual evidence, while future Source-of-Truth maintenance can add annotations where useful.
