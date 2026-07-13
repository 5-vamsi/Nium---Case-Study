import streamlit as st
import plotly.express as px

from database import run_query

st.set_page_config(
    page_title="Market Intelligence",
    layout="wide"
)

st.title("Market Intelligence")

st.markdown("""
Explore the world's leading coffee markets across **production,
consumption, exports, imports, and per-capita consumption**.
""")

# =====================================================
# MARKET KPIs
# =====================================================

from database import kpi_card

kpi = run_query("""
SELECT
SUM(production) production,
SUM(domestic_consumption) consumption,
SUM(exports) exports,
SUM(imports) imports
FROM vw_coffee_market;
""")

c1, c2, c3, c4 = st.columns(4)

kpi_card(c1, "Global Production", kpi.iloc[0]["production"])
kpi_card(c2, "Global Consumption", kpi.iloc[0]["consumption"])
kpi_card(c3, "Global Exports", kpi.iloc[0]["exports"])
kpi_card(c4, "Global Imports", kpi.iloc[0]["imports"])

st.divider()
# =====================================================
# TOP PRODUCERS
# =====================================================

producers = run_query("""
SELECT
    country_name,
    SUM(production) AS total_production
FROM vw_coffee_market
GROUP BY country_name
ORDER BY total_production DESC
LIMIT 10;
""")

fig = px.bar(
    producers,
    x="total_production",
    y="country_name",
    orientation="h",
    title="Top 10 Coffee Producing Countries",
)

fig.update_layout(
    yaxis=dict(categoryorder="total ascending")
)

st.plotly_chart(fig, use_container_width=True)

st.success("""
Brazil and Vietnam dominate global coffee production, making them
strategic sourcing markets and major contributors to global supply.
""")

# =====================================================
# TOP CONSUMERS
# =====================================================

consumers = run_query("""
SELECT
    country_name,
    SUM(domestic_consumption) AS consumption
FROM vw_coffee_market
GROUP BY country_name
ORDER BY consumption DESC
LIMIT 10;
""")

fig = px.bar(
    consumers,
    x="consumption",
    y="country_name",
    orientation="h",
    title="Top 10 Coffee Consuming Countries",
)

fig.update_layout(
    yaxis=dict(categoryorder="total ascending")
)

st.plotly_chart(fig, use_container_width=True)

st.success("""
Large consumer markets indicate strong domestic demand and attractive
opportunities for retailers, distributors and coffee brands.
""")

# =====================================================
# TOP EXPORTERS
# =====================================================

exporters = run_query("""
SELECT
    country_name,
    SUM(exports) AS exports
FROM vw_coffee_market
GROUP BY country_name
ORDER BY exports DESC
LIMIT 10;
""")

fig = px.bar(
    exporters,
    x="exports",
    y="country_name",
    orientation="h",
    title="Top 10 Coffee Exporting Countries",
)

fig.update_layout(
    yaxis=dict(categoryorder="total ascending")
)

st.plotly_chart(fig, use_container_width=True)

st.success("""
Export-oriented countries form the backbone of the global coffee supply
chain and are important trading partners.
""")

# =====================================================
# TOP IMPORTERS
# =====================================================

importers = run_query("""
SELECT
    country_name,
    SUM(imports) AS imports
FROM vw_coffee_market
GROUP BY country_name
ORDER BY imports DESC
LIMIT 10;
""")

fig = px.bar(
    importers,
    x="imports",
    y="country_name",
    orientation="h",
    title="Top 10 Coffee Importing Countries",
)

fig.update_layout(
    yaxis=dict(categoryorder="total ascending")
)

st.plotly_chart(fig, use_container_width=True)

st.success("""
High-import countries rely heavily on international suppliers to satisfy
domestic demand and represent attractive export destinations.
""")

# =====================================================
# PER CAPITA CONSUMPTION
# =====================================================

per_capita = run_query("""
SELECT
    country_name,
    AVG(consumption_per_person) AS avg_consumption
FROM vw_coffee_market
WHERE consumption_per_person IS NOT NULL
GROUP BY country_name
ORDER BY avg_consumption DESC
LIMIT 10;
""")

fig = px.bar(
    per_capita,
    x="avg_consumption",
    y="country_name",
    orientation="h",
    title="Top 10 Countries by Per-Capita Coffee Consumption",
)

fig.update_layout(
    yaxis=dict(categoryorder="total ascending")
)

st.plotly_chart(fig, use_container_width=True)

st.success("""
Per-capita consumption identifies mature coffee-drinking markets where
coffee is deeply embedded in everyday consumer habits.
""")

st.markdown("---")

st.subheader("Executive Takeaways")

st.markdown("""
- **Brazil and Vietnam** remain the world's largest coffee producers.
- **The European Union and the United States** represent major consumption and import markets.
- Export activity is concentrated among relatively few producing countries.
- High-import economies present significant opportunities for coffee exporters.
- Per-capita consumption highlights mature coffee markets beyond overall population size.
""")