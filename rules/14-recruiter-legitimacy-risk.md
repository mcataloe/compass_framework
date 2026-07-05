# 14 — Recruiter Legitimacy and Opportunity Fraud Risk

This file governs COMPASS evaluation of recruiter, staffing-firm, employer-of-record, client, end-customer, application-path, and opportunity-fraud risk.

## Purpose

The Recruiter Legitimacy and Opportunity Fraud Risk Gate evaluates whether an opportunity path is safe and accountable enough to continue engagement.

It answers a separate question from candidate fit:

1. Can the candidate credibly perform the role?
2. Is the role and opportunity worth pursuing?
3. Is the recruiter, company, entity chain, communication path, and requested next action legitimate enough to continue?

A legitimacy concern must not change the candidate-fit score. It changes the recommended action, information-sharing boundary, and verification requirements.

## When This Gate Applies

Run this gate when any of the following are present:

- a recruiter-presented opportunity;
- a staffing-firm, consulting-firm, employer-of-record, or recruiter-controlled requisition;
- a direct-employer opportunity with unclear application path, entity identity, or domain consistency;
- an unsolicited recruiter message;
- a requested right-to-represent, exclusivity, identity document, background-check step, onboarding form, payment setup, equipment purchase, or unusual communication channel;
- a role involving government, defense, public-sector, regulated, security, clearance, infrastructure, procurement, architecture, or sensitive-client context;
- the user explicitly asks whether an opportunity, recruiter, company, message, website, or job appears suspicious, fake, unsafe, or scam-like.

If external research, connector access, or the source material is insufficient, classify unknowns as `Unknown` or `Insufficient`. Do not interpret absence of scam reports as proof of legitimacy.

## Output Classification

Use one of these legitimacy ratings:

- `Verified enough to proceed` — the accountable entity, recruiter or application path, role identity, domain integrity, and requested next action are sufficiently verified for the current stage.
- `Proceed cautiously` — there are verification gaps or weak signals, but no serious red flags. Ask targeted verification questions before sharing sensitive information or investing heavy effort.
- `Do not share sensitive info yet` — entity identity, recruiter authority, application path, domain integrity, client identity, or process legitimacy is materially unclear, or the requested next action is premature.
- `Likely scam / disengage` — evidence indicates impersonation, financial fraud, credential harvesting, malicious links or software, forged entity identity, or other unsafe conduct.

This classification is a decision aid, not a legal finding. Use `Likely scam / disengage` only when evidence supports it. Use `Do not share sensitive info yet` when risk is plausible but not proven.

## Entity Separation

Keep these entities separate unless current evidence supports merging them:

- recruiter or sender;
- recruiting agency or staffing firm;
- consulting firm;
- employer of record;
- direct employer;
- client;
- end customer;
- parent, subsidiary, brand, or acquired entity;
- ATS, application, onboarding, background-check, payroll, or equipment vendor.

Do not allow a legitimate staffing firm to verify an undisclosed client. Do not allow a real client name to verify a suspicious recruiter identity. Do not allow a legitimate ATS vendor to verify a fake job page or unsafe link.

For staffing or consulting opportunities, an undisclosed client is not automatically suspicious. It is a verification gap and should usually produce `Contact first`, `Proceed cautiously`, or `Do not share sensitive info yet` depending on the remaining evidence and requested next action.

## Private Risk Intel Ledger

When a private recruiter-risk intelligence ledger is configured, COMPASS may use it as a defensive cache for prior sourced observations.

Recommended private Source of Truth path:

```text
intel/recruiter-risk-intel-ledger.yaml
```

The public COMPASS Framework repository should contain only the generic template and rules for this ledger. It should not store live lists of named recruiters, people, companies, domains, clients, or alleged bad actors.

Use `templates/recruiter-risk-intel/RECRUITER_RISK_INTEL_LEDGER_TEMPLATE.yaml` as the framework-owned schema template and `prompts/compass-recruiter-risk-intel-update.md` as the maintenance launcher.

A ledger record can support faster triage, but it is not a substitute for current verification when:

- the match is name-only;
- the record is stale or past its next review date;
- the requested next action involves sensitive information, money, identity verification, system access, contract terms, onboarding, background checks, or unusual process steps;
- the opportunity involves staffing, consulting, employer-of-record, government, defense, security, public-sector, regulated, clearance, infrastructure, or sensitive-client context;
- current evidence conflicts with the cached record.

