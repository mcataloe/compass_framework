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

## Density Modes

### Concise

Use when the user needs a shorter resume or when the role is narrower.

### Balanced

Default mode. Preserve enough breadth for staff-level signal while improving role-specific alignment.

### Comprehensive

Use when the user wants a broad recruiter-facing resume or when the role values wide architecture and platform scope.

## Tailoring Priorities

Tailor in this order:

1. Professional summary
2. Staff/principal positioning section
3. Core skills and technical strengths
4. Most relevant recent roles
5. Selected project themes
6. Older roles only when they add useful evidence

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

Use concise bullets for meaning-rich staff-level strengths, strategic capabilities, architectural themes, and product/platform positioning.

Preferred use cases:

- Core Strength Areas
- Staff / Principal Engineering Positioning
- Selected Architecture Patterns when short and curated
- Role-specific product, platform, leadership, reliability, or architecture themes

Bullets in these sections should communicate capability and seniority, not behave like exhaustive keyword dumps.

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
- Free of internal STRIDE analysis
- Consistent with the source resume timeline
