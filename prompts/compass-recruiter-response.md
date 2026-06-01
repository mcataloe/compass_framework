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

Treat this prompt as a workflow launcher, not as an independent source of recruiter-response, artifact, TruthGuard, source-priority, or no-fabrication rules.

Use the strict recruiter response template in rules/06-artifact-rules.md unless I explicitly request a different format.

Do not include COMPASS analysis, scoring, risk notes, compensation strategy, objection notes, or framework commentary inside the sendable recruiter response unless I explicitly request negotiation language or an internal dossier.
```
