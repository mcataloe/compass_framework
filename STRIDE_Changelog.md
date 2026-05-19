# STRIDE Changelog

All notable framework changes should be documented here.

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
