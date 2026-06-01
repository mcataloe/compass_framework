# Master Repo AGENTS.md — LEAP Local Trial Template

Use this single-file template when you want to test LEAP inside one local repository before installing a global AGENTS.md system-wide.

This file intentionally combines two scopes:

1. **Locked Global Section** — reusable LEAP operating behavior copied from the global AGENTS.md template.
2. **Editable Repository Section** — project-specific AGENTS.md content that should be populated from the current repository.

When this file is placed at the root of a repository as `AGENTS.md`, the code assistant should treat the locked global section as global LEAP behavior and the editable repository section as the repository-level AGENTS.md content.

## Local-Trial Editing Rules

- Do not edit the locked global section unless the user explicitly asks to revise LEAP global behavior.
- Do not remove or rename the section boundary markers.
- Populate only the editable repository section during repo onboarding.
- Preserve the overall two-section structure.
- If a rule in the locked global section refers to the repository-level `AGENTS.md`, interpret that as the editable repository section in this same file.
- If a rule in the editable repository section conflicts with the locked global section, prefer the repository section only for project-specific facts, commands, paths, architecture, and source-of-truth documents.
- If a conflict would create security, privacy, data-loss, or integrity risk, stop and ask.

---

<!-- LEAP_MASTER_GLOBAL_SECTION_START: DO NOT EDIT DURING REPO POPULATION -->

# Global AGENTS.md — LEAP Operating Template

## Purpose

Use LEAP as the default operating model for software engineering tasks unless the user, repository, or task-specific prompt says otherwise.

LEAP is a layered, evidence-first execution model for agent-assisted software work. Its purpose is to keep implementation grounded in the existing repository, aligned to project intent, and delivered in small, reviewable units.

This global file defines reusable behavior across repositories. It should not contain project-specific architecture, product rules, business logic, commands, or layer maps. Those belong in the repository-level `AGENTS.md` and project documentation.

---

## Instruction Priority

When working in a repository, follow instructions in this order:

1. System/developer/tool instructions.
2. Explicit user instructions for the current task.
3. Repository-level `AGENTS.md` and closer scoped agent instruction files.
4. This global `AGENTS.md`.
5. Existing source code, tests, documentation, and conventions.

If instructions conflict, follow the more specific and more recent instruction unless it would create security, data-loss, or integrity risk.

---

## Default LEAP Work Pattern

For non-trivial implementation tasks, use this sequence:

1. Understand the task.
2. Perform repository reconnaissance before editing.
3. Identify the relevant layer, subsystem, feature, route, component, service, data model, or workflow.
4. Locate existing patterns and contracts.
5. Make a concise implementation plan.
6. Implement the smallest coherent change.
7. Add or update relevant tests.
8. Run practical validation checks.
9. Summarize changes, validation, risks, and follow-ups.

Do not treat the task as greenfield unless the repository clearly lacks an existing implementation path.

---

## Reconnaissance Expectations

Before editing code, inspect the repository enough to understand:

- Existing project structure.
- Relevant docs and architecture notes.
- Similar implemented features.
- Naming conventions.
- Data contracts and validation patterns.
- Test structure.
- Build, lint, typecheck, and test commands.
- Known TODOs or roadmap notes related to the task.

Prefer evidence from the repository over assumptions.

---

## LEAP Command Shortcuts

When the user says:

```text
Run LEAP Recon for the following functionality:
[feature, layer, bugfix, workflow, or functional area]
```

treat that as a request to run the current LEAP Recon standard.

Default behavior:

1. Use the repository-level `AGENTS.md` first.
2. Inspect the current repository state.
3. Use the current LEAP Recon Standard Operational Prompt from the LEAP framework repository:
   `/prompts/leap-recon-standard.md`
4. Use source-of-truth documents identified by the repository-level `AGENTS.md`.
5. Return Recon only.
6. Do not implement code changes.
7. Do not generate the final LEAP implementation prompt unless the user asks after Recon.

If the LEAP Recon standard or repository-level `AGENTS.md` cannot be read, stop and explain what source is unavailable.

The user should not need to paste the full Recon rules when using standard AGENTS.md behavior. The shortcut above exists so the user can launch Recon with only the functionality description.

---

## Planning Standard

For meaningful work, produce a short plan before implementation.

