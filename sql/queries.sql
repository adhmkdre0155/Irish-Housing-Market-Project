-- ============================================================
-- Irish Housing Market Price & Affordability Analysis — Queries
-- Table: rppi (source: CSO Ireland RPPI, table HPA06, real data)
-- ============================================================

-- 1. YoY price growth by region, most recent year (2025), houses only
SELECT
    Region,
    PriceIndex AS Index2025,
    YoY_Growth_Pct
FROM rppi
WHERE Year = 2025 AND PropertyType = 'houses'
ORDER BY YoY_Growth_Pct DESC;

-- 2. Dublin vs. rest-of-country comparison over time (all residential properties)
SELECT
    Year,
    MAX(CASE WHEN Region = 'Dublin' THEN PriceIndex END) AS Dublin_Index,
    MAX(CASE WHEN Region = 'National ex-Dublin' THEN PriceIndex END) AS RestOfCountry_Index,
    MAX(CASE WHEN Region = 'National' THEN PriceIndex END) AS National_Index
FROM rppi
WHERE PropertyType = 'all residential properties'
GROUP BY Year
ORDER BY Year;

-- 3. Which regions have overheated fastest since the post-2020 recovery
--    (index growth from 2020 to 2025, houses)
WITH base AS (
    SELECT Region, PriceIndex AS Index2020
    FROM rppi WHERE Year = 2020 AND PropertyType = 'houses'
),
latest AS (
    SELECT Region, PriceIndex AS Index2025
    FROM rppi WHERE Year = 2025 AND PropertyType = 'houses'
)
SELECT
    b.Region,
    b.Index2020,
    l.Index2025,
    ROUND((l.Index2025 - b.Index2020) * 100.0 / b.Index2020, 1) AS GrowthPct_2020_2025
FROM base b
JOIN latest l ON b.Region = l.Region
ORDER BY GrowthPct_2020_2025 DESC;

-- 4. Peak-to-trough-to-now: full cycle since the 2007 boom peak (houses, National)
SELECT Year, PriceIndex, YoY_Growth_Pct
FROM rppi
WHERE Region = 'National' AND PropertyType = 'houses'
ORDER BY Year;

-- 5. Regional volatility: which region had the widest swings 2005-2025
--    (max index minus min index, houses, regions with full history only)
SELECT
    Region,
    ROUND(MAX(PriceIndex), 1) AS PeakIndex,
    ROUND(MIN(PriceIndex), 1) AS TroughIndex,
    ROUND(MAX(PriceIndex) - MIN(PriceIndex), 1) AS Swing
FROM rppi
WHERE PropertyType = 'houses' AND Region IN ('National', 'Dublin', 'National ex-Dublin')
GROUP BY Region
ORDER BY Swing DESC;

-- 6. Apartments vs. houses price divergence nationally, most recent 5 years
SELECT
    Year,
    MAX(CASE WHEN PropertyType = 'houses' THEN PriceIndex END) AS Houses_Index,
    MAX(CASE WHEN PropertyType = 'apartments' THEN PriceIndex END) AS Apartments_Index
FROM rppi
WHERE Region = 'National' AND Year >= 2020
GROUP BY Year
ORDER BY Year;
