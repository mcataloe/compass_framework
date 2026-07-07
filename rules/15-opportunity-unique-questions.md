# 15 — Opportunity-Unique Application Questions

This file governs detection, classification, and optional draft preparation for application or qualification questions that are specific to a role, employer, domain, technology, portfolio expectation, work sample, or narrative screen.

## Purpose

Opportunity-unique questions expose hidden hard screens, role-specific evidence expectations, application friction, and preparation burden that may not be obvious from the job description alone.

The goal is to identify and prepare for these questions without silently submitting applications, answering legal attestations, answering sensitive voluntary fields, or inventing candidate evidence.

## When This Rule Applies

Use this rule with COMPASS Verified Opportunity Search when an accessible employer-controlled application flow, recruiter-controlled qualification flow, or accountable application screen exposes questions beyond ordinary contact, resume, location, and standard compliance fields.

This rule may also be used during single-opportunity COMPASS Analysis, application preparation, recruiter qualification preparation, interview preparation, or follow-up drafting when the user asks about role-specific questions.

## Relationship to Verified Opportunity Search

In Verified Opportunity Search, apply this rule after the role has passed the earlier gate sequence for status, live access, eligibility, hard screens, compensation or career constraints, candidate alignment, opportunity quality, and conversion-condition ranking.

Do not spend significant tailoring effort on a role that failed an earlier non-negotiable gate merely because its role-specific questions are interesting.

## Definitions

### Opportunity-unique question

A question is opportunity-unique when it materially asks for role-specific evidence, examples, artifacts, portfolio links, technical judgment, domain experience, narrative explanation, writing samples, work samples, architecture examples, AI or tool experience, product-specific familiarity, leadership examples, open-source work, security or compliance experience, or other evidence connected to the particular opportunity.

Examples include:

- public artifact, portfolio, GitHub, blog, talk, documentation, or writing-sample requests;
- narrative questions about experience with a named technology, domain, architecture pattern, product area, or customer segment;
- prompts asking for a representative project, technical decision, tradeoff, incident, design, migration, leadership example, or evaluation process;
- employer-specific questions about why the role or mission is relevant;
- short-answer hard screens that ask for years, production depth, scale, public evidence, domain tenure, specific tool depth, or comparable experience;
- recruiter qualification questions that shape whether the user should proceed, contact first, apply, or pass.

### Standard administrative field

A standard administrative field includes name, email, phone, location, LinkedIn, resume upload, compensation expectation, availability, ordinary work authorization, sponsorship, current company, referral source, and similar routine application metadata.

Some standard administrative fields may still require user confirmation under Source of Truth or privacy policy.

### Sensitive or voluntary demographic field

Sensitive or voluntary demographic fields include race, ethnicity, gender, gender identity, sexual orientation, disability, medical status, veteran or military status, and similar equal-employment, demographic, or personal-status questions.

These fields must be classified separately and must not be answered automatically.

## Required Inspection Behavior

When the application or qualification flow is accessible, inspect only as deeply as the workflow safely permits without submitting an application, accepting terms, creating an account unnecessarily, or making a legal representation.

State the deepest stage inspected using the existing application-stage visibility labels from `rules/12-verified-opportunity-search.md`.

For each reported opportunity, include an `Opportunity-unique questions` subsection when any non-standard questions are visible, or state `No visible opportunity-unique questions found` when the accessible flow was inspected and none were exposed.

If the application endpoint is reachable but fields are hidden, gated behind account creation, loaded only after file upload, or inaccessible, state the limitation rather than guessing.

## Classification

Classify each visible question as one of:

- `Verified answer` — the exact answer is directly supported by verified Source of Truth or user-provided current facts.
- `Draft answer — user review` — a source-grounded answer can be prepared, but the user should review before submission.
- `User confirmation required` — the answer involves personal judgment, legal or employment attestation, availability, compensation, current-employer presentation, relocation, travel, sponsorship, work authorization, conflict, representation, confidentiality, or another user-owned declaration.
- `Do not answer automatically` — the question asks for sensitive or voluntary demographic, disability, medical, veteran, gender, ethnicity, or similarly protected information, or the user's Source of Truth marks the category as non-automatic.
- `Unsupported / disqualifying` — the required answer would be false, unsupported, or materially inconsistent with verified evidence.

Do not collapse several questions into one classification when one field is answerable and another requires user confirmation.

## Draft Answer Rules

Draft answers may be prepared only when they are grounded in verified Source of Truth, approved claim ledgers, user-provided current context, or public artifacts the user has authorized for use.

Draft answers must:

- answer the question actually asked;
- preserve claim depth and do-not-claim boundaries;
- distinguish public artifacts from private or confidential work;
- distinguish direct experience from adjacent or transferable experience;
- avoid invented metrics, production scale, adoption, outcomes, ownership, technologies, credentials, or domain claims;
- avoid pretending confidential, federal, client, or employer-owned work is public;
- avoid claiming public code, open-source adoption, model benchmarks, eval pipelines, or production LLM systems unless supported;
- be suitable for user review, not represented as submitted.

When a question requests public artifacts and the user's strongest relevant work is private, provide public artifacts first when available, then a brief source-grounded private-work summary within confidentiality limits.

When a question requests LLM, AI, GenAI, evaluation, or coding-agent experience, distinguish:

- AI-assisted software-delivery governance;
- LLM-output, factuality, or model-quality evaluation;
- RAG or source-grounded retrieval design;
- productized AI features;
- private conceptual, architectural, or advisory experience;
- public repositories or write-ups.

Do not blur these categories to improve fit.

## Output Requirements

For every reported role where application-stage questions are visible, include:

- application-stage visibility;
- opportunity-unique questions found;
- classification for each material question;
- evidence basis or source limitation;
- draft answer when safely source-grounded and useful;
- items requiring user confirmation;
- sensitive or voluntary fields labeled `Do not answer automatically` without answer content.

If space is limited in a search shortlist, summarize only the most material unique questions in the main result and offer a separate application-question packet for the selected role.

## Action Boundaries

This rule does not authorize application submission, recruiter contact, legal attestation, account creation, compensation acceptance, representation acceptance, file upload, sensitive-information disclosure, or candidate-status updates.

Preparing a draft answer does not mean the answer was submitted. Inspecting a form does not mean the user applied.

User-specific Source of Truth policies may tighten these boundaries and may define categories that must always remain user-confirmed or non-automatic.