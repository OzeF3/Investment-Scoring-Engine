import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_fundamental_data(ticker: str) -> dict:

    clean_ticker = ticker.strip().upper()

    #API Yfinance / stocks / financialData 
    url = "https://yahoo-finance166.p.rapidapi.com/api/stock/get-financial-data"

    querystring = {"region":"US","symbol":clean_ticker}

    headers = {
        "x-rapidapi-key": os.getenv("API_FUNDAMENTAL_ONE"),
        "x-rapidapi-host": "yahoo-finance166.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()   

    os.makedirs("data_reports", exist_ok=True)

    file_path = f"data_reports/fundamental_{clean_ticker}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    #Quarterly Revenue Growth (yoy) = ( (New Quarter Revenue - Same Quarter Last Year Revenue) / Same Quarter Last Year Revenue ) * 100
    #multipling by 100 to get metric in %
    revenue_growth_raw = (data["quoteSummary"]["result"][0]
            ["financialData"]["revenueGrowth"]["raw"]
        )
    revenue_growth_pct = revenue_growth_raw * 100
    
    #operating margin (ttm) = Operating Income (EBIT) / Revenue
    #multipling by 100 to get metric in %
    operating_margin_raw = (data["quoteSummary"]["result"][0]
            ["financialData"]["operatingMargins"]["raw"]
        )
    operating_margin_pct = operating_margin_raw * 100

    #debt to equity = Total Debt / Total Shareholders' Equity
    debt_to_equity_ratio = (data["quoteSummary"]["result"][0]
            ["financialData"]["debtToEquity"]["raw"])

    #FREE CASH FLOW MARGIN(TTM)% = Levered free cash flow(ttm) / Revenue(ttm) * 100 
    #multipling by 100 to get metric in %
    revenue = (data["quoteSummary"]["result"][0]
            ["financialData"]["totalRevenue"]["raw"])
    
    levered_free_cash_flow = (data["quoteSummary"]["result"][0]
            ["financialData"]["freeCashflow"]["raw"])
    
    free_cash_flow_margin_pct = (levered_free_cash_flow / revenue) * 100

    return {
        "revenue_growth_pct": revenue_growth_pct,
        "operating_margin_pct": operating_margin_pct,
        "debt_to_equity_ratio": debt_to_equity_ratio,
        "free_cash_flow_margin_pct": free_cash_flow_margin_pct
    }

