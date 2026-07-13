"""
load_postgres.py
----------------

Load processed warehouse tables into PostgreSQL.
"""

import pandas as pd
from sqlalchemy import create_engine
from config import (
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
)


def get_engine():
    """
    Create PostgreSQL connection.
    """

    connection_string = (
        f"postgresql+psycopg2://"
        f"{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    return create_engine(
        connection_string,
        connect_args={"sslmode": "require"},
        )


def load_table(csv_path, table_name, engine):
    """
    Load a CSV into PostgreSQL.
    """

    print(f"\nLoading {table_name}...")

    df = pd.read_csv(csv_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False,
    )

    print(f"{len(df)} rows loaded into {table_name}.")


def load_all_tables():
    """
    Load all warehouse tables.
    """

    engine = get_engine()

    load_table(
        "data/processed/dim_country.csv",
        "dim_country",
        engine,
    )

    load_table(
        "data/processed/fact_coffee.csv",
        "fact_coffee",
        engine,
    )

    load_table(
        "data/processed/fact_population.csv",
        "fact_population",
        engine,
    )

    print("\nAll tables loaded successfully.")


if __name__ == "__main__":
    load_all_tables()