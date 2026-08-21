from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class ProfessionalEffectivenessPolicyTests(unittest.TestCase):
    def test_rule_defines_core_taxonomy_and_signal_strengths(self) -> None:
        text = read("rules/20-professional-effectiveness-evidence.md")
        for capability in (
            "critical_thinking",
            "problem_framing",
            "systems_thinking",
            "judgment_under_ambiguity",
            "influence_without_authority",
            "ownership",
            "ambiguity_navigation",
        ):
            self.assertIn(f"`{capability}`", text)

        for strength in ("direct", "corroborated", "indicative"):
            self.assertIn(f"`{strength}`", text)

    def test_rule_keeps_behavioral_labels_derived_and_non_diagnostic(self) -> None:
        text = read("rules/20-professional-effectiveness-evidence.md")
        self.assertIn("Capability tags are derived metadata", text)
        self.assertIn("Do not create professional-effectiveness evidence from a target job description", text)
        self.assertIn("Do not create a personality scorecard", text)
        self.assertIn("Do not create a fourteenth required report section", text)
        self.assertIn("Do not add a generic `Soft Skills` section by default", text)

    def test_analysis_and_artifact_launchers_load_rule_20(self) -> None:
        for path in (
            "prompts/compass-analysis.md",
            "prompts/compass-intake.md",
            "prompts/compass-tailored-resume.md",
            "prompts/recruiter-targeted-resume.md",
            "prompts/compass-cover-letter.md",
            "prompts/compass-interview-prep.md",
        ):
            self.assertIn("rules/20-professional-effectiveness-evidence.md", read(path), path)

    def test_command_registry_routes_affected_workflows_to_rule_20(self) -> None:
        text = read("COMPASS_COMMANDS.md")
        self.assertGreaterEqual(text.count("rules/20-professional-effectiveness-evidence.md"), 6)
        self.assertIn("Professional-effectiveness capability labels", text)
        self.assertIn("generic Soft Skills section", text)

    def test_version_and_current_framework_expose_feature(self) -> None:
        version = read("VERSION.md")
        current = read("COMPASS_Current.md")
        changelog = read("COMPASS_Changelog.md")

        self.assertIn("Current COMPASS Version: vNext 2026-08.7", version)
        self.assertIn("rules/20-professional-effectiveness-evidence.md", version)
        self.assertIn("## Professional Effectiveness Evidence", current)
        self.assertIn("## vNext 2026-08.7 - Professional Effectiveness Evidence", changelog)


if __name__ == "__main__":
    unittest.main()
