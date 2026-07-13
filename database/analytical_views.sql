DROP VIEW IF EXISTS vw_coffee_market;

CREATE VIEW vw_coffee_market AS

SELECT

    dc.country_id,
    dc.country_name,
    dc.iso3,

    fc.market_year,

    fc.production,
    fc.arabica_production,
    fc.robusta_production,

    fc.domestic_consumption,

    fc.exports,
    fc.imports,

    fc.beginning_stocks,
    fc.ending_stocks,

    fp.population,

    CASE
        WHEN fp.population > 0
        THEN (fc.domestic_consumption * 60000.0) / fp.population
        ELSE NULL
    END AS consumption_per_person

FROM fact_coffee fc

JOIN dim_country dc
ON fc.country_id = dc.country_id

LEFT JOIN fact_population fp

ON fc.country_id = fp.country_id

AND fc.market_year = fp.year;