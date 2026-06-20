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

Treat this prompt as a workflow launcher, not as an independent source of resume, formatting, artifact, TruthGuard, page-length, source-priority, or no-fabrication rules.

Use the strict tailored resume template in rules/06-artifact-rules.md unless I explicitly request a different format.

Use the previously analyzed target role, job description, recruiter requirement set, COMPASS findings, and approved role-fit evidence only as tailoring inputs. Do not invent facts, claims, metrics, ownership, credentials, technologies, responsibilities, or experience.

If the previously analyzed role is not available in the current context or approved source records, stop and ask me to provide the target role, job description, or recruiter requirement set instead of generating a generic resume.

If multiple previously analyzed roles are available, stop and ask me which role should control tailoring before generating the resume.

Do not include COMPASS analysis, scoring, risk notes, ATS matrix commentary, compensation strategy, recruiter objection notes, or framework commentary inside the resume artifact.
```
