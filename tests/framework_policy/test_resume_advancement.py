from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class ResumeAdvancementPolicyTests(unittest.TestCase):
    def test_rule_02_defines_advancement_as_bounded_resume_objective(self) -> None:
        text = read("rules/02-resume-generation.md")
        self.assertIn("## Resume Advancement Objective", text)
        self.assertIn("advancement from initial resume review to the next hiring stage", text)
        self.assertIn(
            "Qualification -> differentiation -> uncertainty or objection reduction -> narrative coherence -> credibility -> reviewer interest -> advancement",
            text,
        )
        self.assertIn("primary first-scan zone", text)
        self.assertIn("It is not a measured probability, ATS score, candidate rank", text)
        self.assertIn("rather than inventing a role-specific advancement model", text)

    def test_recoverability_rule_adds_decision_salience_without_ats_simulation(self) -> None:
        text = read("rules/22-criterion-evidence-recoverability.md")
        self.assertIn("## Decision Salience", text)
        self.assertIn("proportionate decision salience", text)
        self.assertIn("**Decision salience**", text)
        self.assertIn("**First-scan contribution**", text)
        self.assertIn("resume-conversion probability or numeric advancement score", text)
        self.assertIn("It cannot create candidate evidence", text)

    def test_current_framework_and_release_metadata_expose_advancement_behavior(self) -> None:
        current = read("COMPASS_Current.md")
        version = read("VERSION.md")
        changelog = read("COMPASS_Changelog.md")
        agents = read("AGENTS.override.md")

        self.assertIn("## Resume Advancement Objective", current)
        self.assertIn("Current COMPASS Version: vNext 2026-09.2", version)
        self.assertIn("## vNext 2026-09.2 - Resume Advancement Objective", changelog)
        self.assertIn("Current active version: `vNext 2026-09.2`", agents)

    def test_advancement_preserves_truthguard_and_clean_artifact_boundary(self) -> None:
        rule = read("rules/02-resume-generation.md")
        current = read("COMPASS_Current.md")

        for text in (rule, current):
            self.assertIn("claim depth", text.lower())
            self.assertIn("hard-screen failure", text)
        self.assertIn("internal scoring", current)
        self.assertIn("remain outside the clean resume", current)


if __name__ == "__main__":
    unittest.main()