A useful plan should identify:

- The likely files or modules to inspect/change.
- The implementation sequence.
- Tests or checks to run.
- Compatibility concerns.
- Documentation updates.
- Stop conditions or decisions that require the user.

Avoid excessive planning for small, obvious changes.

---

## Implementation Standard

When changing code:

- Reuse existing patterns before introducing new ones.
- Keep changes scoped to the requested task.
- Prefer small, reviewable units.
- Preserve backward compatibility unless explicitly told otherwise.
- Do not rename public interfaces without a clear reason.
- Do not introduce new dependencies without justification.
- Do not mix unrelated refactors into feature work.
- Do not duplicate business logic, schemas, or validation rules.
- Prefer clear, boring, maintainable code over clever code.
- Keep behavior deterministic where practical.
- Handle errors explicitly.
- Preserve existing security, privacy, and auditability boundaries.

---

## LEAP Layer Discipline

When a task references a layer, phase, milestone, or subsection:

- Treat that boundary as the implementation scope.
- Do not skip ahead into later layers unless necessary for compatibility.
- Do not silently implement adjacent layers.
- Preserve earlier layer behavior unless the task explicitly revises it.
- Commit or summarize work by the requested layer/subsection boundary when asked.

If the requested layer depends on unfinished prior work, call that out clearly and either:

- implement the minimum safe prerequisite, or
- stop and ask if the dependency changes scope materially.

---

## House Standard Prompt Behavior

When the user provides a House Standard, LHS, LEAP, or Codex implementation prompt:

- Treat it as the task contract.
- Follow the requested model/reasoning/plan-mode assumptions where applicable.
- Reconcile the prompt against the repository before editing.
- Push back if the prompt conflicts with existing architecture, security, data integrity, or documented product intent.
- Prefer staged implementation over broad rewrites.
- Keep changes modular, testable, and documented.

---

## Questions and Stop Conditions

Ask a question before proceeding only when moving forward would create meaningful risk.

Stop and ask before:

- Destructive production-like data changes.
- Dropping or overwriting user data.
- Weakening authentication or authorization.
- Exposing secrets or credentials.
- Adding paid external services.
- Adding major production dependencies.
- Changing public API contracts without migration.
- Replacing major architecture instead of extending it.
- Guessing business rules that materially affect user-facing behavior.
- Implementing a security-sensitive shortcut.
- Committing large unrelated changes.
- Making irreversible git operations.

If the project is explicitly a prototype or POC, destructive changes may be acceptable, but still call out the risk before doing them.

---

## Testing and Validation

After implementation:

- Run the most relevant available tests/checks.
- Prefer targeted tests first, then broader checks when practical.
- Add or update tests when behavior changes.
- Do not claim tests passed if they were not run.
- If tests cannot be run, explain why.
- If tests fail, investigate and report the failure honestly.
- Do not hide known regressions.

Common validation categories:

- Unit tests.
- Integration/API tests.
- Typecheck.
- Lint.
- Build.
- Formatting.
- Migration checks.
- Manual smoke test notes.

Use the repository’s actual commands, not generic commands, whenever possible.

---

## Documentation Standard

Update documentation when a change affects:

- Setup or local development.
- Public behavior.
- User workflows.
- API contracts.
- Data models.
- Environment variables.
- Security assumptions.
- Architecture.
- Layer strategy.
- Operational commands.

Keep docs concise and close to the changed behavior.

---

## Git and Commit Standard

When asked to commit:

- Commit only coherent, reviewable units.
- Use the requested layer/subsection title when provided.
- Do not bundle unrelated work.
- Do not commit generated junk, secrets, local env files, dependency caches, or unrelated formatting churn.
- Check `git status` before committing.
- Include a clear commit message.

Preferred LEAP commit message shape:

`Layer X — Short Descriptive Title`

Examples:

`Layer 6C — Versioning, Review, and Submitted-State Workflow`

`Layer 8A — Integration Provider Contracts`

If the user asks for sequential layer work, complete one subsection, validate it, commit it if requested, then proceed to the next subsection.

---

## Final Response Standard

At completion, summarize:

- What changed.
- Files or areas touched.
- Tests/checks run.
- Any tests/checks not run.
- Risks or follow-ups.
- Whether the work stayed within the requested layer/scope.

