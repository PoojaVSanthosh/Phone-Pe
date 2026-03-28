# Phone-Pe
PhonePe Transaction Insights
🚀 Project Overview

This project analyzes digital payment data from the PhonePe Pulse dataset to uncover insights into transaction trends, user behavior, and insurance adoption across India. Using a combination of ETL pipelines, SQL analysis, Python visualization, and a Streamlit dashboard, the project delivers actionable business insights for decision-making.

🎯 Objectives
Analyze transaction patterns across states, districts, and pincodes
Identify top-performing regions and payment categories
Understand user engagement and device distribution
Evaluate insurance transaction trends
Build an interactive dashboard for real-time insights
🧠 Problem Statement

With the increasing reliance on digital payment systems like PhonePe, it is essential to understand transaction dynamics, user engagement, and insurance adoption to improve services and target users effectively.

This project aims to transform raw data into meaningful insights that support:

Customer segmentation
Fraud detection (pattern-based insights)
Geographic targeting
Product optimization
📂 Dataset
Source: PhonePe Pulse GitHub Repository
Format: JSON files
Categories:
Aggregated Data
Map Data
Top Data
🛠️ Tech Stack
Python (Pandas, JSON, SQLAlchemy)
MySQL (Database & SQL queries)
Matplotlib / Seaborn (Data visualization)
Streamlit (Dashboard)
Git & GitHub (Version control)
🔄 ETL Pipeline
Extract
Parsed JSON files from the dataset
Transform
Cleaned and structured nested data
Converted into tabular format (DataFrames)
Load
Stored data into MySQL tables:
aggregated_transaction
map_transaction
top_transaction
aggregated_user
aggregated_insurance
top_insurance
🗄️ Database Schema
Table Name	Description
aggregated_transaction	State-level transaction data
map_transaction	District-level transaction data
top_transaction	Top states, districts, pincodes
aggregated_user	User device and engagement data
aggregated_insurance	Insurance transaction data
top_insurance	Top insurance entities
📊 Key Analyses
🔹 Transaction Analysis
Top states by transaction amount and count
Payment category distribution
Year-wise and quarter-wise trends
🔹 Geographic Insights
Top districts by transaction volume
Top pincodes by transaction value
🔹 User Analysis
Top mobile brands by usage
Brand-wise engagement percentage
🔹 Insurance Analysis
Top states by insurance usage
Insurance growth trends
📈 Visualizations
Bar charts for top states, districts, and brands
Line charts for yearly trends
Category distribution charts
