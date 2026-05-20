# Recruiter-Targeted Resume Prompt

Use this prompt when tailoring for a recruiter rather than a single job description.

```text
Generate a recruiter-targeted staff-level resume using the latest approved source resume or CV.

Before running this workflow, read the latest STRIDE framework files from the connected GitHub repo `mjcataldi/stride_framework` on the `main` branch.

Use the repository as the source of truth for STRIDE behavior. Do not rely on cached STRIDE instructions when the repo is available.

Required framework files:
- VERSION.md
- STRIDE_Current.md
- rules/00-operating-principles.md
- rules/02-resume-generation.md
- rules/04-truthguard.md
- rules/06-artifact-rules.md

If GitHub access fails, say so clearly before proceeding. Do not reconstruct STRIDE behavior from memory unless explicitly authorized.

Position broadly for Staff Engineer / Platform Architect / Senior Technical Consultant opportunities unless otherwise specified.
Preserve the breadth of relevant platform engineering, cloud, distributed systems, modernization, leadership, architecture, compliance, AI systems, and enterprise integration experience.
Do not over-tailor to a single role unless a specific role is provided.
Do not invent technologies, metrics, ownership, credentials, employment history, or experience.
Do not include STRIDE analysis inside the resume artifact.
Use the STRIDE resume skills formatting standard: Core Strength Areas should use synthesized staff-level bullets rather than long one-keyword-per-line inventories, and Technical Skills Inventory should use comma-separated category lines for dense tool and technology coverage.

Generate the resume as a DOCX-first artifact when document-generation tools are available.

For the DOCX artifact, explicitly apply the STRIDE ATS-safe Word formatting standard:
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

Do not rely on Markdown, canvas/textdoc rendering, browser copy/paste, Word theme defaults, Markdown-to-DOCX defaults, or generic export behavior to apply these styles.

If a DOCX artifact cannot be generated or validated, say so clearly in chat and do not claim that Word formatting or page count has been verified.

Markdown and PDF outputs may be provided as secondary exports, but the DOCX artifact is authoritative for formatting and page count.

Create the resume as a clean artifact suitable for Word, PDF, and Markdown export, with DOCX treated as the source of truth when page count or styling matters.

Recruiter name:
[RECRUITER NAME]

Recruiter context, domain, or target role family:
[OPTIONAL CONTEXT]
```

## Notes

Recruiter-targeted resumes should stay broader than cold-apply resumes because recruiters may have access to multiple opportunities.

When document-generation tools are available, recruiter-targeted resumes should be generated DOCX-first with explicit STRIDE ATS-safe Word styles applied. Canvas/textdoc and Markdown versions are reviewable content drafts, not authoritative evidence of Word formatting or pagination.
