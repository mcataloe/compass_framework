# COMPASS Analysis Prompt

```text
Run a COMPASS analysis.

Before running this workflow, read the latest COMPASS framework files from the connected repository or Project sources.

Required framework files:
- VERSION.md
- COMPASS_Current.md
- rules/00-operating-principles.md
- rules/01-analysis-workflow.md
- rules/04-truthguard.md
- rules/06-artifact-rules.md
- rules/10-opportunity-recon.md
- rules/14-recruiter-legitimacy-risk.md when the role, recruiter, company, application path, or opportunity source involves recruiter-controlled, staffing, consulting, unclear-entity, sensitive-work, suspicious-domain, or unsafe-process signals

Treat this prompt as a workflow launcher, not as an independent source of analysis, artifact, TruthGuard, opportunity-recon, source-priority, recruiter-legitimacy, or no-fabrication rules.

Use the strict analysis report template in rules/06-artifact-rules.md unless I explicitly request a different format.

For identifiable-company role analysis, apply the Opportunity Reality Layer from rules/10-opportunity-recon.md. Separate candidate fit from requested-candidate rarity, company and interview evidence, and pursuit economics. Apply rules/14-recruiter-legitimacy-risk.md when legitimacy, impersonation, entity-chain, unsafe-process, or sensitive-information concerns are present. Report insufficient external evidence rather than speculating.

Use the user's current instruction, verified Intake claim ledger and do-not-claim list, and latest approved canonical record before imported source documents. Treat imported resumes, CVs, LinkedIn profiles, cover letters, and generated artifacts as evidence and provenance only unless their material claims have been verified through Intake. Do not invent facts, claims, metrics, ownership, credentials, or experience.
```
