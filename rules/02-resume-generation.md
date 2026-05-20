# 02 — Resume Generation

This file governs STRIDE-tailored resume artifacts.

## Resume Generation Trigger

Do not generate a resume during the analysis phase unless the user explicitly requests resume generation.

## Source Requirements

A tailored resume must be derived from:

1. The latest approved source resume or CV
2. The target job description or recruiter requirement set
3. The current STRIDE analysis, when available
4. Any user-provided constraints or confirmations

## No-Fabrication Rule

Do not add unverified technologies, ownership, metrics, credentials, team sizes, budgets, customer names, project names, responsibilities, or achievements.

If a job description asks for something not present in the source resume, either omit it or mention it only as adjacent experience when that is truthful.

## Resume Artifact Separation

A resume artifact must not include:

- STRIDE scoring
- ATS matrix commentary
- Compensation strategy
- Risk notes
- Recruiter objection notes
- Framework explanations
- Private tactical notes

## Master CV vs Application Resume

The latest approved source resume or CV may be comprehensive by design. Treat it as the source-of-truth archive, not as the application artifact.

A STRIDE-tailored resume should select, compress, and prioritize source evidence for the target role. Do not reproduce the master CV exhaustively unless the user explicitly requests a full CV, federal-style resume, or comprehensive archive.

The goal is to preserve truthful ATS alignment while making the resume readable for recruiters and hiring managers. More source material is not automatically better once a human reviewer sees the document.

## Resume Length Policy

Default target length by use case:

- Cold application resume: 3–4 pages
- Staff / Principal / Platform / Cloud / Federal / Architect resume: 4–5 pages maximum when role scope justifies the depth
- Recruiter broad resume: 4–5 pages maximum
- Sharp Apply resume: 2 pages, only when explicitly requested or clearly selected by the user
- Concise resume: 2–3 pages when the user requests brevity or the role is narrow
- Master CV / full archive: unlimited, but only when explicitly requested

Do not generate a 10+ page application resume by default. A 20-page master CV is appropriate as a private source archive, but it should not be treated as the standard submitted resume.

When the user states a page length or page limit, the page count refers to the rendered Word/DOCX artifact using the STRIDE ATS-safe Word formatting standard. It does not refer to a canvas/textdoc preview, Markdown view, browser render, pasted text without styles, or any unformatted representation.

A stated page limit is the maximum allowed page count in the generated Word/DOCX file. The generator must compress, consolidate, or remove lower-priority evidence until the rendered Word/DOCX artifact fits within the stated maximum. Do not exceed the page limit unless the user explicitly approves the overflow.

If content cannot fit within the page maximum without weakening readability or truthfulness, prioritize truthful role-relevant proof, remove repeated or lower-value evidence, and explain the tradeoff outside the resume artifact. Do not hide overflow inside smaller-than-standard formatting.

Only exceed 5 pages when one of the following is true:

- The user explicitly requests a full CV, federal-style resume, or exhaustive archive
- The application instructions specifically request comprehensive project history
- The target artifact is a proposal, bid-support document, interview dossier, or internal career archive rather than a standard resume
- The user explicitly approves exceeding the normal page maximum after being told why compression would weaken the artifact

## Density Modes

### Balanced

Default mode. Preserve enough breadth for staff-level signal while improving role-specific alignment.

Target length: 3–4 rendered Word/DOCX pages under the STRIDE ATS-safe Word formatting standard.

Balanced remains the standard STRIDE resume mode unless the user explicitly requests another mode. Do not silently downgrade Balanced to Sharp Apply just because a role is narrow.

Balanced page targets are maximums unless the user explicitly says the page count is approximate or minimum. A Balanced resume should not exceed 4 rendered Word/DOCX pages by default.

### Sharp Apply

Opt-in mode for a tight 2-page resume.

Target length: 2 rendered Word/DOCX pages under the STRIDE ATS-safe Word formatting standard.

Use Sharp Apply only when the user explicitly requests "Sharp Apply," "2-page resume," or equivalent language indicating a deliberately compressed application artifact.

Sharp Apply is intended for:

- Narrow cold applications with clear target requirements
- Recruiter qualification screens where fast human review matters
- Roles with a tight technology/domain match
- Situations where the user wants to test a shorter resume against the Balanced Staff resume

Sharp Apply must preserve staff-level signal through selected proof rather than breadth. It should prioritize the strongest role-specific evidence, compress older roles aggressively, use compact skills formatting, and avoid master-CV-style completeness.

