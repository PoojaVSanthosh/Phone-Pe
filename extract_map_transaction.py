import json
import pandas as pd
import os

path = "pulse/data/map/transaction/hover/country/india/state"

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
                    for item in content["data"]["hoverDataList"]:
                        data.append({
                            "state": state,
                            "year": int(year),
                            "quarter": int(file.replace(".json","")),
                            "district": item["name"],
                            "count": item["metric"][0]["count"],
                            "amount": item["metric"][0]["amount"]
                        })
                except:
                    pass

df = pd.DataFrame(data)
df.to_csv("map_transaction.csv", index=False)
print(df.head())