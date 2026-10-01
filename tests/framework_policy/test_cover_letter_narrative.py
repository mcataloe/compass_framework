from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class CoverLetterNarrativePolicyTests(unittest.TestCase):
    def test_rule_03_uses_adaptive_narrative_archetypes(self) -> None:
        text = read("rules/03-cover-letter-generation.md")
        for anchor in (
            "## Adaptive Narrative Archetypes",
            "### Conversation Continuation",
            "### Story / Lesson Led",
            "### Operating-Model Fit",
            "### Problem / Insight Led",
            "### Direct Fit",
            "one central argument",
            "progressively",
        ):
            self.assertIn(anchor, text)

    def test_rule_03_defines_portable_character_budget_without_minimum(self) -> None:
        text = read("rules/03-cover-letter-generation.md")
        self.assertIn("2,000 characters including spaces and punctuation", text)
        self.assertIn("application-provider or application-field", text)
        self.assertIn("user-specific Source-of-Truth", text)
        self.assertIn("no generic minimum cover-letter length", text)

    def test_fixed_semantic_cover_letter_template_is_removed(self) -> None:
        rule = read("rules/03-cover-letter-generation.md")
        artifacts = read("rules/06-artifact-rules.md")
        prompt = read("prompts/compass-cover-letter.md")
        for text in (rule, artifacts, prompt):
            self.assertNotIn("Opening fit statement", text)
            self.assertNotIn("Evidence-backed value paragraph", text)
            self.assertNotIn("Role-specific alignment paragraph", text)
        self.assertIn("## Cover Letter Structural Scaffold", artifacts)
        self.assertIn("Do not default to an opening-fit-statement structure", prompt)

    def test_human_authenticity_supports_grounded_personalization_and_continuity(self) -> None:
        text = read("rules/08-human-authenticity.md")
        self.assertIn("## Grounded Personalization and Cover-Letter Continuity", text)
        self.assertIn("preserve continuity where useful", text)
        self.assertIn("Do not invent passion, admiration, culture fit, mission affinity", text)

    def test_current_framework_and_release_metadata_expose_cover_letter_behavior(self) -> None:
        version = read("VERSION.md")
        current = read("COMPASS_Current.md")
        changelog = read("COMPASS_Changelog.md")
        agents = read("AGENTS.override.md")
        self.assertIn("Current COMPASS Version: vNext 2026-10.0", version)
        self.assertIn("## Adaptive Cover Letter Narrative", current)
        self.assertIn("## vNext 2026-10.0 - Adaptive Cover Letter Narrative", changelog)
        self.assertIn("Current active version: `vNext 2026-10.0`", agents)


if __name__ == "__main__":
    unittest.main()
