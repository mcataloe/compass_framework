# COMPASS Career Profile: Recruiter-Targeted Resume Prompt

```text
Generate a COMPASS recruiter-targeted resume using the user's current instruction, verified Intake claim ledger and do-not-claim list, and latest approved canonical career record first. Use imported resumes, comprehensive resumes, master CVs, Initial Seed Artifacts under `/sources/seed/`, LinkedIn profiles, and similar artifacts only as evidence and provenance unless their material claims have been verified through Intake. If verified Intake records are incomplete and seed material must be used, follow Provisional Resume / CV Mode from the active resume-generation rule.

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
- rules/22-criterion-evidence-recoverability.md

Treat this prompt as a workflow launcher, not as an independent source of resume, formatting, artifact, TruthGuard, professional-effectiveness, criterion-recoverability, page-length, source-priority, or no-fabrication rules.

Use the strict recruiter-targeted resume template in rules/06-artifact-rules.md unless I explicitly request a different format.

Treat every generated file as a staged, untrusted artifact. Load the current user-specific resume release profile and employment-coverage plan when configured, then follow rules/16-resume-release-assurance.md. Do not present a file path or download as final until every required check is PASS and the matching manifest authorizes atomic publication. FAIL or UNKNOWN blocks release. Keep the manifest and internal validation detail out of the resume and do not display them unless I request them.

Use broad positioning appropriate for a recruiter who may have multiple opportunities, while preserving TruthGuard and source-grounding. When professional-effectiveness evidence is used, prefer recurring corroborated patterns from approved work—such as cross-team technical leadership, judgment under ambiguity, systems thinking, stakeholder alignment, mentoring, ownership, or adaptability—rather than a generic soft-skill keyword list.

Do not invent a bounded target taxonomy for a broad recruiter resume. If the user explicitly bounds the recruiter resume to a concrete job description or requirement set, apply rules/22-criterion-evidence-recoverability.md after drafting so supported load-bearing criteria are recoverable from coherent source-backed evidence without inventing ATS scores, proprietary ranking behavior, or unsupported coverage.

Do not include COMPASS analysis, scoring, risk notes, ATS matrix commentary, compensation strategy, recruiter objection notes, criterion-recoverability matrices, or framework commentary inside the resume artifact.
```
