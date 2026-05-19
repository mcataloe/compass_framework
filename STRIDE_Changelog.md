# STRIDE Changelog

All notable framework changes should be documented here.

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