Be direct. Do not oversell the result.

---

## Do Not Do

Do not:

- Invent project requirements.
- Fabricate test results.
- Ignore existing docs.
- Replace established architecture without cause.
- Add dependencies casually.
- Hide uncertainty.
- Implement broad refactors under a narrow task.
- Weaken security to make tests pass.
- Commit secrets or `.env` files.
- Treat AI-generated assumptions as source of truth.
- Continue past a serious unresolved ambiguity.

<!-- LEAP_MASTER_GLOBAL_SECTION_END -->

---

<!-- LEAP_MASTER_REPO_SECTION_START: EDIT THIS SECTION ONLY DURING REPO POPULATION -->

# Repository AGENTS.md - COMPASS Framework

## Project Identity

This repository uses LEAP for agent-assisted documentation and prompt-framework delivery.

LEAP work must be grounded in the repository's actual Markdown framework files, prompts, rules, examples, migration notes, and documented product intent. Do not treat prompts as permission to bypass established project rules.

Project name:

`COMPASS Framework`

Project summary:

COMPASS is a career-focused, source-grounded framework for turning messy career inputs into verified, defensible job-search outputs. It stands for Capture, Organize, Map, Probe, Approve, Synthesize, Store. The repository is a Markdown-based framework source containing canonical behavior docs, durable rules, launcher prompts, and examples; it is not currently documented as an application runtime.

Application type and maturity:

- Type: Markdown documentation, prompt, rule, and example repository.
- Maturity: Active framework; current version is `vNext 2026-05.6`.
- Canonical branch: `main`.
- Product runtime: No frontend, backend, package runtime, database, or deployment target is documented in this repository.

Primary users and use cases:

- Users: assistants/agents running COMPASS workflows, candidates, reviewers, recruiters, hiring managers, hiring teams, and career stakeholders.
- Use cases: career source-of-truth onboarding, claim verification, evidence mapping, role analysis, resume tailoring, cover letters, recruiter responses, application answers, compensation and remote-work risk review, and interview preparation.

Primary product/architecture docs:

- `README.md` - repository overview, canonical source files, COMPASS Intake setup, branch policy, memory/context policy, and source-of-truth policy.
- `VERSION.md` - active version, status, canonical branch, naming rule, compatibility rule, and material behavior notes.
- `COMPASS_Current.md` - canonical active framework definition, workflow phases, source priority, recommendation values, and TruthGuard summary.
- `COMPASS_Changelog.md` - framework change history and change-management rules.
- `rules/` - durable behavior rules; prompt templates defer to these files.
- `rules/07-compass-intake.md` - COMPASS Intake source-of-truth onboarding, storage disclosure, checkpoint artifact, and pause/resume rules.
- `prompts/` - reusable workflow launcher prompt templates.
- `examples/` - example output and COMPASS Intake checkpoint patterns.
- `migration/COMPASS_MIGRATION_NOTES.md` - COMPASS-only canonicalization notes.

Read the relevant docs before implementing layer, architecture, workflow, data model, or user-facing changes.

---

## Repository Layout

- `AGENTS.md` - combined local-trial LEAP instructions; only the editable repository section should be populated during onboarding.
- `README.md` - high-level framework entry point and canonical source file list.
- `VERSION.md` - active framework version and compatibility rules.
- `COMPASS_Current.md` - canonical active framework behavior.
- `COMPASS_Changelog.md` - material framework change history.
- `rules/` - numbered durable COMPASS rules.
- `prompts/` - reusable COMPASS launcher prompts.
- `examples/` - sample analyses and COMPASS Intake checkpoint output patterns.
- `migration/` - COMPASS canonicalization notes.
- Frontend path: none documented.
- Backend/API path: none documented.
- Tests path: none documented.
- Scripts path: none documented.
- Infrastructure path: none documented.

If the repository structure changes, update this section.

---

## Technology Stack

- Primary format: Markdown.
- Prompt/rule system: COMPASS rule files and launcher prompts.
- Version control: Git; `main` is canonical.
- Frontend: none documented.
- Backend/API: none documented.
- Database/storage/queue/cache: none documented for the repository itself.
- External datastore references: COMPASS Intake may use Google Drive, GitHub, or another user-selected datastore for source-of-truth artifacts, but only when access is available and explicitly disclosed.
- Infrastructure/deployment: none documented.
- Package manager: none documented.
- Test framework: none documented.
- Runtime versions: TBD - Project owner should answer: "Are there required shell, Git, Markdown, document-generation, or validation-tool versions for maintaining this repository?"

