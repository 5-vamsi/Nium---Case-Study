import streamlit as st
import plotly.express as px
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from database import (
    run_query,
    kpi_card,
)


# PAGE CONFIGURATION


st.set_page_config(
    page_title="Executive Overview",
    page_icon="☕",
    layout="wide"
)

st.title("☕ Executive Overview")

st.markdown("""
This page presents a high-level summary of the global coffee market,
including production, consumption, trade performance and long-term
market trends.
""")


# KPI


kpi = run_query("""
SELECT

SUM(production) total_production,

SUM(domestic_consumption) total_consumption,

SUM(exports) total_exports,

SUM(imports) total_imports,

COUNT(DISTINCT country_name) countries,

MAX(market_year) latest_year

FROM vw_coffee_market;
""")

c1, c2, c3, c4, c5, c6 = st.columns(6)

kpi_card(
    c1,
    "Production",
    kpi.iloc[0]["total_production"]
)

kpi_card(
    c2,
    "Consumption",
    kpi.iloc[0]["total_consumption"]
)

kpi_card(
    c3,
    "Exports",
    kpi.iloc[0]["total_exports"]
)

kpi_card(
    c4,
    "Imports",
    kpi.iloc[0]["total_imports"]
)

c5.metric(
    "Countries",
    int(kpi.iloc[0]["countries"])
)

c6.metric(
    "Latest Year",
    int(kpi.iloc[0]["latest_year"])
)

st.success("""
The global coffee market demonstrates sustained long-term growth,
supported by increasing production, expanding consumer demand and
strong international trade activity.

The latest dataset covers **93 coffee-producing countries**
through **2025**, providing a comprehensive view of market dynamics.
""")

st.divider()


# Production & Consumption


production = run_query("""
SELECT

market_year,

SUM(production) production

FROM vw_coffee_market

GROUP BY market_year

ORDER BY market_year;
""")

consumption = run_query("""
SELECT

market_year,

SUM(domestic_consumption) consumption

FROM vw_coffee_market

GROUP BY market_year

ORDER BY market_year;
""")

left, right = st.columns(2)

with left:

    fig = px.line(
        production,
        x="market_year",
        y="production",
        markers=True,
        title="Global Coffee Production Trend (1960–2025)"
    )

    fig.update_traces(line_width=3)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    fig = px.line(
        consumption,
        x="market_year",
        y="consumption",
        markers=True,
        title="Global Coffee Consumption Trend (1960–2025)"
    )

    fig.update_traces(line_width=3)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.info("""
**Note**

The noticeable increase after **2001** likely reflects changes in
reporting coverage and data availability rather than a sudden
change in global coffee demand.
""")

st.divider()


# Production vs Consumption

compare = run_query("""
SELECT

market_year,

SUM(production) production,

SUM(domestic_consumption) consumption

FROM vw_coffee_market

GROUP BY market_year

ORDER BY market_year;
""")

fig = px.line(
    compare,
    x="market_year",
    y=["production", "consumption"],
    markers=True,
    title="Global Production vs Consumption"
)

fig.update_traces(line_width=3)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()


# EXECUTIVE OBSERVATIONS


st.subheader("Executive Observations")

st.markdown("""
- Coffee production has increased steadily over the study period.
- Global consumption follows a similar long-term upward trend, indicating sustained demand.
- Production consistently exceeds consumption, supporting export-driven markets.
- International trade plays a critical role in balancing supply and demand.
- Long-term trends indicate a stable and growing global coffee industry.
""")