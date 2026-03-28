import pandas as pd
from sqlalchemy import create_engine

# Update with your MySQL username/password
username = "root"
password = "root"
host = "localhost"
database = "phonepe"

csv_file = "aggregated_transaction.csv"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

df = pd.read_csv(csv_file)

print("Preview:")
print(df.head())
print("Shape:", df.shape)

df.to_sql("aggregated_transaction", con=engine, if_exists="append", index=False)

print("Data inserted successfully into aggregated_transaction table.")