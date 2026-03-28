import pandas as pd
from sqlalchemy import create_engine

username = "root"
password = "root"
host = "localhost"
database = "phonepe"

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}")

files_and_tables = {
    "aggregated_transaction.csv": "aggregated_transaction",
    "map_transaction.csv": "map_transaction",
    "top_transaction.csv": "top_transaction",
    "aggregated_insurance.csv": "aggregated_insurance",
    "top_insurance.csv": "top_insurance",
    "aggregated_user.csv": "aggregated_user",
}

for csv_file, table_name in files_and_tables.items():
    try:
        df = pd.read_csv(csv_file)
        print(f"Loading {csv_file} -> {table_name}, shape={df.shape}")
        df.to_sql(table_name, con=engine, if_exists="append", index=False)
        print(f"Loaded {table_name} successfully")
    except FileNotFoundError:
        print(f"Skipped {csv_file} (not found)")
    except Exception as e:
        print(f"Failed loading {csv_file}: {e}")