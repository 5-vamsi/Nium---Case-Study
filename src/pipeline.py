"""
pipeline.py
-----------

Main ETL pipeline for the Coffee Market Analysis project.
"""

from src.extract import load_all_datasets
from src.harmonize import harmonize_country_names
from src.transform import (
    transform_coffee_data,
    transform_population_data,
)
from src.validate import (
    validate_raw_dataset,
    validate_fact_table,
)
from src.analytics import (
    build_country_dimension,
    attach_country_id,
)


def run_pipeline():
    """
    Execute the complete ETL pipeline.
    """

    print("=" * 80)
    print("COFFEE MARKET ANALYSIS PIPELINE")
    print("=" * 80)

    # ==========================================================
    # 1. EXTRACT
    # ==========================================================

    print("\n[1/4] Loading datasets...")

    coffee_df, population_df, country_df = load_all_datasets()

    print("Datasets loaded successfully.")

    # ==========================================================
    # RAW DATA VALIDATION
    # ==========================================================

    validate_raw_dataset(coffee_df, "Coffee")
    validate_raw_dataset(population_df, "Population")
    validate_raw_dataset(country_df, "Country Codes")

    # ==========================================================
    # 2. HARMONIZE
    # ==========================================================

    print("\n[2/4] Harmonizing country names...")

    coffee_df = harmonize_country_names(
        coffee_df,
        "Country_Name",
    )

    population_df = harmonize_country_names(
        population_df,
        "Country Name",
    )

    print("Country harmonization completed.")

    # ==========================================================
    # 3. TRANSFORM
    # ==========================================================

    print("\n[3/4] Transforming datasets...")

    coffee_fact = transform_coffee_data(coffee_df)

    population_fact = transform_population_data(population_df)

    print("Transformations completed.")

    # ==========================================================
    # FACT TABLE VALIDATION
    # ==========================================================

    validate_fact_table(
        coffee_fact,
        "Coffee Fact",
        "standardized_country_name",
        "market_year",
    )

    validate_fact_table(
        population_fact,
        "Population Fact",
        "standardized_country_name",
        "year",
    )

    # ==========================================================
    # BUILD COUNTRY DIMENSION
    # ==========================================================

    print("\nBuilding Country Dimension...")

    dim_country = build_country_dimension(
        coffee_fact,
        population_fact,
        country_df,
    )

    print("Country Dimension Created.")

    # ==========================================================
    # ATTACH COUNTRY IDS
    # ==========================================================

    print("\nAttaching Country IDs...")

    coffee_fact = attach_country_id(
        coffee_fact,
        dim_country,
    )

    population_fact = attach_country_id(
        population_fact,
        dim_country,
    )

    print("Country IDs attached.")

    # ==========================================================
    # WAREHOUSE VALIDATION
    # ==========================================================

    print("\n" + "=" * 80)
    print("WAREHOUSE VALIDATION")
    print("=" * 80)

    print(f"Coffee Rows      : {len(coffee_fact)}")
    print(f"Population Rows  : {len(population_fact)}")
    print(f"Country Rows     : {len(dim_country)}")

    print("\nMissing country_id")

    print(
        "Coffee      :",
        coffee_fact["country_id"].isna().sum(),
    )

    print(
        "Population  :",
        population_fact["country_id"].isna().sum(),
    )

    coffee_ids = set(coffee_fact["country_id"])
    population_ids = set(population_fact["country_id"])
    dimension_ids = set(dim_country["country_id"])

    print("\nCoffee IDs missing in Dimension:")
    print(coffee_ids - dimension_ids)

    print("\nPopulation IDs missing in Dimension:")
    print(population_ids - dimension_ids)

    print("\nUnique Country Counts")

    print(
        "Coffee      :",
        coffee_fact["country_id"].nunique(),
    )

    print(
        "Population  :",
        population_fact["country_id"].nunique(),
    )

    print(
        "Dimension   :",
        dim_country["country_id"].nunique(),
    )

    # ==========================================================
    # COUNTRY COVERAGE VALIDATION
    # ==========================================================

    coffee_countries = set(
        coffee_fact["standardized_country_name"]
    )

    population_countries = set(
        population_fact["standardized_country_name"]
    )

    print("\n" + "=" * 80)
    print("COUNTRY COVERAGE VALIDATION")
    print("=" * 80)

    print("\nCoffee countries NOT in Population:")
    print(coffee_countries - population_countries)

    print("\nPopulation countries NOT in Coffee:")
    print(population_countries - coffee_countries)

    print("\nCommon Countries:")
    print(len(coffee_countries.intersection(population_countries)))

    # ==========================================================
    # 4. SAVE
    # ==========================================================

    print("\n[4/4] Saving processed datasets...")

    dim_country.to_csv(
        "data/processed/dim_country.csv",
        index=False,
    )

    coffee_fact.to_csv(
        "data/processed/fact_coffee.csv",
        index=False,
    )

    population_fact.to_csv(
        "data/processed/fact_population.csv",
        index=False,
    )

    print("Processed datasets saved.")

    print("\n" + "=" * 80)
    print("PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 80)

    return (
        dim_country,
        coffee_fact,
        population_fact,
    )