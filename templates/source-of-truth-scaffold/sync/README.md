# COMPASS Experience Sync Configuration

This directory stores private Source of Truth configuration for downstream experience repositories.

`COMPASS_Experience_Targets.yaml` is the authoritative routing map for COMPASS Experience Sync. It may contain the actual Source of Truth repository, target repository locations, target IDs, branches, publication defaults, protected paths, and write policy.

## Privacy boundary

This file belongs in the private Source of Truth repository. Do not copy it into a public experience repository.

The public target manifest should contain only a stable source identifier, reconciliation commits, framework version, publication metadata, and target-local configuration. It should not expose the private Source of Truth repository name or URL.

## Multiple targets

A Source of Truth may define more than one downstream target, such as:

- a public experience repository;
- a personal website content repository;
- a recruiter-facing evidence repository;
- an internal portfolio;
- a future retrieval or MCP service.

Each target must have a stable `id`. Experience Sync should resolve the requested target by ID before falling back to an explicitly supplied repository override.

## Safety

Source Rebase may create this missing scaffold file only in approved `create-missing-only` mode. Experience Sync reads this configuration but does not modify the Source of Truth.
