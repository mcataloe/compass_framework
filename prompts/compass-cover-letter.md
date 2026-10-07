# COMPASS Career Profile: Cover Letter Prompt

```text
Generate the COMPASS cover letter from the user's current instruction, verified claim ledgers, do-not-claim records, latest approved canonical career record, and the controlling job description as tailoring context only.

Required framework files:
- VERSION.md
- COMPASS_Current.md
- rules/00-operating-principles.md
- rules/03-cover-letter-generation.md
- rules/04-truthguard.md
- rules/06-artifact-rules.md
- rules/08-human-authenticity.md
- rules/20-professional-effectiveness-evidence.md

Load the user's current artifact-generation, cover-letter style, candidate-voice, and recommended-opportunity-artifact policies when available.

Before drafting, run the Pre-Draft Artifact Materiality Gate in `rules/06-artifact-rules.md` and the cover-letter-specific criteria in `rules/03-cover-letter-generation.md`. Inspect available authoritative context first and ask only unresolved material questions. Zero questions is valid. If the user requested a resume for the same target in the same operation, inspect both artifacts first and issue one coordinated materiality session before drafting either artifact.


Before drafting:

1. Determine the relationship context: cold application, prior recruiter contact, completed recruiter screen, referral, direct hiring-manager interaction, or established professional relationship.
2. Identify what the resume, LinkedIn profile, and other application materials already prove.
3. Discover the strongest genuine connection available among mission/purpose, people/relationship, role/problem, or professional point of view. Do not invent one.
4. Identify what useful human, relational, reflective, or judgment-based information the cover letter can add.
5. Define one central argument or connection for continued conversation.
6. Choose one primary narrative archetype from Rule 03: Conversation Continuation, Story / Lesson Led, Operating-Model Fit, Problem / Insight Led, or Direct Fit.
7. Select one anchor story when one materially strengthens the argument; allow grounded vulnerability, changed minds, mistakes, failed approaches, or direct emotion when they reveal useful judgment or connection.
8. Use qualification evidence selectively rather than cataloging matching skills or projects already established elsewhere.
9. Resolve the content budget using this precedence: explicit application-provider limit, current user-specific limit, then the COMPASS default portable ceiling of 2,000 characters including spaces and punctuation.
10. Draft with progressive technical disclosure so the reader understands why an example matters before encountering dense implementation detail; for a highly personal grounded connection, the story may develop before the technical payoff.
11. Prefer an ending that lands the central human or intellectual idea over ceremonial application language when the stronger ending reads naturally.
12. Run the finished draft through the connection, qualification-duplication, resume-recap, job-description-echo, grounded-personalization, vulnerability-relevance, technical-density, central-argument, continuity, ending-resonance, deletion, TruthGuard, and Human Authenticity checks.

Do not default to an opening-fit-statement structure. Do not force a cold-application voice when prior interaction provides meaningful context. Do not invent motivation, affinity, enthusiasm, mission alignment, culture fit, or personality in order to personalize the letter.

Keep the letter professional, natural, specific, source-grounded, and free of internal COMPASS analysis.

When the role materially values critical thinking, systems thinking, judgment, communication, influence, collaboration, ownership, adaptability, stakeholder management, or related behavior, apply rules/20-professional-effectiveness-evidence.md. Demonstrate the strongest relevant capability through one or two concrete source-backed actions, decisions, tradeoffs, or outcomes rather than listing soft-skill adjectives.

When more than one role is available, ask which role controls only when the set is ambiguous. When the user explicitly requests all recommended roles from a completed Verified Opportunity Search, or otherwise identifies a bounded multi-role set, generate one independently tailored cover letter per eligible role under the user's recommended-opportunity-artifact policy.
```
