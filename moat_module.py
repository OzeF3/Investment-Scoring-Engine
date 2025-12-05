
from scoring_utils import score_ratio

ROIC_THRESHOLDS = [
    (3, 20),    
    (7, 40),    
    (12, 60),   
    (18, 80),   
    (25, 90),   
                    ]
ROIC_DEFAULT_SCORE = 98   

def roic(roic_5y_avg: float) -> int:
    return score_ratio(roic_5y_avg, ROIC_THRESHOLDS, ROIC_DEFAULT_SCORE)