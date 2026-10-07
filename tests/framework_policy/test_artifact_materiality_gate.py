from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class ArtifactMaterialityGatePolicyTests(unittest.TestCase):
    def test_shared_artifact_rule_defines_materiality_gate(self) -> None:
        text = read("rules/06-artifact-rules.md")
        for anchor in (
            "## Pre-Draft Artifact Materiality Gate",
            "INSPECT -> CLASSIFY -> ASK / ASSUME / STOP -> RE-EVALUATE",
            "Zero questions is a valid and common outcome.",
            "### Coordinate multiple requested artifacts",
            "**Shared**",
            "**Resume**",
            "**Cover Letter**",
            "### No Gate modifier",
        ):
            self.assertIn(anchor, text)

    def test_resume_rule_defines_artifact_specific_materiality(self) -> None:
        text = read("rules/02-resume-generation.md")
        self.assertIn("## Resume Materiality Criteria", text)
        self.assertIn("hard screen, load-bearing qualification, or central responsibility", text)
        self.assertIn("direct, adjacent, transferable, provisional", text)
        self.assertIn("Do not ask which project to emphasize", text)

    def test_cover_letter_rule_protects_personal_meaning(self) -> None:
        text = read("rules/03-cover-letter-generation.md")
        self.assertIn("## Cover Letter Materiality Criteria", text)
        self.assertIn("must not invent personal meaning, motivation, affinity, or emotional connection", text)
        self.assertIn("genuine mission, purpose, people, role, problem, or domain connection", text)
        self.assertIn("single coordinated materiality session", text)

    def test_launchers_coordinate_companion_artifacts(self) -> None:
        resume = read("prompts/compass-tailored-resume.md")
        cover = read("prompts/compass-cover-letter.md")
        self.assertIn("Pre-Draft Artifact Materiality Gate", resume)
        self.assertIn("one coordinated materiality session before drafting either artifact", resume)
        self.assertIn("Pre-Draft Artifact Materiality Gate", cover)
        self.assertIn("one coordinated materiality session before drafting either artifact", cover)

    def test_command_and_current_surfaces_expose_gate(self) -> None:
        commands = read("COMPASS_COMMANDS.md")
        current = read("COMPASS_Current.md")
        version = read("VERSION.md")
        changelog = read("COMPASS_Changelog.md")
        agents = read("AGENTS.override.md")

        self.assertIn("Pre-Draft Artifact Materiality Gate", commands)
        self.assertIn("## Pre-Draft Artifact Materiality Gate", current)
        self.assertIn("Current COMPASS Version: vNext 2026-10.1", version)
        self.assertIn("## vNext 2026-10.1 - Pre-Draft Artifact Materiality Gate", changelog)
        self.assertIn("Current active version: `vNext 2026-10.1`", agents)


if __name__ == "__main__":
    unittest.main()
