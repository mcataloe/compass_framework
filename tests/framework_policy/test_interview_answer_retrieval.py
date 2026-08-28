from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class InterviewAnswerRetrievalPolicyTests(unittest.TestCase):
    def test_rule_defines_recall_first_contract(self) -> None:
        text = read("rules/21-interview-answer-retrieval.md")
        for anchor in (
            "## Recall-First Contract",
            "**Core**",
            "**Memory hook**",
            "**Three beats**",
            "**Story hook**",
            "`Do not memorize verbatim`",
        ):
            self.assertIn(anchor, text)

    def test_rule_limits_primary_beats_and_supports_example_pivot(self) -> None:
        text = read("rules/21-interview-answer-retrieval.md")
        self.assertIn("at most three competing top-level ideas", text)
        self.assertIn("## Principle-to-Example Pivot", text)
        self.assertIn("switch directly into one story", text)
        self.assertIn("Stop -> Re-anchor -> Core answer -> Stop", text)

    def test_story_shapes_preserve_source_grounding(self) -> None:
        text = read("rules/21-interview-answer-retrieval.md")
        for shape in (
            "Problem -> Action or decision -> Result",
            "Change -> People -> Action -> Result",
            "Constraint -> Options -> Decision -> Consequence",
        ):
            self.assertIn(shape, text)
        self.assertIn("Do not splice unrelated experiences into a synthetic story", text)

    def test_interview_launcher_loads_rule_21(self) -> None:
        prompt = read("prompts/compass-interview-prep.md")
        self.assertIn("rules/21-interview-answer-retrieval.md", prompt)
        self.assertIn("semantic recall and natural reconstruction under pressure", prompt)

    def test_existing_interview_artifact_contract_remains_intact(self) -> None:
        artifact_rules = read("rules/06-artifact-rules.md")
        for section in (
            "1. Role or conversation context",
            "2. Likely interviewer priorities",
            "3. Source-backed talking points",
            "4. Evidence examples to prepare",
            "5. Likely objections or risk areas",
            "6. Questions to ask",
            "7. TruthGuard cautions",
            "8. Final prep checklist",
        ):
            self.assertIn(section, artifact_rules)

    def test_version_and_changelog_expose_feature(self) -> None:
        version = read("VERSION.md")
        changelog = read("COMPASS_Changelog.md")
        self.assertIn("rules/21-interview-answer-retrieval.md", version)
        self.assertIn("recall-first interview answer retrieval", version.lower())
        self.assertIn(
            "## vNext 2026-08.8 - Recall-First Interview Answer Retrieval",
            changelog,
        )


if __name__ == "__main__":
    unittest.main()