Use ledger statuses as cached evidence, not automatic conclusions. A `verified_legitimate` record does not prove a new sender or domain is legitimate. A `suspicious_unverified` record does not prove wrongdoing. A `verified_adverse_official` record must preserve source, date, scope, and entity identity.

For ledger matching, prefer exact domains, email domains, profile URLs, requisition IDs, and application URLs over names. Treat name-only matches as weak signals requiring live verification.

## Evidence Tiers

Prefer current evidence in this order:

1. Official company, staffing-firm, employer-of-record, or government-controlled sources.
2. Official ATS or application pages reachable from an official domain.
3. Recruiter profiles that are tied to the accountable entity through multiple consistent signals.
4. Current reputable reporting, business records, regulatory filings, acquisition announcements, or company announcements.
5. Current scam warnings, fraud alerts, complaints, impersonation reports, or public enforcement actions from credible sources.
6. Private recruiter-risk intelligence ledger records when configured, preserving record date, match strength, status, confidence, and limitations.
7. Review platforms, forums, social posts, and anonymous reports as contextual or anecdotal evidence only.

Preserve source type, recency, entity identity, and confidence. Do not generalize isolated allegations. Do not promote anonymous reports into verified facts.

## Required Checks

### 1. Identity and Domain Integrity

Evaluate:

- official website domain;
- recruiter email domain and whether it matches the accountable entity;
- lookalike, recently created, or suspicious domains when evidence is available;
- personal email addresses used for purported corporate recruiting;
- mismatched display names, reply-to addresses, links, signatures, and domains;
- whether the recruiter is plausibly employed by or authorized to represent the accountable entity;
- whether the company has real leadership, staff, address, operating history, customers, products, postings, or business footprint.

### 2. Role and Requisition Reality

Evaluate:

- concrete role title, responsibilities, level, employment structure, work mode, location, duration, hours, compensation or rate, and client identity when disclosed;
- official posting or accountable recruiter-controlled requisition;
- consistency across recruiter message, job description, company website, ATS page, and staffing-firm listing;
- whether the description is coherent or appears generic, copied, inflated, or inconsistent;
- whether the compensation is plausible for the role, location, seniority, and structure;
- whether urgency or pressure is being used to bypass verification.

### 3. Process Safety

Treat these as high-risk or disqualifying until independently verified and appropriate for the stage:

- requests for money, unusual payment behavior, or financial transactions outside normal payroll or vendor processes;
- equipment-purchase requests before a verified employer-controlled onboarding process;
- sensitive identity, tax, banking, immigration, or background-check information before a verified offer or legitimate onboarding stage;
- account credentials, access codes, password-reset actions, or authentication prompts;
- installation of unknown software, remote-access tools, browser extensions, executables, or mobile apps;
- unusual movement to personal messaging channels or non-corporate portals without a legitimate reason;
- requests to keep the process secret from normal verification channels;
- requests to sign broad exclusivity, representation, confidentiality, IP, or commercial terms before the accountable entity, role, rate, client path, and submission scope are clear.

### 4. Clearance, Government, and Sensitive-Work Risk

Apply heightened scrutiny when the candidate has government, defense, intelligence, public-sector, regulated, security, infrastructure, or clearance-adjacent experience.

Flag elevated risk when:

- vague consulting, advisory, research, geopolitical, defense, security, procurement, architecture, or government-insight work is offered by a thinly verified entity;
- the opportunity asks for non-public government, vendor, client, system, architecture, security, procurement, mission, operational, or internal process information;
- payment is offered for reports, briefings, interviews, or analysis about current or former sensitive work;
- the company appears newly created, lightly documented, foreign-controlled, opaque, or staffed by unverifiable personas;
- the process appears designed to exploit recent layoff status, financial stress, clearance status, or government access;
- the recruiter asks about classified, controlled, export-controlled, confidential, client-sensitive, or non-public information.

Never recommend sharing classified, controlled, confidential, client-sensitive, government-sensitive, proprietary, credential, identity, or banking information through an unverified channel.

### 5. Staffing-Firm and Contract Controls

For staffing-firm, consulting-firm, employer-of-record, C2C, C2H, W-2 contract, 1099, fractional, bridge, or temporary opportunities, evaluate:

- accountable entity and recruiter authority;
- client identity when disclosed, or explicit `Undisclosed / unverified` when not disclosed;
- employment structure;
- expected hours;
- duration;
- rate or compensation;
- benefits treatment when relevant;
- right-to-represent scope;
- exclusivity or representation limitations;
- confidentiality, IP, conflict, notice, exit, and conversion terms when relevant;
- whether sensitive information is being requested before the relationship is verified.

