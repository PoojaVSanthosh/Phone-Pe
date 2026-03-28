import json
import pandas as pd
import os

path = "pulse/data/aggregated/user/country/india/state"

data = []

for state in os.listdir(path):
    state_path = os.path.join(path, state)

    for year in os.listdir(state_path):
        year_path = os.path.join(state_path, year)

        for file in os.listdir(year_path):
            file_path = os.path.join(year_path, file)

            with open(file_path, "r") as f:
                content = json.load(f)

                try:
                    users = content["data"]["usersByDevice"]
                    if users is not None:
                        for item in users:
                            data.append({
                                "state": state,
                                "year": int(year),
                                "quarter": int(file.replace(".json", "")),
                                "brand": item["brand"],
                                "count": item["count"],
                                "percentage": item["percentage"]
                            })
                except:
                    pass

df = pd.DataFrame(data)
df.to_csv("aggregated_user.csv", index=False)

print(df.head())
print(df.shape)