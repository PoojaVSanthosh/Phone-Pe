import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

username = "root"
password = "root"
host = "localhost"
database = "phonepe"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

# Top states by amount
query1 = """
SELECT state, SUM(amount) AS total_amount
FROM aggregated_transaction
GROUP BY state
ORDER BY total_amount DESC
LIMIT 10
"""

df1 = pd.read_sql(query1, engine)

plt.figure(figsize=(12, 6))
plt.bar(df1["state"], df1["total_amount"])
plt.xticks(rotation=45, ha="right")
plt.title("Top 10 States by Transaction Amount")
plt.xlabel("State")
plt.ylabel("Total Amount")
plt.tight_layout()
plt.show()

# Payment category distribution
query2 = """
SELECT transaction_type, SUM(amount) AS total_amount
FROM aggregated_transaction
GROUP BY transaction_type
ORDER BY total_amount DESC
"""

df2 = pd.read_sql(query2, engine)

plt.figure(figsize=(10, 6))
plt.bar(df2["transaction_type"], df2["total_amount"])
plt.xticks(rotation=45, ha="right")
plt.title("Transaction Amount by Payment Category")
plt.xlabel("Transaction Type")
plt.ylabel("Total Amount")
plt.tight_layout()
plt.show()

# Year-wise trend
query3 = """
SELECT year, SUM(amount) AS total_amount
FROM aggregated_transaction
GROUP BY year
ORDER BY year
"""

df3 = pd.read_sql(query3, engine)

plt.figure(figsize=(8, 5))
plt.plot(df3["year"], df3["total_amount"], marker="o")
plt.title("Year-wise Transaction Amount Trend")
plt.xlabel("Year")
plt.ylabel("Total Amount")
plt.tight_layout()
plt.show()

