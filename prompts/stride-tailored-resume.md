# STRIDE Tailored Resume Prompt

Use this prompt after a STRIDE analysis when the user wants a tailored resume.

```text
Generate the STRIDE-tailored resume using the latest approved source resume or CV.

Before running this workflow, read the latest STRIDE framework files from the connected GitHub repo `mjcataldi/stride_framework` on the `main` branch.

Use the repository as the source of truth for STRIDE behavior. Do not rely on cached STRIDE instructions when the repo is available.

Required framework files:
- VERSION.md
- STRIDE_Current.md
- rules/00-operating-principles.md
- rules/02-resume-generation.md
- rules/04-truthguard.md
- rules/06-artifact-rules.md

If GitHub access fails, say so clearly before proceeding. Do not reconstruct STRIDE behavior from memory unless explicitly authorized.

Use the STRIDE findings above.
Resume density mode: Balanced unless otherwise specified.
Keep it truthful, ATS-aware, staff-level, and recruiter-readable.
Do not include STRIDE analysis inside the resume artifact.
Do not invent technologies, metrics, ownership, credentials, employment history, or experience.
Create the resume as a clean artifact suitable for Word, PDF, and Markdown export.

Target role:
[ROLE TITLE / COMPANY]
```

## Notes

The generated resume should be a clean resume only. Any caveats, TruthGuard notes, or strategic warnings should be placed in chat outside the artifact.