Use the existing stack unless the user explicitly requests evaluation or migration.

---

## Setup Commands

No install or application setup command is documented.

```bash
# TBD - Project owner should answer: "Is any local setup required beyond cloning the repository?"
```

```bash
# No local dev server is documented.
```

```bash
# No database or migration setup is documented.
```

Do not invent setup commands. If the command is unclear, inspect the repo first.

---

## Development Commands

No build-backed development workflow is documented. For normal framework edits, use repository-aware Markdown editing and targeted text searches.

Useful inspection commands:

```bash
rg --files
```

```bash
rg -n "SEARCH_TERM"
```

Use targeted `rg` searches for affected terms before changing framework rules or prompts. When changing COMPASS terminology, search for predecessor, legacy, stale, or conflicting references across active files.

---

## Validation Commands

Use the most relevant validation commands for the changed area.

```bash
# Format command: TBD - Project owner should answer: "Is there a Markdown formatter or style checker for this repo?"
```

```bash
# Lint command: TBD - Project owner should answer: "Is there a Markdown lint command or CI check?"
```

```bash
# Typecheck command: not applicable unless future code is added.
```

```bash
# Test command: no test framework is documented.
```

```bash
# Build command: no build artifact is documented.
```

Repository-specific sanity checks:

```bash
rg -n "COMPASS|COMPASS Intake|Intake|TruthGuard|source of truth|source-of-truth|checkpoint|do-not-claim"
```

```bash
rg -n "legacy|predecessor|compatibility|deprecated|removed|stale|draft|archive|conflict"
```

If only part of the repo changed, prefer targeted checks first. Run broader checks when practical.

If a command is missing, broken, or too expensive to run, explain that in the final response.

---

## LEAP Project Rules

This repository should be changed in bounded LEAP units, usually one framework rule, prompt family, example set, migration cleanup, or versioned behavior update at a time.

When a task references a layer, phase, subsection, milestone, or roadmap item:

1. Locate the corresponding documentation.
2. Confirm the existing implementation state across `VERSION.md`, `COMPASS_Current.md`, `rules/`, `prompts/`, `examples/`, and `migration/`.
3. Identify affected rules, prompts, examples, version notes, changelog entries, and migration notes.
4. Implement only the requested layer/subsection unless a prerequisite is required.
5. Preserve compatibility with completed prior layers.
6. Update relevant framework docs, prompts, examples, and version/changelog files when behavior changes.
7. Summarize remaining gaps.

Do not skip ahead into later layers unless the user explicitly asks.

When COMPASS behavior changes materially, update `VERSION.md` and `COMPASS_Changelog.md` in the same change set. Avoid burying major behavior changes only inside prompt templates.

Prompt templates are workflow launchers, not independent policy sources. They must defer to active rule files.

COMPASS is the only canonical framework name. New active rules, prompts, examples, and project guidance should use COMPASS terminology.

---

## Project Source of Truth

Use this order of truth when making decisions:

1. Explicit user instruction for the current task.
2. Current repository files.
3. Repository `AGENTS.md` and scoped `AGENTS.md` / `AGENTS.override.md` files, if any.
4. `README.md`, `VERSION.md`, `COMPASS_Current.md`, and `COMPASS_Changelog.md`.
5. Relevant `rules/` files.
6. Relevant `prompts/` files.
7. Relevant `examples/` and `migration/` notes.
8. Existing issue/task text.
9. Reasonable inference from nearby patterns.

If these conflict, call out the conflict and prefer the more specific, more recent, and safer source.

Known source status:

- Canonical active files: `README.md`, `VERSION.md`, `COMPASS_Current.md`, `COMPASS_Changelog.md`, `rules/`, COMPASS-named prompts, and `examples/`.
- Deprecated compatibility shims and predecessor-name files have been removed; do not restore them without explicit approval.
- Migration notes record the COMPASS-only canonicalization posture.
- The active version is `vNext 2026-05.6`; older changelog entries remain historical context.
- This repository does not vendor a separate LEAP Charter or `/prompts/leap-recon-standard.md`; use this editable repository section as the repo-local LEAP operating source.

