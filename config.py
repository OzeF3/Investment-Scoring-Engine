
# file will help determine between differnet type of sector and help selidify weighted scores per sector.

def fundamental_weight(sector_name: str) -> dict:
    
    SECTOR_WEIGHTS = {
    "technology": {
        "growth": 0.30,
        "profit": 0.30,
        "debt_to_equity": 0.20,
        "fcf": 0.20
                },
    "healthcare": {
        "growth": 0.25,
        "profit": 0.35,
        "debt_to_equity": 0.20,
        "fcf": 0.20
                    },
    "financials": {
        "growth": 0.20,
        "profit": 0.40,
        "debt_to_equity": 0.30,
        "fcf": 0.10
                    }
                    }

    sector_name = sector_name.lower().strip()

    if sector_name not in SECTOR_WEIGHTS:
        raise ValueError(f"Unsupported sector: sector {sector_name} is not defind in the system")
    return SECTOR_WEIGHTS[sector_name]

    





def valuation_weight(sector_name: str) -> dict:
    pass

def moat_weight(sector_name: str) -> dict:
    pass

def total_weight(sector_name: str) -> dict:
    pass

