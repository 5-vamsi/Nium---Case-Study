"""
analytics.py
------------

Analytics layer for building the warehouse model.
"""

import pandas as pd


def build_country_dimension(
    coffee_fact: pd.DataFrame,
    population_fact: pd.DataFrame,
    country_codes: pd.DataFrame,
):
    """
    Build the Country Dimension.
    """
    

    # Coffee countries
    coffee = coffee_fact[
        [
            "standardized_country_name",
            "country_name",
            "country_code",
        ]
    ].drop_duplicates()

    # Population countries
    population = population_fact[
        [
            "standardized_country_name",
            "country_name",
            "country_code",
        ]
    ].drop_duplicates()

    # Combine
    countries = pd.concat(
        [coffee, population],
        ignore_index=True,
    ).drop_duplicates(
        subset="standardized_country_name"
    )

    # Join with country codes
    dim_country = countries.merge(
        country_codes[
            [
                "LABEL EN",
                "ISO2 CODE",
                "ISO3 CODE",
                "ONU CODE",
            ]
        ],
        how="left",
        left_on="standardized_country_name",
        right_on="LABEL EN",
    )

    # Cleanup
    dim_country = dim_country.rename(
    columns={
        "country_code": "coffee_country_code",
        "ISO2 CODE": "iso2",
        "ISO3 CODE": "iso3",
        "ONU CODE": "onu_code",
    }
)

    dim_country = dim_country.drop(
        columns=["LABEL EN"]
    )

    # Generate surrogate key
    dim_country.insert(
        0,
        "country_id",
        range(1, len(dim_country) + 1),
    )

    return dim_country

def attach_country_id(
    fact_df: pd.DataFrame,
    dim_country: pd.DataFrame
) -> pd.DataFrame:
    """
    Attach country_id to a fact table using standardized country names.
    """

    fact = fact_df.merge(
        dim_country[
            [
                "country_id",
                "standardized_country_name"
            ]
        ],
        on="standardized_country_name",
        how="left"
    )

    # Move country_id to the front
    cols = ["country_id"] + [
        c for c in fact.columns
        if c != "country_id"
    ]

    fact = fact[cols]

    return fact