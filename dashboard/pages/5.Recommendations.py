import streamlit as st
import plotly.express as px

from database import run_query

st.set_page_config(
    page_title="Business Recommendations",
    page_icon="💡",
    layout="wide"
)

st.title("💡 Business Recommendations")

st.markdown(
    """
    Key business insights derived from production,
    consumption and international trade patterns.
    """
)

# ---------------------------------------------------
# Production Surplus
# ---------------------------------------------------

surplus = run_query("""
SELECT
    country_name,
    SUM(production-domestic_consumption) AS surplus
FROM vw_coffee_market
GROUP BY country_name
ORDER BY surplus DESC
LIMIT 10;
""")

fig = px.bar(
    surplus,
    x="country_name",
    y="surplus",
    title="Top Production Surplus Countries"
)

st.plotly_chart(fig, use_container_width=True)

st.success(
"""
Recommendation

These countries consistently produce more coffee than they consume,
making them attractive export partners and suppliers.
"""
)

# ---------------------------------------------------
# Production Deficit
# ---------------------------------------------------

deficit = run_query("""
SELECT
    country_name,
    SUM(domestic_consumption-production) AS deficit
FROM vw_coffee_market
GROUP BY country_name
ORDER BY deficit DESC
LIMIT 10;
""")

fig = px.bar(
    deficit,
    x="country_name",
    y="deficit",
    title="Top Coffee Deficit Countries"
)

st.plotly_chart(fig, use_container_width=True)

st.warning(
"""
Recommendation

These markets depend on imports and may represent attractive
opportunities for exporters and distributors.
"""
)

# ---------------------------------------------------
# Import Dependency
# ---------------------------------------------------

imports = run_query("""
SELECT
    country_name,
    ROUND(
        SUM(imports) /
        NULLIF(SUM(domestic_consumption),0),
        2
    ) AS dependency
FROM vw_coffee_market
GROUP BY country_name
ORDER BY dependency DESC
LIMIT 10;
""")

fig = px.bar(
    imports,
    x="country_name",
    y="dependency",
    title="Highest Import Dependency"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# Export Dependency
# ---------------------------------------------------

exports = run_query("""
SELECT
    country_name,
    ROUND(
        SUM(exports) /
        NULLIF(SUM(production),0),
        2
    ) AS dependency
FROM vw_coffee_market
GROUP BY country_name
ORDER BY dependency DESC
LIMIT 10;
""")

fig = px.bar(
    exports,
    x="country_name",
    y="dependency",
    title="Highest Export Dependency"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# Final Summary
# ---------------------------------------------------

st.header("Executive Summary")

st.markdown("""
### Key Findings

- Global coffee production is concentrated among a small number of countries.
- Several countries consistently produce more coffee than they consume, supporting strong export markets.
- Import-dependent countries present potential opportunities for exporters.
- Coffee consumption continues to grow in many markets, indicating sustained long-term demand.
- Population-adjusted consumption highlights mature coffee-drinking markets that differ from simply looking at total consumption.
""")