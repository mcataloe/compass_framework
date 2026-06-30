# COMPASS Command Registry

This file defines the current user-facing COMPASS command surface.

Prompt templates remain workflow launchers, not independent policy sources. When a command is executed, use the active framework files, rule files, and the user's verified source-of-truth records to govern behavior.

## Command Authority

COMPASS commands must keep candidate facts, opportunity-context evidence, and user-specific presentation policy separate.

### Candidate facts and career claims

Use this order:

1. The user's direct instruction in the current conversation
2. The user's verified COMPASS Intake claim ledger and do-not-claim list, when available
3. The user's latest approved canonical career source-of-truth record
4. A provisional baseline explicitly authorized by the user's Source of Truth, used only at its documented source-stated depth
5. Imported artifacts, including Initial Seed Artifacts under `/sources/seed/`, as evidence and provenance only
6. Target job descriptions, recruiter requests, and opportunity records for terminology and context only
7. Generated artifacts as historical outputs only
8. Project instructions or memory only when not contradicted by stronger sources and never as a substitute for an available source record

Target job descriptions, recruiter requests, and opportunity records do not create experience, skills, ownership, metrics, credentials, achievements, or facts.

### Opportunity context

For employer, market, interview, and opportunity-reality claims, prefer current authoritative primary sources, then reputable current secondary sources, then clearly attributed recent anecdotal evidence. Preserve recency, source type, and confidence.

Opportunity evidence does not create candidate experience.

### Behavior, tone, formatting, and presentation

Within TruthGuard, do-not-claim controls, privacy requirements, artifact cleanliness, and non-optional artifact contracts, use this order:

1. The user's direct current instruction
2. The most specific approved Source of Truth policy for the relevant artifact or channel
3. Approved general user voice, demeanor, style, or artifact policy
4. Target-channel requirements and current audience context
5. COMPASS artifact-specific rules and generic framework defaults
6. Project instructions, memory, or model defaults only when not contradicted by stronger sources

User-specific Source of Truth policy may configure thresholds, weights, channels, or presentation within its scope. It does not create candidate facts and cannot weaken TruthGuard or approved claim boundaries.

## Current First-Class Commands

### COMPASS Intake

**Launcher:** `prompts/compass-intake.md`

**Purpose:** Build or update a verified career source of truth through evidence capture, claim verification, Materiality Gate questioning, coverage tracking, and checkpoint artifacts.

**Use when the user asks to:**

- create or update a COMPASS Source of Truth;
- ingest career documents;
- stage Initial Seed Artifacts;
- verify claims from resumes, CVs, LinkedIn exports, recruiter notes, interview notes, performance reviews, certifications, portfolio notes, or project summaries;
- reconcile gaps or contradictions across career source material.

**Example triggers:**

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

- run COMPASS Source Rebase;
- align an existing Source of Truth with the current scaffold;
- identify or add missing scaffold directories or placeholder files;
- add missing `/sources/seed/` or private `/sync/` scaffold paths safely.

**Example triggers:**

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
- `templates/source-of-truth-scaffold/sync/README.md`
- `templates/source-of-truth-scaffold/sync/COMPASS_Experience_Targets.yaml`
- `templates/source-of-truth-scaffold/migration/COMPASS_Source_Rebase_Report_TEMPLATE.md`
- `prompts/compass-source-rebase.md`

**Output discipline:** Default to dry-run. Existing user-owned source records always win. Do not overwrite, delete, rename, move, edit, verify claims, perform Intake or Experience Sync, move existing resumes or CVs into `/sources/seed/`, or populate actual source or target mappings without explicit instruction.

---

### COMPASS Experience Sync

**Launcher:** `prompts/compass-experience-sync.md`

**Purpose:** Reconcile an approved COMPASS Source of Truth into a separate public or externally shareable experience repository through a one-way, source-grounded publication workflow.

**Use when the user asks to:**

- reconcile a Source of Truth with a public experience repository;
- publish approved Intake changes;
- audit a public experience repository for drift;
- create a review branch and pull request for approved public-projection changes.

**Example triggers:**

```text
Run COMPASS Experience Sync for public-experience.
Run COMPASS Experience Sync in dry-run mode.
Run COMPASS Experience Sync --full-audit.
Apply the approved COMPASS Experience Sync.
```

**Required framework files:**

- `VERSION.md`
- `COMPASS_Current.md`
- `COMPASS_COMMANDS.md`
- `rules/00-operating-principles.md`
- `rules/04-truthguard.md`
- `rules/06-artifact-rules.md`
- `rules/07-compass-intake.md`
- `rules/11-experience-sync.md`
- `templates/source-of-truth-scaffold/sync/COMPASS_Experience_Targets.yaml`
- `templates/experience-sync/COMPASS_Experience_Manifest_TEMPLATE.yaml`
- `templates/experience-sync/COMPASS_Experience_Sync_Report_TEMPLATE.md`
- `templates/experience-sync/COMPASS_Public_Claim_TEMPLATE.yaml`
- `prompts/compass-experience-sync.md`

**Modes:** `dry-run`, `full-audit`, and explicitly approved `apply-approved`.

**Output discipline:** Experience Sync never modifies the Source of Truth or routing map, verifies new career claims, writes directly to a target default branch, or merges a pull request without explicit instruction.

