# COMPASS Custom GPT Deployment

This directory defines the candidate-neutral ChatGPT custom GPT distribution of
the COMPASS Framework. The canonical framework remains the GitHub repository;
the GPT is a versioned conversational runtime, not a second source of framework
truth.

## Architecture

- **Canonical framework:** `mcataloe/compass_framework`
- **GPT runtime:** configuration and instructions in this directory
- **Candidate workspace:** a ChatGPT Project with project-specific bootstrap
  instructions and working context
- **Candidate authority:** a separate private Source of Truth repository

Candidate facts, private repository paths, recruiter history, compensation
constraints, and user-specific policies must never be copied into this public
deployment package.

## Builder configuration

1. Create a GPT in an eligible ChatGPT Business, Enterprise, or Edu workspace.
2. Use the direct configuration editor.
3. Copy the public fields and capability selections from `gpt-config.json`.
4. Copy `instructions.md` into the GPT Instructions field.
5. Enable connected **Apps**, including GitHub. Do not configure custom Actions;
   a GPT can use Apps or Actions, but not both.
6. Do not upload candidate Source of Truth files as GPT Knowledge.
7. Keep sharing private during validation.
8. Run every case in `evals.json` in Preview.
9. Record the created GPT identifier and deployed framework revision outside
   this public repository if either value is workspace-sensitive.

## Runtime expectations

The GPT retrieves the current framework control files from GitHub before
performing COMPASS work. When invoked inside a configured candidate Project, it
also follows that Project's bootstrap and retrieves the candidate runtime and
evidence from the candidate's private Source of Truth repository.

Project conversations and generated artifacts are working context, not factual
authority. Repository retrieval failure, an unresolved framework-version
mismatch, or a missing governing candidate record must fail closed for the
affected candidate-specific output.

## Validation

From the repository root:

```bash
python -m unittest discover -s deployments/chatgpt-custom-gpt/tests -v
```

The test performs structural checks and blocks obvious candidate-specific
content from entering the public GPT package. Preview evals remain required
because static validation cannot prove model behavior or connected-app access.
