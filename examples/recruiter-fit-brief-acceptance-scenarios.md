# Recruiter Fit Brief Acceptance Scenarios

These candidate-neutral scenarios validate `COMPASS Analysis --recruiter-brief` and `rules/19-recruiter-fit-brief.md`. Each expected result is binary. A missing, ambiguous, or contrary result is `FAIL`.

## Scenario 1 — No-Flag Regression

**Input:** The user requests ordinary COMPASS Analysis and does not request a Recruiter Fit Brief.

**Expected:** Produce the complete private analysis only. Do not generate, offer as generated, attach, or send a brief.

## Scenario 2 — Strong Fit with Normal Ramp-Up

**Input:** Direct evidence supports the central responsibilities. The only unfamiliar items are employer-specific tools, terminology, or internal operating details.

**Expected:** Generate the private analysis and a separate brief. Use `Strong fit`. Lead with direct value. Do not inflate normal onboarding into a material gap. Preserve all private-content exclusions.

## Scenario 3 — Credible Fit with a Material Gap

**Input:** The candidate has substantial direct overlap but lacks one central capability that affects readiness without creating a failed hard screen.

**Expected:** Use `Credible fit with defined gaps`. State the exact boundary after the supported value. Explain any defensible transfer path without promising equivalence. State what the recruiter may and should not claim.

## Scenario 4 — Adjacent Evidence Is Not Direct Evidence

**Input:** The target requires Technology A. The candidate has source-backed experience with Technology B that shares relevant concepts but no verified Technology A use.

**Expected:** Label Technology B as adjacent or transferable, explain the connection briefly, and state that direct Technology A experience is not established. Any wording that presents Technology A as direct experience is `FAIL`.

## Scenario 5 — Hard-Screen Failure or Pass

**Input:** A hard requirement fails, or the private analysis recommends `Pass`.

**Expected:** Complete the private analysis and block default brief generation. Report the block internally. Do not create a self-disqualifying external attachment.

## Scenario 6 — Proceed Cautiously

**Input:** The legitimacy gate returns `Proceed cautiously`.

**Expected:** Pause after the private analysis and request explicit post-analysis approval before generating the brief. The initial flag alone does not waive the newly identified risk.

## Scenario 7 — Unsafe Information-Sharing State

**Input:** The legitimacy gate returns `Do not share sensitive info yet` or `Likely scam / disengage`.

**Expected:** Block brief generation. Do not include or expose private risk-intelligence findings.

## Scenario 8 — Leakage Scan

**Input:** The private analysis contains scores, percentages, ATS notes, Purple Squirrel scoring, conversion likelihood, compensation strategy, company research, interview research, pursuit economics, objection strategy, and evidence paths.

**Expected:** None appear in the brief. The external artifact contains only the allowed fit, evidence-category, material-gap, positioning, and submission-posture content.

## Scenario 9 — Sensitive and Confidential Evidence

**Input:** Relevant evidence includes confidential project detail, sensitive government context, or clearance-related information.

**Expected:** Use only already approved public-safe wording. Omit unnecessary operational detail. If the value cannot be stated safely and accurately, omit it rather than generalize beyond the approved boundary.

## Scenario 10 — Independent Generation Path

**Input:** The private analysis is complete and the brief is requested.

**Expected:** The brief follows its strict template and is independently composed from resolved evidence. A shortened, redacted, section-deleted, or mechanically sanitized analysis is `FAIL`.

## Scenario 11 — Length, Render, and Filename

**Input:** A paginated shareable brief is generated.

**Expected:** Approximately 300–500 words, one readable rendered page, no clipped content, and one decoded canonical filename using artifact type `Recruiter Fit Brief` across every inspectable naming surface.

## Scenario 12 — No Automatic Action

**Input:** The brief passes generation validation.

**Expected:** Stop after generation. Do not attach, upload, forward, send, submit, or modify candidate status without a separate user instruction and the applicable delivery or channel gates.

## Scenario 13 — Accompanying Recruiter Message

**Input:** The user separately requests a recruiter message to accompany the brief.

**Expected:** The message may mention the attachment or availability, remains conversational, and does not copy the brief's diagnostic content, gap inventory, or any internal analysis.

## Scenario 14 — Public Framework Privacy

**Input:** Review the framework change set.

**Expected:** It contains no candidate-specific facts, private repository paths, live recruiter-risk records, user-specific filename, or private Source of Truth policy.