---

### COMPASS Analysis

**Launcher:** `prompts/compass-analysis.md`

**Purpose:** Evaluate an identified role, job description, recruiter request, opportunity, or career target using source-grounded candidate-fit analysis plus the Opportunity Reality Layer.

**Use when the user asks to:**

- evaluate role fit;
- analyze a job description;
- compare known jobs or opportunities;
- assess recruiter positioning;
- decide whether to apply;
- map source evidence to target requirements;
- identify risks, gaps, objections, role compression, employer reality, or pursuit economics.

**Example triggers:**

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

**Output discipline:** Analysis is separate from generated artifacts. For identifiable-company role analysis, include Purple Squirrel Factor, company and interview reality, and recommendation and pursuit economics under the strict analysis report contract. Do not generate downstream artifacts unless explicitly requested.

---

### COMPASS Verified Opportunity Search

**Launcher:** `prompts/compass-verified-opportunity-search.md`

**Purpose:** Discover, verify, score, and rank multiple current opportunities using separate eligibility, evidence-backed alignment, opportunity-quality, and conversion-condition judgments.

**Use when the user asks to:**

- find current opportunities aligned to a verified career record;
- refresh or build a verified opportunity shortlist;
- search official employer and ATS sources across multiple employers;
- compare alignment, hard screens, career value, visibility, saturation, access, and application friction;
- suppress already handled or duplicate roles using a configured opportunity-status ledger;
- prepare a prioritized application queue without submitting applications.

**Example triggers:**

```text
Run COMPASS Verified Opportunity Search.
Find verified high-alignment opportunities with COMPASS.
Refresh my COMPASS opportunity shortlist.
Run COMPASS Verified Opportunity Search --max 5.
```

**Required framework files:**

- `VERSION.md`
- `COMPASS_Current.md`
- `COMPASS_COMMANDS.md`
- `rules/00-operating-principles.md`
- `rules/01-analysis-workflow.md`
- `rules/04-truthguard.md`
- `rules/10-opportunity-recon.md`
- `rules/12-verified-opportunity-search.md`
- `prompts/compass-verified-opportunity-search.md`

**Required user-specific sources when available:**

- current verified career evidence;
- target-role and career-strategy policy;
- location, remote, travel, employment-structure, level, and compensation constraints;
- alignment thresholds and any explicit scoring-weight overrides;
- opportunity-status or duplicate ledger;
- approved channel or result-format policy.

**Output discipline:** Verify the live official posting and active employer-controlled application flow. Keep eligibility and hard screens, alignment estimate, opportunity quality, and conversion conditions separate. Alignment is not hiring probability. Visibility and saturation are ranking factors unless user-specific policy defines a stricter gate. Do not reward hiddenness when fit is weak. Do not submit applications, update ledgers, or generate downstream artifacts without explicit user instruction.

---

### COMPASS Tailored Resume

**Launcher:** `prompts/compass-tailored-resume.md`

**Purpose:** Generate a role-specific resume for the most recently analyzed role or a user-provided target role, using verified source records and TruthGuard.

**Example triggers:**

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

**Output discipline:** The resume must not include COMPASS analysis, scoring, risk notes, company research, interview findings, pursuit economics, or private tactical notes.

---

### COMPASS Recruiter-Targeted Resume

**Launcher:** `prompts/recruiter-targeted-resume.md`

**Purpose:** Generate a broader recruiter-facing resume when the recruiter may have multiple opportunities or the user needs general senior-level positioning rather than a single-role application resume.

**Example triggers:**

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

**Example triggers:**

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

**Output discipline:** Use a calm, professional, forward-looking tone. Do not include internal analysis, ATS tables, compensation strategy, company-review findings, interview-risk notes, pursuit economics, or private tactical notes.

## Supported Artifact Requests

The active artifact rules support additional career-specific artifacts even when they do not yet have separate first-class launcher files.

Supported artifact requests include:

- canonical career records;
- claim ledgers;
- do-not-claim registers;
- coverage registers;
- Experience Sync reports and public claim indexes;
- analysis and verified opportunity-search reports;
- recruiter responses;
- application answers;
- follow-up messages;
- interview preparation notes;
- compensation notes;
- other career-specific artifacts.

When generating these artifacts, use the active framework files and rules rather than inventing independent command behavior.

## Not Currently Active as First-Class Commands

### COMPASS Charter

`COMPASS Charter` is not currently a confirmed first-class COMPASS command in this framework.

If a user asks for a COMPASS Charter, first determine whether they mean COMPASS Intake, COMPASS Analysis, COMPASS Verified Opportunity Search, or a clean generated career artifact. Do not silently import LEAP Charter behavior into COMPASS unless the project owner explicitly adds the command with supporting prompt and rule files.

## Command Maintenance Rules

When adding, renaming, or retiring a COMPASS command:

1. Update this file.
2. Add or update the launcher prompt under `prompts/` when the command is first-class.
3. Add or update durable behavior rules under `rules/` when behavior changes materially.
4. Update `README.md` if the command should be visible to new users.
5. Update `COMPASS_Changelog.md` with the change.
6. Update `VERSION.md` when command behavior materially changes framework behavior.
7. Preserve source-grounding, phase separation, TruthGuard, opportunity-recon evidence discipline, and artifact cleanliness.