# 22 - Criterion Evidence Recoverability

## Purpose

This rule extends role-tailored resume generation with a post-draft evidence-recoverability check.

COMPASS must not assume that an employer uses any particular ATS, ranking model, reranker, parser, embedding system, classifier, or scoring architecture. Instead, it optimizes for a durable invariant:

> Important qualifications that the candidate truthfully satisfies should be independently recoverable from the finished resume by a human reviewer or a reasonable automated criterion evaluator without requiring speculative inference.

This rule governs tailored resumes and any recruiter-targeted resume that is explicitly bounded to a concrete job description or requirement set. It does not create a target taxonomy for broad recruiter resumes.

## Relationship to Existing Resume Prioritization

`rules/02-resume-generation.md` governs target-criterion importance, qualification versus differentiation, claim-depth-aware wording, bullet construction, and resume structure.

This rule does not replace those decisions. It adds a verification loop after a draft has been assembled:

1. classify the bounded target criteria under Rule 02;
2. resolve only source-backed candidate evidence under the active Source of Truth;
3. select and order evidence using qualification-plus-differentiation logic;
4. draft the resume;
5. audit criterion-level evidence recoverability in the actual finished draft;
6. revise only when recoverability is materially weak and stronger truthful presentation is available;
7. preserve human readability, TruthGuard, claim depth, artifact cleanliness, and release assurance.

## Criterion Scope

The recoverability audit is mandatory for every criterion classified as:

- **Hard screen** that the candidate truthfully satisfies and that is appropriate to expose in the resume;
- **Load-bearing required qualification** that the candidate truthfully satisfies;
- **Material central responsibility** for which the candidate has source-backed evidence.

The audit may also cover differentiating preferred qualifications when they materially affect reviewer value, but preferred evidence must not crowd out required qualification coverage.

Do not create evidence for an unsupported criterion merely because it appears in the target. Unsupported criteria remain unsupported and are handled by existing analysis, TruthGuard, and gap-salience rules.

## Internal Recoverability Record

For each in-scope target criterion, build an internal record containing at least:

- target criterion;
- target importance classification;
- whether governing Source-of-Truth evidence exists;
- governing evidence scope or scopes;
- approved claim depth and any do-not-claim boundary;
- resume location or locations where the evidence appears;
- recoverability status;
- revision action when needed.

This internal record is validation working state. Do not place the matrix, scores, framework labels, or validation notes inside the resume artifact unless the user explicitly requests an annotated artifact.

## Recoverability Status

Use these internal statuses:

### Strong

A reviewer can identify the relevant qualification from explicit, coherent, source-backed resume evidence with little or no inference.

Strong evidence normally identifies the candidate's action, responsibility, technical mechanism, scope, or consequence in a way that makes the target capability recognizable.

### Adequate

The qualification is recoverable from coherent source-backed evidence, but the wording is somewhat broader, less prominent, or less direct than the strongest available formulation.

Adequate is acceptable when greater specificity would overstate claim depth, create unnatural prose, add redundant detail, or reduce overall reviewer readability.

### Weak

The candidate has governing source-backed evidence, but the finished resume exposes it only indirectly, ambiguously, too generically, too far from the relevant work context, or only through a broad skills inventory when stronger contextual evidence is available.

Weak recoverability should trigger revision when a truthful, coherent improvement is available without materially harming higher-priority evidence or readability.

### Unsupported

No governing source-backed evidence supports the target criterion at the needed depth.

Unsupported is not a drafting defect. Do not revise the resume to manufacture coverage. Preserve the gap under applicable analysis and TruthGuard rules.

### Not Applicable

The target element does not require resume exposure under the active bounded criterion set, or the active Source-of-Truth/public-disclosure policy prohibits or makes exposure inappropriate.

## Recoverability Tests

A criterion is not Strong merely because the exact target keyword appears somewhere in the document.

Evaluate at least these questions:

1. **Explicitness** — Does the resume state enough of the capability that a reviewer can recognize it without inventing missing context?
2. **Context** — Is the capability connected to actual work, responsibility, project, decision, or implementation rather than appearing only as an isolated keyword?
3. **Claim depth** — Does the wording remain within the governing approved depth?
4. **Coherence** — Does the evidence arise naturally from one underlying accomplishment or work scope rather than from artificial keyword aggregation?
5. **Placement** — Is the evidence visible in a section and position proportionate to the criterion's importance?
6. **Distinct coverage** — Are different load-bearing criteria actually represented, rather than several early bullets redundantly proving one baseline capability?
7. **Human readability** — Would the wording still make sense to a human reviewer if no ATS optimization existed?

