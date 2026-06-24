# 06 - Artifact Rules

This file defines COMPASS artifact behavior.

## Artifact Types

COMPASS may generate canonical career records, claim ledgers, do-not-claim registers, coverage registers, Experience Sync reports, public claim indexes, analysis reports, tailored resumes, recruiter-targeted resumes, cover letters, recruiter responses, application answers, follow-up messages, interview preparation notes, compensation notes, and other career-specific artifacts.

## Default Download Formats

When COMPASS generates downloadable resume artifacts and no user-specific source-of-truth override or explicit user instruction says otherwise, the default downloadable formats are:

1. Word/DOCX
2. PDF
3. Markdown

Use the same human-readable base artifact name across formats. Word/DOCX and PDF filenames should use normal spaces, not underscores and not URL-encoded spaces. Markdown filenames may use underscores in place of spaces when useful for repository or plain-text workflows.

Default naming examples:

```text
Candidate Name - Company Role Title - YYYY-MM.docx
Candidate Name - Company Role Title - YYYY-MM.pdf
Candidate_Name_Company_Role_Title_YYYY_MM.md
```

A user's source-of-truth style guide may narrow or override the default downloadable formats for that user. User-specific file naming rules supersede these framework defaults when present.

## Strict Template Rule

Generated artifacts must use the strict output template for their artifact type unless the user explicitly requests a different format.

If a requested artifact does not match a named template, use the closest template below and preserve the source-priority, TruthGuard, and artifact-cleanliness rules.

Missing or unsupported material must be handled according to artifact type:

- Clean deliverables such as resumes, cover letters, recruiter responses, application answers, and follow-up messages must omit unsupported claims.
- Analysis, interview preparation, compensation notes, source-of-truth records, ledgers, and Experience Sync reports may identify gaps when those gaps are part of the artifact's purpose.
- Target documents, job descriptions, recruiter requests, and opportunity records may supply terminology and context only. They must not create experience, skills, ownership, metrics, credentials, or facts the user does not have.
- Compensation and remote-work content must stay out of clean resumes and cover letters unless the user explicitly asks for negotiation language.

## Separation Rule

External generated artifacts must be clean deliverables. Do not include internal COMPASS analysis in an external artifact unless the user explicitly requests an internal dossier.

Analysis reports, interview preparation notes, compensation notes, source-of-truth records, ledgers, and Experience Sync reports may include internal context, gaps, risk notes, provenance, publication decisions, Purple Squirrel scoring, company research, interview-reality findings, and pursuit economics when those sections are part of the strict template.

Company research, employee sentiment, interview reports, opportunity scoring, conversion-likelihood judgments, and private pursuit strategy must remain outside clean resumes, cover letters, recruiter responses, application answers, and follow-up messages unless the user explicitly requests an internal dossier or appropriate sendable language.

Generated artifacts are downstream outputs, not factual authorities. Do not use an old resume, cover letter, recruiter message, LinkedIn draft, application answer, portfolio draft, or public experience repository as source truth unless it has been separately imported, extracted, reconciled, and verified through COMPASS Intake.

## Human Authenticity Pass

Clean external deliverables must pass a Human Authenticity review before final output.

This applies to tailored resumes, recruiter-targeted resumes, cover letters, recruiter responses, application answers, follow-up messages, LinkedIn or about summaries, public experience narratives, and similar external career artifacts.

The pass requires:

- Source-backed specificity
- No generic AI-coded filler
- No invented motivation, personality, values, or company affinity
- No unsupported claims
- No private analysis, scoring, risk notes, ATS notes, or framework commentary in clean artifacts
- Natural but professional language
- Claims the candidate can defend in an interview
- ATS-safe structure where relevant

Human Authenticity cannot override source priority, TruthGuard, public-disclosure controls, or the strict template for the artifact type.

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

## Experience Sync Report Template

Use `templates/experience-sync/COMPASS_Experience_Sync_Report_TEMPLATE.md` and preserve this section order:

1. Mode and date
2. Framework version
3. Source repository, branch, and commit
4. Target repository, branch, and commit
5. Previous reconciliation state
6. Source scope examined
7. Authority and coverage findings
8. Proposed public additions
9. Proposed wording updates and narrowings
10. Proposed removals and do-not-claim corrections
11. Provisional claims retained, replaced, or withheld
12. Disclosure abstractions and withheld content
13. Conflicts and manual decisions
14. Target files that would change
15. Forbidden actions not performed
16. Validation performed
17. Storage status
18. Applied change metadata, when applicable
19. Next safe action

