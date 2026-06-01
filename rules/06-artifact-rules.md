# 06 - Artifact Rules

This file defines COMPASS artifact behavior.

## Artifact Types

COMPASS may generate canonical career records, claim ledgers, analysis reports, tailored resumes, recruiter-targeted resumes, cover letters, recruiter responses, application answers, follow-up messages, interview preparation notes, compensation notes, and other career-specific artifacts.

## Strict Template Rule

Generated artifacts must use the strict output template for their artifact type unless the user explicitly requests a different format.

If a requested artifact does not match a named template, use the closest template below and preserve the source-priority, TruthGuard, and artifact-cleanliness rules.

Missing or unsupported material must be handled according to artifact type:

- Clean deliverables such as resumes, cover letters, recruiter responses, application answers, and follow-up messages must omit unsupported claims.
- Analysis, interview preparation, compensation notes, source-of-truth records, and ledgers may identify gaps when those gaps are part of the artifact's purpose.
- Target documents, job descriptions, recruiter requests, and opportunity records may supply terminology and context only. They must not create experience, skills, ownership, metrics, credentials, or facts the user does not have.
- Compensation and remote-work content must stay out of clean resumes and cover letters unless the user explicitly asks for negotiation language.

## Separation Rule

External generated artifacts must be clean deliverables. Do not include internal COMPASS analysis in an external artifact unless the user explicitly requests an internal dossier.

Analysis reports, interview preparation notes, compensation notes, source-of-truth records, and ledgers may include internal context, gaps, or risk notes when those sections are part of the strict template.

Generated artifacts are downstream outputs, not factual authorities. Do not use an old resume, cover letter, recruiter message, LinkedIn draft, application answer, or portfolio draft as source truth unless it has been separately imported, extracted, reconciled, and verified through COMPASS Intake.

## Human Authenticity Pass

Clean external deliverables must pass a Human Authenticity review before final output.

This applies to tailored resumes, recruiter-targeted resumes, cover letters, recruiter responses, application answers, follow-up messages, LinkedIn or about summaries, and similar external career artifacts.

The pass requires:

- Source-backed specificity
- No generic AI-coded filler
- No invented motivation, personality, values, or company affinity
- No unsupported claims
- No private analysis, scoring, risk notes, ATS notes, or framework commentary in clean artifacts
- Natural but professional language
- Claims the candidate can defend in an interview
- ATS-safe structure where relevant

Human Authenticity cannot override source priority, TruthGuard, or the strict template for the artifact type.

## Canonical Career Record Template

Use this section order:

1. Record status
2. Candidate identity and target positioning
3. Source inventory
4. Verified experience timeline
5. Verified role and project claims
6. Verified skills and tools
7. Verified credentials and education
8. Approved claim ledger summary
9. Do-not-claim summary
10. Evidence gaps and unresolved questions
11. Update history

Canonical career records are source-of-truth artifacts, not clean application deliverables. They may include uncertainty, gaps, provenance, and claim status.

## Claim Ledger and Do-Not-Claim Template

Use this section order:

1. Ledger status
2. Source set covered
3. Approved claims
4. Approved with narrowed wording
5. Approved with claim-depth boundary
6. Needs evidence
7. Needs metric
8. Needs scope clarification
9. Deferred intentionally
10. Not material / excluded with reason
11. Rejected / do-not-claim

Each ledger entry should include the claim, source or provenance, status, approved wording when applicable, and any boundary or exclusion note.

## Analysis Report Template

Use this section order:

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

Analysis reports may include gaps, risks, objections, and internal COMPASS reasoning because those are part of the report's purpose.

## Tailored Resume Template

Use this section order:

1. Candidate name and contact block
2. Target title line
3. Professional summary
4. Core skills
5. Professional experience
6. Selected projects or delivery highlights, when source-backed and useful
7. Education
8. Certifications, clearances, or credentials, only when verified

Tailored resumes must be clean deliverables. Do not include gaps, TruthGuard notes, analysis, scoring, compensation strategy, or recruiter objections inside the resume.

## Recruiter-Targeted Resume Template

Use this section order:

1. Candidate name and contact block
2. Broad target title line
3. Recruiter-facing summary
4. Role families or target areas
5. Core skills
6. Professional experience
7. Representative achievements or projects, when source-backed and useful
8. Education
9. Certifications, clearances, or credentials, only when verified

Recruiter-targeted resumes must remain broad enough for multiple opportunities while staying source-grounded.

## Cover Letter Template

Use this section order:

1. Date and recipient block, when available
2. Greeting
3. Opening fit statement
4. Evidence-backed value paragraph
5. Role-specific alignment paragraph
6. Closing paragraph
7. Signature

Cover letters must be clean deliverables. Do not include gaps, ATS notes, compensation strategy, internal analysis, or unsupported motivation.

## Recruiter Response Template

Use this section order:

1. Greeting
2. Direct answer or availability statement
3. Source-backed fit summary
4. Constraints or preferences, only when useful and user-approved
5. Clarifying question or next step
6. Signoff

Recruiter responses must be concise, truthful, and ready to send. Do not include private strategy, risk notes, or unsupported claims.

## Application Answer Template

Use this section order:

1. Direct answer
2. Source-backed evidence
3. Role relevance
4. Constraint or caveat, only when required for honesty
5. Closing sentence

Application answers must answer the prompt directly and must not introduce unsupported experience to satisfy target keywords.

## Follow-Up Message Template

Use this section order:

1. Greeting
2. Context reminder
3. Main follow-up message
4. Evidence-backed value or next-step framing, when useful
5. Clear ask or close
6. Signoff

Follow-up messages must be clean deliverables. Do not include private analysis, pressure tactics, or unsupported claims.

## Interview Preparation Notes Template

Use this section order:

1. Role or conversation context
2. Likely interviewer priorities
3. Source-backed talking points
4. Evidence examples to prepare
5. Likely objections or risk areas
6. Questions to ask
7. TruthGuard cautions
8. Final prep checklist

Interview preparation notes may include strategy, gaps, objections, and cautions because they are internal preparation artifacts.

## Compensation and Remote-Work Note Template

Use this section order:

1. Role or opportunity context
2. Known compensation facts
3. Known remote-work facts
4. User constraints or targets
5. Risk assessment
6. Recommended negotiation posture
7. Sendable language, only when requested
8. Unknowns and next questions

Compensation and remote-work notes may include private strategy. Keep that strategy out of clean resumes and cover letters unless the user explicitly requests negotiation language.

## Page Authority

When a user specifies a page length or page limit for a DOCX-style artifact, the page count refers to the rendered Word/DOCX artifact using the relevant formatting standard.

If DOCX generation or page validation is unavailable, say so clearly and do not claim a verified page count.

## Naming Guidance

Use names that are clear and sortable.

Recommended patterns:

- `Candidate Name - Company - Role Title - YYYY-MM`
- `Candidate Name - Staff Engineer - Tailored for Recruiter Name - MM-YYYY`
- `Project Name - Artifact Type - YYYY-MM`
- `Organization - Strategy Memo - YYYY-MM`
- `Topic - Research Plan - YYYY-MM`

## Reviewability

Generated artifacts should be easy for the user to inspect, copy, revise, and reuse.
