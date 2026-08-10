"""
Cleaning step for the Irish Housing Market Price & Affordability Analysis project.
Source: CSO Ireland Residential Property Price Index (HPA06, annual), fetched
directly from the CSO PxStat API (ws.cso.ie) — real published data, not simulated.

  1. Standardize region/county names (CSO uses inconsistent formatting across
     dwelling type categories, e.g. "Mid-East including Louth - houses").
  2. Handle missing quarters/years: several regional breakdowns (Dublin City,
     Dun Laoghaire-Rathdown, Fingal, South Dublin, and the 7 non-Dublin regions)
     only start publishing in 2010 — earlier years are genuinely not collected
     at that granularity by the CSO, not a data error, so they're left as
     missing rather than backfilled or dropped.
  3. Split the combined "Region - Type" label into separate Region and
     PropertyType columns for easier querying.
"""
import pandas as pd

df = pd.read_csv("cso_rppi_raw.csv")
raw_rows = len(df)

# Parse the combined label into Region + PropertyType
def split_label(label):
    label = label.strip()
    if " - " in label:
        region, ptype = label.rsplit(" - ", 1)
    else:
        region, ptype = label, "all residential properties"
    return region.strip(), ptype.strip()

parsed = df["Type of Residential Property"].apply(split_label)
df["Region"] = parsed.apply(lambda x: x[0])
df["PropertyType"] = parsed.apply(lambda x: x[1])

# Standardize region naming (shorten CSO's verbose labels for consistency)
region_map = {
    "National": "National",
    "Dublin": "Dublin",
    "National excluding Dublin": "National ex-Dublin",
    "Dublin City": "Dublin City",
    "Dun Laoghaire-Rathdown": "Dun Laoghaire-Rathdown",
    "Fingal": "Fingal",
    "South Dublin": "South Dublin",
    "Border excluding Louth": "Border (ex-Louth)",
    "Midland": "Midland",
    "West": "West",
    "Mid-East including Louth": "Mid-East (incl. Louth)",
    "Mid-West including South Tipperary": "Mid-West (incl. S. Tipp)",
    "South-East excluding South Tipperary": "South-East (ex-S. Tipp)",
    "South-West": "South-West",
}
df["Region"] = df["Region"].map(region_map).fillna(df["Region"])

df["Year"] = df["Year"].astype(int)
df["PriceIndex"] = pd.to_numeric(df["VALUE"], errors="coerce")

clean = df[["Year", "Region", "PropertyType", "PriceIndex"]].dropna(subset=["PriceIndex"])
clean = clean.sort_values(["Region", "PropertyType", "Year"]).reset_index(drop=True)

# Derived: YoY % growth, computed directly rather than trusting a separate
# CSO percent-change table, so the two are guaranteed consistent
clean["YoY_Growth_Pct"] = (
    clean.groupby(["Region", "PropertyType"])["PriceIndex"].pct_change() * 100
).round(2)

clean.to_csv("rppi_clean.csv", index=False)

print(f"Raw rows:   {raw_rows}")
print(f"Clean rows: {len(clean)}")
print(f"Regions: {sorted(clean['Region'].unique())}")
print(f"Property types: {sorted(clean['PropertyType'].unique())}")
print(f"Year range: {clean['Year'].min()}-{clean['Year'].max()}")
print(f"Missing-data note: regional breakdowns below Dublin/National only start in {clean[clean.Region.isin(['Dublin City','Fingal','West','Midland'])]['Year'].min()}")
