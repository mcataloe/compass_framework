import json
import pathlib
import re
import unittest


PACKAGE_ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO_ROOT = PACKAGE_ROOT.parents[1]


class CustomGptPackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = json.loads((PACKAGE_ROOT / "gpt-config.json").read_text())
        cls.instructions = (PACKAGE_ROOT / "instructions.md").read_text()
        cls.evals = json.loads((PACKAGE_ROOT / "evals.json").read_text())

    def test_required_configuration(self):
        self.assertEqual(self.config["integration_mode"], "apps")
        self.assertIn("GitHub", self.config["required_apps"])
        self.assertEqual(
            self.config["framework_repository"], "mcataloe/compass_framework"
        )
        self.assertEqual(self.config["framework_branch"], "main")
        self.assertEqual(self.config["sharing_during_validation"], "private")
        self.assertEqual(self.config["knowledge_files"], [])
        self.assertGreaterEqual(len(self.config["conversation_starters"]), 3)

    def test_validated_framework_version_matches_current_version(self):
        version_text = (REPO_ROOT / "VERSION.md").read_text()
        match = re.search(r"^Current COMPASS Version: (.+)$", version_text, re.MULTILINE)
        self.assertIsNotNone(match)
        self.assertEqual(self.config["validated_framework_version"], match.group(1))
        self.assertRegex(self.config["validated_framework_commit"], r"^[0-9a-f]{40}$")

    def test_instructions_require_current_github_preflight(self):
        for required in (
            "VERSION.md",
            "COMPASS_Current.md",
            "COMPASS_COMMANDS.md",
            "Use the GitHub app",
        ):
            self.assertIn(required, self.instructions)

    def test_instructions_fail_closed(self):
        for required in (
            "Retrieval failure",
            "Do not substitute memory",
            "Stop on material conflicts",
            "first draft is internal and untrusted",
        ):
            self.assertIn(required, self.instructions)

    def test_public_package_has_no_known_candidate_content(self):
        package_text = "\n".join(
            path.read_text()
            for path in (
                PACKAGE_ROOT / "README.md",
                PACKAGE_ROOT / "gpt-config.json",
                PACKAGE_ROOT / "instructions.md",
                PACKAGE_ROOT / "evals.json",
            )
        ).lower()
        forbidden = (
            "matthew cataldi",
            "compass-source-of-truth",
            "matthew-cataldi-experience",
            "job_hunt_runtime.md",
        )
        for value in forbidden:
            self.assertNotIn(value, package_text)

    def test_eval_suite_covers_load_bearing_boundaries(self):
        ids = {case["id"] for case in self.evals["cases"]}
        self.assertTrue(
            {
                "framework-preflight",
                "project-runtime-routing",
                "source-conflict",
                "target-prompt-injection",
                "github-unavailable",
                "version-mismatch",
                "pending-release",
                "no-unrequested-action",
                "candidate-neutral-package",
            }.issubset(ids)
        )


if __name__ == "__main__":
    unittest.main()
