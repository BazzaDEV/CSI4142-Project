----- Part 1: Standard OLAP Operations -----

-- a) Drill Down, Roll Up (2 queries)
SELECT  C.country_code,F.quality_of_life_index,D.year_,D.month_,D.decade
FROM country as C, date_ as D, fact_table as F
WHERE C.surrogate_key = F.country_surrogate AND D.surrogate_key = F.date_surrogate
GROUP BY  (C.country_code,F.quality_of_life_index,D.year_,D.month_,D.decade)
ORDER BY D.year_,D.month_,D.decade

SELECT  C.country_code, AVG(F.income_index),D.year_,D.month_,D.decade
FROM country as C,date_ as D, fact_table as F
WHERE C.surrogate_key = F.country_surrogate AND D.surrogate_key = F.date_surrogate
GROUP BY (C.country_code,D.year_,D.month_,D.decade)
ORDER BY D.year_,D.month_,D.decade

-- b) Slice (1 query)
SELECT  C.country_code,F.quality_of_life_index,F.human_development_index,F.income_index
FROM country as C, date_ as D, fact_table as F
WHERE C.surrogate_key = F.country_surrogate AND D.surrogate_key = F.date_surrogate 
AND D.year_ in (2005,2006,2007,2008,2009,2010)
GROUP BY (C.country_code ,F.quality_of_life_index,F.human_development_index,F.income_index)

-- c) Dice (2 queries)
SELECT F.income_index,C.country_code, E.literacy_rate, D.year_
FROM fact_table as F, country as C, education as E, date_ as D
WHERE F.country_surrogate=C.surrogate_key and F.education_surrogate=E.surrogate_key and F.date_surrogate=D.surrogate_key
and C.country_code in ('CAN','MEX','USA') and D.year_ in (2015,2016,2017,2018,2019,2020)
GROUP BY (F.income_index,C.country_code, E.literacy_rate, D.year_)

SELECT F.human_development_index, C.country_code, L.final_consumption_expenditure, D.year_
FROM fact_table as F, country as C, living_conditions as L, date_ as D
WHERE F.country_surrogate=C.surrogate_key and F.living_conditions_surrogate=L.surrogate_key and F.date_surrogate=D.surrogate_key
and C.country_code in ('UKR','IRN','THA') and D.year_ in (2010,2011,2012,2013,2014)
GROUP BY (F.human_development_index,C.country_code, L.final_consumption_expenditure, D.year_)

-- d) Combining OLAP Operations (4 queries)
SELECT P.net_migration,C.country_code,D.month_,D.year_,D.decade
FROM fact_table as F, country as C, population_ as P, date_ as D
WHERE F.country_surrogate=C.surrogate_key and F.population_surrogate=P.surrogate_key and F.date_surrogate=D.surrogate_key
and C.country_code in ('CAN','MEX','USA')
GROUP BY (P.net_migration,C.country_code, D.month_,D.year_,D.decade)
ORDER BY D.month_,D.year_,D.decade

SELECT P.unemployment_rate,C.country_code,D.quarter,D.year_,D.decade
FROM fact_table as F, country as C, population_ as P, date_ as D
WHERE F.country_surrogate=C.surrogate_key and F.population_surrogate=P.surrogate_key and F.date_surrogate=D.surrogate_key
and C.country_code in ('UKR','IRN','THA')
GROUP BY (P.unemployment_rate,C.country_code,D.quarter,D.month_,D.year_,D.decade)
ORDER BY D.month_,D.year_,D.decade

--population compared to export_gdp, ordered by year and income index--
SELECT F.income_index, C.export_percent_gdp, D.year_,D.quarter,D.decade
FROM fact_table as F, country as C, date_ as D
WHERE F.country_surrogate=C.surrogate_key and F.date_surrogate=D.surrogate_key
and C.country_code in ('UKR','IRN','THA')
GROUP BY (F.income_index, C.export_percent_gdp, D.year_,D.quarter,D.decade)
ORDER BY D.year_,D.quarter,D.decade

--gdp growth compared to population growth, ordered by year and income index
SELECT F.income_index, C.gdp_growth, D.year_,D.quarter,D.decade
FROM fact_table as F, country as C, date_ as D
WHERE F.country_surrogate=C.surrogate_key and F.date_surrogate=D.surrogate_key
and C.country_code in ('CAN','MEX','USA')
GROUP BY (F.income_index, C.gdp_growth, D.year_,D.quarter,D.decade)
ORDER BY D.year_,D.quarter,D.decade


----- Part 2: Explorative Operations -----

-- a) Iceberg Query
SELECT  C.country_code,AVG(F.quality_of_life_index) as avg_quality_of_life_index
FROM country as C, date_ as D, fact_table as F
WHERE C.surrogate_key = F.country_surrogate AND D.surrogate_key = F.date_surrogate
AND D.decade = 2010
GROUP BY C.country_code
ORDER BY avg_quality_of_life_index DESC
LIMIT 3;

-- b) Windowing Query
SELECT Co.country_code, D.year_, E.enrollment_primary, avg(E.enrollment_primary)
OVER (PARTITION BY co.country_code ORDER BY D.year_)
FROM "CSI4142".fact_table as F, "CSI4142".education as E, "CSI4142".country as Co, "CSI4142".date_ as D
WHERE F.country_surrogate=Co.surrogate_key and F.education_surrogate=E.surrogate_key and F.date_surrogate=D.surrogate_key and D.year_>2015;

-- c) Using the Window clause
SELECT co.country_code, D.year_, E.enrollment_primary, avg(E.enrollment_primary) OVER W
FROM "CSI4142".fact_table as F, "CSI4142".education as E, "CSI4142".country as Co, "CSI4142".date_ as D
WHERE F.country_surrogate=co.surrogate_key and F.education_surrogate=E.surrogate_key and F.date_surrogate=D.surrogate_key
WINDOW W AS (PARTITION BY co.country_code 
			 ORDER BY D.year_);