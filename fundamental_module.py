
from scoring_utils import score_by_thresholds
from config import fundamental_weight

#creating table with limits and score limits
REVENUE_GROWTH_PCT_THRESHOLDS = [
    (0.0,20),
    (5.0,40),
    (15.0,60),
    (30.0,80),
                    ]
REVENUE_GROWTH_PCT_DEFAULT = 95

OPERATING_MARGIN_PCT_THRESHOLDS = [
    (0.0,20),
    (5.0,40),
    (15.0,60),
    (25.0,80),
                    ]
OPERATING_MARGIN_PCT_DEFAULT = 95

DEBT_TO_EQUITY_RATIO_THRESHOLDS = [
    (0.2, 95), 
    (0.5, 80),  
    (1.0, 60), 
    (2.0, 40),
                 ]
DEBT_TO_EQUITY_RATIO_DEFAULT = 20

FREE_CASH_FLOW_MARGIN_PCT_THRESHOLDS = [
    (0, 20),
    (5, 40),
    (10, 60),
    (20, 80),
                ]
FREE_CASH_FLOW_MARGIN_PCT_DEFAULT = 95

#specific function that sends info to the generic function in order to help it find score
def revenue_growth_pct_score(revenue_growth_pct: float) -> int:
    return score_by_thresholds(revenue_growth_pct, REVENUE_GROWTH_PCT_THRESHOLDS, REVENUE_GROWTH_PCT_DEFAULT)

def operating_margin_pct_score(operating_margin_pct: float) -> int:
    return score_by_thresholds(operating_margin_pct, OPERATING_MARGIN_PCT_THRESHOLDS, OPERATING_MARGIN_PCT_DEFAULT)

def debt_to_equity_ratio_score(debt_to_equity: float) -> int:
    return score_by_thresholds(debt_to_equity, DEBT_TO_EQUITY_RATIO_THRESHOLDS, DEBT_TO_EQUITY_RATIO_DEFAULT)

def free_cash_flow_margin_pct_score(free_cash_flow_margin_pct: float) -> int:
    return score_by_thresholds(free_cash_flow_margin_pct, FREE_CASH_FLOW_MARGIN_PCT_THRESHOLDS, FREE_CASH_FLOW_MARGIN_PCT_DEFAULT)

def fundamental_weighted_score(
        g: int,
        p: int,
        d: int,
        f: int,
        wbs: dict
                            ) -> int:

    growth_weight = wbs['growth']      
    margin_weight = wbs['profit']   
    dte_weight = wbs['debt_to_equity'] 
    fcf_weight = wbs['fcf']           

    weighted_together = (growth_weight * g + margin_weight * p + dte_weight * d + fcf_weight * f)
    return round(weighted_together)

def calculate_fundamental_scores(
    revenue_growth_pct: float,
    operating_margin_pct: float,
    debt_to_equity_ratio: float,
    free_cash_flow_margin_pct: float,
    sector_name: str
                                    ) -> dict:   
    """
    Core function of the fundamentals module.
    Gets raw inputs and returns all scores + final fundamentals_score.
    """
    g = revenue_growth_pct_score(revenue_growth_pct)
    p = operating_margin_pct_score(operating_margin_pct)
    d = debt_to_equity_ratio_score(debt_to_equity_ratio)
    f = free_cash_flow_margin_pct_score(free_cash_flow_margin_pct)
    weight_by_sector = fundamental_weight(sector_name)

    final_score = fundamental_weighted_score(g, p, d, f, weight_by_sector)

    return {
        "revenue_growth_pct_score": g,
        "operating_margin_pct_score": p,
        "debt_to_equity_ratio_score": d,
        "free_cash_flow_margin_pct_score": f,
        "sector_name": sector_name,
        "weight_currently_being_used": weight_by_sector,
        "fundamentals_score": final_score
            }




