# 17 - COMPASS Comprehensive Career CV

## Purpose

The COMPASS Comprehensive Career CV is a broad, human-readable and ATS-readable career publication generated from the current approved career Source of Truth.

It fills the gap between a role-specific resume and a browsable experience repository. It is intended for recruiters, hiring managers, interviewers, and other reviewers who need a coherent single-document view of the candidate's approved professional history.

The comprehensive CV is a generated publication view. It is not a canonical career record, claim ledger, evidence archive, dossier collection, or substitute Source of Truth.

## Trigger

Use this rule only when the user explicitly asks for a comprehensive career CV, master CV, full career CV, complete career history document, or invokes:

```text
COMPASS Comprehensive Career CV
```

Do not replace a targeted application resume with a comprehensive CV by default.

## Authority and Source Resolution

Before drafting:

1. Apply the user's current direct instruction.
2. Resolve the current career Source of Truth and its authority mode.
3. Retrieve applicable approved claim ledgers and do-not-claim records.
4. Retrieve the canonical employment timeline and every material governing role or project record.
5. Retrieve coverage and source registers needed to determine whether a scope is approved, provisional, incomplete, rejected, or intentionally excluded.
6. Retrieve the most specific user-owned CV, resume, artifact, disclosure, filename, and work-mode policies.
7. Treat imported resumes and prior CVs only as evidence or an explicitly authorized provisional fallback.

When the requested CV spans multiple roles or projects, resolve each material scope independently. Do not use one broad resume, profile, or dossier as a substitute for the applicable records.

A source conflict, unresolved material date conflict, or incompatible claim-depth record blocks the affected content. Do not select the more favorable wording.

## Compilation, Not Concatenation

The CV must compile approved evidence into a readable career narrative. It must not concatenate dossiers or reproduce Source of Truth records.

Exclude from the clean CV:

- evidence inventories;
- claim status labels;
- do-not-claim rationale;
- Intake questions or checkpoints;
- internal collaborator names when unnecessary;
- private source paths or repository locations;
- private strategy, compensation, opportunity analysis, or framework commentary;
- repeated architecture inventories that obscure the candidate's action, scope, decision, or consequence.

Preserve contribution boundaries, implementation stages, collaborator transitions, environment maturity, and qualitative outcome limits in natural external language.

## Coverage Gate

Every canonical employment role must receive one internal disposition:

- `detailed`;
- `compressed`;
- `excluded`, with a source-grounded reason.

A role may be excluded from a public CV when its only available material is provisional and public policy forbids provisional publication. The omission must be disclosed in completion notes or reconciliation reports, not inside the clean CV.

Do not call a document a complete verified history when material employment or project scopes remain unresolved and omitted. Use wording such as `comprehensive approved career history` or `comprehensive career CV based on currently approved records` when that distinction matters.

## Variants

### Recruiter Variant

The recruiter variant may include approved direct contact information and broader recruiter-facing positioning. It may use authorized provisional content only when the user's Source of Truth explicitly permits it for this audience and the content remains at its documented source-stated depth.

### Public Variant

The public variant must pass both:

1. the Truth Gate; and
2. the Publication Gate from COMPASS Experience Sync.

Unless the current user explicitly approves otherwise, the public variant must:

- exclude phone number, personal email, home address, and other direct PII;
- exclude private strategy and raw Intake material;
- omit individual colleague names;
- abstract customer-sensitive and security-sensitive implementation detail;
- exclude unresolved or provisional claims when the target publication policy forbids them;
- avoid exposing the private Source of Truth repository name or URL;
- remain a one-way downstream projection.

Publishing the public variant into an experience repository must use COMPASS Experience Sync and its branch-and-pull-request policy.

## Required Structure

Use this section order unless the user's current instruction or a more specific user-owned style policy requires a different order:

1. Candidate name
2. Broad professional title or positioning line
3. Professional profile
4. Core capability areas
5. Professional experience
   - employer;
   - official role title and dates;
   - concise role context;
   - major approved projects or initiatives;
   - contribution and outcome bullets.
