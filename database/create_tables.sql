-- =====================================================
-- Coffee Market Analysis
-- Data Warehouse Schema
-- =====================================================

DROP TABLE IF EXISTS fact_population;
DROP TABLE IF EXISTS fact_coffee;
DROP TABLE IF EXISTS dim_country;

-- =====================================================
-- Dimension Table
-- =====================================================

CREATE TABLE dim_country (

    country_id INTEGER PRIMARY KEY,

    standardized_country_name VARCHAR(150) NOT NULL,

    country_name VARCHAR(150),

    coffee_country_code VARCHAR(10),

    iso2 VARCHAR(5),

    iso3 VARCHAR(5),

    onu_code INTEGER

);

-- =====================================================
-- Coffee Fact Table
-- =====================================================

CREATE TABLE fact_coffee (

    country_id INTEGER,

    country_name VARCHAR(150),

    standardized_country_name VARCHAR(150),

    country_code VARCHAR(10),

    market_year INTEGER,

    arabica_production NUMERIC,

    bean_exports NUMERIC,

    bean_imports NUMERIC,

    beginning_stocks NUMERIC,

    domestic_consumption NUMERIC,

    ending_stocks NUMERIC,

    exports NUMERIC,

    imports NUMERIC,

    other_production NUMERIC,

    production NUMERIC,

    roast_and_ground_exports NUMERIC,

    roast_and_ground_imports NUMERIC,

    robusta_production NUMERIC,

    rstground_dom_consum NUMERIC,

    soluble_dom_cons NUMERIC,

    soluble_exports NUMERIC,

    soluble_imports NUMERIC,

    total_distribution NUMERIC,

    total_supply NUMERIC

);

-- =====================================================
-- Population Fact Table
-- =====================================================

CREATE TABLE fact_population (

    country_id INTEGER,

    country_name VARCHAR(150),

    standardized_country_name VARCHAR(150),

    country_code VARCHAR(10),

    indicator_name VARCHAR(150),

    indicator_code VARCHAR(50),

    year INTEGER,

    population NUMERIC

);