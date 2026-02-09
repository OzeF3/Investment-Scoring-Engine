import requests
import json

def fetch_moat_data(ticker: str) -> dict:

    clean_ticker = ticker.strip().upper()

    url = "https://yahoo-finance166.p.rapidapi.com/api/stock/get-financial-data"

    querystring = {"region":"US","symbol":ticker}

    headers = {
        "x-rapidapi-key": "ac7d1c4b19mshe08636b12ca178bp1254e4jsn916ba406437e",
        "x-rapidapi-host": "yahoo-finance166.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())
    data = response.json()   # ← זה המילון

    # 👇 שמירה לקובץ JSON
    with open(f"Saved to fundamental_{clean_ticker}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Saved to fundamental_{clean_ticker}.json")

    revenue_growth_raw = (
    data["quoteSummary"]["result"][0]
            ["financialData"]["revenueGrowth"]["raw"]
        )
    revenue_growth_pct = revenue_growth_raw * 100

    operating_margin_raw = (
    data["quoteSummary"]["result"][0]
            ["financialData"]["operatingMargins"]["raw"]
        )
    operating_margin = operating_margin_raw * 100

    debt_to_equity = (
    data["quoteSummary"]["result"][0]
            ["financialData"]["debtToEquity"]["raw"])

    #FREE CASH FLOW MARGIN(TTM) = (Levered free cash flow(ttm)/ Revenue(ttm) )

    revenue = (
    data["quoteSummary"]["result"][0]
            ["financialData"]["totalRevenue"]["raw"])
    
    levered_free_cash_flow = (
    data["quoteSummary"]["result"][0]
            ["financialData"]["freeCashflow"]["raw"])
    
    free_cash_flow_margin = levered_free_cash_flow / revenue

    print(f"Quarterly Revenue Growth (yoy): {revenue_growth_pct:.2f}%")
    print(f" Operating Margin (ttm): {operating_margin:.2f}%")
    print(f" Total Debt/Equity (mrq): {debt_to_equity:.2f}%")
    print(f" Free Cash Flow Margin(ttm): {free_cash_flow_margin:.2f}%")

    return {
        "revenuegrowth": revenue_growth_pct,
        "operatingmargin": operating_margin,
        "debttoequity": debt_to_equity,
        "freecashflowmargin": free_cash_flow_margin
    }
