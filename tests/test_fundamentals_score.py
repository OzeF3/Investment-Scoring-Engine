
from fundamental_module import calculate_fundamental_scores

def test_fundamentals_score_in_int_range():

    result = calculate_fundamental_scores(
        growth_pct=25,
        operating_margin_pct=23,
        debt_to_equity=1.2,
        free_cash_flow_margin_pct=5,
        sector_name="Energy"
    )

    final_fundamental_score = result["Fundamentals_score"]

    assert isinstance(final_fundamental_score, int)
    assert 0 <= final_fundamental_score <= 100