Do not use Sharp Apply automatically for broad Staff, Principal, Platform, Cloud, Federal, or Architect roles unless the user explicitly requests it.

### Concise

Use when the user needs a shorter resume or when the role is narrower, but has not specifically requested the 2-page Sharp Apply experiment.

Target length: 2–3 rendered Word/DOCX pages under the STRIDE ATS-safe Word formatting standard.

Concise may be slightly less rigid than Sharp Apply. If the user specifically asks for the 2-page experiment, use Sharp Apply rather than Concise.

### Comprehensive

Use when the user wants a broad recruiter-facing resume or when the role values wide architecture and platform scope.

Target length: 4–5 rendered Word/DOCX pages under the STRIDE ATS-safe Word formatting standard for normal resume use. Do not treat Comprehensive mode as permission to reproduce the full master CV unless the user explicitly asks for a full CV or archive.

## ATS-Safe Word Formatting Standard

STRIDE-generated resume artifacts should be easy to convert into ATS-safe Word, PDF, and Markdown formats.

For DOCX resume artifacts, the formatting below must be explicitly applied during generation. Do not rely on Markdown-to-Word defaults, Word theme mappings, browser copy/paste behavior, or canvas/textdoc rendering to apply these styles.

Required formatting for Word/DOCX exports:

- Name: 16 pt
- Target title line: 14 pt
- Section headers: 13 pt, bold or accent color
- Company / role subheaders: 12 pt, bold
- Body text: 11 pt
- Skills inventory: 11 pt
- Margins: 0.75 inches
- Line spacing: single
- Paragraph spacing: 3–6 pt, reducible to 0–3 pt near page target
- Layout: single-column ATS version

These font sizes are the default STRIDE resume formatting standard, not loose ranges. Only deviate when the user explicitly requests a different format or when a specific destination system requires it.

Paragraph spacing may be reduced to fit the page target, but font sizes must not be reduced below the stated standard simply to satisfy page length unless the user explicitly approves smaller text.

Avoid ATS-risky formatting for standard resumes:

- Two-column main layouts
- Text boxes for important content
- Tables for core experience or skills
- Icons, rating bars, charts, or visual skill meters
- Headers/footers containing critical contact information
- Excessive decorative lines, spacing, or section padding

Formatting should support the resume length policy. If the content is near the page budget, first reduce paragraph spacing within the allowed range, then consolidate repeated content, then remove lower-priority evidence. Do not claim a page target has been met until the rendered Word/DOCX artifact has been checked or generated with these settings.

## DOCX Navigation and Table of Contents

DOCX-first resume artifacts should preserve useful document navigation when the resume is longer than two rendered pages.

Unless the user explicitly requests otherwise, generated DOCX resumes longer than two rendered pages should include a compact Word-compatible table of contents or navigation structure near the beginning of the document when tool support allows it and when doing so does not create ATS risk.

The table of contents should be generated from the resume heading hierarchy rather than manually typed links whenever possible. It should remain compact, plain-text, and based on standard Word heading styles.

Do not use text boxes, multi-column layouts, decorative navigation elements, icons, or nonstandard objects for resume navigation. If the table of contents would push a Balanced resume beyond its page target, compress lower-value content before removing the TOC. Remove the TOC only when keeping it would materially weaken the resume or violate a hard page limit.

## Bullet and Hanging Indentation Rules

Bulleted resume content must use proper hanging indentation in DOCX outputs.

For standard resume bullets, the bullet marker should sit to the left while all wrapped continuation lines align with the first line of bullet text. Continuation lines must not drift farther right or left than the first line of bullet text.

Recommended DOCX behavior:

- Use Word paragraph numbering/bullet properties or an equivalent hanging-indent implementation.
- Keep bullet text aligned consistently across wrapped lines.
- Avoid manually typed bullet symbols when they prevent stable hanging indentation.
- Apply the same indentation rules to Staff-level positioning bullets, Core Strength Areas, Professional Experience bullets, and any other resume bullet lists.
- Validate wrapped bullet behavior visually or through generated DOCX style/numbering inspection when tool support allows it.

## Section and Role Spacing Rules

DOCX resume artifacts should preserve enough vertical separation for human readability while staying within the page target.

Apply modest top spacing before major sections, selected work labels, selected technical environment blocks, and each new role in the Professional Experience section so the reader can visually distinguish one section from the next.

Recommended defaults:

