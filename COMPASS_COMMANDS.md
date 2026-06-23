# COMPASS Command Registry

This file defines the current user-facing COMPASS command surface.

Prompt templates remain workflow launchers, not independent policy sources. When a command is executed, use the active framework files, rule files, and the user's verified source-of-truth records to govern behavior.

## Command Source Priority

When resolving a COMPASS command, use this priority order:

1. The user's direct instruction in the current conversation
2. The user's verified COMPASS Intake claim ledger and do-not-claim list, when available
3. The user's latest approved canonical career source-of-truth record
4. The active COMPASS framework files on the canonical branch
5. Imported artifacts, including Initial Seed Artifacts under `/sources/seed/`, as evidence and provenance only
6. Generated artifacts as historical outputs only
7. ChatGPT memory only when not contradicted by stronger sources

Target job descriptions, recruiter requests, and opportunity records provide target terminology and context only. They do not create experience, skills, ownership, metrics, credentials, achievements, or facts.

## Current First-Class Commands

### COMPASS Intake

**Launcher:** `prompts/compass-intake.md`

**Purpose:** Build or update a verified career source of truth through evidence capture, claim verification, Materiality Gate questioning, coverage tracking, and checkpoint artifacts.

**Use when the user asks to:**

- create a COMPASS Source of Truth
- update an existing COMPASS Source of Truth
- ingest career documents
- stage Initial Seed Artifacts before or during Intake
- verify claims from resumes, CVs, LinkedIn exports, recruiter notes, interview notes, performance reviews, certifications, portfolio notes, or project summaries
- reconcile gaps or contradictions across career source material

**Example trigger phrases:**

```text
Run COMPASS Intake.
Start COMPASS Intake for my career source of truth.
Ingest these source documents with COMPASS.
Update my COMPASS Source of Truth.
```

**Required framework files:**

- `VERSION.md`
- `COMPASS_Current.md`
- `rules/00-operating-principles.md`
- `rules/07-compass-intake.md`
- `prompts/compass-intake.md`

---

### COMPASS Source Rebase

**Launcher:** `prompts/compass-source-rebase.md`

**Purpose:** Safely align an existing COMPASS source-of-truth repository with the current framework-owned scaffold without overwriting, deleting, renaming, moving, or modifying existing user-owned source records.

**Use when the user asks to:**

- run COMPASS Source Rebase
- rebase a COMPASS source-of-truth repository scaffold
- align an existing COMPASS source repository after a framework upgrade
- add missing source-of-truth scaffold structure safely without overwriting current files
- identify missing scaffold directories or placeholder files
- add the missing `/sources/seed/` scaffold safely

**Example trigger phrases:**

```text
Run COMPASS Source Rebase.
Rebase my COMPASS source-of-truth repo.
Align my COMPASS Source of Truth with the current scaffold.
Dry-run the source repo scaffold update.
```

**Required framework files:**

- `VERSION.md`
- `COMPASS_Current.md`
- `COMPASS_COMMANDS.md`
- `rules/00-operating-principles.md`
- `rules/09-source-rebase.md`
- `templates/source-of-truth-scaffold/README.md`
- `templates/source-of-truth-scaffold/COMPASS_Source_Manifest.md`
- `templates/source-of-truth-scaffold/sources/seed/README.md`
- `templates/source-of-truth-scaffold/sources/seed/SEED_ARTIFACTS_MANIFEST.md`
- `templates/source-of-truth-scaffold/migration/COMPASS_Source_Rebase_Report_TEMPLATE.md`
- `prompts/compass-source-rebase.md`

**Output discipline:** Source Rebase defaults to dry-run mode. Existing user-owned source records always win. Report existing files, missing scaffold files, drift, and legacy or historical paths. Do not overwrite, delete, rename, move, edit, verify claims, perform COMPASS Intake, or move existing resumes/CVs into `/sources/seed/` during Source Rebase. Create missing scaffold paths only after explicit approval for `create-missing-only`.

---

### COMPASS Analysis

**Launcher:** `prompts/compass-analysis.md`

**Purpose:** Evaluate a role, job description, recruiter request, opportunity, or career target using source-grounded candidate-fit analysis plus the Opportunity Reality Layer.

**Use when the user asks to:**

- evaluate role fit
- analyze a job description
- compare jobs or opportunities
- assess recruiter positioning
- decide whether to apply
- map source evidence to target requirements
- identify risks, gaps, or objections
- assess how rare or compressed the requested candidate profile is
- research the employer, employee sentiment, or technical interview process
- determine whether the opportunity is worth the candidate's time

**Example trigger phrases:**

```text
Run COMPASS Analysis on this role.
Use COMPASS on this job description.
Evaluate this opportunity with COMPASS.
Run a COMPASS fit analysis.
```

**Required framework files:**

- `VERSION.md`
- `COMPASS_Current.md`
- `rules/00-operating-principles.md`
- `rules/01-analysis-workflow.md`
- `rules/04-truthguard.md`
- `rules/06-artifact-rules.md`
- `rules/10-opportunity-recon.md`
- `prompts/compass-analysis.md`

