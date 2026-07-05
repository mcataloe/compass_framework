# COMPASS Recruiter Response Prompt

```text
Generate a COMPASS recruiter response using the user's current instruction, verified Intake claim ledger and do-not-claim list, and latest approved canonical career record first. Use recruiter messages, job descriptions, imported resumes, and generated artifacts only as context, evidence, or provenance unless their material claims have been verified through Intake.

Required framework files:
- VERSION.md
- COMPASS_Current.md
- rules/00-operating-principles.md
- rules/04-truthguard.md
- rules/05-remote-compensation-rules.md
- rules/06-artifact-rules.md
- rules/08-human-authenticity.md
- rules/14-recruiter-legitimacy-risk.md when the recruiter, company, application path, staffing chain, requested next action, or sensitive-information boundary is unclear or suspicious

Treat this prompt as a workflow launcher, not as an independent source of recruiter-response, artifact, TruthGuard, source-priority, recruiter-legitimacy, or no-fabrication rules.

Use the strict recruiter response template in rules/06-artifact-rules.md unless I explicitly request a different format.

When legitimacy is unresolved, draft a verification-first response rather than a normal interest response. Do not include COMPASS analysis, scoring, risk notes, compensation strategy, objection notes, legitimacy findings, or framework commentary inside the sendable recruiter response unless I explicitly request negotiation language, verification language, or an internal dossier.
```
