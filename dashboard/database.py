"""
database.py
-----------

Database utilities for the Coffee Market Analysis Dashboard.
Provides:
- PostgreSQL connection
- SQL query execution
- Number formatting utilities
"""

import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

# ==========================================================
# DATABASE CONFIGURATION
# ==========================================================

DB_NAME = "coffee_market_db"
DB_USER = "chiruhasbonam"
DB_PASSWORD = ""
DB_HOST = "localhost"
DB_PORT = "5432"

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ==========================================================
# DATABASE ENGINE
# ==========================================================

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

# ==========================================================
# QUERY EXECUTION
# ==========================================================

@st.cache_data(show_spinner=False)
def run_query(query: str) -> pd.DataFrame:
    """
    Execute a SQL query and return a Pandas DataFrame.
    Results are cached for better dashboard performance.
    """

    try:
        return pd.read_sql(query, engine)

    except Exception as e:
        st.error(f"Database Error:\n{e}")
        return pd.DataFrame()

# ==========================================================
# NUMBER FORMATTER
# ==========================================================

def format_number(value):
    """
    Convert large numbers into readable format.

    Example:
        1520 -> 1.5K
        8200000 -> 8.2M
    """

    if pd.isna(value):
        return "-"

    value = float(value)

    if abs(value) >= 1_000_000_000:
        return f"{value/1_000_000_000:.1f}B"

    if abs(value) >= 1_000_000:
        return f"{value/1_000_000:.1f}M"

    if abs(value) >= 1_000:
        return f"{value/1_000:.1f}K"

    return f"{value:,.0f}"

# ==========================================================
# KPI CARD
# ==========================================================

def kpi_card(column, label, value):
    """
    Display a formatted KPI card.
    """

    column.metric(
        label=label,
        value=format_number(value)
    )