6. Independent products and selected technical work, when approved and materially distinct
7. Earlier professional experience
8. Technical capability index, when it improves retrieval without duplicating the experience section
9. Education
10. Certifications, clearances, and credentials
11. Public evidence links, when approved and useful

The document may be longer than a normal resume. Length is determined by approved career breadth and reviewer value, not by a fixed page target.

## Human and ATS Readability

The same factual CV should serve both human and parser review unless the user requests a materially different system-specific variant.

Use:

- a single-column structure;
- standard section headings;
- ordinary employer, title, date, and project hierarchy;
- native bullets in DOCX;
- straightforward typography;
- text-based links;
- consistent date formats;
- no sidebars, graphics, icons, text boxes, hidden text, or parsing tricks;
- enough technical specificity to establish credibility without keyword dumping.

ATS-readable does not mean role-optimized. State in completion notes that targeted resumes remain the default application artifact.

## Claim and Stage Discipline

Preserve the difference among:

- designed;
- implemented;
- evaluated;
- supported;
- operated;
- prototype or proof of concept;
- test or integration;
- non-production;
- production;
- attributed post-transition outcomes.

Do not convert design into implementation, test into production, an intended benefit into a realized outcome, team activity into sole ownership, or an attributed later result into the candidate's delivery ownership.

## Generation and Reconciliation Metadata

A repository-published public CV should record, outside the clean CV body when practical:

- generation or reconciliation date;
- framework version;
- sanitized stable source identifier;
- source commit or revision identifier that does not expose a private repository location;
- target commit;
- publication audience;
- whether provisional claims were allowed;
- coverage exclusions;
- latest Experience Sync report path.

The generated CV never becomes factual authority merely because it has a commit history.

## Filenames and Formats

Use the user's current filename policy when available. The recommended artifact type label is:

```text
Comprehensive Career CV
```

For a broad, non-company-specific artifact, use the configured general-company and broad-title segments rather than omitting required filename segments.

Resolve the user's current artifact-format policy before generation. When that policy requires DOCX for resume-class or Comprehensive Career CV releases, DOCX is mandatory and Markdown is a companion format only; a Markdown-only result is a blocked CV release. When the user-owned policy is silent, the generic text default is Markdown. Generate DOCX only when the applicable artifact-release contract supports the comprehensive-CV filename, required sections, employment coverage, and publication path.

## DOCX Release Assurance

A downloadable comprehensive-CV DOCX is a resume-class artifact and must pass `rules/16-resume-release-assurance.md` plus any stricter user-specific release profile.

If the active release contract covers only conventional resume filenames or sections, do not relabel an unvalidated DOCX as final. Update and validate the applicable contract first. Releasing only another format is permitted only when the user-owned format policy does not require DOCX.

Aggregate `FAIL` blocks DOCX delivery. Aggregate `UNKNOWN`, missing template verification, unavailable rendering, or missing every-page visual review blocks final DOCX publication; an applicable user-owned Source of Truth may authorize delivery only as `Generated — Release Validation Pending` under `rules/16-resume-release-assurance.md`. Missing material employment coverage, unsupported claims, unreadable output, or an inspectable canonical filename mismatch remains a hard delivery blocker.

## Output Separation

Keep these separate:

1. the clean recruiter or public CV;
2. the internal coverage plan;
3. the Experience Sync or source reconciliation report;
4. source conflicts and withheld-content notes;
5. DOCX release manifests and visual attestations.

Do not leak internal evidence mechanics into the external CV.

## Final Validation

Before release, verify:

- every material factual claim is supported at the published depth;
- every canonical role has an internal disposition;
- employment dates are consistent with controlling date records;
- no rejected or forbidden claim appears;
- public disclosure rules are satisfied;
- public and recruiter variants differ only where audience policy requires it;
- the CV is readable without repository context;
- repository links are supplemental rather than required to understand the career history;
- the document is not presented as a targeted application resume;
- generated outputs are not treated as Source of Truth records.
