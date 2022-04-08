
'''1d'''

'''2b'''
SELECT co.country_code, D.year_, E.enrollment_primary, avg(E.enrollment_primary)
OVER (PARTITION BY co.country_code ORDER BY D.year_)
FROM "CSI4142".fact_table as F, "CSI4142".education as E, "CSI4142".country as Co, "CSI4142".date_ as D
WHERE F.country_surrogate=co.surrogate_key and F.education_surrogate=E.surrogate_key and F.date_surrogate=D.surrogate_key and D.year_>2015;

'''2c'''
SELECT co.country_code, D.year_, E.enrollment_primary, avg(E.enrollment_primary) OVER W
FROM "CSI4142".fact_table as F, "CSI4142".education as E, "CSI4142".country as Co, "CSI4142".date_ as D
WHERE F.country_surrogate=co.surrogate_key and F.education_surrogate=E.surrogate_key and F.date_surrogate=D.surrogate_key
WINDOW W AS (PARTITION BY co.country_code 
			 ORDER BY D.year_);