"""
validate.py
-----------

Validation utilities for the Coffee Market Analysis project.
"""

import pandas as pd


def validate_raw_dataset(df: pd.DataFrame, dataset_name: str):
    """
    Validate a raw dataset.
    """

    print("\n" + "=" * 70)
    print(f"RAW DATA VALIDATION : {dataset_name.upper()}")
    print("=" * 70)

    print(f"Shape: {df.shape}")

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nMissing Values:")
    print(df.isnull().sum())


def validate_fact_table(
    df: pd.DataFrame,
    dataset_name: str,
    country_column: str,
    year_column: str,
):
    """
    Validate transformed fact tables.
    """

    print("\n" + "=" * 70)
    print(f"FACT TABLE VALIDATION : {dataset_name.upper()}")
    print("=" * 70)

    print(f"Shape: {df.shape}")

    duplicates = df.duplicated(
        subset=[country_column, year_column]
    ).sum()

    print(f"\nDuplicate Country-Year Records: {duplicates}")

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nYear Range:")

    print(
        df[year_column].min(),
        "->",
        df[year_column].max()
    )