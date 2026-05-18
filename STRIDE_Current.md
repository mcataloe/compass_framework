# STRIDE Current Framework

STRIDE is a phased framework for evaluating roles and generating truthful, source-grounded job-search materials.

STRIDE focuses on whether a hiring team can quickly understand the candidate's value, evidence, seniority, and fit for the role.

## Core Question

Would the hiring manager, recruiter, and ATS understand the candidate's value quickly enough to move the candidate forward?

## Default Workflow

STRIDE runs in phases:

1. Analysis only
2. Tailored resume only when requested
3. Cover letter only when requested
4. Follow-up recruiter or application responses only when requested

Strategic analysis and generated application artifacts must remain separate.

## Standard STRIDE Analysis Sections

A complete STRIDE analysis should include:

1. Role fit summary
2. 10-second hiring manager scan
3. ATS and semantic alignment matrix
4. Narrative cohesion assessment
5. Job-description-to-resume evidence mapping
6. Missing high-priority terms
7. Recruiter and hiring-manager objection prediction
8. Compensation and remote-work risk
9. TruthGuard notes
10. Recommendation

## Recommendation Values

Use one of the following recommendation values:

- Pass
- Apply
- Apply cautiously
- Recruiter-only
- Top choice

## Operating Principles

### Truth First

Never invent technologies, metrics, credentials, responsibilities, ownership, employers, timelines, project names, or business outcomes.

### Evidence Mapping

Every strong claim in a resume, cover letter, or application answer should be traceable to the source resume, the user's direct statement, or the job description.

### Staff-Level Signal

For staff-level roles, emphasize cross-system reasoning, architecture, delivery leadership, stakeholder influence, operational readiness, risk reduction, maintainability, and platform-scale ownership.

### ATS Without Keyword Stuffing

STRIDE should improve semantic alignment with the job description while preserving readable, credible prose.

### Narrative Cohesion

Tailoring should make the candidate's career story easier to understand, not merely add keywords.

### Objection Prediction

STRIDE should identify likely recruiter or hiring-manager objections before materials are generated.

### Artifact Separation

Resume artifacts must not contain STRIDE analysis, ATS notes, compensation strategy, risk commentary, or private tactical notes.

### Clarifying Questions

Ask up to three clarifying questions only when a missing fact materially affects truthfulness or positioning. Do not ask for information that can be reasonably obtained from the provided job description, source resume, or project files.

## TruthGuard Summary

TruthGuard is the anti-fabrication layer. It must flag:

- Missing required experience
- Unverified technologies
- Unsupported business metrics
- Ambiguous ownership claims
- Credentials or compliance claims not present in the source
- Role scope that may be overstated
- Terms that should be included only if user confirms them

## Source Priority

When sources conflict, use this priority order:

1. User's direct current instruction
2. Current job description or recruiter message
3. Latest approved source resume or CV
4. STRIDE repository rules
5. Project instructions
6. ChatGPT memory

If repository or source-resume access fails, say so clearly instead of reconstructing unavailable facts from memory.
