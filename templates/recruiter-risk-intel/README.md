# Recruiter Risk Intel Templates

This directory contains framework-owned templates for maintaining a private recruiter-risk intelligence ledger.

The COMPASS Framework repository should not store live lists of named recruiters, people, companies, domains, clients, or alleged bad actors. Actual ledger records belong in the user's private Source of Truth or another explicitly configured private store.

## Intended private path

Recommended private Source of Truth path:

```text
intel/recruiter-risk-intel-ledger.yaml
```

## Purpose

A recruiter-risk intelligence ledger is a defensive cache used by `rules/14-recruiter-legitimacy-risk.md` to reduce repeated research and preserve sourced observations across recruiter interactions.

The ledger is not a public accusation list. It is not a substitute for current verification when:

- the record is stale;
- the match is name-only;
- the requested next action is sensitive;
- the opportunity involves staffing, consulting, employer-of-record, government, regulated, security, clearance, or sensitive-client context;
- current evidence conflicts with the cached record.

## Files

- `RECRUITER_RISK_INTEL_LEDGER_TEMPLATE.yaml` — private-ledger scaffold and record schema.

## Maintenance guidance

Use `prompts/compass-recruiter-risk-intel-update.md` to review, refresh, and update a configured private ledger.

Ledger entries should preserve source, date, confidence, status, uncertainty, and the recommended safe action. Prefer exact identifiers such as domains, email domains, profile URLs, requisition identifiers, and application URLs over names alone.
