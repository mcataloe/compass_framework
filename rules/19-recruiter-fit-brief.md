# 19 - Recruiter Fit Brief

This rule governs the optional externally shareable Recruiter Fit Brief produced by `COMPASS Analysis --recruiter-brief`.

## Purpose and Invocation

The Recruiter Fit Brief helps a recruiter evaluate and position a candidate accurately for one identified opportunity. It is a candidate-prepared external artifact, not an independent assessment, third-party validation, objective score, or substitute for the resume.

Generate it only when the user explicitly invokes `--recruiter-brief` or gives an equally explicit instruction to create this named artifact. Without that authorization, ordinary COMPASS Analysis produces only the private analysis.

The flag authorizes generation only. It does not authorize attachment, upload, forwarding, sending, submission, or any other external action.

## Mandatory Separation

Complete the full private COMPASS Analysis before considering the brief.

Generate the brief from the same resolved role and evidence set through `templates/recruiter-fit-brief/COMPASS_Recruiter_Fit_Brief_TEMPLATE.md`. Never create it by shortening, redacting, deleting sections from, mechanically sanitizing, or copying prose from the internal analysis.

The internal analysis and external brief remain separate artifacts. Neither may be embedded inside the other.

## Generation Eligibility

A brief may be generated only when all of the following are true:

1. The role and candidate evidence have been resolved under the current source-priority and TruthGuard rules.
2. No failed hard requirement makes the submission misleading or nonviable.
3. The COMPASS recommendation is not `Pass`.
4. The opportunity supports one of the allowed external submission postures:
   - `Strong fit`
   - `Credible fit with defined gaps`
5. The applicable recruiter-legitimacy and information-sharing gate permits external disclosure.
6. Every proposed line is public-safe, source-backed, interview-defensible, and appropriate if forwarded unchanged to a hiring manager.

If a hard-screen failure or `Pass` recommendation applies, block default brief generation and report the reason inside the private analysis. Use the appropriate recruiter-response or decline workflow only when separately requested.

## Legitimacy and Information-Sharing Gate

Apply `rules/14-recruiter-legitimacy-risk.md` when its trigger conditions are present.

- `Verified enough to proceed`: generation may continue when all other gates pass.
- `Proceed cautiously`: pause after analysis and obtain explicit post-analysis user approval before generating the brief. The original flag is not a waiver of a newly identified legitimacy risk.
- `Do not share sensitive info yet`: block generation.
- `Likely scam / disengage`: block generation.

A private risk-intelligence match, legitimacy score, verification rationale, or sensitive-information analysis must never appear in the external brief.

## Gap Taxonomy and Disclosure

Lead with supported value before limitations. Transparent gap disclosure is a core feature, but negative-first positioning is prohibited.

### Material readiness gap

Disclose a gap when it affects a central responsibility, hard requirement, expected delivery readiness, level, or accurate recruiter representation. State the exact boundary without broadening it into a larger deficiency.

### Credible adjacent or transferable experience

Identify the evidence as adjacent or transferable. Explain the defensible connection concisely and never imply equivalence to direct experience.

### Normal employer-specific ramp-up

Do not frame the target organization's tools, implementation details, domain context, terminology, or operating model as a candidate deficiency. Mention normal ramp-up only when it materially clarifies onboarding or prevents a misleading impression.

### Non-material omission

Exclude it. The brief is not an inventory of every technology, domain, or experience absent from the candidate's record.

## Required Structure

Target approximately 300–500 words and one readable rendered page when a paginated format is produced.

Use this order:

1. Candidate-prepared disclosure
2. Fit thesis
3. Directly supported alignment
4. Transferable or adjacent alignment
5. Material gaps and boundaries
6. Accurate recruiter positioning
7. Submission posture

Place this disclosure near the top:

> Candidate-prepared summary to support accurate role evaluation and submittal positioning.

The accurate-positioning section must state what the recruiter may claim and, when material, what the recruiter should not claim.

If no credible adjacent evidence or no material gap exists, use the template's permitted omission language rather than inventing content or padding the brief.

## Private Content Exclusions

The brief must exclude:

- alignment percentages and COMPASS scores;
- Purple Squirrel scoring;
- ATS commentary;
- conversion-likelihood judgments;
- pursuit economics and opportunity cost;
- compensation or rate strategy;
- company sentiment and interview research;
- recruiter-legitimacy analysis and private risk intelligence;
- private objection strategy;
- source paths, ledgers, dossiers, coverage registers, evidence maps, and framework mechanics;
- confidential or unnecessarily detailed project information;
- sensitive clearance or government-project detail beyond already approved public-safe wording.

A brief may disclose the existence and exact boundary of a material capability gap. That does not authorize copying the internal gap analysis, risk reasoning, evidence-map logic, or diagnostic labels.

## Evidence, Safety, and Authenticity

Every candidate claim remains subject to:

- `rules/04-truthguard.md`;
- current source priority and evidence resolution;
- applicable approved-claim and do-not-claim controls;
- public-disclosure and sensitive-information boundaries;
- `rules/08-human-authenticity.md`;
- the clean-artifact and filename-integrity requirements in `rules/06-artifact-rules.md`;
- any more specific user-owned Source of Truth policy.

Use concise, specific, defensible language. Do not use generic marketing copy, synthetic praise, unsupported motivation, or pseudo-objective scoring.

## Format and Naming

The generic framework does not force a candidate-specific export format. Follow the most specific user-owned artifact policy. When a paginated shareable format is requested or required, verify one-page rendering, readability at normal zoom, and absence of clipping.

Use the canonical artifact type `Recruiter Fit Brief` in the filename. Resolve one decoded filename before creation and apply the end-to-end artifact-name integrity gate.

Do not repurpose the resume-release validator or claim that a Recruiter Fit Brief is a resume-class artifact.

## Validation Gate

Every applicable check must be `PASS`. `FAIL` or `UNKNOWN` blocks release of the brief:

1. Explicit flag or equivalent named-artifact authorization
2. Complete private analysis
3. Separate generation path; no truncation or redaction
4. Eligible recommendation and no hard-screen failure
5. Allowed external submission posture
6. TruthGuard and evidence resolution
7. Direct versus adjacent evidence separation
8. Material-gap boundary accuracy
9. Legitimacy and information-sharing safety
10. Private-content leakage scan
11. Public-safety scan
12. Human Authenticity
13. Approximately 300–500 words
14. One readable rendered page when applicable
15. Canonical filename integrity
16. No automatic external action

Generation does not satisfy delivery validation. If the user later requests attachment, upload, forwarding, or sending, apply the governing channel and delivery gates separately.

## Accompanying Messages

A separately requested recruiter message may mention that the Recruiter Fit Brief is attached or available. It must remain conversational and must not reproduce the brief's diagnostic content, gap inventory, or internal COMPASS analysis.

## Regression Boundary

Without `--recruiter-brief`, COMPASS Analysis behavior is unchanged.

This rule does not modify candidate evidence, source authority, scoring, recommendation values, resume generation, resume schemas, resume release tooling, or recruiter-response behavior outside the narrow attachment-reference rule above.
