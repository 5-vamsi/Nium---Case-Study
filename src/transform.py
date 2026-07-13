"""
transform.py
------------

Transform raw datasets into analytical tables.
"""

import re
import pandas as pd


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert column names into SQL-friendly snake_case.
    """

    columns = []

    for column in df.columns:

        column = column.lower()
        column = column.replace("&", "and")
        column = column.replace(",", "")
        column = column.replace(".", "")
        column = column.replace(" ", "_")

        column = re.sub(r"_+", "_", column)

        columns.append(column)

    df.columns = columns

    return df


def transform_coffee_data(coffee_df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform coffee data from long to wide format.
    """

    coffee_fact = coffee_df.pivot_table(
        index=[
    "Country_Name",
    "standardized_country_name",
    "Country_Code",
    "Market_Year"
],
        columns="Attribute_Description",
        values="Value",
        aggfunc="first"
    ).reset_index()

    coffee_fact = standardize_column_names(coffee_fact)

    return coffee_fact


def transform_population_data(population_df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform World Bank population data from wide to long format.
    """

    id_columns = [
    "Country Name",
    "standardized_country_name",
    "Country Code",
    "Indicator Name",
    "Indicator Code"
]

    population_fact = population_df.melt(
        id_vars=id_columns,
        var_name="Year",
        value_name="Population"
    )

    population_fact["Year"] = pd.to_numeric(
        population_fact["Year"],
        errors="coerce"
    )

    population_fact = population_fact.dropna(subset=["Year"])

    population_fact["Year"] = population_fact["Year"].astype(int)

    population_fact = standardize_column_names(population_fact)

    return population_fact