- Major section headings: 8–10 pt before, 3–4 pt after.
- Company / role headings: 8–10 pt before, 2–3 pt after, with slightly more spacing before a new employer or major role group.
- Selected work and selected technical environment lines: 4–6 pt before when following bullets or dense paragraphs.
- Standard body paragraphs and bullets: compact spacing, generally 0–3 pt after, unless additional spacing is required for readability.

If page length pressure exists, reduce lower-value content before eliminating all section separation. Do not create a visually cramped resume simply to preserve excess content.

## Artifact Type and Page Validation

Canvas/textdoc resume artifacts are reviewable content drafts. They are useful for inspecting and editing resume content, but they cannot guarantee exact Word pagination, font sizes, margins, paragraph spacing, or style behavior.

When the user requests or implies a page-count-constrained resume, STRIDE should treat the DOCX artifact as the authoritative artifact for page length and formatting.

If tool support is available, generate or validate the DOCX file with explicit formatting before saying the page limit has been satisfied. If DOCX generation or page validation is not available, state that clearly and describe the content-level compression performed without claiming verified page count.

## Experience Heading Compression

Use compact experience headings when they improve readability and reduce vertical bloat.

Preferred compact pattern for standard resume entries:

```markdown
### Company Name — Role Title
**Dates | Location / Remote | Clearance or credential context when relevant**
```

Use this pattern when a company has one primary role or when the role can be clearly represented on one line.

For consulting roles with multiple client/project subsections, prefer:

```markdown
### Company Name — Role Title
**Dates | Location / Remote | Clearance or credential context when relevant**

**Selected work:** Project A, Project B, Project C
```

Do not split company and role into separate lines by default when combining them preserves clarity. Separate company, role, and project names only when doing so materially improves comprehension, such as when there are multiple roles at the same employer, promotions, overlapping contracts, or several named client engagements that need distinction.

## Tailoring Priorities

Tailor in this order:

1. Professional summary
2. Staff/principal positioning section
3. Core skills and technical strengths
4. Most relevant recent roles
5. Selected project themes
6. Older roles only when they add useful evidence

## Sharp Apply Construction Rules

When generating a Sharp Apply resume:

- Keep the artifact to 2 rendered Word/DOCX pages.
- Make page 1 carry the role fit: title, targeted summary, role-specific alignment, strongest proof, and most relevant recent experience.
- Keep only the strongest 3–4 relevant roles or projects with meaningful detail.
- Compress older roles into short summary lines, grouped prior experience, or omit them when they do not add target-role evidence.
- Use compact, role-specific technical skills rather than broad master-CV inventory coverage.
- Preserve Staff-level signal through cross-system impact, architecture judgment, delivery leadership, and operational reasoning.
- Avoid repeated architecture-pattern blocks and repeated keyword clusters.
- Do not include a master CV link by default.
- If important evidence cannot fit without weakening readability, place the tradeoff note in chat outside the artifact rather than expanding past 2 pages.

## Compression Rules

When deriving a resume from a comprehensive master CV:

- Keep role-relevant proof over broad completeness.
- Select the strongest recent evidence first.
- Compress older roles aggressively unless they provide unique evidence for the target job.
- Avoid repeating the same architecture-pattern language across many roles.
- Keep dense tool coverage in the Technical Skills Inventory instead of repeating it in every experience section.
- Prefer fewer, higher-signal bullets over exhaustive bullet coverage.
- Remove or consolidate bullets that only restate keywords without adding new evidence.
- Use optional appendix-style detail only when the role or user explicitly justifies it.
- Combine company and role headings onto one line when doing so saves space without reducing clarity.
- Treat page targets as layout constraints, not merely content-density labels.

## Master CV Links

Do not include a link to the master CV by default.

A master CV link may be included only when the user explicitly requests it or when the target process clearly benefits from supplemental detail. Prefer LinkedIn, portfolio, or project links over exposing an exhaustive 20-page archive in standard applications.

When extra detail may be useful but a link is not appropriate, use a simple note outside the resume artifact such as: "Additional architecture or project detail available upon request."

## Staff-Level Resume Signal

For staff-level and principal-level roles, emphasize:

- Ambiguous problem decomposition
- Cross-system architecture
- Platform and cloud modernization
- Integration boundaries
- Operational readiness
- Reliability and maintainability
- Stakeholder and executive communication
- Technical leadership without unsupported people-management claims
- Build-vs-buy and vendor evaluation
- Security and compliance collaboration

