import streamlit as st
import plotly.express as px

from database import run_query

st.set_page_config(
    page_title="Business Recommendations",
    page_icon="💡",
    layout="wide"
)

st.title("💡 Business Recommendations")

st.markdown("""
This page summarizes the final business recommendations for ACME Baristas
based on the insights generated from the analytical dashboards.
""")

# ==========================================================
# TOP RECOMMENDED MARKETS
# ==========================================================

st.header("🏆 Recommended Markets for ACME Baristas")

st.info("""
The recommended markets were identified by combining insights from multiple dashboard pages.
The analysis considered coffee consumption, coffee imports, per-capita consumption,
population size and historical market trends rather than relying on a single metric.
""")

st.markdown("""
### 🥇 United States

**Why was it selected?**

- High overall coffee consumption indicates strong market demand.
- Large population provides a broad potential customer base.
- Strong coffee import volumes suggest sustained domestic demand.
- Historical trends demonstrate consistent coffee consumption.

**Supporting Dashboard Pages**

- **Market Intelligence** → Top Coffee Consumers
- **Market Intelligence** → Coffee Import Analysis
- **Country Explorer** → Country-level market insights
- **Trend Analysis** → Historical demand trends

---

### 🥈 Japan

**Why was it selected?**

- High dependence on coffee imports.
- Strong per-capita coffee consumption.
- Stable long-term demand indicates a mature coffee market.

**Supporting Dashboard Pages**

- **Market Intelligence** → Import Analysis
- **Market Intelligence** → Per-Capita Consumption
- **Country Explorer**
- **Trend Analysis**

---

### 🥉 Canada

**Why was it selected?**

- Strong coffee consumption relative to population.
- Consistent import activity indicates stable market demand.
- Long-term trends support continued market potential.

**Supporting Dashboard Pages**

- **Market Intelligence** → Consumption Analysis
- **Market Intelligence** → Import Analysis
- **Country Explorer**
- **Trend Analysis**
""")

# ==========================================================
# Production Surplus
# ==========================================================

st.header("🌍 Production Surplus Analysis")

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

st.success("""
### Business Insight

Countries with a large production surplus consistently produce more coffee than they consume.

**Opportunity**

These countries can serve as reliable sourcing partners and suppliers
for ACME Baristas' global supply chain.
""")

# ==========================================================
# Production Deficit
# ==========================================================

st.header("📦 Production Deficit Analysis")

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

st.warning("""
### Business Insight

Countries with large production deficits consume more coffee than they produce.

**Opportunity**

These markets rely heavily on imports and represent attractive expansion
opportunities for coffee retailers and distributors.
""")

# ==========================================================
# Executive Summary
# ==========================================================

st.header("📋 Executive Business Conclusions")

st.success("""
### Business Question 1

**Which three markets should ACME Baristas enter?**

Based on the combined analysis across the dashboard, the recommended
markets are:

1. 🇺🇸 United States
2. 🇯🇵 Japan
3. 🇨🇦 Canada

The recommendation is supported by insights from:

• Market Intelligence Dashboard
• Country Explorer Dashboard
• Trend Analysis Dashboard

---

### Business Question 2

**Is this a good time to enter the coffee market?**

Yes.

Historical production and consumption trends indicate sustained
global coffee demand, while import-dependent markets continue to
offer attractive expansion opportunities.

---

### Business Question 3

**Opportunities**

• Growing global coffee demand

• Import-dependent consumer markets

• Large and mature coffee-drinking populations

• Long-term market growth potential

**Risks**

• Climate impacts on coffee production

• Commodity price fluctuations

• Supply chain disruptions

• Strong competition from established coffee brands
""")