import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:root@localhost/phonepe")

st.set_page_config(page_title="PhonePe Transaction Insights", layout="wide")
st.title("📊 PhonePe Transaction Insights Dashboard")

section = st.sidebar.selectbox(
    "Select Analysis",
    [
        "Top States by Amount",
        "Top States by Count",
        "Payment Category Analysis",
        "Yearly Trend",
        "Quarterly Trend",
        "Top Districts",
        "Top Pincodes",
        "User Brand Analysis",
        "Insurance Analysis"
    ]
)

if section == "Top States by Amount":
    query = """
    SELECT state, SUM(amount) AS total_amount
    FROM aggregated_transaction
    GROUP BY state
    ORDER BY total_amount DESC
    LIMIT 10
    """
    df = pd.read_sql(query, engine)
    st.subheader("Top 10 States by Transaction Amount")
    st.dataframe(df)
    st.bar_chart(df.set_index("state"))

elif section == "Top States by Count":
    query = """
    SELECT state, SUM(count) AS total_count
    FROM aggregated_transaction
    GROUP BY state
    ORDER BY total_count DESC
    LIMIT 10
    """
    df = pd.read_sql(query, engine)
    st.subheader("Top 10 States by Transaction Count")
    st.dataframe(df)
    st.bar_chart(df.set_index("state"))

elif section == "Payment Category Analysis":
    query = """
    SELECT transaction_type, SUM(amount) AS total_amount
    FROM aggregated_transaction
    GROUP BY transaction_type
    ORDER BY total_amount DESC
    """
    df = pd.read_sql(query, engine)
    st.subheader("Payment Category Distribution")
    st.dataframe(df)
    st.bar_chart(df.set_index("transaction_type"))

elif section == "Yearly Trend":
    query = """
    SELECT year, SUM(amount) AS total_amount
    FROM aggregated_transaction
    GROUP BY year
    ORDER BY year
    """
    df = pd.read_sql(query, engine)
    st.subheader("Year-wise Transaction Trend")
    st.dataframe(df)
    st.line_chart(df.set_index("year"))

elif section == "Quarterly Trend":
    query = """
    SELECT quarter, SUM(amount) AS total_amount
    FROM aggregated_transaction
    GROUP BY quarter
    ORDER BY quarter
    """
    df = pd.read_sql(query, engine)
    st.subheader("Quarter-wise Transaction Trend")
    st.dataframe(df)
    st.line_chart(df.set_index("quarter"))

elif section == "Top Districts":
    query = """
    SELECT district, SUM(amount) AS total_amount
    FROM map_transaction
    GROUP BY district
    ORDER BY total_amount DESC
    LIMIT 10
    """
    df = pd.read_sql(query, engine)
    st.subheader("Top 10 Districts by Transaction Amount")
    st.dataframe(df)
    st.bar_chart(df.set_index("district"))

elif section == "Top Pincodes":
    query = """
    SELECT entity_name AS pincode, SUM(amount) AS total_amount
    FROM top_transaction
    WHERE entity_type = 'pincode'
    GROUP BY entity_name
    ORDER BY total_amount DESC
    LIMIT 10
    """
    df = pd.read_sql(query, engine)
    st.subheader("Top 10 Pincodes by Transaction Amount")
    st.dataframe(df)
    st.bar_chart(df.set_index("pincode"))

elif section == "User Brand Analysis":
    query = """
    SELECT brand, SUM(count) AS total_users
    FROM aggregated_user
    GROUP BY brand
    ORDER BY total_users DESC
    LIMIT 10
    """
    df = pd.read_sql(query, engine)
    st.subheader("Top Mobile Brands by User Count")
    st.dataframe(df)
    st.bar_chart(df.set_index("brand"))

elif section == "Insurance Analysis":
    query = """
    SELECT state, SUM(amount) AS total_amount
    FROM aggregated_insurance
    GROUP BY state
    ORDER BY total_amount DESC
    LIMIT 10
    """
    df = pd.read_sql(query, engine)
    st.subheader("Top States by Insurance Amount")
    st.dataframe(df)
    st.bar_chart(df.set_index("state"))