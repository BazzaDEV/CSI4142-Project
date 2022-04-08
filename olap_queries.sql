----- Part 1: Standard OLAP Operations -----

-- a) Drill Down, Roll Up (2 queries)
SELECT  C.country_code
       ,D.year
       ,F.quality_of_life_index
       ,F.human_development_index
       ,F.education_index
FROM country C, date_ D, fact_table F
WHERE C.surrogate_key = F.country_surrogate
AND D.surrogate_key = F.date_surrogate
GROUP BY  C.country_code, D.year;

SELECT  C.country_code
       ,AVG(F.education_index)
       ,SUM(P.current_education_expenditure)
FROM country C, population_ P date_ D, fact_table F
WHERE C.surrogate_key = F.country_surrogate
AND P.surrogate_key = F.population_surrogate
AND D.surrogate_key = F.date_surrogate
GROUP BY C.country_code;

-- b) Slice (1 query)
SELECT  C.country_code
       ,F.quality_of_life_index
       ,F.human_development_index
       ,F.education_index
FROM country C, date_ D, fact_table F
WHERE C.surrogate_key = F.country_surrogate
AND D.surrogate_key = F.date_surrogate
AND D.year_ = 2000;

-- c) Dice (2 queries)

-- d) Combining OLAP Operations (4 queries)



----- Part 2: Explorative Operations -----

-- a) Iceberg Query
SELECT  C.country_code
       ,AVG(F.quality_of_life_index) as quality_of_life_index
FROM country C, date_ D, fact_table F
WHERE C.surrogate_key = F.country_surrogate
AND D.surrogate_key = F.date_surrogate
AND D.decade = 2010
ORDER BY quality_of_life_index DESC
OPTIMIZE FOR 3 ROWS;

-- b) Windowing Query

-- c) Using the Window clause