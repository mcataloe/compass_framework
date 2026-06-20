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

## Staff and Principal Evidence Prioritization

For Staff Engineer, Principal Engineer, Architect, senior platform, and comparable senior individual-contributor resumes:

- Preserve the candidate's official employment titles. Communicate operating level through verified scope, decisions, influence, and accountability rather than title inflation.
- Prioritize verified evidence of architecture ownership, technical direction, cross-team influence, organizational leverage, mentoring or enablement, operational accountability, and hands-on implementation.
- Place the strongest target-relevant evidence in the professional summary and the early bullets of recent relevant roles.
- Order bullets primarily by target relevance, contribution depth, decision consequence, and reviewer value rather than merely by chronology.
- Do not bury approved `Owned` or `Led others` evidence beneath long technology inventories or lower-signal task descriptions.
- Preserve contributor-level work when it is the strongest truthful evidence. Senior positioning must not erase collaboration or imply authority the candidate did not have.
- Keep broad recruiter resumes sufficiently versatile, but still lead with the candidate's strongest verified senior-level signals.

## Claim-Depth-Aware Wording

Use the approved claim depth to constrain wording. The following is non-exhaustive semantic guidance, not a word-substitution engine:

| Claim depth | Generally safe wording when context supports it |
|---|---|
| Awareness | familiar with, researched, developed awareness of |
| Exposure | encountered, worked around, participated in discussions involving |
| Supported | supported, contributed to, collaborated on, assisted with |
| Implemented | built, developed, configured, integrated, migrated, implemented |
| Owned | owned, established, drove within a defined scope, was responsible for |
| Led others | led, guided, directed, served as technical lead, shaped direction across contributors |

Safeguards:

- Select wording from the actual work context, not from the table alone.
- Mixed-depth claims must preserve each boundary. Architecture leadership, implementation, operational ownership, and people leadership may have different approved depths.
- `Owned` does not automatically mean `Led others`.
- `Led others` does not imply sole contribution, sole authorship, or personal implementation of every component.
- Initial leadership followed by transition must preserve sequence and later ownership boundaries.
- Technical Product Owner, primary technical contact, architect, and similar role-context claims do not automatically imply formal people management.
- Mentoring, onboarding, interviewing, or technical enablement do not imply formal management unless formal management is separately verified.
- Formal management remains valid evidence even when it occurred outside a conventional software-engineering title.
- Vague verbs such as `supported`, `helped`, `participated`, and `worked with` should be replaced with a more specific verified action when the source record supports one; they must not be mechanically upgraded to leadership or ownership language.

## Evidence-Grounded Outcomes

- Numerical metrics are useful only when verified by source evidence, an approved claim ledger, or direct user confirmation.
- Qualitative consequences are valid when source-backed and material to the work.
- Qualitative outcomes may include reduced delivery risk, preserved service or architecture continuity, clarified ownership, enabled a technical or business decision, improved maintainability, reduced duplication, improved operational visibility, or made a material tradeoff explicit.
- Distinguish an intended benefit, evaluated tradeoff, recommendation, implementation result, and realized outcome.
- Do not convert a plausible consequence into a claimed realized result without evidence.
- Do not force a metric into every bullet. Specific scope, decision authority, technical consequence, and stakeholder value may communicate impact without a percentage or dollar figure.

## Bullet Construction and Prioritization

Prefer a useful combination of:

1. Problem, constraint, or operating context
2. Candidate action or decision
3. Relevant technical mechanism
4. Scope, collaborators, or stakeholders
5. Outcome, consequence, or operational value

Not every bullet must contain all five components. Use the minimum structure needed to make the candidate's contribution and its significance clear.

Additional rules:

- Lead with the candidate's verified action or decision when that is clearer than leading with the technology.
- Keep technical detail subordinate to the work it explains.
- Consolidate overlapping bullets when they describe the same underlying contribution.
- Use project or initiative subheadings when they improve scanability, not merely to reproduce a master-CV project log.
- Preserve enough technical specificity to establish credibility and target-role alignment.

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

## Resume Typography Contract

This section defines the generic COMPASS typography schema for generated resume artifacts. User-specific source-of-truth style guides may override any value using the same named section, field, or rule.

### Authority and Fallback

- `rules/02-resume-generation.md` defines the generic COMPASS resume typography default.
- A user-specific source-of-truth style guide may override any value using the same named section and field.
- User-specific values control over framework defaults.
- Missing user-specific values fall back to the framework defaults in this section.
- Target job descriptions may influence wording, emphasis, and role terminology, but they do not alter typography unless the user explicitly requests a special layout.
- Do not infer missing typography values from prior generated resumes unless the source-of-truth style file or current user instruction confirms them.
- Preserve source priority, TruthGuard, and artifact cleanliness regardless of typography choices.

### Global Typography Defaults

- Font family: Arial or similarly clean ATS-safe sans-serif.
- Accent color: use a restrained blue or neutral accent when a color is used; otherwise use black for maximum compatibility.
- Body text: 11 pt.
- Margins: 0.75 inches.
- Line spacing: single.
- Paragraph spacing: 3-6 pt, reducible to 0-3 pt near a page target.
- Layout: single-column ATS-safe layout.
- Bullets: native Word bullets/list formatting, not typed bullet characters when DOCX generation supports list formatting.
- Wrapped bullet lines should align under the bullet text rather than under the bullet marker.

