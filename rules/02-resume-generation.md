# 02 - Career Profile: Resume Generation

This file governs COMPASS career-profile resume artifacts.

## Resume Generation Trigger

Do not generate a resume during the analysis phase unless the user explicitly requests resume generation.

## Source Requirements

A tailored resume must be derived from:

1. The user's current direct instruction
2. The verified Intake claim ledger and do-not-claim list when available
3. The latest approved canonical career record
4. Imported resumes, CVs, LinkedIn profiles, and similar artifacts as evidence and provenance only
5. The target job description or recruiter requirement set for terminology and context only
6. The current COMPASS analysis, when available
7. Any user-provided constraints or confirmations

## No-Fabrication Rule

Do not add unverified technologies, ownership, metrics, credentials, team sizes, budgets, customer names, project names, responsibilities, or achievements.

## Master CV vs Application Resume

An imported master CV may be comprehensive by design. Treat it as an evidence archive until material claims are verified through Intake. After verified ingestion, use the canonical source-of-truth record and approved ledgers as the downstream authority.

## Resume Download Formats

Unless a user-specific source-of-truth style guide or explicit user instruction says otherwise, generated downloadable resume artifacts should default to:

1. Word/DOCX
2. PDF
3. Markdown

Use the same human-readable base artifact name across formats. Word/DOCX and PDF filenames should use normal spaces. Markdown filenames may use underscores when useful for repository or plain-text workflows. Do not URL-encode spaces in final user-facing filenames.

User-specific source-of-truth rules override these default resume download formats and file-naming rules when present.

## Resume Length Policy

Default target length by use case:

- Cold application resume: 3-4 pages
- Staff / Principal / Platform / Cloud / Federal / Architect resume: 4-5 pages maximum when role scope justifies the depth
- Recruiter broad resume: 4-5 pages maximum
- Sharp Apply resume: 2 pages, only when explicitly requested
- Concise resume: 2-3 pages
- Master CV / full archive: unlimited, but only when explicitly requested

## Artifact Separation

A resume artifact must not include COMPASS scoring, ATS matrix commentary, compensation strategy, risk notes, recruiter objection notes, framework explanations, or private tactical notes.

## Human Authenticity

Resumes should be evidence-led and candidate-specific.

Professional summaries should identify the candidate's actual positioning rather than using generic branding language.

Bullets should preserve actual scope, technology, role, contribution level, and outcome when those details are source-backed.

Use target terminology only when supported by source evidence, verified claim ledgers, or the user's direct confirmation. Do not use target keywords as experience when source evidence is missing.

Avoid unnatural bullet symmetry, buzzword stacking, inflated executive language, and repeated formulaic phrasing.

Keep ATS-safe formatting intact. Human Authenticity must not add hidden text, parser tricks, fake imperfections, or AI-detector evasion tactics.

## Strict Resume Section Order

Tailored resumes must use this section order:

1. Candidate name and contact block
2. Target title line
3. Professional summary
4. Core skills
5. Professional experience
6. Selected projects or delivery highlights, when source-backed and useful
7. Education
8. Certifications, clearances, or credentials, only when verified

Recruiter-targeted resumes must use this section order:

1. Candidate name and contact block
2. Broad target title line
3. Recruiter-facing summary
4. Role families or target areas
5. Core skills
6. Professional experience
7. Representative achievements or projects, when source-backed and useful
8. Education
9. Certifications, clearances, or credentials, only when verified

If a section has no verified source-backed content, omit it rather than filling it with unsupported claims. Do not mark gaps inside the resume artifact.

## ATS-Safe Word Formatting Standard

Required formatting for Word/DOCX exports:

- Name: 16 pt
- Target title line: 14 pt
- Section headers: 13 pt, bold or accent color
- Company / role subheaders: 12 pt, bold
- Body text: 11 pt
- Skills inventory: 11 pt
- Margins: 0.75 inches
- Line spacing: single
- Paragraph spacing: 3-6 pt, reducible to 0-3 pt near page target
- Layout: single-column ATS version
