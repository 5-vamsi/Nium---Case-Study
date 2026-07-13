"""
extract.py
----------

Responsible for reading raw datasets from disk.
No cleaning or transformation is performed here.
"""

import pandas as pd

from src.config import (
    COFFEE_DATA_FILE,
    POPULATION_DATA_FILE,
    COUNTRY_CODES_FILE
)


def load_coffee_data():
    """Load the coffee dataset."""
    return pd.read_csv(COFFEE_DATA_FILE)


def load_population_data():
    """Load the population dataset."""
    return pd.read_csv(
        POPULATION_DATA_FILE,
        skiprows=4
    )


def load_country_codes():
    """Load the country codes dataset."""
    return pd.read_csv(
        COUNTRY_CODES_FILE,
        sep=";"
    )


def load_all_datasets():
    """
    Load all datasets and return them.

    Returns
    -------
    tuple
        coffee_df, population_df, country_df
    """

    coffee_df = load_coffee_data()
    population_df = load_population_data()
    population_df = population_df.loc[:,
                                      ~population_df.columns.str.contains("^Unnamed")]
    country_df = load_country_codes()

    return (
        coffee_df,
        population_df,
        country_df
    )