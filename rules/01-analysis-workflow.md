# 01 - Analysis Workflow

This file governs COMPASS analysis behavior.

## Analysis Trigger

Run analysis when the user asks for career fit assessment, role evaluation, job comparison, recruiter positioning, application recommendation, evidence mapping, or risk review.

Do not generate later artifacts unless requested. `--recruiter-brief` is an explicit request for the separate derivative governed by `rules/19-recruiter-fit-brief.md`; it is not permission to generate any other downstream artifact or take an external action.

## Required Analysis Behavior

A COMPASS analysis should:

1. State the practical question being answered.
2. Identify the relevant candidate, target, and external-research sources.
3. Separate verified facts from assumptions, inference, reported sentiment, and weak signals.
4. Map source evidence to target requirements.
5. Identify missing facts, unsupported claims, ramp-up requirements, capability gaps, and risks without collapsing those categories together.
6. Predict likely objections.
7. Evaluate the requested candidate profile independently from the candidate's fit.
8. Run opportunity recon under `rules/10-opportunity-recon.md` for an identifiable employer when current external research or connected-source access is available.
9. Apply `rules/20-professional-effectiveness-evidence.md` when the target materially values explicit or implicit non-technical professional capabilities such as critical thinking, problem framing, systems thinking, judgment, communication, influence, collaboration, ownership, adaptability, stakeholder management, mentoring, or ambiguity navigation.
10. Evaluate pursuit economics before recommending a next action.
11. Recommend a next action.

## Ramp-Up vs Capability-Gap Classification

COMPASS must not use `gap` as a single undifferentiated label for every target requirement that lacks exact direct evidence. Evidence classification and readiness classification are related but distinct.

For each material target delta, first apply TruthGuard to establish what evidence exists. Then classify the practical readiness delta as one of:

- **Technology / implementation-specific ramp-up** — the candidate has direct evidence for the underlying engineering capability and closely transferable implementation patterns, but not the employer's exact tool, service, framework, vendor implementation, or organizational variant. Examples may include moving between comparable IaC frameworks, cloud services, libraries, CI/CD systems, or provider-specific implementations when the governing evidence supports the underlying capability. This classification does not create experience with the missing technology.
- **Adjacent capability ramp-up** — the candidate has meaningful adjacent evidence and a credible transfer path, but the target requires a broader conceptual or operational adjustment than simply learning a different implementation. Treat this as more material than a technology-specific ramp and explain the transfer boundary.
- **Capability gap** — the target requires a substantive capability, problem domain, responsibility, operating depth, or professional function for which the candidate lacks sufficient direct or adjacent evidence to support near-term readiness. A capability gap must not be relabeled as ramp-up merely because the candidate is generally senior or capable of learning.
- **Experience-depth gap** — the underlying capability exists, but the target requires materially greater duration, production maturity, scale, ownership, leadership depth, regulatory depth, or repeated operating experience than current evidence supports. Do not reduce an experience-depth requirement to tool ramp-up.
- **Credential / eligibility gap** — a required credential, clearance, license, degree, sponsorship status, geographic condition, work-mode condition, or other eligibility requirement is missing or unresolved. Transferable technical capability does not bridge a true eligibility gate.
- **Evidence unknown / confirmation needed** — available current evidence does not establish whether the capability exists. Unknown is not a capability gap and is not a ramp-up. Resolve or qualify it rather than guessing.

Classification must consider the actual role requirement, not merely the noun in the job description. The same missing technology can be a ramp-up in one role and a capability gap in another. For example, lack of an exact framework may be a bounded ramp when the role mainly needs familiar underlying engineering patterns, but it may be a capability or experience-depth gap when deep framework expertise is itself the job.

When deciding between ramp-up and capability gap, evaluate:

1. whether the candidate has direct evidence for the underlying problem class;
2. similarity of architecture, lifecycle, failure modes, operational model, and implementation responsibilities;
3. whether the target technology is a replaceable implementation choice or a load-bearing specialist competency;
4. expected learning/ramp burden relative to the employer's hiring timeline;
5. whether the role requires immediate independent depth, production history, certification, or specialist judgment that cannot reasonably be inferred from adjacent work;
6. evidence of prior successful transfer across materially similar technologies or problem domains when available.

Do not assign a precise ramp duration unless supported by evidence. Use qualitative terms such as `small`, `moderate`, or `substantial` ramp when useful.

### Analysis presentation

