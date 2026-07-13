import streamlit as st
import plotly.express as px

from database import run_query

st.set_page_config(
    page_title="Trend Analysis",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Trend Analysis")

st.markdown("""
Analyze long-term trends in the global coffee market across
production, consumption, trade, and inventory levels.
""")

# ============================================================
# GLOBAL PRODUCTION TREND
# ============================================================

production = run_query("""
SELECT
    market_year,
    SUM(production) AS production
FROM vw_coffee_market
GROUP BY market_year
ORDER BY market_year;
""")

fig = px.line(
    production,
    x="market_year",
    y="production",
    markers=True,
    title="Global Coffee Production Trend"
)

fig.update_traces(line_width=3)

st.plotly_chart(fig, use_container_width=True)

st.info("""
Coffee production has shown a strong long-term upward trend,
reflecting expansion in cultivation and increasing global demand.
""")

# ============================================================
# GLOBAL CONSUMPTION TREND
# ============================================================

consumption = run_query("""
SELECT
    market_year,
    SUM(domestic_consumption) AS consumption
FROM vw_coffee_market
GROUP BY market_year
ORDER BY market_year;
""")

fig = px.line(
    consumption,
    x="market_year",
    y="consumption",
    markers=True,
    title="Global Coffee Consumption Trend"
)

fig.update_traces(line_width=3)

st.plotly_chart(fig, use_container_width=True)

st.info("""
Global coffee consumption continues to rise, indicating sustained
consumer demand across developed and emerging markets.
""")

# ============================================================
# GLOBAL TRADE TREND
# ============================================================

trade = run_query("""
SELECT
    market_year,
    SUM(exports) AS exports,
    SUM(imports) AS imports
FROM vw_coffee_market
GROUP BY market_year
ORDER BY market_year;
""")

fig = px.line(
    trade,
    x="market_year",
    y=["exports", "imports"],
    markers=True,
    title="Global Coffee Trade Trend"
)

fig.update_traces(line_width=3)

st.plotly_chart(fig, use_container_width=True)

st.info("""
Exports and imports have grown steadily over time,
highlighting increasing globalization of the coffee market.
""")

# ============================================================
# GLOBAL STOCK TREND
# ============================================================

stocks = run_query("""
SELECT
    market_year,
    SUM(beginning_stocks) AS beginning_stock,
    SUM(ending_stocks) AS ending_stock
FROM vw_coffee_market
GROUP BY market_year
ORDER BY market_year;
""")

fig = px.line(
    stocks,
    x="market_year",
    y=["beginning_stock", "ending_stock"],
    markers=True,
    title="Global Coffee Inventory Trend"
)

fig.update_traces(line_width=3)

st.plotly_chart(fig, use_container_width=True)

st.info("""
Inventory levels fluctuate based on production cycles,
global demand, and international trade dynamics.
""")

# ============================================================
# EXECUTIVE SUMMARY
# ============================================================

st.markdown("---")

st.subheader("Executive Summary")

st.markdown("""
### Key Findings

- Coffee production has increased consistently over the past several decades.
- Global consumption continues to grow, reflecting expanding consumer demand.
- International coffee trade has become increasingly important, with exports and imports rising together.
- Inventory levels fluctuate over time but generally remain balanced, indicating a stable global supply chain.
- Overall, the coffee market demonstrates sustained long-term growth supported by production expansion and increasing international trade.
""")