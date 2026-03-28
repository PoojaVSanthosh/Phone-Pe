
import json
import pandas as pd
import os

path = "pulse/data/top/transaction/country/india/state"

data = []

for state in os.listdir(path):
    state_path = os.path.join(path, state)

    for year in os.listdir(state_path):
        year_path = os.path.join(state_path, year)

        for file in os.listdir(year_path):
            file_path = os.path.join(year_path, file)

            with open(file_path, 'r') as f:
                content = json.load(f)

                try:
                    for item in content["data"]["districts"]:
                        data.append({
                            "state": state,
                            "year": int(year),
                            "quarter": int(file.replace(".json","")),
                            "entity_name": item["entityName"],
                            "entity_type": "district",
                            "count": item["metric"]["count"],
                            "amount": item["metric"]["amount"]
                        })

                    for item in content["data"]["pincodes"]:
                        data.append({
                            "state": state,
                            "year": int(year),
                            "quarter": int(file.replace(".json","")),
                            "entity_name": item["entityName"],
                            "entity_type": "pincode",
                            "count": item["metric"]["count"],
                            "amount": item["metric"]["amount"]
                        })
                except:
                    pass

df = pd.DataFrame(data)
df.to_csv("top_transaction.csv", index=False)

print(df.head())
print(df.shape)