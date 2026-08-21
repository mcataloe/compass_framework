# COMPASS Career Profile: Tailored Resume Prompt

```text
Generate the COMPASS-tailored resume for the role most recently analyzed by COMPASS in this conversation, using the user's current instruction, verified Intake claim ledger and do-not-claim list, and latest approved canonical career record first. Use imported resumes, comprehensive resumes, master CVs, Initial Seed Artifacts under `/sources/seed/`, LinkedIn profiles, and similar artifacts only as evidence and provenance unless their material claims have been verified through Intake. If verified Intake records are incomplete and seed material must be used, follow Provisional Resume / CV Mode from the active resume-generation rule.

Required framework files:
- VERSION.md
- COMPASS_Current.md
- rules/00-operating-principles.md
- rules/02-resume-generation.md
- rules/04-truthguard.md
- rules/06-artifact-rules.md
- rules/08-human-authenticity.md
- rules/16-resume-release-assurance.md
- rules/20-professional-effectiveness-evidence.md

Load the user's current artifact-generation and recommended-opportunity-artifact policies when available.

Treat this prompt as a workflow launcher, not as an independent source of resume, formatting, artifact, TruthGuard, professional-effectiveness, page-length, source-priority, or no-fabrication rules.

Use the strict tailored resume template in rules/06-artifact-rules.md unless I explicitly request a different format.

Treat every generated file as a staged, untrusted artifact. Load the current user-specific resume release profile and employment-coverage plan when configured, then follow rules/16-resume-release-assurance.md. Do not present a file path or download as final until every required check is PASS and the matching manifest authorizes atomic publication. FAIL or UNKNOWN blocks release. Keep the manifest and internal validation detail out of the resume and do not display them unless I request them.

Use the previously analyzed target role, job description, recruiter requirement set, COMPASS findings, and approved role-fit evidence only as tailoring inputs. Do not invent facts, claims, metrics, ownership, credentials, technologies, responsibilities, or experience.

Apply rules/20-professional-effectiveness-evidence.md when the target role values critical thinking, systems thinking, judgment, communication, influence, collaboration, ownership, adaptability, stakeholder management, or related behavior. Prefer source-backed bullets that demonstrate those capabilities through actual decisions, actions, tradeoffs, coordination, or consequences. Do not add a generic Soft Skills section or unsupported behavioral adjectives merely for keyword coverage.

If the previously analyzed role is not available in the current context or approved source records, stop and ask me to provide the target role, job description, or recruiter requirement set instead of generating a generic resume.

If multiple roles are available and I have not identified the controlling role or bounded set, ask which role should control tailoring. If I explicitly request all recommended roles from a completed Verified Opportunity Search, or otherwise provide a bounded multi-role set, generate one independently tailored resume per eligible role under the user's recommended-opportunity-artifact policy; do not ask me to choose only one.

Do not include COMPASS analysis, scoring, risk notes, ATS matrix commentary, compensation strategy, recruiter objection notes, or framework commentary inside the resume artifact.
```
