# STRIDE Cover Letter Prompt

Use this prompt after STRIDE analysis when the user wants a role-specific cover letter.

```text
Generate a STRIDE-based cover letter for this role.

Before running this workflow, read the latest STRIDE framework files from the connected GitHub repo `mjcataldi/stride_framework` on the `main` branch.

Use the repository as the source of truth for STRIDE behavior. Do not rely on cached STRIDE instructions when the repo is available.

Required framework files:
- VERSION.md
- STRIDE_Current.md
- rules/00-operating-principles.md
- rules/03-cover-letter-generation.md
- rules/04-truthguard.md
- rules/06-artifact-rules.md

If GitHub access fails, say so clearly before proceeding. Do not reconstruct STRIDE behavior from memory unless explicitly authorized.

Tone: professional, grounded, forward-looking, not overly enthusiastic.
Use only truthful experience from the latest approved source resume or CV and the job description.
Keep it concise and role-specific.
Do not include STRIDE analysis inside the cover letter.
Do not invent technologies, metrics, ownership, credentials, employment history, or experience.
```

## Notes

The cover letter should be clean, direct, and suitable for submission. Strategic caveats should appear outside the artifact.