Missing client identity or rate should not automatically imply fraud, but it should prevent `Apply now` when those terms are load-bearing.

## Recommended Action Values

Use the smallest safe next action:

- `Continue normal COMPASS analysis`;
- `Ask recruiter verification questions`;
- `Use official company application path only`;
- `Request corporate-email or official-domain confirmation`;
- `Limit response to non-sensitive qualification questions`;
- `Do not share sensitive information yet`;
- `Decline or disengage`;
- `Preserve evidence and report through appropriate channels`.

When the legitimacy gate is unresolved, prefer verification before tailoring, sending resumes with sensitive details, completing forms, signing representation terms, or scheduling extensive interviews.

## Required Output

When this gate is invoked, report:

1. Legitimacy rating.
2. One-paragraph reason for the rating.
3. Entity map: recruiter, recruiting firm, employer of record, direct employer, client, end customer, official domain, application path.
4. Evidence-backed red flags.
5. Evidence-backed green flags.
6. Unknowns and verification gaps.
7. Private ledger match summary when a configured ledger was checked.
8. Sensitive-information boundary.
9. Safe next action.
10. Optional verification reply when the user needs sendable language.

Do not include accusations in sendable recruiter language unless the user explicitly asks to disengage because fraud is established. Prefer neutral verification wording.

## Integration With COMPASS Analysis

COMPASS Analysis should apply this gate for recruiter-presented, staffing, consulting, unclear-entity, or suspicious opportunities.

The result belongs in risk, constraint, company/interview reality, or pursuit-economics analysis. It must not be embedded in clean resumes, cover letters, application answers, or recruiter responses unless the user asks for an internal dossier or a verification message.

A poor legitimacy rating may change the recommendation from `Apply`, `Apply cautiously`, or `Recruiter-only` to a verification-first or disengagement action. It must not reduce or increase evidence-backed candidate alignment.

## Integration With COMPASS Verified Opportunity Search

Verified Opportunity Search should use this gate when evaluating recruiter-controlled, staffing-firm, employer-of-record, contract, consulting, suspicious, or unclear application paths.

For primary direct-employer roles, this gate should verify domain and application-path integrity when evidence indicates impersonation or link risk.

For secondary contract results, report legitimacy concerns alongside contract utility without blending the two. A role may be technically aligned and commercially useful while still requiring verification before sensitive engagement.

## Integration With Recruiter Responses

When a recruiter response is requested and legitimacy is unresolved, draft a verification-first response rather than a normal interest response.

The response should:

- avoid accusations unless fraud is established;
- ask only for the minimum verification facts needed for the next decision;
- avoid sharing sensitive personal, financial, clearance, client, government, or proprietary information;
- keep internal analysis, scoring, and risk commentary out of the sendable text.

## Integration With Recruiter Risk Intel Updates

`prompts/compass-recruiter-risk-intel-update.md` may update a configured private ledger when the user explicitly requests ledger maintenance.

Ledger maintenance must:

- preserve source provenance, record dates, match strength, confidence, uncertainty, and safe-action history;
- avoid storing unnecessary personal data;
- avoid storing sensitive candidate, financial, credential, government, client, or proprietary information;
- mark stale, superseded, unresolved, or cleared records rather than silently deleting them;
- report whether persistence was completed, degraded, not completed, or not configured.

Ledger maintenance must not modify career claim ledgers, resumes, opportunity registries, candidate-status records, or unrelated Source of Truth files unless explicitly instructed.

## TruthGuard Integration

This rule follows `rules/04-truthguard.md` and `rules/10-opportunity-recon.md`.

In particular:

- do not claim an opportunity is legitimate merely because no scam reports were found;
- do not claim an opportunity is fraudulent without evidence;
- do not treat missing evidence as positive or negative proof;
- do not treat a private ledger record as current proof when stale, weakly matched, or contradicted;
- do not conflate recruiter, staffing firm, employer of record, client, and end customer;
- do not infer rates, hours, duration, client identity, contract terms, application status, representation status, or offer status;
- do not convert anonymous allegations into verified facts;
- do not include private risk analysis in clean external artifacts unless explicitly requested;
- do not recommend sharing sensitive identity, banking, credential, clearance, government, client, proprietary, or confidential information before the channel and stage are verified.
