from pytrends.request import TrendReq
import pandas as pd
from datetime import datetime

pytrends = TrendReq(hl='en-US', tz=360)

keyword = "Karen"
geo = "US"

all_data = []

for year in range(2016, 2026):
    start = f"{year}-01-01"
    end = f"{year+1}-01-01"
    timeframe = f"{start} {end}"

    pytrends.build_payload(
        [keyword],
        cat=0,
        timeframe=timeframe,
        geo=geo,
        gprop=""
    )

    yearly_data = pytrends.interest_over_time()

    if "isPartial" in yearly_data.columns:
        yearly_data = yearly_data.drop(columns=["isPartial"])

    yearly_data = yearly_data.reset_index()
    all_data.append(yearly_data)

# Combine all years
data = pd.concat(all_data)

# Add metadata
data["word"] = keyword
data["country"] = geo
data["search_type"] = "web"
data["pulled_at"] = datetime.utcnow()

data = data.rename(columns={keyword: "interest_score"})

data.to_csv("karen_us_web_trends_weekly.csv", index=False)

print("Extraction complete.")
print("Total rows:", len(data))
print(data.head())
