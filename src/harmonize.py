"""
harmonize.py
------------

Country harmonization utilities.
"""

import pandas as pd

COUNTRY_ALIASES = {
    "Vietnam": "Viet Nam",
    "Russia": "Russian Federation",
    "Iran": "Iran, Islamic Rep.",
    "Egypt": "Egypt, Arab Rep.",
    "Turkey": "Turkiye",
    "Korea, South": "Korea, Rep.",
    "Laos": "Lao PDR",
    "Venezuela": "Venezuela, RB",
    "Congo (Brazzaville)": "Congo, Rep.",
    "Congo (Kinshasa)": "Congo, Dem. Rep.",
    "Yemen": "Yemen, Rep.",
    "Yemen (Sanaa)": "Yemen, Rep."
}


def harmonize_country_names(df, country_column):
    """
    Preserve original country names while creating a
    standardized country name for joins.
    """

    df = df.copy()

    df["standardized_country_name"] = (
        df[country_column]
        .replace(COUNTRY_ALIASES)
    )

    return df