## Skills-Section Rule

A Core Skills entry may strengthen recognizability, terminology matching, or parsing, but it is not automatically sufficient proof of a load-bearing qualification.

When stronger source-backed contextual evidence exists, a hard screen, load-bearing qualification, or material central responsibility should normally be recoverable from Professional Experience, Selected Projects, or another substantive evidence-bearing section.

Do not duplicate every technology from every bullet into Core Skills. Use the skills section as a curated index, not as a substitute for work evidence.

## Semantic Equivalence and Exact Terminology

COMPASS should preserve truthful semantic equivalence rather than blindly mirroring target wording.

Use the employer's terminology when:

- it accurately describes the candidate's verified experience;
- it improves recognizability without changing meaning or claim depth; and
- it reads naturally in context.

Do not force an exact target phrase when the candidate's actual experience is adjacent, broader, narrower, differently implemented, or unsupported.

A criterion may be Strong without an exact lexical match when the resume's evidence is unmistakably equivalent. Conversely, an exact keyword match may still be Weak if it lacks supporting context.

## Revision Loop

After drafting the tailored resume:

1. Audit every in-scope criterion against the actual draft.
2. Identify only material Weak findings where governing evidence exists.
3. Revise by improving one or more of:
   - evidence selection;
   - wording specificity;
   - target-accurate terminology;
   - evidence placement;
   - bullet order;
   - non-redundant coverage across early bullets;
   - contextual support for a skills-section term.
4. Rerun the audit after revision.
5. Stop revising when every supported hard screen and load-bearing qualification is Strong or Adequate and material central responsibilities have proportionate recoverability.

Do not continue rewriting merely to maximize keyword count or make every criterion Strong. Adequate is a valid terminal state when further optimization would weaken truthfulness, claim-depth precision, readability, differentiation, or overall resume quality.

## Human-First Constraint

Criterion recoverability is not permission to turn a resume into a machine-facing requirement checklist.

The finished artifact must remain:

- natural for a human reviewer;
- source-grounded;
- candidate-specific;
- concise enough for the active resume density policy;
- coherent at the bullet and role level;
- free of internal scores, matrices, or framework jargon;
- free of hidden text, parser tricks, white-on-white terms, keyword blocks, or other deceptive ATS tactics.

When machine recognizability and human readability conflict, prefer the strongest truthful wording that preserves human usefulness. Do not optimize for a speculative proprietary ATS behavior.

## No ATS Score or Proprietary-System Simulation

COMPASS must not invent or report:

- an ATS score;
- a candidate rank;
- a reranker score;
- an embedding similarity score;
- a probability that an ATS will advance the candidate;
- a claim that a named vendor uses a particular model architecture unless current reliable evidence establishes it and the workflow actually requires that research.

System-specific knowledge may inform terminology or artifact choices when verified, but the core resume behavior remains vendor-neutral criterion evidence recoverability.

## TruthGuard and Source Authority

This rule may change selection, wording, ordering, and placement only. It cannot create candidate evidence.

All candidate facts remain governed by the active Source of Truth, claim-depth boundaries, do-not-claim controls, collaborator and ownership boundaries, implementation stage, outcome status, confidentiality, and public-disclosure policy.

If the audit reveals that a material target criterion lacks governing evidence, mark it Unsupported internally and preserve the gap. Do not use target language, an older resume, a generated artifact, or semantic similarity as substitute evidence.

## Release Behavior

Criterion Evidence Recoverability is a content-quality gate that runs before final resume release assurance.

A tailored resume should not be treated as content-complete when a supported hard screen or load-bearing qualification remains materially Weak solely because the draft failed to expose available governing evidence and a truthful revision is available.

This rule does not alter the executable resume-release contract, artifact-name integrity rules, visual validation, employment coverage requirements, or `PASS` / `FAIL` / `UNKNOWN` semantics of `rules/16-resume-release-assurance.md`.
