def calculate_risk_score(age, annual_income, claim_count, postcode_risk):
    """Return an illustrative insurance risk score.

    This is deliberately simplified training code. It is not a real
    underwriting or pricing model.
    """
    score = 0

    if age < 25:
        score += 20
    elif age >= 65:
        score += 10

    if annual_income < 30_000:
        score += 10

    score += claim_count * 15

    postcode_adjustments = {
        "low": 0,
        "medium": 5,
        "high": 15,
    }
    score += postcode_adjustments[postcode_risk]

    return score


def risk_band(score):
    """Map a score to a human-readable risk band."""
    if score >= 50:
        return "high"
    if score >= 25:
        return "medium"
    return "low"


def describe_customer_risk(customer):
    """Return a readable risk summary for one customer record."""
    score = calculate_risk_score(
        age=customer["age"],
        annual_income=customer["annual_income"],
        claim_count=customer["claim_count"],
        postcode_risk=customer["postcode_risk"],
    )
    return f'{customer["customer_id"]}: {risk_band(score)} ({score})'