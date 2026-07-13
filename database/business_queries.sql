/* Top 10 Coffee Producing Countries */
SELECT

country_name,

SUM(production) AS total_production

FROM vw_coffee_market

GROUP BY country_name

ORDER BY total_production DESC

LIMIT 10;

/* Top 10 Coffee Consuming Countries */

SELECT

country_name,

SUM(domestic_consumption) AS consumption

FROM vw_coffee_market

GROUP BY country_name

ORDER BY consumption DESC

LIMIT 10;

/* Top 10 Coffee Exporting Countries */

SELECT

country_name,

SUM(exports) AS exports

FROM vw_coffee_market

GROUP BY country_name

ORDER BY exports DESC

LIMIT 10;

/* Top 10 Coffee Importing Countries */

SELECT

country_name,

SUM(imports) AS imports

FROM vw_coffee_market

GROUP BY country_name

ORDER BY imports DESC

LIMIT 10;

/* Top 20 Countries by Average Consumption */

SELECT

country_name,

AVG(consumption_per_person) AS avg_consumption

FROM vw_coffee_market

WHERE consumption_per_person IS NOT NULL

GROUP BY country_name

ORDER BY avg_consumption DESC

LIMIT 20;

/* Country-wise Production, Consumption, Exports, Imports */

SELECT

country_name,

SUM(production) production,

SUM(domestic_consumption) consumption,

SUM(production)-SUM(domestic_consumption) surplus

FROM vw_coffee_market

GROUP BY country_name

ORDER BY surplus DESC;

/* Global KPIs */

SELECT
    SUM(production) AS total_production,
    SUM(domestic_consumption) AS total_consumption,
    SUM(exports) AS total_exports,
    SUM(imports) AS total_imports,
    SUM(population) AS total_population
FROM vw_coffee_market;

/* Latest Market Year */
SELECT MAX(market_year) AS latest_year
FROM vw_coffee_market;

/* Number of Countries */
SELECT COUNT(DISTINCT country_name) AS countries
FROM vw_coffee_market;

/* Production Over Time */
SELECT
    market_year,
    SUM(production) AS production
FROM vw_coffee_market
GROUP BY market_year
ORDER BY market_year;

/* Arabica and Robusta Production Over Time */
SELECT
    market_year,
    SUM(arabica_production) AS arabica,
    SUM(robusta_production) AS robusta
FROM vw_coffee_market
GROUP BY market_year
ORDER BY market_year;

/* Top 10 Arabica Producing Countries */
SELECT
    country_name,
    SUM(arabica_production) AS arabica
FROM vw_coffee_market
GROUP BY country_name
ORDER BY arabica DESC
LIMIT 10;

/* Top 10 Robusta Producing Countries */
SELECT
    country_name,
    SUM(robusta_production) AS robusta
FROM vw_coffee_market
GROUP BY country_name
ORDER BY robusta DESC
LIMIT 10;

/* Consumption Over Time */
SELECT
    market_year,
    SUM(domestic_consumption) AS consumption
FROM vw_coffee_market
GROUP BY market_year
ORDER BY market_year;

/* Average Consumption by Country */
SELECT
    country_name,
    AVG(consumption_per_person) AS avg_consumption
FROM vw_coffee_market
WHERE consumption_per_person IS NOT NULL
GROUP BY country_name
ORDER BY avg_consumption DESC
LIMIT 15;

/* Average Consumption Over Time */
SELECT
    market_year,
    AVG(domestic_consumption) AS avg_consumption
FROM vw_coffee_market
GROUP BY market_year
ORDER BY market_year;

/* Trade Balance by Country */

SELECT
    country_name,
    SUM(exports - imports) AS trade_balance
FROM vw_coffee_market
GROUP BY country_name
ORDER BY trade_balance DESC;

/* Exports Over Time */
SELECT
    market_year,
    SUM(exports) AS exports
FROM vw_coffee_market
GROUP BY market_year
ORDER BY market_year;

/* Imports Over Time */
SELECT
    market_year,
    SUM(imports) AS imports
FROM vw_coffee_market
GROUP BY market_year
ORDER BY market_year;

/* Stock Levels Over Time */
SELECT
    market_year,
    SUM(beginning_stocks) AS beginning_stock,
    SUM(ending_stocks) AS ending_stock
FROM vw_coffee_market
GROUP BY market_year
ORDER BY market_year;

/* Top 15 Countries by Ending Stock Levels */
SELECT
    country_name,
    SUM(ending_stocks) AS stock
FROM vw_coffee_market
GROUP BY country_name
ORDER BY stock DESC
LIMIT 15;

/* Top 15 Countries by Surplus */
SELECT
    country_name,
    SUM(production - domestic_consumption) AS surplus
FROM vw_coffee_market
GROUP BY country_name
ORDER BY surplus DESC;

/* Top 15 Countries by Deficit */
SELECT
    country_name,
    SUM(domestic_consumption - production) AS deficit
FROM vw_coffee_market
GROUP BY country_name
ORDER BY deficit DESC;

/* Import Dependency */
SELECT
    country_name,
    SUM(imports) /
    NULLIF(SUM(domestic_consumption),0) AS import_dependency
FROM vw_coffee_market
GROUP BY country_name
ORDER BY import_dependency DESC;

/* Export Dependency */
SELECT
    country_name,
    SUM(exports) /
    NULLIF(SUM(production),0) AS export_dependency
FROM vw_coffee_market
GROUP BY country_name
ORDER BY export_dependency DESC;

