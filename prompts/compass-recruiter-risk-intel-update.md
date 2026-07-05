# COMPASS Recruiter Risk Intel Update Prompt

```text
Run COMPASS Recruiter Risk Intel Update.

Purpose:
Review, refresh, and update a configured private recruiter-risk intelligence ledger used by rules/14-recruiter-legitimacy-risk.md.

Required framework files:
- VERSION.md
- COMPASS_Current.md
- COMPASS_COMMANDS.md
- rules/04-truthguard.md
- rules/10-opportunity-recon.md
- rules/14-recruiter-legitimacy-risk.md
- templates/recruiter-risk-intel/RECRUITER_RISK_INTEL_LEDGER_TEMPLATE.yaml

Required private source when configured:
- intel/recruiter-risk-intel-ledger.yaml

Treat this prompt as a workflow launcher, not as an independent source of truth, accusation authority, investigation authority, or no-fabrication rules.

Scope:
- Review existing private-ledger records whose next_review_due is today or past due.
- Refresh records whose last_verified date is stale under the ledger policy.
- Add records only when supported by source evidence.
- Update status, confidence, evidence, and safe-action fields only when the evidence supports the change.
- Preserve provenance, uncertainty, prior observations, and related-record links.
- Do not delete records unless explicitly instructed; prefer superseded, stale, cleared, or merged status notes.

Evidence discipline:
- Prefer current authoritative, company-controlled, regulator-controlled, or other primary sources when available.
- Use accountable staffing-firm or recruiter-controlled sources only for the facts they directly support.
- Treat review sites, forums, social posts, and anonymous reports as contextual evidence only.
- Preserve source type, source date, entity identity, match strength, confidence, and uncertainty.
- Do not treat absence of a prior ledger record as proof of legitimacy.
- Do not treat absence of external reports as proof of legitimacy.
- Do not label an entity as adverse without evidence.
- Do not conflate recruiter, staffing firm, employer of record, direct employer, client, end customer, ATS, or application vendor.
- Do not conflate a legitimate organization with an impersonating or unrelated entity.

Matching discipline:
- Exact domain, email-domain, profile URL, requisition ID, and application URL matches are stronger than name matches.
- Name-only matches are weak signals and require live verification before changing the recommended action.
- Stale records are leads, not current conclusions.
- High-risk next actions require live verification even when a cached record exists.

Privacy discipline:
- Do not store sensitive candidate identity data, banking data, credentials, private addresses, classified or controlled information, non-public client information, or unnecessary personal data.
- Store only what is needed to support future recruiter-legitimacy and opportunity-risk decisions.

Output:
1. Ledger path used, or `Persistence not configured` if no private ledger is available.
2. Entries reviewed.
3. Entries added.
4. Entries updated.
5. Entries marked stale, superseded, or requiring human review.
6. Entries left unchanged and why.
7. Refused updates and why.
8. Write status: `Persisted`, `Persistence degraded`, `Not persisted`, or `Persistence not configured`.

Write behavior:
If repository write access is available and the private ledger path exists, update the ledger directly and verify the write. If write access or the private ledger is unavailable, produce a copy-ready YAML patch and state exactly where it should be saved.
```