## Skills Formatting Standard

STRIDE resumes should balance ATS parseability with human readability. Use simple, plain-text formatting that survives Markdown, DOCX, PDF, and applicant-tracking-system parsing.

### Core Strength Areas and Strategic Positioning

Core Strength Areas should communicate strategic capability and staff-level seniority. They should not become exhaustive one-keyword-per-line inventories.

Use concise, synthesized bullets for meaning-rich staff-level strengths, strategic capabilities, architectural themes, and product/platform positioning.

Preferred use cases:

- Core Strength Areas
- Staff / Principal Engineering Positioning
- Selected Architecture Patterns when short and curated
- Role-specific product, platform, leadership, reliability, or architecture themes

Preferred pattern:

```markdown
### Software, Platform, and Product Engineering

- Staff-level architecture across scalable software, SaaS platforms, cloud-native applications, and distributed systems.
- Backend API development, API-first platform design, data modeling, and database migration planning.
- Full-stack product engineering across user-facing workflows, platform services, and integration boundaries.
- Multi-tenant SaaS systems, data ingestion, normalization, analytics, and reporting platforms.
- Maintainable code, refactoring, clean-code practices, and engineering standards.
```

Guidelines:

- Prefer 3–6 synthesized bullets per Core Strength subsection.
- Combine closely related capabilities into readable staff-level statements.
- Use one-skill-per-bullet formatting only for short, high-signal lists.
- If a subsection grows beyond 5–7 bullets, consolidate related items into broader bullets or convert the subsection to a comma-separated category line.
- Keep dense tool and keyword coverage in the Technical Skills Inventory, not in Core Strength Areas.

### Technical Skills Inventory

Use comma-separated category lines for dense technical inventories.

Preferred pattern:

```markdown
## Technical Skills Inventory

**Languages:** C#, TypeScript, JavaScript, Python, SQL, T-SQL, Ruby, VB.NET, VBA, HTML, CSS, SCSS, Razor, JSX/TSX

**Backend & Application Platforms:** FastAPI, Express.js, Node.js, ASP.NET Core, Ruby on Rails, SQLAlchemy, Alembic, Prisma, Entity Framework, Pydantic

**Databases & Data Tools:** PostgreSQL, SQL Server, MySQL, SQLite, DB2, DynamoDB, Athena, SSRS, SSIS, XML data processing

**Cloud & Infrastructure:** AWS, AWS GovCloud, Azure, GCP, ECS, EKS, Fargate, Lambda, API Gateway, RDS, S3, CloudWatch, CloudTrail, Terraform, Docker, Kubernetes

**Frontend:** React, Vite, Next.js, Angular, Vue, Mantine UI, Redux, Bootstrap

**Testing & Delivery:** Jest, NUnit, Jasmine, RSpec, MSTest, TDD, BDD, API testing, GitLab CI/CD, Jenkins, CircleCI, GitHub Enterprise
```

This format keeps important keywords visible to ATS systems while reducing vertical bloat and improving recruiter readability.

### Pipe-Separated Values

Avoid pipe-separated lists as the default technical inventory format.

Pipes may be used sparingly for very short top-line summaries, such as a compact selected-technology line, but should not replace categorized comma-separated inventory sections.

Acceptable limited example:

```markdown
Platform Engineering | Backend Systems | PostgreSQL | Terraform | React | AWS | Distributed Systems
```

Do not use long pipe-separated lists that read as keyword stuffing or become visually noisy.

### Formatting Anti-Patterns

Avoid:

- One bullet per skill in long Core Strength Area subsections
- One bullet per skill in long technical inventory sections
- Dense paragraph-style keyword blocks
- Tables or multi-column skill layouts for ATS-first resumes
- Overly long pipe-separated lists
- Nonstandard symbols, icons, rating bars, or visual skill meters
- Unsupported keywords included only because the job description mentions them

## Keyword Alignment

Use the job description's terminology when truthful. Do not stuff keywords. Each major keyword should connect to real experience.

## Final Resume Quality Bar

The final resume should be:

- Truthful
- ATS-aware
- Staff-level
- Recruiter-readable
- Hiring-manager-readable
- Length-bounded for the target use case
- Free of internal STRIDE analysis
- Consistent with the source resume timeline
- Formatted according to the STRIDE ATS-safe Word formatting standard when generated as DOCX
- Within the stated rendered Word/DOCX maximum page limit when the user provides one
