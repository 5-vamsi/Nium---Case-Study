"""
config.py
---------

Central configuration file for the Coffee Market Analysis project.

This module contains:
1. Project paths
2. Raw data file locations
3. Processed data file locations
4. Database configuration (to be updated later)
"""

from pathlib import Path

# ==========================================================
# PROJECT ROOT
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ==========================================================
# DATA DIRECTORIES
# ==========================================================

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MAPPING_DATA_DIR = DATA_DIR / "mapping"

# ==========================================================
# RAW DATA FILES
# ==========================================================

COFFEE_DATA_FILE = RAW_DATA_DIR / "psd_coffee.csv"

POPULATION_DATA_FILE = (
    RAW_DATA_DIR / "API_SP.POP.TOTL_DS2_EN_csv_v2_3107.csv"
)

COUNTRY_CODES_FILE = RAW_DATA_DIR / "countries-codes.csv"

# ==========================================================
# PROCESSED FILES
# ==========================================================

COFFEE_CLEAN_FILE = PROCESSED_DATA_DIR / "coffee_clean.csv"

POPULATION_CLEAN_FILE = PROCESSED_DATA_DIR / "population_clean.csv"

COUNTRY_CLEAN_FILE = PROCESSED_DATA_DIR / "country_clean.csv"

COUNTRY_MAPPING_FILE = (
    MAPPING_DATA_DIR / "country_mapping.csv"
)

# ==========================================================
# DATABASE CONFIGURATION
# (Will be updated once PostgreSQL is configured)
# ==========================================================

DB_NAME = "coffee_market_db"
DB_USER = "chiruhasbonam"
DB_PASSWORD = ""
DB_HOST = "localhost"
DB_PORT = "5432"

# ==========================================================
# PROJECT SETTINGS
# ==========================================================

LATEST_ANALYSIS_YEAR = 2025

COFFEE_UNIT = "1000 60 KG BAGS"


COUNTRY_KEY = "ISO3"
GENERATED_MAPPING_FILE = (
    MAPPING_DATA_DIR / "country_mapping_generated.csv"
)