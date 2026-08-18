from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class RepositoryPersistencePolicyTests(unittest.TestCase):
    def test_operating_principles_abstract_storage_shape(self) -> None:
        text = read("rules/00-operating-principles.md")
        self.assertIn("## 12. Source-of-Truth Persistence Abstraction", text)
        self.assertIn("current equivalent authority or state", text)
        self.assertIn("do not infer an override", text)

    def test_intake_keeps_default_and_requires_explicit_override(self) -> None:
        text = read("rules/07-compass-intake.md")
        self.assertIn("### Default Artifact Persistence", text)
        self.assertIn("### Repository-Defined Canonical Persistence", text)
        self.assertIn("Do not infer a persistence override", text)
        self.assertIn("may not weaken TruthGuard", text)
        self.assertIn("checkpoint Markdown record", text)

    def test_source_rebase_excludes_explicit_retired_paths(self) -> None:
        text = read("rules/09-source-rebase.md")
        self.assertIn("## Retired Active-Tree Paths", text)
        self.assertIn("do not classify its absence as missing drift", text)
        self.assertIn("do not recreate it", text)
        self.assertIn("Source Rebase", text)
        self.assertIn("must not delete", text)

    def test_generic_manifest_exposes_opt_in_policy(self) -> None:
        text = read("templates/source-of-truth-scaffold/COMPASS_Source_Manifest.md")
        self.assertIn("## Persistence and Lifecycle Policy", text)
        self.assertIn("default_artifact_persistence", text)
        self.assertIn("repository_defined_canonical_persistence", text)
        self.assertIn("Retired active-tree paths", text)

    def test_version_and_changelog_agree(self) -> None:
        version_text = read("VERSION.md")
        changelog = read("COMPASS_Changelog.md")
        match = re.search(r"^Current COMPASS Version: (.+)$", version_text, re.MULTILINE)
        self.assertIsNotNone(match)
        version = match.group(1)
        heading = next(line for line in changelog.splitlines() if line.startswith("## "))
        self.assertTrue(heading.startswith(f"## {version} -"), (version, heading))


if __name__ == "__main__":
    unittest.main()
