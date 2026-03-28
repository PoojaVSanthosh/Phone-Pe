import json
import pandas as pd
import os

# Base path (update if needed)
path = "pulse/data/aggregated/transaction/country/india/state"

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
                    for item in content["data"]["transactionData"]:
                        data.append({
                            "state": state,
                            "year": int(year),
                            "quarter": int(file.replace(".json","")),
                            "transaction_type": item["name"],
                            "count": item["paymentInstruments"][0]["count"],
                            "amount": item["paymentInstruments"][0]["amount"]
                        })
                except:
                    pass

df = pd.DataFrame(data)

print(df.head())
print(df.shape)

# Save for later use
df.to_csv("aggregated_transaction.csv", index=False)