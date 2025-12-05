# Investment Scoring Algorithm (V1)

*A modular multi-factor scoring engine for evaluating technology & growth companies.*

## Overview

This project is a fully modular **investment scoring algorithm** designed to evaluate companies — primarily in the **Technology, Software, AI, and Growth sectors**.

The algorithm produces a **0–100 score** per module and a **final weighted score**, based on three analytical pillars:

1. **Fundamentals Module** – Growth, profitability, leverage, free cash flow  
2. **Valuation Module** – P/E, Forward P/E, EV/EBITDA, P/S, price-to-FCF
3. **Moat Module** – Quality, innovation, and long-term competitive advantage  

Each module operates independently and returns a structured dictionary of scores.

This project is part of my personal learning journey in Python, financial modeling, and algorithmic thinking — and may evolve into a full product.

## Project Structure

```
project_root/
│
├── fundemental_module.py      # Fundamentals scoring logic
├── valuation_module.py        # Valuation scoring logic
├── moat_module.py             # Moat/Quality scoring logic
├── scoring_utils.py           # Shared scoring utilities (threshold logic, ratios)
├── main.py                    # Current CLI orchestrator (future API-ready)
├── LICENSE                    # Usage restrictions (all rights reserved)
└── README.md                  # Project documentation
```

## Modules Breakdown

## 1. Fundamentals Module
Evaluates the company’s core financial performance:

- Revenue Growth  
- Operating Margin  
- Debt-to-Equity Ratio  
- Free Cash Flow Margin  

Each metric is mapped to thresholds and combined into a weighted fundamentals score.

## 2. Valuation Module
Uses stock ratio vs. sector values:

- P/E  
- Forward P/E  
- EV/EBITDA  
- Price/Sales  
- Price/Free Cash Flow  

Each ratio is scored using a ratio-to-sector comparison, then weighted.

## 3. Moat Module
Evaluates long-term quality and competitive durability using four catalysts:

- ROIC (5-year average) 
- FCF Growth (3–5 year CAGR) 
- Gross Margin Stability (range analysis)
- R&D-to-Revenue (%)

A weighted Moat Score reflects innovation intensity, efficiency, and economic moat strength.

## Current Limitations & Scope

This model is currently optimized for:

- Technology companies  
- Software / SaaS  
- AI-driven companies  
- Asset-light growth businesses  

It is not yet designed for sectors such as:

- Banks & Financials  
- Utilities  
- Insurance  
- Energy  
- REITs  

Future versions may add sector-specific adjustments.

## Future Roadmap

- Add support for real financial data via API  
- Build sector-aware scoring adjustments  
- Add sentiment/analyst module  
- Create a web dashboard or REST API  
- Deploy as a microservice  

## How to Run

(Currently CLI-based)

```bash
python main.py
```

You will be prompted for financial values manually.  
A future version will pull all values automatically from APIs.

## License

This project is protected under an **All Rights Reserved – Educational Use Only** license.  
You may *view* and *study* the code, but:

- No commercial use  
- No redistribution  
- No modification  
- No integration into products  

See the LICENSE file for full details.

## Author

**Oz Efraty**  
Python developer & tech investor in progress.
Sharing my journey on LinkedIn.
