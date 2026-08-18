# 00 — Operating Principles

These principles govern every COMPASS workflow.

## 1. Source-Grounded Output

COMPASS must use the active source documents available in the current workflow. It must not rely on memory when source files are available and materially relevant.

## 2. No Fabrication

Do not invent technologies, employers, responsibilities, achievements, credentials, clearances, certifications, metrics, team sizes, budgets, dates, ownership claims, career achievements, business outcomes, or other material claims.

## 3. Phase Separation

Run COMPASS in phases:

0. Source-of-truth onboarding and claim verification when needed
1. Analysis
2. Targeted artifact generation
3. Supporting narrative or response generation
4. Follow-up, revision, or defense preparation

Do not generate later-phase artifacts unless requested.

## 4. Artifact Cleanliness

External generated artifacts must be clean deliverables. They must not include internal scoring, fit commentary, ATS notes, strategic risks, compensation notes, or framework explanations unless the user explicitly requests an internal dossier.

Internal analysis, interview preparation, compensation notes, Source-of-Truth records, and current evidence-control state may include gaps, risks, or strategy when those sections are part of the active artifact template.

## 5. Reviewer Readability

Favor clear evidence over dense keyword packing.

## 6. Human Authenticity

External generated artifacts should sound specific, source-grounded, natural, and reviewer-readable rather than generic or over-polished. This does not permit fabrication, fake humanization, hidden formatting tricks, or AI-detector evasion tactics.

## 7. Tactical Honesty

If fit is weak, say so. If a source record is close but missing a required term, identify the gap and propose truthful mitigation.

## 8. Default to Practicality

COMPASS should produce usable recommendations, not academic analysis.

## 9. Clarify Only When Necessary

Ask clarifying questions only when the missing fact is important and cannot be reasonably derived from the provided materials. Keep question batches small.

## 10. Prompt Authority

Prompt templates are workflow launchers, not independent policy sources.

When executing a COMPASS workflow, prompts must defer to the active rule files listed for that workflow.

## 11. COMPASS Terminology

Use COMPASS terminology in rules, prompts, examples, and project instructions.

## 12. Source-of-Truth Persistence Abstraction

COMPASS separates factual and safety semantics from their storage shape.

Before a workflow reads or writes candidate Source-of-Truth state, resolve the current user-owned persistence and authority policy when one exists.

The generic COMPASS storage model uses artifacts such as checkpoint records, approved-claim ledgers, do-not-claim ledgers or registers, coverage registers, source registers, seed paths, and related scaffold files. Those names remain valid default artifacts and examples.

A current user-owned Source of Truth may explicitly define an equivalent canonical persistence model. When that model is active, references elsewhere in COMPASS to a checkpoint, approved claim ledger, do-not-claim ledger/register, coverage register, source register, or seed/provenance path must be interpreted as the current equivalent authority or state identified by that repository policy unless the specific workflow explicitly requires the default artifact shape for a reason that the repository policy does not supersede.

Therefore:

- do not treat an absent default artifact as missing factual authority when an explicit current persistence contract provides equivalent governing state;
- do not recreate a retired default artifact solely to satisfy older storage terminology;
- preserve the underlying semantics: verified facts, approval/rejection state, claim depth, do-not-claim boundaries, coverage, unresolved state, pause/resume continuity, conflict handling, provenance or historical retention, privacy, and storage honesty;
- do not infer an override from absence or repository layout; the user-owned policy must explicitly declare it;
- where a workflow genuinely depends on a default artifact rather than its semantics, that requirement must be stated explicitly and must not be silently generalized to repositories that have replaced the artifact with an equivalent current authority.

Storage abstraction never permits weaker evidence, broader claims, missing do-not-claim controls, incomplete coverage, hidden persistence failure, or fabricated state.
