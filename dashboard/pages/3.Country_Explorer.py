import streamlit as st
import plotly.express as px

from database import (
    run_query,
    kpi_card,
)

st.set_page_config(
    page_title="Country Explorer",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Country Explorer")

st.markdown("""
Explore historical coffee market performance for an individual country,
including production, consumption, trade, inventory levels and market indicators.
""")

# ==========================================================
# COUNTRY SELECTION
# ==========================================================

countries = run_query("""
SELECT DISTINCT country_name
FROM vw_coffee_market
ORDER BY country_name;
""")

selected_country = st.sidebar.selectbox(
    "Select Country",
    countries["country_name"]
)

years = run_query(f"""
SELECT DISTINCT market_year
FROM vw_coffee_market
WHERE country_name='{selected_country}'
ORDER BY market_year;
""")

selected_year = st.sidebar.selectbox(
    "Select Year",
    years["market_year"]
)

# ==========================================================
# KPI
# ==========================================================

kpi = run_query(f"""
SELECT

production,

domestic_consumption,

exports,

imports,

population,

(exports-imports) trade_balance

FROM vw_coffee_market

WHERE country_name='{selected_country}'
AND market_year={selected_year};
""")

c1, c2, c3 = st.columns(3)

c4, c5, c6 = st.columns(3)

kpi_card(
    c1,
    "Production",
    kpi.iloc[0]["production"]
)

kpi_card(
    c2,
    "Consumption",
    kpi.iloc[0]["domestic_consumption"]
)

kpi_card(
    c3,
    "Population",
    kpi.iloc[0]["population"]
)

kpi_card(
    c4,
    "Exports",
    kpi.iloc[0]["exports"]
)

kpi_card(
    c5,
    "Imports",
    kpi.iloc[0]["imports"]
)

kpi_card(
    c6,
    "Trade Balance",
    kpi.iloc[0]["trade_balance"]
)

st.divider()

# ==========================================================
# HISTORY
# ==========================================================

history = run_query(f"""
SELECT

market_year,

production,

domestic_consumption

FROM vw_coffee_market

WHERE country_name='{selected_country}'

ORDER BY market_year;
""")

trade = run_query(f"""
SELECT

market_year,

exports,

imports

FROM vw_coffee_market

WHERE country_name='{selected_country}'

ORDER BY market_year;
""")

left, right = st.columns(2)

with left:

    if history["production"].sum() == 0:

        st.warning(
            "No production data available for this country."
        )

    else:

        fig = px.line(
            history,
            x="market_year",
            y=["production", "domestic_consumption"],
            markers=True,
            title=f"{selected_country}: Production vs Consumption"
        )

        fig.update_traces(line_width=3)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

with right:

    if (
        trade["exports"].sum() == 0
        and
        trade["imports"].sum() == 0
    ):

        st.warning(
            "No trade data available for this country."
        )

    else:

        fig = px.bar(
            trade,
            x="market_year",
            y=["exports", "imports"],
            barmode="group",
            title=f"{selected_country}: Imports vs Exports"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

st.divider()

# ==========================================================
# STOCKS
# ==========================================================

stocks = run_query(f"""
SELECT

market_year,

beginning_stocks,

ending_stocks

FROM vw_coffee_market

WHERE country_name='{selected_country}'

ORDER BY market_year;
""")

if (
    stocks["beginning_stocks"].sum() == 0
    and
    stocks["ending_stocks"].sum() == 0
):

    st.info(
        "No inventory data is available for this country."
    )

else:

    fig = px.line(
        stocks,
        x="market_year",
        y=["beginning_stocks", "ending_stocks"],
        markers=True,
        title=f"{selected_country}: Coffee Inventory Trend"
    )

    fig.update_traces(line_width=3)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()
# ==========================================================
# BUSINESS SUMMARY
# ==========================================================

production = kpi.iloc[0]["production"]
consumption = kpi.iloc[0]["domestic_consumption"]
exports = kpi.iloc[0]["exports"]
imports = kpi.iloc[0]["imports"]

summary = []

if production == 0:
    summary.append(
        "- No domestic coffee production is reported for the selected year."
    )
else:
    summary.append(
        "- The country contributes to global coffee production."
    )

if imports > exports:
    summary.append(
        "- The country is a net importer of coffee and depends on international supply."
    )
elif exports > imports:
    summary.append(
        "- The country is a net exporter and contributes to global coffee trade."
    )

if consumption > production:
    summary.append(
        "- Domestic demand exceeds local production, increasing reliance on imports."
    )
elif production > consumption:
    summary.append(
        "- Production exceeds domestic demand, creating export opportunities."
    )

summary_text = "\n".join(summary)

st.success(
    f"""
### Business Summary

**{selected_country} ({selected_year})**

{summary_text}
"""
)