### Candidate Name and Contact Block

#### Name / Title-Name Line

- Text source: candidate legal or preferred resume name.
- Font size: 16 pt.
- Color: accent color or black.
- Weight: regular, medium, or bold according to the active style guide.
- Character spacing: normal unless a user-specific style guide specifies expanded or condensed character spacing.
- Alignment: centered.
- Paragraph spacing before: 0 pt.
- Paragraph spacing after: 0 pt.
- Line spacing: single.
- Rule: this must be the largest text in the resume header.

#### Target Role Descriptor / Target Title Line

- Text source: tailored target title and descriptor.
- Font size: 13-14 pt by default.
- Color: black or accent color according to the active style guide.
- Alignment: centered.
- Wrapping: keep to one line when reasonable; shrink slightly before wrapping only if readability and ATS safety are preserved.
- Paragraph spacing before: 0 pt.
- Paragraph spacing after: 0 pt.
- Line spacing: single.
- Rule: this line should be smaller than the name and larger than the contact text.

#### Contact and Links

- Text source: location, remote status when relevant, clearance when relevant, phone, email, LinkedIn, GitHub, portfolio, or other approved links.
- Font size: 9-10 pt by default.
- Alignment: centered.
- Paragraph spacing before: 0 pt.
- Paragraph spacing after: 0 pt.
- Line spacing: single.
- Hyperlinks: preserve readable URL text and avoid decorative icons.
- Do not add unapproved websites, portfolios, handles, credentials, or social links.

### Section Headers

Applies to:

- `PROFESSIONAL SUMMARY`
- `CORE SKILLS`
- `PROFESSIONAL EXPERIENCE`
- `SELECTED PROJECTS` or `SELECTED PROJECTS OR DELIVERY HIGHLIGHTS`
- `EDUCATION`
- `CERTIFICATIONS, CLEARANCES & CREDENTIALS`

Defaults:

- Font size: 13 pt.
- Color: accent color or black.
- Weight: bold.
- Case: uppercase.
- Paragraph spacing before: compact but visible.
- Paragraph spacing after: compact.
- Line spacing: single.

### Professional Summary

- Structure: single paragraph unless a user explicitly requests otherwise.
- Font size: body text size.
- Alignment: left.
- Paragraph spacing before: compact.
- Paragraph spacing after: compact.
- Rule: do not use bullets in the professional summary.
- Rule: keep the summary source-grounded and tailored without adding unsupported claims.

### Core Skills

- Structure: grouped skill lines or bullets.
- Category labels: bold.
- Skill text: comma-separated skills.
- Font size: body text size.
- Bullet type: native Word bullet/list formatting when bullets are used.
- Bullet indentation: compact.
- Hanging indent: wrapped lines align under the bullet text.
- Rule: include only skills supported by the source record, approved ledgers, or the user's direct confirmation.

### Professional Experience

#### Company Heading

- Font size: 12 pt by default.
- Weight: bold.
- Color: black unless the active style guide specifies otherwise.
- Paragraph spacing before: modest, especially between roles.
- Paragraph spacing after: compact.

#### Role / Metadata Line

- Content pattern: `Role Title | Date Range | Location / Remote | Clearance or credential context where relevant`.
- Font size: body text size.
- Style: italic or regular according to the active style guide.
- Paragraph spacing before: 0 pt.
- Paragraph spacing after: compact.
- Preserve the official employment title unless the source record explicitly approves a normalized or dual-title presentation.
- Communicate senior operating level through verified evidence in the summary and bullets, not by silently rewriting the official title.

#### Experience Bullets

- Font size: body text size.
- Bullet type: native Word bullet/list formatting.
- Bullet indentation: compact.
- Hanging indent: wrapped lines align under the bullet text.
- Paragraph spacing: compact.
- Rule: preserve actual scope, technology, contribution depth, and outcome when source-backed.
- For senior-IC target roles, apply the Staff and Principal Evidence Prioritization, Claim-Depth-Aware Wording, Evidence-Grounded Outcomes, and Bullet Construction rules above.

#### Role-to-Role Spacing

- Add a modest visual gap between the final bullet of one role and the next company heading.
- Do not add a large gap before the first role immediately under the `Professional Experience` section header.

### Selected Projects or Delivery Highlights

- Use only when source-backed and useful.
- Section header follows section-header typography.
- Project heading follows company/project subheading typography.
- Body text follows body text typography.
- Bullets follow standard bullet typography.
- Omit this section if it would duplicate the Professional Experience section without adding scanability.

### Education

- Section header follows section-header typography.
- Entries use body text typography.
- Keep concise.
- May use bullets or compact lines.

### Certifications, Clearances, or Credentials

- Section header follows section-header typography.
- Entries use body text typography.
- Include only verified credentials, certifications, clearances, or licenses.
- Do not imply active status unless verified.
