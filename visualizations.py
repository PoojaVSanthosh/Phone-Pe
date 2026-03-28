import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:root@localhost/phonepe")

# 1. Top states by transaction amount
q1 = """
SELECT state, SUM(amount) AS total_amount
FROM aggregated_transaction
GROUP BY state
ORDER BY total_amount DESC
LIMIT 10
"""
df1 = pd.read_sql(q1, engine)

plt.figure(figsize=(12, 6))
plt.bar(df1["state"], df1["total_amount"])
plt.xticks(rotation=45, ha="right")
plt.title("Top 10 States by Transaction Amount")
plt.xlabel("State")
plt.ylabel("Total Amount")
plt.tight_layout()
plt.savefig("top_states_transaction_amount.png")
plt.show()

# 2. Payment category distribution
q2 = """
SELECT transaction_type, SUM(amount) AS total_amount
FROM aggregated_transaction
GROUP BY transaction_type
ORDER BY total_amount DESC
"""
df2 = pd.read_sql(q2, engine)

plt.figure(figsize=(10, 6))
plt.bar(df2["transaction_type"], df2["total_amount"])
plt.xticks(rotation=45, ha="right")
plt.title("Payment Category Distribution")
plt.xlabel("Transaction Type")
plt.ylabel("Total Amount")
plt.tight_layout()
plt.savefig("payment_category_distribution.png")
plt.show()

# 3. Yearly trend
q3 = """
SELECT year, SUM(amount) AS total_amount
FROM aggregated_transaction
GROUP BY year
ORDER BY year
"""
df3 = pd.read_sql(q3, engine)

plt.figure(figsize=(8, 5))
plt.plot(df3["year"], df3["total_amount"], marker="o")
plt.title("Year-wise Transaction Trend")
plt.xlabel("Year")
plt.ylabel("Total Amount")
plt.tight_layout()
plt.savefig("yearly_transaction_trend.png")
plt.show()

# 4. Top districts
q4 = """
SELECT district, SUM(amount) AS total_amount
FROM map_transaction
GROUP BY district
ORDER BY total_amount DESC
LIMIT 10
"""
df4 = pd.read_sql(q4, engine)

plt.figure(figsize=(12, 6))
plt.bar(df4["district"], df4["total_amount"])
plt.xticks(rotation=45, ha="right")
plt.title("Top 10 Districts by Transaction Amount")
plt.xlabel("District")
plt.ylabel("Total Amount")
plt.tight_layout()
plt.savefig("top_districts_transaction_amount.png")
plt.show()

# 5. Top mobile brands
q5 = """
SELECT brand, SUM(count) AS total_users
FROM aggregated_user
GROUP BY brand
ORDER BY total_users DESC
LIMIT 10
"""
df5 = pd.read_sql(q5, engine)

plt.figure(figsize=(10, 6))
plt.bar(df5["brand"], df5["total_users"])
plt.xticks(rotation=45, ha="right")
plt.title("Top 10 Mobile Brands by User Count")
plt.xlabel("Brand")
plt.ylabel("Total Users")
plt.tight_layout()
plt.savefig("top_mobile_brands.png")
plt.show()

# 6. Insurance by state
q6 = """
SELECT state, SUM(amount) AS total_amount
FROM aggregated_insurance
GROUP BY state
ORDER BY total_amount DESC
LIMIT 10
"""
df6 = pd.read_sql(q6, engine)

plt.figure(figsize=(12, 6))
plt.bar(df6["state"], df6["total_amount"])
plt.xticks(rotation=45, ha="right")
plt.title("Top 10 States by Insurance Amount")
plt.xlabel("State")
plt.ylabel("Insurance Amount")
plt.tight_layout()
plt.savefig("top_states_insurance_amount.png")
plt.show()