Experience Sync reports are internal reconciliation artifacts. They may contain private source paths, do-not-claim references, gaps, publication decisions, and disclosure rationale. Do not copy the report into a public experience narrative unless the user explicitly approves a sanitized version.

## Public Claim Index Template

Use `templates/experience-sync/COMPASS_Public_Claim_TEMPLATE.yaml` as the default shape when a target experience repository maintains structured public claims.

Each public claim should include, when practical:

1. Stable public claim ID
2. Approved public wording
3. Source status
4. Source references
5. Source commit
6. Coverage status
7. Claim-depth or contribution boundary
8. Public-projection status
9. Publication abstraction note
10. Limitations
11. Tags
12. Last reconciled date

Public claim indexes are downstream publication metadata, not factual authority. Do not copy private evidence or do-not-claim rationale into the public index merely to strengthen provenance.

## Analysis Report Template

Use this section order:

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

Analysis reports may include gaps, risks, objections, external-research limitations, and internal COMPASS reasoning because those are part of the report's purpose.

For identifiable-company role analysis, sections 8 and 9 are required. When external company or interview evidence is unavailable or insufficient, preserve the section and report the limitation and confidence rather than omitting it or speculating.

The final recommendation and pursuit-economics section should include, when relevant:

- the standard COMPASS recommendation value;
- best application channel;
- expected conversion likelihood as Low, Moderate, or High;
- required effort;
- opportunity cost;
- conditions that would change the recommendation.

Do not express conversion likelihood as a statistically measured probability unless reliable evidence supports that precision. Follow `rules/10-opportunity-recon.md` for opportunity-reality behavior and `rules/04-truthguard.md` for candidate and employer evidence boundaries.

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

Tailored resumes must be clean deliverables. Do not include gaps, TruthGuard notes, analysis, scoring, compensation strategy, recruiter objections, company sentiment, interview research, Purple Squirrel scoring, or pursuit economics inside the resume.

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

Cover letters must be clean deliverables. Do not include gaps, ATS notes, compensation strategy, internal analysis, company-review findings, interview-risk notes, or unsupported motivation.

## Recruiter Response Template

Use this section order:

1. Greeting
2. Direct answer or availability statement
3. Source-backed fit summary
4. Constraints or preferences, only when useful and user-approved
5. Clarifying question or next step
6. Signoff

Recruiter responses must be concise, truthful, and ready to send. Do not include private strategy, Purple Squirrel scoring, company sentiment, interview research, risk notes, or unsupported claims.

## Application Answer Template

Use this section order:

1. Direct answer
2. Source-backed evidence
3. Role relevance
4. Constraint or caveat, only when required for honesty
5. Closing sentence

Application answers must answer the prompt directly and must not introduce unsupported experience to satisfy target keywords. Do not include private opportunity-recon analysis.

## Follow-Up Message Template

Use this section order:

1. Greeting
2. Context reminder
3. Main follow-up message
4. Evidence-backed value or next-step framing, when useful
5. Clear ask or close
6. Signoff

Follow-up messages must be clean deliverables. Do not include private analysis, company-review findings, pursuit economics, pressure tactics, or unsupported claims.

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

Interview preparation notes may include strategy, gaps, objections, opportunity-recon findings, and cautions because they are internal preparation artifacts.

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

Recommended base-name patterns:

- `Candidate Name - Company Role Title - YYYY-MM`
- `Candidate Name - Staff Engineer - Tailored for Recruiter Name - MM-YYYY`
- `Project Name - Artifact Type - YYYY-MM`
- `Organization - Strategy Memo - YYYY-MM`
- `Topic - Research Plan - YYYY-MM`
- `COMPASS Experience Sync Report - YYYY-MM-DD`

Filename rules for downloadable generated artifacts:

- Word/DOCX filenames should use normal human-readable spaces, not underscores.
- PDF filenames should use normal human-readable spaces, not underscores.
- Markdown filenames may use underscores in place of spaces when useful for repository or plain-text workflows.
- Do not URL-encode spaces in final user-facing filenames.

## Reviewability

Generated artifacts should be easy for the user to inspect, copy, revise, and reuse.
