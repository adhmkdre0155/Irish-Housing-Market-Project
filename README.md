# Irish Housing Market Price & Affordability Analysis

**Data Analyst portfolio project — Adham AlHers**
[Live interactive dashboard](https://adhmkdre0155.github.io/Irish-Housing-Market-Project/dashboard/index.html) · [LinkedIn](https://www.linkedin.com/in/adhamalhers/) · [Portfolio home](https://app.notion.com/p/Data-Business-Analyst-Portfolio-Adham-AlHers-3b63ac1ddec780c1b2d6c221c6bcbb59?source=copy_link)

## This project uses real, public CSO Ireland data — not a simulation

Every number in this project traces back to the **CSO Ireland Residential Property Price Index** (table HPA06) and the **CSO Earnings and Labour Costs release**, fetched directly from the CSO's public PxStat API (`ws.cso.ie`). Nothing here is generated or simulated — this is the same data Irish policymakers, journalists, and banks use.

## Problem statement
Prospective renters/buyers and policymakers want a clear view of how Irish property prices have moved by region and property type — and whether affordability is keeping pace with wages.

## Business context
This project is deliberately built on Irish-specific public data rather than a generic Kaggle dataset, to demonstrate genuine engagement with the Irish market to Dublin-based hiring managers.

## Dataset
CSO Ireland Residential Property Price Index (HPA06, annual, 2005–2025), covering National, Dublin (+ its 4 local authorities), National-excluding-Dublin, and 7 CSO regional groupings, across houses/apartments/all-properties. Paired with real average weekly earnings figures from CSO's Earnings and Labour Costs release for the affordability comparison.

**A note on geography:** CSO's RPPI does not publish at the level of all 26 individual counties — true county-level sample sizes are too small for a reliable index. The real published breakdown is National / Dublin (+4 local authorities) / National ex-Dublin / 7 regions (e.g. "Border excluding Louth", "Mid-East including Louth"). This project uses that actual geography rather than approximating county-level detail the source data doesn't support — see `data/clean_data.py` for the full mapping.

## Tools
Python (pandas) for cleaning · SQL (SQLite) for analysis · Chart.js interactive dashboard (Tableau Public alternative — see note below) · Excel for the formula-driven summary workbook.

## Repository structure
```
├── data/
│   ├── cso_rppi_raw.csv       # Raw CSO data, fetched directly from the PxStat API
│   ├── clean_data.py          # Parses region/property-type labels, computes YoY growth
│   └── rppi_clean.csv         # Cleaned, analysis-ready long-format data
├── sql/
│   └── queries.sql            # YoY growth by region, Dublin vs. rest-of-country, cycle analysis
├── excel/
│   └── Irish_Housing_Market_Dashboard.xlsx   # Formula-driven dashboard with KPI cards and charts
├── dashboard/
│   └── index.html             # Self-contained interactive web dashboard
└── docs/
    └── insights_memo.docx/.pdf
```

## Step-by-step approach
1. **Pulled the real data** directly from the CSO PxStat REST API (`ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/HPA06/CSV/1.0/en`) — no manual download, no simulation.
2. **Cleaned in Python** — parsed CSO's combined "Region - Type" labels into separate Region and PropertyType columns, and explicitly documented where regional breakdowns are genuinely unavailable pre-2010 (a real CSO data-collection limit, not a cleaning error).
3. **Queried in SQL** — YoY growth by region, Dublin vs. rest-of-country over the full 2005–2025 cycle, and growth specifically since the 2020 recovery.
4. **Built a dashboard** — a formula-driven Excel workbook and a self-contained interactive HTML dashboard (Tableau Public was not accessible in this environment to publish to; the HTML dashboard delivers the same county-heatmap-style view, trend lines, and affordability ratio described in the original brief, fully interactive and hostable for free).

## Key insight
Since the 2020 recovery began, **Border (excl. Louth) house prices have grown 67.7%** — nearly double Dublin's growth of just 38.4% (the *slowest* of any tracked region). The popular narrative that Dublin is where Irish house prices are overheating no longer matches the data: regional Ireland is now growing meaningfully faster than the capital, plausibly reflecting remote-work-driven demand shifting outward into regions with a smaller existing housing stock.

Separately: **national house prices grew 17.0% (2023→2025) while average weekly earnings grew only 10.6%** (Q1 2024→Q1 2026) — a 6.4 percentage-point gap, meaning affordability has genuinely worsened over the most recent comparable period.

## Recommendation
For policymakers: regional housing supply — not just Dublin supply — is now the more urgent lever, since regional demand growth is outpacing regional stock. For the affordability conversation specifically: wage growth is not keeping pace with price growth even in the most recent 2-year window, so affordability pressure is intensifying, not stabilizing.

## Business impact
A conversation-starter project in interviews — shows initiative to engage with real, current Irish data rather than a template dataset, and surfaces a genuinely counter-narrative finding (regional overheating > Dublin overheating) that most surface-level coverage of Irish house prices misses.

---
*All data is real and publicly sourced from CSO Ireland via the PxStat API — see `data/cso_rppi_raw.csv` for the unmodified source extract. No figures in this project are simulated.*
