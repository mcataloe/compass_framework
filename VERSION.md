# STRIDE Version

Current STRIDE Version: vNext 2026-05

Canonical Branch: main

Status: Active

Initialized: 2026-05-18

## Version Rule

The version declared here governs the active framework behavior when used from the `main` branch.

When STRIDE changes materially, update this file and `STRIDE_Changelog.md` in the same change set.

## Active Behavior Notes

The active vNext 2026-05 framework includes resume length discipline:

- Comprehensive source resumes / master CVs are treated as source-of-truth archives, not default submitted application resumes.
- STRIDE-tailored application resumes should be length-bounded by use case, generally 3–4 pages for cold applications and 4–5 pages for Staff / Principal / Platform / Cloud / Federal / Architect roles when depth is justified.
- When a user specifies a resume page length or page limit, the page count refers to the rendered Word/DOCX artifact using the STRIDE ATS-safe Word formatting standard, not to a canvas/textdoc preview, Markdown view, browser render, or unformatted copy/paste result.
- Page limits are maximums in the generated Word/DOCX artifact. Do not exceed the stated limit unless the user explicitly approves the overflow.
- Balanced remains the default resume density mode unless the user explicitly requests another mode.
- Sharp Apply is an explicit opt-in 2-page resume mode for narrow cold applications, recruiter qualification screens, tightly matched roles, or user-directed resume-length experiments.
- Resume generation should preserve ATS alignment through targeted evidence selection and truthful role-specific keyword use, not exhaustive source reproduction.
- Master CV links should not be included by default.
- ATS-safe Word formatting must be explicitly applied during resume generation for DOCX artifacts: 16 pt name, 14 pt target title, 13 pt section headers, 12 pt company / role subheaders, 11 pt body text, 11 pt skills inventory, 0.75 inch margins, single line spacing, 3–6 pt paragraph spacing reducible to 0–3 pt near the page target, single-column ATS layout, and compact combined company / role headings when clear.
- Canvas/textdoc resume artifacts are reviewable content drafts and cannot by themselves guarantee Word pagination or exact Word font/style behavior. When page length matters, generate or validate an actual DOCX artifact.

## Compatibility Rule

Future STRIDE changes should preserve the core operating principles unless explicitly superseded:

- Truthful source-grounded output
- Phased workflow
- Staff-level positioning unless another target is explicitly requested
- No fabricated technologies, metrics, credentials, employment history, or project ownership
- Separate strategic analysis from resume and cover-letter artifacts
- Length-bounded application resumes derived from comprehensive source resumes / master CVs unless a full CV, federal-style resume, proposal, bid-support document, interview dossier, or archive is explicitly requested
- Balanced resume mode remains the default unless the user explicitly requests Sharp Apply, Concise, Comprehensive, full CV, or another named resume mode
- Standard ATS resume formatting remains single-column and compact unless the user explicitly requests a design-heavy or non-ATS presentation version
- User-specified page lengths are interpreted as maximum rendered Word/DOCX page counts under the STRIDE ATS-safe Word formatting standard
