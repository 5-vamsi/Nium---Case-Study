# ☕ Coffee Market Analysis Dashboard

An end-to-end Business Intelligence solution for analyzing the global coffee market using Python, PostgreSQL, SQL, and Streamlit.

---

## Project Overview

This project transforms raw coffee market and population datasets into an interactive Business Intelligence dashboard that enables users to explore global coffee production, consumption, trade, inventory, and market trends.

The solution follows a complete analytics pipeline:

- Extract and transform raw datasets
- Validate and clean data
- Build a PostgreSQL data warehouse
- Create analytical SQL views
- Generate business insights using SQL
- Visualize insights through an interactive Streamlit dashboard

---

## Objectives

The primary objectives of this project are to:

- Analyze global coffee production and consumption trends
- Identify leading coffee-producing and consuming countries
- Explore international coffee trade patterns
- Compare production, consumption, imports, and exports
- Provide business recommendations based on analytical findings

---

# Architecture

```
Raw CSV Files
       │
       ▼
Python ETL Pipeline
       │
       ▼
Data Cleaning & Validation
       │
       ▼
Country Harmonization
       │
       ▼
PostgreSQL Data Warehouse
       │
       ▼
SQL Views & Business Queries
       │
       ▼
Interactive Streamlit Dashboard
```

---

# Project Structure

```
Case study/

│
├── dashboard/
│   ├── app.py
│   ├── database.py
│   └── pages/
│
├── database/
│   ├── create_database.sql
│   ├── create_tables.sql
│   ├── analytical_views.sql
│   └── business_queries.sql
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│
├── requirements.txt
├── README.md
└── coffee_market_db.sql
```

---

# ETL Pipeline

The ETL pipeline consists of four stages:

### 1. Extract

- Coffee Market Dataset
- World Bank Population Dataset
- Country Code Dataset

### 2. Transform

- Standardized column names
- Country harmonization
- Long-to-wide transformation
- Population reshaping
- Data cleaning

### 3. Validate

- Missing values
- Duplicate records
- Referential integrity
- Warehouse validation

### 4. Load

Processed data is loaded into PostgreSQL.

---

# Data Warehouse

## Dimension Table

### dim_country

Stores country metadata including:

- Country ID
- Country Name
- ISO Codes
- ONU Code

---

## Fact Tables

### fact_coffee

Contains:

- Production
- Consumption
- Imports
- Exports
- Stocks
- Market Year

### fact_population

Contains:

- Population
- Country
- Year

---

## SQL View

### vw_coffee_market

Analytical view combining:

- Coffee production
- Population
- Per-capita consumption
- Country information

---

# Dashboard Pages

## Executive Overview

- Global KPIs
- Production trends
- Consumption trends
- Executive summary

---

## Market Intelligence

- Top producers
- Top consumers
- Top exporters
- Top importers
- Per-capita consumption

---

## Country Explorer

Interactive analysis including:

- Country filters
- Year filters
- Production
- Consumption
- Trade
- Inventory
- Business summary

---

## Trend Analysis

- Production trends
- Consumption trends
- Trade trends
- Inventory trends

---

## Business Recommendations

Provides insights regarding:

- Production surplus
- Production deficit
- Import dependency
- Export dependency
- Strategic recommendations

---

# Key Business Insights

- Brazil and Vietnam consistently dominate global coffee production.
- Coffee consumption has generally increased over time.
- International trade plays a critical role in balancing supply and demand.
- Import-dependent countries represent attractive export opportunities.
- Per-capita consumption highlights mature coffee markets beyond population size.

---

# Technologies Used

### Programming

- Python

### Database

- PostgreSQL

### Data Processing

- Pandas

### Visualization

- Plotly
- Streamlit

### SQL

- PostgreSQL SQL


---

# Run ETL

```bash
python main.py
```

---

# Load PostgreSQL

```bash
python src/load_postgressql.py
```

---

# Launch Dashboard

```bash
streamlit run dashboard/app.py
```

---
# Reflection

## Key Design Choices

The solution was designed as an end-to-end Business Intelligence pipeline to transform raw coffee market data into actionable business insights. Rather than analyzing the data directly from raw files, I implemented a structured ETL process followed by a PostgreSQL data warehouse and an interactive Streamlit dashboard.

A dimensional star schema was chosen for the database design, consisting of a dim_country dimension table and two fact tables (fact_coffee and fact_population). This structure simplifies analytical queries, improves data organization, and supports scalable reporting.

One of the key design decisions was to create a country harmonization module using ISO country codes. Since the coffee and population datasets used different country naming conventions, standardizing country names before loading the data ensured accurate joins and consistent reporting.

To maintain data quality, validation checks were incorporated throughout the ETL pipeline, including missing value detection, duplicate record validation, referential integrity checks, and warehouse validation. These checks ensured that only clean and consistent data was loaded into the warehouse.

Instead of querying multiple tables repeatedly, an analytical SQL view (vw_coffee_market) was created to combine coffee market data, population, and calculated metrics such as per-capita coffee consumption. This simplified dashboard development and improved query readability.

The dashboard was organized into five business-focused sections—Executive Overview, Market Intelligence, Country Explorer, Trend Analysis, and Business Recommendations. This structure allows users to move from high-level KPIs to detailed country-level analysis while directly addressing ACME Baristas' business questions.

Overall, the design emphasizes modularity, data quality, scalability, and ease of analysis, making the solution suitable for both technical users and business decision-makers.

## Challenges Faced

Several challenges were encountered during the project.

The primary challenge was harmonizing country names across different datasets, as inconsistent naming conventions prevented accurate joins. This was addressed by creating a standardized country dimension using ISO country codes.

Another challenge was reshaping the World Bank population dataset from a wide format into a normalized long format suitable for analytical queries.

While developing the PostgreSQL warehouse, referential integrity and foreign key consistency were validated to ensure accurate relationships between dimension and fact tables.

Dashboard development also required handling countries with missing production or trade values so that visualizations remained informative instead of displaying misleading charts.

## Assumptions Made

The following assumptions were made during the analysis:

Historical coffee market trends provide a reasonable basis for evaluating market opportunities.
Country harmonization using ISO codes correctly maps equivalent country names across datasets.
Missing values represent unavailable data rather than zero activity unless explicitly stated.
Population estimates from the World Bank are suitable for calculating per-capita coffee consumption.
The analysis focuses on historical market behavior and does not attempt to forecast future demand.


## Future Improvements

- Automated data refresh
- Cloud deployment
- Predictive demand forecasting
- Machine learning models
- Interactive geographical maps
- User authentication

---

## Data that strengthen insights

While the available coffee production, consumption, trade, and population data provided a strong foundation for analysis, additional datasets would have enabled more comprehensive market recommendations.

Economic indicators such as GDP per capita, disposable income, and consumer spending would have helped assess purchasing power and identify markets with higher revenue potential. Information on existing coffee shop density, competitor presence, and market share would have provided a clearer understanding of competitive intensity in each target market.

Consumer behavior data, including coffee consumption preferences, demographic trends, and customer purchasing habits, would have supported more targeted market selection and product positioning. Additionally, coffee price data, inflation rates, exchange rates, and logistics costs would have strengthened the financial feasibility analysis.