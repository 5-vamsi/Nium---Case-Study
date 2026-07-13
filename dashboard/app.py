import streamlit as st

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Coffee Market Analysis Dashboard",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)



# ==========================================================
# MAIN PAGE
# ==========================================================

st.title("☕ Coffee Market Analysis Dashboard")

st.markdown("""
This project analyzes historical global coffee market data using an end-to-end analytics pipeline.

The solution includes:

- Automated ETL pipeline
- PostgreSQL data warehouse
- SQL analytical views
- Interactive Streamlit dashboard
- Business insights and recommendations
""")

# ==========================================================
# PROJECT OBJECTIVE
# ==========================================================

st.subheader("Project Objective")

st.markdown("""
The objective of this project is to transform raw coffee production and
population datasets into actionable business insights.

The dashboard enables stakeholders to:

- Monitor global coffee production and consumption
- Analyze international trade patterns
- Explore country-level performance
- Identify market opportunities
- Support data-driven business decisions
""")

# ==========================================================
# DASHBOARD OVERVIEW
# ==========================================================

st.subheader("Dashboard Pages")

overview = {
    "Executive Overview":
        "High-level KPIs and long-term market trends.",

    "Market Intelligence":
        "Top producers, consumers, exporters and importers.",

    "Country Explorer":
        "Interactive country-wise performance analysis.",

    "Trend Analysis":
        "Historical trends in production, trade and inventory.",

    "Business Recommendations":
        "Key findings and strategic recommendations."
}

st.table(overview)

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.caption("""
Coffee Market Analysis Dashboard

Business Case Study

Built using Python • PostgreSQL • SQL • Plotly • Streamlit
""")