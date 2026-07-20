# COMPASS Comprehensive Career CV Launcher

Use the current COMPASS framework and the user's current career Source of Truth to generate a comprehensive approved career CV.

## Invocation

```text
Run COMPASS Comprehensive Career CV.
```

Optional audience selectors:

```text
Run COMPASS Comprehensive Career CV --recruiter.
Run COMPASS Comprehensive Career CV --public.
Run COMPASS Comprehensive Career CV --both.
```

Default to `--recruiter` when the user requests a personal full CV without naming a public audience. Default to `--public` only when publication or an external experience repository is explicitly requested.

## Required Framework Inputs

Load:

- `VERSION.md`;
- `COMPASS_Current.md`;
- `COMPASS_COMMANDS.md`;
- `rules/00-operating-principles.md`;
- `rules/02-resume-generation.md`;
- `rules/04-truthguard.md`;
- `rules/06-artifact-rules.md`;
- `rules/08-human-authenticity.md`;
- `rules/11-experience-sync.md` for a public repository publication;
- `rules/16-resume-release-assurance.md` for downloadable DOCX output;
- `rules/17-comprehensive-career-cv.md`;
- the current user-specific artifact, filename, disclosure, work-mode, and CV/resume style policies.

## Required Source Behavior

1. Resolve the current Source of Truth authority and coverage model.
2. Resolve every material role and project scope.
3. Use approved ledgers and do-not-claim controls ahead of imported CVs or generated artifacts.
4. Build an internal employment coverage plan with `detailed`, `compressed`, or `excluded` disposition for every canonical role.
5. Stop on material source conflicts affecting the requested publication.
6. Exclude unresolved or provisional material from a public variant when public policy forbids provisional claims.
7. Compile the approved evidence into a readable CV; do not concatenate dossiers.

## Deliverables

For `--recruiter`:

- clean recruiter-facing comprehensive CV;
- internal completion note identifying any excluded or provisional scopes;
- DOCX only when the applicable executable release gate passes;
- Markdown when requested or useful.

For `--public`:

- clean public comprehensive CV with public-disclosure abstractions;
- updated public claim provenance or Experience Manifest when the target uses them;
- Experience Sync reconciliation report;
- branch and pull request only when writes are explicitly authorized and the target is configured;
- no direct write to the target default branch;
- no merge without explicit user instruction.

For `--both`:

- use one resolved factual content model;
- apply separate recruiter and public publication envelopes;
- do not allow the public variant to weaken or expand the recruiter's factual basis;
- report audience-specific exclusions.

## Output Discipline

- Keep the CV clean and external-facing.
- Keep source conflicts, evidence status, coverage decisions, and publication rationale outside the CV.
- Do not call the public repository or generated CV the Source of Truth.
- Do not treat ATS readability as role-specific optimization.
- Continue to use targeted resumes as the default application artifact.
- Do not claim final DOCX publication unless every required executable release check is `PASS`.