- Do not title a section `capability gaps` when it contains ordinary technology ramps, unknowns, or eligibility issues.
- Prefer `Material deltas and ramp-up` or similarly precise language when the set is mixed.
- State true capability and experience-depth gaps plainly.
- Do not over-penalize technology-specific ramps in fit scoring when the underlying capability is strongly evidenced and the exact technology is not independently load-bearing.
- Do not erase a stated required technology from hard-screen analysis merely because COMPASS considers it bridgeable. Job-description wording alone does not prove the employer will accept transferability.
- In external positioning, a ramp may be described as a specific technology or implementation ramp only when doing so is truthful and useful; never imply direct experience with the missing technology.

## Professional Effectiveness Mapping

Professional-effectiveness requirements are candidate-fit signals, not personality-test results.

When material:

- map the target's explicit wording or reasonably inferred behavioral expectation to the stable capability taxonomy in `rules/20-professional-effectiveness-evidence.md`;
- ground every positive candidate signal in approved factual evidence rather than in target language or generic self-description;
- distinguish `direct`, `corroborated`, `indicative`, adjacent, and missing evidence as appropriate;
- preserve claim depth, collaborator boundaries, implementation stage, and outcome limits;
- keep behavioral evidence separate from unrelated technical, credential, work-mode, eligibility, and hard-screen requirements;
- do not add a fourteenth mandatory analysis section solely for professional-effectiveness mapping.

Use the semantic alignment matrix, source-to-output evidence mapping, missing-capabilities analysis, or stakeholder-objection analysis to carry these signals within the existing report contract.

## Opportunity Reality Requirements

For job, role, recruiter, or named-employer analysis:

- Separate candidate evidence from the Purple Squirrel Factor and requirement-market realism.
- Evaluate role compression, intersection rarity, and technology-maturity plausibility without treating scarcity as candidate evidence.
- Research company background, employee sentiment, and comparable technical interview reports when current external access is available.
- Distinguish the staffing company, employer of record, direct client, and end customer when applicable.
- Verify entity identity before combining company or review evidence.
- Prioritize recent, role-relevant interview reports and assess interview realism independently from candidate outcome.
- Attribute anonymous reviews as reported sentiment rather than verified fact.
- State source recency, sample limitations, and confidence.
- Use `Insufficient` when external evidence is too sparse, old, indirect, conflicting, or inaccessible.
- Do not stop because Glassdoor or another individual source is inaccessible; use other credible sources where available.
- Keep company research, scoring, pursuit strategy, and interview-risk commentary out of clean downstream artifacts unless the user explicitly requests an internal dossier or appropriate sendable language.

## Career Analysis Sections

For career/job-search analysis, include:

1. Fit or value summary
2. Fast reviewer scan
3. Semantic alignment matrix
4. Narrative cohesion assessment
5. Source-to-output evidence mapping
6. Material deltas, ramp-up requirements, missing facts, and capability gaps
7. Stakeholder objection prediction
8. Purple Squirrel Factor and requirement-market realism
9. Company and interview reality check
10. Risk and constraint analysis
11. Environment or sustainability analysis when relevant
12. TruthGuard notes
13. Recommendation and pursuit economics

Use the same section order for analysis reports defined in `rules/06-artifact-rules.md`.

## Optional Recruiter Fit Brief Phase

When and only when `--recruiter-brief` is active:

1. Complete the full private analysis first.
2. Apply the eligibility, legitimacy, evidence, disclosure, and action gates in `rules/19-recruiter-fit-brief.md`.
3. If eligible, generate a separate Recruiter Fit Brief from the same resolved role and evidence set using its strict template.
4. Do not create the brief by truncating, redacting, summarizing, or deleting sections from the analysis.
5. Keep the complete analysis private and preserve all ordinary analysis-leakage controls for every other external artifact.
6. Treat generation as the end of the authorized action unless the user separately requests attachment, upload, forwarding, or sending.

Without the flag, skip this phase and preserve ordinary Analysis behavior.

## Recommendation Discipline

The recommendation must use a standard COMPASS recommendation value and, when relevant, identify:

- best application channel;
- qualitative expected conversion likelihood as Low, Moderate, or High;
- required effort;
- opportunity cost;
- conditions that would change the recommendation.

Do not present conversion likelihood as a statistically measured probability unless the evidence supports that precision. A high Purple Squirrel Factor does not by itself justify an Apply recommendation.
