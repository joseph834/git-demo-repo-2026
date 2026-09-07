import unittest

from src.risk_score import calculate_risk_score, risk_band


class RiskScoreTests(unittest.TestCase):
    def test_low_risk_customer(self):
        score = calculate_risk_score(
            age=41,
            annual_income=56_000,
            claim_count=0,
            postcode_risk="low",
        )
        self.assertEqual(score, 0)
        self.assertEqual(risk_band(score), "low")

    def test_high_risk_customer(self):
        score = calculate_risk_score(
            age=22,
            annual_income=28_000,
            claim_count=2,
            postcode_risk="high",
        )
        self.assertEqual(score, 75)
        self.assertEqual(risk_band(score), "high")


if __name__ == "__main__":
    unittest.main()