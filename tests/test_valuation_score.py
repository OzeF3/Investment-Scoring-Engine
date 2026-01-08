
from valuation_module import calculate_valuation_scores

def test_valuation_final_score_int_range():

    result = calculate_valuation_scores(
        stock_pe=12,
        sector_pe=13,
        stock_fpe=10,
        sector_fpe=15,
        stock_eveb=12.0,
        sector_eveb=15.0,
        stock_ps=3.2,
        sector_ps=4,
        stock_pfcf=18,
        sector_pfcf=25,
        sector_name="Utilities",

    )

    final_valuation_score = result["Valuation_score"]

    assert isinstance (final_valuation_score,int)
    assert 0 <= final_valuation_score <= 100