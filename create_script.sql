CREATE TABLE IF NOT EXISTS "CSI4142".country
(
    country_id SERIAL PRIMARY KEY,
    surrogate_key INTEGER,
    country_name VARCHAR(255),
    land_area INTEGER,
    export_percent_gdp NUMERIC,
    continent VARCHAR(255),
    region VARCHAR(255),
    currency VARCHAR(255),
    cell_subscriptions NUMERIC,
    total_population INTEGER,
    population_growth NUMERIC,
    forest_area NUMERIC,
    gdp NUMERIC,
    co2_emissions NUMERIC
);

CREATE TABLE IF NOT EXISTS "CSI4142".date_
(
    date_id SERIAL PRIMARY KEY,
    surrogate_key INTEGER,
    quarter INTEGER,
    month_ VARCHAR(255),
    year_ INTEGER,
    decade INTEGER
);

CREATE TABLE IF NOT EXISTS "CSI4142".population_
(
    population_id SERIAL PRIMARY KEY,
    surrogate_key INTEGER,
    life_expectancy_female NUMERIC,
    life_expectancy_male NUMERIC,
    life_expectancy NUMERIC,
    net_migration NUMERIC,
    urban_population NUMERIC,
    urban_population_growth NUMERIC,
    urban_poverty_headcount_ratio NUMERIC,
    rural_population NUMERIC,
    rural_population_growth NUMERIC,
    rural_poverty_headcount_ratio NUMERIC,
    labor_force_female NUMERIC,
    labor_force_male NUMERIC GENERATED ALWAYS AS (100 - labor_force_female) STORED,
    labor_force_total NUMERIC,
    unemployment_rate NUMERIC,
    unemployment_rate_male NUMERIC,
    unemployment_rate_female NUMERIC
);

CREATE TABLE IF NOT EXISTS "CSI4142".living_conditions
(
    living_conditions_id SERIAL PRIMARY KEY,
    surrogate_key INTEGER,
    access_electricity NUMERIC,
    coverage_social_insurance_programs NUMERIC,
    coverage_social_protection_and_labor_programs NUMERIC,
    coverage_social_safety_net_programs NUMERIC,
    coverage_unemployment_benefits_ALMP NUMERIC,
    health_expenditure NUMERIC,
    access_to_fuels_for_cooking NUMERIC,
    final_consumption_expenditure NUMERIC,
    fossil_fuel_consumption NUMERIC,
    hospital_beds_per_1000 INTEGER,
    households_consumption_expenditure NUMERIC,
    investment_water_and_sanitation NUMERIC,
    investment_transport NUMERIC,
    people_using_basic_drinking_water_services NUMERIC,
    people_using_basic_sanitation_services NUMERIC,
    people_with_basic_handwashing_facilities NUMERIC
);

CREATE TABLE IF NOT EXISTS "CSI4142".education
(
    education_id SERIAL PRIMARY KEY,
    surrogate_key INTEGER,
    enrollment_primary NUMERIC,
    enrollment_secondary NUMERIC,
    enrollment_tertiary NUMERIC,
    completed_primary NUMERIC,
    literacy_rate NUMERIC,
    compulsory_education_years INTEGER,
    current_education_expenditure NUMERIC,
    educational_attainment_at_least_bachelor NUMERIC,
    educational_attainment_at_least_completed_lower_secondary NUMERIC,
    educational_attainment_at_least_completed_post_secondary NUMERIC,
    educational_attainment_at_least_completed_primary NUMERIC,
    educational_attainment_at_least_completed_short_cycle_tertiary NUMERIC,
    educational_attainment_at_least_completed_upper_secondary NUMERIC,
    educational_attainment_at_least_master NUMERIC,
    educational_attainment_doctoral NUMERIC,
    expenditure_on_primary_education NUMERIC,
    expenditure_on_secondary_education NUMERIC,
    expenditure_on_tertiary_education NUMERIC,
    government_expenditure_on_education NUMERIC,
    government_expenditure_per_student_primary NUMERIC,
    government_expenditure_per_student_secondary NUMERIC,
    government_expenditre_per_student_tertiary NUMERIC,
    over_age_students_primary NUMERIC
);

CREATE TABLE IF NOT EXISTS "CSI4142".health
(
    health_id SERIAL PRIMARY KEY,
    surrogate_key INTEGER,
    birthr_rate NUMERIC,
    capital_Health_expenditure NUMERIC,
    cause_of_death_non_communicable_injury NUMERIC,
    death_rate NUMERIC,
    maternal_mortality_ratio NUMERIC,
    mortality_air_pollution NUMERIC,
    maternal_deaths NUMERIC,
    under_five_deaths NUMERIC,
    physicians_per_1000 NUMERIC,
    nurses_and_midwives_per_1000 NUMERIC,
    hospital_beds_per_1000 NUMERIC,
    number_surgical_procedures_per_100000 NUMERIC,
    prevalence_of_overweight_female NUMERIC,
    prevalence_of_overweight_male NUMERIC,
    prevalence_of_current_tobacco_use_male  NUMERIC,
    prevalence_of_current_tobacco_use_female NUMERIC,
    prevalence_of_hypertension_female  NUMERIC,
    prevalence_of_hypertension NUMERIC
);

CREATE TABLE IF NOT EXISTS "CSI4142".event_
(
    event_id SERIAL PRIMARY KEY,
    surrogate_key INTEGER,
    event_name VARCHAR(255),
    event_category VARCHAR(255),
    date_start DATE,
    date_end DATE,
    country_code VARCHAR(255),
    year_ INTEGER
);

CREATE TABLE IF NOT EXISTS "CSI4142".fact_table
(
    fact_table_id SERIAL PRIMARY KEY,
    date_surrogate INTEGER,
    country_surrogate INTEGER,
    population_surrogate INTEGER,
    living_conditions_surrogate INTEGER,
    education_surrogate INTEGER,
    health_surrogate INTEGER,
    event_surrogate INTEGER,
    quality_of_life_index NUMERIC,
    human_development_index NUMERIC,
    education_index NUMERIC,
    FOREIGN KEY(country_surrogate) 
    REFERENCES country(surrogate_key),
    FOREIGN KEY(date_surrogate)
    REFERENCES date_(surrogate_key),
    FOREIGN KEY(population_surrogate) 
    REFERENCES population_(surrogate_key),
    FOREIGN KEY(living_conditions_surrogate) 
    REFERENCES living_conditions(surrogate_key),
    FOREIGN KEY(education_surrogate) 
    REFERENCES education(surrogate_key),
    FOREIGN KEY(health_surrogate) 
    REFERENCES health(surrogate_key),
    FOREIGN KEY(event_surrogate) 
    REFERENCES event_(surrogate_key),
	CONSTRAINT fact_pkey PRIMARY KEY(country_surrogate,date_surrogate,population_surrogate,living_conditions_surrogate,education_surrogate,health_surrogate,event_surrogate)
)
