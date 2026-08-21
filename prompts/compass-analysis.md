# COMPASS Analysis Prompt

```text
Run a COMPASS analysis.

Optional: add `--recruiter-brief` to request the complete private analysis plus a separate externally shareable Recruiter Fit Brief.

Before running this workflow, read the latest COMPASS framework files from the connected repository or Project sources.

Required framework files:
- VERSION.md
- COMPASS_Current.md
- rules/00-operating-principles.md
- rules/01-analysis-workflow.md
- rules/04-truthguard.md
- rules/06-artifact-rules.md
- rules/10-opportunity-recon.md
- rules/20-professional-effectiveness-evidence.md
- rules/14-recruiter-legitimacy-risk.md when the role, recruiter, company, application path, or opportunity source involves recruiter-controlled, staffing, consulting, unclear-entity, sensitive-work, suspicious-domain, or unsafe-process signals
- rules/19-recruiter-fit-brief.md and templates/recruiter-fit-brief/COMPASS_Recruiter_Fit_Brief_TEMPLATE.md only when `--recruiter-brief` is active

Treat this prompt as a workflow launcher, not as an independent source of analysis, artifact, TruthGuard, opportunity-recon, professional-effectiveness, source-priority, recruiter-legitimacy, or no-fabrication rules.

Use the strict analysis report template in rules/06-artifact-rules.md unless I explicitly request a different format. Without `--recruiter-brief`, do not generate a Recruiter Fit Brief.

When `--recruiter-brief` is active, finish the private analysis first, then apply Rule 19. If generation is permitted, create a separate brief from the same resolved evidence using the strict Recruiter Fit Brief template. Never truncate or redact the analysis into the brief. The flag authorizes generation only, never attachment, upload, forwarding, or sending.

For identifiable-company role analysis, apply the Opportunity Reality Layer from rules/10-opportunity-recon.md. Separate candidate fit from requested-candidate rarity, company and interview evidence, and pursuit economics. Apply rules/14-recruiter-legitimacy-risk.md when legitimacy, impersonation, entity-chain, unsafe-process, or sensitive-information concerns are present. Report insufficient external evidence rather than speculating.

Apply rules/20-professional-effectiveness-evidence.md to explicit and implicit non-technical hiring signals. Map only source-backed behavior to capabilities such as critical thinking, systems thinking, judgment, communication, influence, ownership, and adaptability. Keep these signals inside the existing analysis sections rather than adding a new mandatory section, and do not let behavioral alignment erase technical or credential gaps.

Use the user's current instruction, verified Intake claim ledger and do-not-claim list, and latest approved canonical record before imported source documents. Treat imported resumes, CVs, LinkedIn profiles, cover letters, and generated artifacts as evidence and provenance only unless their material claims have been verified through Intake. Do not invent facts, claims, metrics, ownership, credentials, or experience.
```
