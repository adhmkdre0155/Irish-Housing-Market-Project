# 📊 Irish Housing Market Price & Affordability Analysis

**Type:** Data Analyst project · **Tools:** SQL, Python, interactive dashboard · **Status:** Complete
**⭐ Uses real, public CSO Ireland data — not simulated**

[🔗 Live interactive dashboard](#) · [🔗 GitHub repository](#) · [📄 Insights memo (PDF)](#)

---

### The problem
Prospective renters/buyers and policymakers want a clear view of how Irish property prices have moved by region and property type — and whether affordability is keeping pace with wages.

### Why this project is different from the others
Every number here traces back to the real **CSO Ireland Residential Property Price Index**, fetched directly from CSO's public API — the same data Irish policymakers and banks use. Nothing is simulated.

### What I did
1. **Pulled real data directly from CSO's PxStat API** (no manual download, no template dataset).
2. **Cleaned in Python** — parsed CSO's combined region/property-type labels, and explicitly documented where regional data genuinely isn't available before 2010 (a real CSO collection limit, not a cleaning gap).
3. **Queried in SQL** — YoY growth by region, Dublin vs. rest-of-country across the full 2005–2025 boom/bust/recovery cycle, and growth specifically since 2020.
4. **Built an interactive dashboard** with trend lines, a regional growth comparison, and an affordability ratio using real CSO earnings data.

### A note on "26 counties"
CSO's Residential Property Price Index doesn't actually publish at the level of all 26 individual counties — county-level samples would be too small for a reliable index. The real geography is National / Dublin (+4 local authorities) / 7 regional groupings. This project uses that actual published geography rather than approximating detail the source data doesn't support.

### 🔑 Key insight
> Since the 2020 recovery, **Border (excl. Louth)** house prices have grown **67.7%** — nearly double Dublin's growth of just **38.4%**, the *slowest* of any region tracked. The popular "Dublin is overheating" narrative no longer matches the data — regional Ireland is now growing meaningfully faster than the capital.

### Affordability
National house prices grew **17.0%** (2023→2025) while average weekly earnings grew only **10.6%** (Q1 2024→Q1 2026) — a **6.4 percentage-point gap**. Affordability has genuinely worsened over the most recent comparable window.

### Recommendation
For policymakers: regional housing supply, not just Dublin supply, is now the more urgent lever, since regional demand growth is outpacing regional stock.

### Business impact
A genuine conversation-starter in interviews — shows initiative to engage with real, current Irish data and surfaces a counter-narrative finding most coverage of Irish house prices misses.

---

**CV / LinkedIn bullet:**
*Built an interactive dashboard on CSO Ireland's real Residential Property Price Index data, surfacing that regional Ireland (Border, Midland, West) has outpaced Dublin in price growth since 2020 (67.7% vs. 38.4%), and that national affordability has worsened by 6.4 percentage points in the most recent 2-year window.*

**Skills demonstrated:** Working with real government/public APIs · Data cleaning with documented limitations · SQL · Time-series analysis · Dashboard design · Turning a counter-narrative finding into a clear insight
