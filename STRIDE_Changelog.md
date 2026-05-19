# STRIDE Changelog

All notable framework changes should be documented here.

## vNext 2026-05 — Exact ATS-Safe Word Formatting Defaults

Updated STRIDE's ATS-safe Word resume formatting standard from loose ranges to exact default sizes:

- Name: 16 pt
- Target title line: 14 pt
- Section headers: 13 pt, bold or accent color
- Company / role subheaders: 12 pt, bold
- Body text: 11 pt
- Skills inventory: 11 pt
- Margins: 0.75 inches
- Line spacing: single
- Paragraph spacing: 3–6 pt after paragraphs, reduced to 0–3 pt when page length exceeds the target
- Layout: single-column for the main ATS version

These are now the default STRIDE resume formatting values unless the user explicitly requests a different format or a destination system requires it.

## vNext 2026-05 — ATS-Safe Word Formatting Standard

Added a formatting standard for clean ATS-safe Word resume outputs:

- Name should generally use 16–18 pt type.
- Target title line should generally use 12–13 pt type.
- Section headers should generally use 12–13 pt type, bold or accent color.
- Company / role subheaders should generally use 11–12 pt type, bold.
- Body text and skills inventory should generally use 10.5–11 pt type.
- Use single line spacing with compact paragraph spacing, generally 3–6 pt after paragraphs and 0–3 pt when the resume is near the page budget.
- Use 0.5–0.7 inch margins for standard ATS-safe Word resumes.
- Use a single-column layout for the main ATS resume version.
- Avoid text boxes, tables for core content, icons, rating bars, critical contact information in headers/footers, and design-heavy formatting for standard ATS resumes.
- Prefer compact combined company / role headings when they save space without reducing clarity.

## vNext 2026-05 — Sharp Apply Resume Mode

Added Sharp Apply as an explicit opt-in resume density mode:

- Balanced remains the default STRIDE resume mode and generally targets 3–4 pages.
- Sharp Apply targets a tight 2-page application resume.
- Sharp Apply should be used only when the user explicitly requests "Sharp Apply," "2-page resume," or equivalent language indicating a deliberately compressed artifact.
- Sharp Apply is intended for narrow cold applications, recruiter qualification screens, tightly matched roles, and user-directed resume-length experiments.
- Sharp Apply must preserve Staff-level signal through selected proof rather than breadth.
- STRIDE should not automatically use Sharp Apply for broad Staff, Principal, Platform, Cloud, Federal, or Architect roles unless the user explicitly requests it.

## vNext 2026-05 — Resume Length Discipline

Added framework-level resume length discipline to prevent application resumes from becoming reproduced master CVs:

- Treat comprehensive source resumes / master CVs as private source-of-truth archives, not default submitted artifacts.
- Default cold-application resumes should target 3–4 pages.
- Staff, Principal, Platform, Cloud, Federal, and Architect resumes may use 4–5 pages when the role scope justifies the depth.
- Recruiter broad resumes should generally stay within 4–5 pages.
- Master CV / full archive / federal-style / proposal / bid-support / interview-dossier artifacts may exceed 5 pages only when explicitly requested or clearly required.
- Preserve ATS alignment through targeted evidence selection and truthful role-specific keyword use rather than exhaustive source reproduction.
- Do not include master CV links by default; prefer LinkedIn, portfolio/project links, or “additional detail available upon request” when supplemental detail is useful.

## vNext 2026-05 — Resume Skills Formatting Refinement

Updated resume-generation behavior to improve ATS parseability and human readability:

- Core Strength Areas should use synthesized staff-level bullets instead of long one-keyword-per-line inventories.
- Core Strength subsections should generally target 3–6 synthesized bullets and consolidate when they exceed 5–7 bullets.
- Technical Skills Inventory should use comma-separated category lines for dense tool and technology coverage.
- Pipe-separated lists should be limited to short top-line summaries only.
- Resume prompt templates were updated to reference the skills formatting standard.

## vNext 2026-05 — Initial Repository Baseline

Initialized the STRIDE framework repository with:

- Canonical active framework definition
- Version marker
- Operating principles
- Analysis workflow rules
- Resume generation rules
- Cover letter generation rules
- TruthGuard rules
- Remote and compensation risk rules
- Artifact separation rules
- Prompt templates
- Example output patterns

## Change Management Rules

When changing STRIDE:

1. Update the relevant framework or rules file.
2. Update `VERSION.md` if the change materially affects framework behavior.
3. Add a changelog entry explaining what changed and why.
4. Preserve backward compatibility unless the change intentionally supersedes prior behavior.
5. Avoid burying major behavior changes only inside prompt templates.

## Versioning Guidance

Use date-based framework versions until semantic versioning becomes useful.

Recommended format:

`vNext YYYY-MM`

Example:

`vNext 2026-05`
