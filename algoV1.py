

def score_growth(growth_pct: float) -> int:
    
    if growth_pct < 0:
        return 20
    elif growth_pct < 5:
        return 40
    elif growth_pct < 15:
        return 60
    elif growth_pct < 30:
        return 80
    else:
        return 95

sc = input("PLS input growth pct: ")
growth_percentage = float(sc)
print(score_growth(growth_percentage))

    

# GROWTH_TRSESHHOLDS = [
#     (0.0,20),
#     (5.0,40),
#     (15.0,60),
#     (30.0,80),
# ]
# GROWTH_DEFAULT = 95