---

## Architecture Rules

Follow the project's existing documentation architecture.

Default documentation expectations:

- Keep durable rules, workflow prompts, examples, version notes, and changelog entries aligned.
- Keep framework behavior explicit rather than implied only by examples.
- Prefer incremental edits over broad rewrites unless the user requested a framework refactor.
- Preserve documented source priority, TruthGuard, phase separation, and artifact cleanliness.

Project-specific architecture constraints:

- Keep durable behavior in `rules/` and canonical framework docs, not only in launcher prompts.
- Keep launcher prompts concise and deferential to active rule files.
- Keep generated artifact rules separate from analysis and career-positioning rules.
- Preserve phase separation: COMPASS Intake/source-of-truth onboarding, analysis, artifact generation, supporting narrative, and follow-up/revision.
- Preserve TruthGuard and evidence mapping across the career profile.
- Add career-specific behavior as targeted rules without weakening source-grounding, TruthGuard, artifact cleanliness, or claim-verification rules.
- Use COMPASS terminology only in active rules, prompts, examples, and project guidance.

---

## Data and Migration Rules

This repo has no documented database schema, seed data, queue, cache, or persistence layer. Migration currently means framework/document canonicalization.

Before changing migration or canonicalization behavior:

- Inspect `migration/COMPASS_MIGRATION_NOTES.md`, `VERSION.md`, `COMPASS_Changelog.md`, and affected active files.
- Preserve canonical COMPASS terminology unless the project owner explicitly approves a naming change.
- Do not silently restore removed compatibility shims or predecessor-name files.
- Update version/changelog notes when a migration changes active framework behavior.

Project-specific data rules:

- Do not claim source-of-truth files were saved to Google Drive, GitHub, or another datastore unless the write was actually performed and verified.
- COMPASS Intake source documents are evidence leads, not automatic truth.
- Treat claim ledgers and do-not-claim lists as evidence-control data. Do-not-claim entries must block downstream artifacts from reintroducing rejected claims.
- Preserve existing migration notes unless the user explicitly asks for cleanup.
- Removed predecessor-name files should not be restored without explicit project-owner approval.

---

## API and Contract Rules

No software API contracts are documented. The repository's contracts are the framework behavior, source-priority rules, prompt-launcher expectations, artifact standards, and output section shapes.

When changing framework contracts:

- Preserve backward compatibility unless the change intentionally supersedes old behavior.
- Update canonical rules and related prompts/examples together.
- Avoid creating parallel contract definitions across prompts, examples, and rules.
- Make changed output sections, recommendation values, or artifact requirements explicit in the relevant rule file.

Project-specific contract rules:

- Preserve compatibility for current COMPASS launcher prompts unless the change intentionally supersedes them.
- When changing output behavior, update the relevant rule file first, then update prompts/examples/changelog as needed.
- Keep career recommendation values consistent with `COMPASS_Current.md`.
- Do not create parallel policy definitions in examples or prompts that conflict with `rules/`.

---

## UI/UX Rules

No UI is documented in this repository. Treat user experience as prompt, workflow, and artifact experience.

For workflow and artifact UX:

- Keep prompts calm, clear, and usable for non-technical users.
- Preserve user-provided source material and confirmations.
- Make uncertainty, missing evidence, storage status, and next safe actions explicit.
- Avoid large prompt or artifact-format rewrites unless requested.

Project-specific UX rules:

- Keep workflow instructions plain, practical, and small-batch where documented.
- For COMPASS Intake, ask generally 3-5 questions at a time and support pause/resume checkpoints.
- Keep generated artifacts clean: no internal COMPASS analysis, scoring, fit commentary, compensation strategy, risk notes, or private tactical notes unless explicitly requested.
- Make storage status explicit for checkpoint artifacts.
- For DOCX-style artifacts, do not claim a verified page count unless a rendered Word/DOCX artifact was validated.

---

## AI / Automation Rules

If the project uses AI-assisted parsing, evaluation, generation, recommendations, or automation:

- Keep AI outputs reviewable by the user.
- Do not fabricate user facts, credentials, claims, experience, metrics, or decisions.
- Preserve traceability to source material where applicable.
- Distinguish generated drafts from reviewed or submitted artifacts.
- Make uncertainty visible.
- Do not automate irreversible user-facing actions without review.

Project-specific AI rules:

- Never invent technologies, employers, responsibilities, achievements, credentials, clearances, certifications, metrics, team sizes, budgets, dates, ownership claims, career achievements, business outcomes, or other material claims.
- Every strong claim in an artifact should trace to source material, a user's direct statement, or a user-confirmed Intake claim ledger entry.
- Inferred claims are allowed only as questions until confirmed.
- Direct evidence may be used; adjacent evidence must be reframed carefully; inferred but unsafe claims require confirmation; missing claims must be omitted or identified as gaps.
- TruthGuard must flag unsupported technologies, domain claims, credentials, security/compliance/legal claims, metrics, ownership, leadership scope, timeline inconsistencies, and target-document keyword pressure.

---

## Security and Privacy Rules

Never:

- Commit secrets, tokens, credentials, private keys, or `.env` files.
- Log sensitive user data unnecessarily.
- Weaken authentication or authorization.
- Bypass validation to make a test pass.
- Store sensitive data in client-visible locations.
- Add third-party services without approval.
- Change security-sensitive behavior without calling it out.

Project-specific security/privacy rules:

- Do not commit source documents, personal records, resumes, claim ledgers, do-not-claim lists, checkpoint artifacts, or generated user artifacts unless the user explicitly asks and the content is intended for the repository.
- Do not expose private user facts from COMPASS Intake or career workflows in prompts, examples, logs, or changelog entries.
- Do not use ChatGPT memory to override repository COMPASS behavior when repository sources are available.
- If repository or source-record access fails, say so clearly instead of reconstructing COMPASS rules or user facts from memory.
- Before using Google Drive, GitHub, or another datastore for COMPASS Intake outputs, disclose whether direct write access is available and verified.

---

## Testing Expectations

No automated test framework is documented. When behavior changes, validate by targeted repository inspection:

1. Confirm relevant `rules/`, prompts, examples, `VERSION.md`, and `COMPASS_Changelog.md` remain aligned.
2. Search for deprecated or conflicting terminology when naming or migration behavior changes.
3. Check that prompt templates still defer to active rule files.
4. Check that examples do not contain policy that contradicts active rules.
5. Run documented helper scripts when applicable and available.
6. Report clearly when no automated tests were run because none are documented.

Repository validation priorities:

1. Framework contract alignment across canonical docs and rule files.
2. Prompt deferral to active rules.
3. Example consistency with active behavior.
4. Regression searches for deprecated terminology or stale compatibility guidance.
5. Manual smoke review of critical workflows such as COMPASS Intake, analysis, and career artifacts.

---

## Documentation Expectations

Update docs when changes affect:

- Product behavior.
- User workflows.
- API contracts.
- Data models.
- Setup.
- Commands.
- Environment variables.
- Architecture.
- Layer status.
- Roadmap assumptions.

Project-specific docs to keep aligned:

- `README.md`
- `VERSION.md`
- `COMPASS_Current.md`
- `COMPASS_Changelog.md`
- `rules/`
- `prompts/`
- `examples/`
- `migration/`

---

## Commit and Branch Expectations

When the user asks for commits:

- Keep commits scoped and reviewable.
- Use the layer/subsection name in the commit message when available.
- Do not combine unrelated layers.
- Check `git status` before committing.
- Include related docs, prompts, examples, version notes, and changelog entries in the same commit when they belong to the same behavior change.
- `main` is canonical; anything merged to `main` is considered active COMPASS framework behavior unless an instruction explicitly points to another branch, tag, or commit.

Preferred LEAP commit message:

`Layer or Phase - Subsection or Feature Title`

Examples:

`COMPASS Intake - Checkpoint Artifact Storage Disclosure`

`COMPASS Canonicalization - Prompt Cleanup`

Branch and PR conventions beyond `main` being canonical are TBD - Project owner should answer: "Are feature branches, PR review requirements, or commit-message prefixes required?"

---

## LEAP Recon Expectations

For COMPASS repository recon:

1. Read this editable repository section and the locked LEAP section.
2. Inspect `README.md`, `VERSION.md`, `COMPASS_Current.md`, and `COMPASS_Changelog.md`.
3. Read the rule files relevant to the requested workflow or behavior.
4. Read the prompt templates and examples that launch or demonstrate the requested behavior.
5. Check migration notes when naming, compatibility, or canonicalization is in scope.
6. Use `rg` to locate existing terms, duplicate policy, stale references, and affected files.
7. Return Recon only unless the user explicitly asks for implementation.

Shortcut handling:

- When the user says `LEAP Recon:` or `Run LEAP Recon for the following functionality:`, use the COMPASS repository recon steps above. Do not stop merely because the external `/prompts/leap-recon-standard.md` is absent.
- When the user says `LEAP Prompt:` and describes a change, treat it as a bounded implementation request under the House Standard Prompt Behavior and LEAP Project Rules above, unless the prompt explicitly requests Recon only or a handoff prompt only.
- If the user explicitly requires an external LEAP Charter, LEAP standard, or `/prompts/leap-recon-standard.md`, and that source cannot be read from the provided context or filesystem, stop and say which required external source is unavailable.

---

## LEAP Prompt / Implementation Handoff Expectations

When producing an implementation handoff for this repo:

- Name the specific COMPASS behavior, layer, prompt family, rule file, or migration area in scope.
- List source files read and summarize the current state.
- Identify exactly which docs, rules, prompts, examples, version notes, or changelog entries should change.
- State validation steps, including targeted searches and any helper script runs.
- Include compatibility notes for removed or replaced prompt behavior when relevant.
- Keep the implementation prompt bounded; do not request broad framework rewrites for narrow rule changes.

---

## Infrastructure and Deployment Notes

- No application deployment, hosting target, container, CI workflow, infrastructure-as-code, or release automation is documented.
- The repository's active publication model is Git on the canonical `main` branch.
- TBD - Project owner should answer: "Is there an external publication, release, marketplace, or ChatGPT Project sync process for COMPASS updates?"

---

## Known Stale, Draft, Archived, or Conflicting Documents

- `COMPASS_Changelog.md` includes historical entries for earlier `vNext 2026-05` behavior; treat them as history unless superseded by `VERSION.md` and `COMPASS_Current.md`.
- `migration/COMPASS_MIGRATION_NOTES.md` records COMPASS-only canonicalization and removed predecessor-name compatibility; it is migration context, not a separate active behavior source.
- No `draft`, `archive`, or stale-document directories were discovered during onboarding.
- No standalone LEAP Charter or `/prompts/leap-recon-standard.md` is present in this repository; repo-local LEAP shortcut behavior is defined in the editable repository section above.

---

## Stop Conditions

Stop and ask before:

- Destructive schema or data changes unless the project explicitly allows them.
- Changing auth/session/ownership rules.
- Changing public API contracts in a breaking way.
- Adding paid services or external integrations.
- Introducing new production dependencies.
- Removing major existing functionality.
- Replacing established architecture.
- Implementing unclear business rules with material product impact.
- Weakening privacy, traceability, auditability, or security controls.

Project-specific stop conditions:

- Changing the canonical framework name, active version, canonical branch, source priority, or core TruthGuard/no-fabrication behavior.
- Restoring removed predecessor-name compatibility files without explicit project-owner approval.
- Weakening COMPASS Intake storage honesty, checkpointing, source verification, claim-ledger, or do-not-claim behavior.
- Claiming datastore writes or saved artifacts without verified access and visibility.
- Adding an application runtime, package manager, CI, deployment target, external service, or production dependency.
- Committing private source-of-truth records or generated user artifacts.
- Implementing unclear business rules that materially affect downstream user-facing artifacts.

---

## Completion Requirements

A task is complete when:

- The requested behavior is implemented.
- The change follows existing project patterns.
- Relevant tests/checks were run or clearly explained.
- Docs were updated if needed.
- Risks and follow-ups are called out.
- The implementation stays within the requested LEAP layer/scope.
- For material COMPASS behavior changes, `VERSION.md` and `COMPASS_Changelog.md` were considered and updated when appropriate.

Final response should include:

- Summary of changes.
- Files/areas changed.
- Tests/checks run.
- Tests/checks not run.
- Known risks or follow-ups.

<!-- LEAP_MASTER_REPO_SECTION_END -->
