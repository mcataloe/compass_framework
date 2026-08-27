from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class VerifiedOpportunitySearchReadinessTests(unittest.TestCase):
    def test_active_version_and_changelog_are_aligned(self) -> None:
        self.assertIn("Current COMPASS Version: vNext 2026-08.8", read("VERSION.md"))
        self.assertIn(
            "## vNext 2026-08.8 - Adaptive Opportunity Yield and Staged Contract Readiness",
            read("COMPASS_Changelog.md"),
        )
        self.assertIn("Current active version: `vNext 2026-08.8`", read("AGENTS.override.md"))

    def test_contract_readiness_is_staged(self) -> None:
        rule = read("rules/12-verified-opportunity-search.md")
        current = read("COMPASS_Current.md")
        prompt = read("prompts/compass-verified-opportunity-search.md")

        for text in (rule, current, prompt):
            self.assertIn("application-stage", text.lower())
            self.assertIn("agreement-stage", text.lower())

        for term in (
            "Intellectual-property assignment",
            "confidentiality detail",
            "termination language",
            "notice obligations",
            "non-solicitation",
        ):
            self.assertIn(term, rule)
        self.assertNotIn(
            "When rate, hours, duration, employment structure, client identity, exclusivity, conversion compensation, or another load-bearing term is missing",
            rule,
        )

    def test_unknown_evidence_detail_is_not_negative_evidence(self) -> None:
        rule = read("rules/12-verified-opportunity-search.md")
        prompt = read("prompts/compass-verified-opportunity-search.md")
        self.assertIn("Do not convert an unresolved evidence detail", rule)
        self.assertIn("exact cadence, frequency, duration, task allocation", rule)
        self.assertIn("Do not convert an unresolved evidence detail", prompt)

    def test_minimum_actionable_result_objective_is_bounded(self) -> None:
        breadth = read("rules/18-opportunity-search-breadth-telemetry.md")
        current = read("COMPASS_Current.md")
        for anchor in (
            "## Minimum Actionable-Result Objectives",
            "configured_search_ceiling_reached",
            "result_objective_status",
            "unmet_after_bounded_exhaustion",
            "baseline breadth checkpoint",
        ):
            self.assertIn(anchor, breadth)
        self.assertIn("minimum actionable-result objective", current)

    def test_pressure_tests_cover_new_behavior(self) -> None:
        cases = read("tests/opportunity_search_breadth/README.md")
        for anchor in (
            "Case 20 — Minimum actionable result continues beyond baseline",
            "Case 21 — Objective satisfied during expansion",
            "Case 22 — Bounded exhaustion below objective",
            "Case 23 — Viability-based no-yield threshold",
            "Case 24 — Evidence detail unknown is not negative evidence",
        ):
            self.assertIn(anchor, cases)


if __name__ == "__main__":
    unittest.main()