**Output discipline:** Analysis is separate from generated artifacts. For identifiable-company role analysis, include Purple Squirrel Factor and requirement-market realism, company and interview reality, and recommendation and pursuit economics under the strict 13-section analysis report template. Report insufficient external evidence rather than speculating. Do not generate resumes, cover letters, recruiter messages, or other downstream artifacts unless the user explicitly asks.

---

### COMPASS Tailored Resume

**Launcher:** `prompts/compass-tailored-resume.md`

**Purpose:** Generate a role-specific resume for the most recently analyzed role or a user-provided target role, using verified source records and TruthGuard.

**Use when the user asks to:**

- generate a resume for a specific role
- tailor a resume to a job description
- create an application resume after COMPASS Analysis

**Example trigger phrases:**

```text
Generate the COMPASS Tailored Resume.
Create the tailored resume for the role we just analyzed.
Build a COMPASS resume for this job description.
```

**Required framework files:**

- `VERSION.md`
- `COMPASS_Current.md`
- `rules/00-operating-principles.md`
- `rules/02-resume-generation.md`
- `rules/04-truthguard.md`
- `rules/06-artifact-rules.md`
- `rules/08-human-authenticity.md`
- `prompts/compass-tailored-resume.md`

**Output discipline:** The resume artifact must not include COMPASS analysis, scoring, risk notes, ATS matrix commentary, compensation strategy, recruiter objection notes, company research, interview findings, pursuit economics, private tactical notes, or framework commentary.

---

### COMPASS Recruiter-Targeted Resume

**Launcher:** `prompts/recruiter-targeted-resume.md`

**Purpose:** Generate a broader recruiter-facing resume when the recruiter may have multiple opportunities or when the user needs general Staff/Principal-level positioning rather than a single-role application resume.

**Use when the user asks to:**

- generate a recruiter-targeted resume
- create a broad Staff Engineer resume for a recruiter
- prepare a resume for a recruiter who may represent multiple roles

**Example trigger phrases:**

```text
Generate a COMPASS Recruiter-Targeted Resume.
Create a broad recruiter resume for this recruiter.
Build a Staff Engineer recruiter resume with COMPASS.
```

**Required framework files:**

- `VERSION.md`
- `COMPASS_Current.md`
- `rules/00-operating-principles.md`
- `rules/02-resume-generation.md`
- `rules/04-truthguard.md`
- `rules/06-artifact-rules.md`
- `rules/08-human-authenticity.md`
- `prompts/recruiter-targeted-resume.md`

**Output discipline:** Preserve broad recruiter positioning while respecting TruthGuard, source-grounding, user-specific style rules, and do-not-claim constraints.

---

### COMPASS Cover Letter

**Launcher:** `prompts/compass-cover-letter.md`

**Purpose:** Generate a clean, source-grounded cover letter for a specific target role or opportunity.

**Use when the user asks to:**

- generate a cover letter
- write a cover letter for a role previously analyzed by COMPASS
- produce a cover letter from a job description and verified source record

**Example trigger phrases:**

```text
Generate the COMPASS Cover Letter.
Create a cover letter for this role.
Write the COMPASS cover letter for the job we analyzed.
```

**Required framework files:**

- `VERSION.md`
- `COMPASS_Current.md`
- `rules/00-operating-principles.md`
- `rules/03-cover-letter-generation.md`
- `rules/04-truthguard.md`
- `rules/06-artifact-rules.md`
- `rules/08-human-authenticity.md`
- `prompts/compass-cover-letter.md`

**Output discipline:** Use a calm, professional, forward-looking tone. Do not include internal COMPASS analysis, ATS tables, compensation strategy, company-review findings, interview-risk notes, pursuit economics, objection notes, or private tactical notes inside the cover letter artifact.

## Supported Artifact Requests

The active artifact rules support additional career-specific artifacts even when they do not yet have separate first-class launcher files.

Supported artifact requests include:

- canonical career records
- claim ledgers
- do-not-claim registers
- coverage registers
- analysis reports
- recruiter responses
- application answers
- follow-up messages
- interview preparation notes
- compensation notes
- other career-specific artifacts

When generating these artifacts, use the active framework files and rules rather than inventing an independent command behavior.

## Not Currently Active as First-Class Commands

### COMPASS Charter

`COMPASS Charter` is not currently a confirmed first-class COMPASS command in this framework.

If a user asks for a COMPASS Charter, first determine whether they mean one of the current COMPASS workflows:

- COMPASS Intake for source-of-truth onboarding
- COMPASS Analysis for role or opportunity evaluation
- a clean generated artifact such as a resume, cover letter, recruiter response, or interview-prep note

Do not silently import LEAP Charter behavior into COMPASS unless the project owner explicitly adds a COMPASS Charter command to this registry and creates the supporting prompt/rule files.

## Command Maintenance Rules

When adding, renaming, or retiring a COMPASS command:

1. Update this file.
2. Add or update the launcher prompt under `prompts/` when the command is first-class.
3. Add or update durable behavior rules under `rules/` when behavior changes materially.
4. Update `README.md` if the command should be visible to new users.
5. Update `COMPASS_Changelog.md` with the change.
6. Update `VERSION.md` only when command behavior materially changes framework behavior.
7. Preserve source-grounding, phase separation, TruthGuard, opportunity-recon evidence discipline, and artifact cleanliness.
