import numpy as np
import pandas as pd
import os

from telegram import PassportElementErrorDataField

dir = os.path.dirname(__file__)

countryCodes={"CAF":" Central African Republic", "CAN":" Canada", "USA":" United States", "MEX":" Mexico","IRN":" Iran (Islamic Republic of)", "UKR":" Ukraine", "MLI":" Mali","THA":" Thailand", "TCD":" Chad"}

def getDataPoint(rows,year,attribute):
    return rows[np.where(rows[:,2]==attribute)][:,year-2001][0]

def getIndexPoint(sheet,year,country):
    row = sheet[np.where(sheet[:,1]==countryCodes[country])][0]
    return row[(year-1990)*2+2]

def getEvents(country, year, events): 
    events = (events[np.where(events[:,4]==country)])
    return events[np.where(events[:,5]==year)]


#Loading all data
countryData = pd.read_csv(dir + "/data/country.csv").values
educationData = pd.read_csv(dir + "/data/education.csv").values
healthData = pd.read_csv(dir + "/data/health.csv").values
livingConditionData = pd.read_csv(dir + "/data/living_conditions.csv").values
populationData = pd.read_csv(dir + "/data/population.csv").values
eventData = pd.read_csv(dir + "/data/events.csv",  encoding = "ISO-8859-1").values

countries = np.unique(educationData[:,1])

#sorting by country
countryData = countryData[countryData[:,3].argsort()]
educationData = educationData[educationData[:,3].argsort()]
healthData = healthData[healthData[:,3].argsort()]
livingConditionData = livingConditionData[livingConditionData[:,3].argsort()]
populationData = populationData[populationData[:,3].argsort()]

hDIndex = pd.read_csv(dir + "/data/human_development_index.csv", encoding = "ISO-8859-1").values
incomeIndex = pd.read_csv(dir + "/data/income_index.csv", encoding = "ISO-8859-1").values
educationIndex = pd.read_csv(dir + "/data/education_index.csv", encoding = "ISO-8859-1").values

#Target Tables
factTable = [[]]
dateTable = [[]]
countryTable = [[]]
livingConditionTable = [[]]
healthTable = [[]]
educationTable = [[]]
populationTable = [[]]
eventsTable = [[
    0,
    "Null Event",
    None,
    None,
    None,
    None,
    None
]]

#surrogateKeys
dateSK = 0
countrySK = 0
educationSK = 0
healthSK = 0
livingConditionSK = 0
populationSK = 0
eventSK = 0


for year in range(2005,2021):
    dateSK+=1
    dateTable+=[[dateSK,1,"",year,year-year%10]]

    for country in countries:

        #country
        countrySK+=1
        rows = countryData[np.where(countryData[:,1]==country)]
        countryTable+=[
                        [countrySK,
                        country,
                        getDataPoint(rows,year,"Land area (sq. km)"),
                        getDataPoint(rows,year,"Access to electricity (% of population)"),
                        getDataPoint(rows,year,"Exports of goods and services (% of GDP)"),
                        getDataPoint(rows,year,"Imports of goods and services (% of GDP)"),
                        getDataPoint(rows,year,"Mobile cellular subscriptions (per 100 people)"),
                        getDataPoint(rows,year,"Population, total"),
                        getDataPoint(rows,year,"Population growth (annual %)"),
                        getDataPoint(rows,year,"Forest area (sq. km)"),
                        getDataPoint(rows,year,"GDP growth (annual %)"),
                        getDataPoint(rows,year,"GDP (current US$)"),
                        getDataPoint(rows,year,"GDP (constant 2015 US$)"),
                        getDataPoint(rows,year,"CO2 emissions (kt)"),
                        getDataPoint(rows,year,"CO2 emissions (metric tons per capita)"),
                        ]
        ]
        
        #education
        educationSK+=1
        rows = educationData[np.where(educationData[:,1]==country)]
        educationTable+=[
                        [educationSK,
                        getDataPoint(rows,year,"School enrollment, primary (% gross)"),
                        getDataPoint(rows,year,"School enrollment, secondary (% gross)"),
                        getDataPoint(rows,year,"School enrollment, tertiary (% gross)"),
                        getDataPoint(rows,year,"Literacy rate, adult total (% of people ages 15 and above)"),
                        getDataPoint(rows,year,"Literacy rate, youth total (% of people ages 15-24)"),
                        getDataPoint(rows,year,"Compulsory education, duration (years)"),
                        getDataPoint(rows,year,"Current education expenditure, total (% of total expenditure in public institutions)"),
                        getDataPoint(rows,year,"Educational attainment, at least Bachelor's or equivalent, population 25+, total (%) (cumulative)"),
                        getDataPoint(rows,year,"Educational attainment, at least completed post-secondary, population 25+, total (%) (cumulative)"),
                        getDataPoint(rows,year,"Educational attainment, at least completed primary, population 25+ years, total (%) (cumulative)"),
                        getDataPoint(rows,year,"Educational attainment, at least completed short-cycle tertiary, population 25+, total (%) (cumulative)"),
                        getDataPoint(rows,year,"Educational attainment, at least completed upper secondary, population 25+, total (%) (cumulative)"),
                        getDataPoint(rows,year,"Educational attainment, at least Master's or equivalent, population 25+, total (%) (cumulative)"),
                        getDataPoint(rows,year,"Educational attainment, Doctoral or equivalent, population 25+, total (%) (cumulative)"),
                        getDataPoint(rows,year,"Expenditure on primary education (% of government expenditure on education)"),
                        getDataPoint(rows,year,"Expenditure on secondary education (% of government expenditure on education)"),
                        getDataPoint(rows,year,"Expenditure on tertiary education (% of government expenditure on education)"),
                        getDataPoint(rows,year,"Government expenditure on education, total (% of GDP)")
                        ]
        ]

        #health
        healthSK+=1
        rows = healthData[np.where(healthData[:,1]==country)]
        healthTable+=[
                        [healthSK,
                        getDataPoint(rows,year,"Birth rate, crude (per 1,000 people)"),
                        getDataPoint(rows,year,"Capital health expenditure (% of GDP)"),
                        getDataPoint(rows,year,"Cause of death, by injury (% of total)"),
                        getDataPoint(rows,year,"Death rate, crude (per 1,000 people)"),
                        getDataPoint(rows,year,"Maternal mortality ratio (modeled estimate, per 100,000 live births)"),
                        getDataPoint(rows,year,"Mortality rate attributed to household and ambient air pollution (per 100,000 population)"),
                        getDataPoint(rows,year,"Number of maternal deaths"),
                        getDataPoint(rows,year,"Number of under-five deaths"),
                        getDataPoint(rows,year,"Physicians (per 1,000 people)"),
                        getDataPoint(rows,year,"Nurses and midwives (per 1,000 people)"),
                        getDataPoint(rows,year,"Hospital beds (per 1,000 people)"),
                        getDataPoint(rows,year,"Number of surgical procedures (per 100,000 population)"),
                        getDataPoint(rows,year,"Prevalence of overweight, female (% of female adults)"),
                        getDataPoint(rows,year,"Prevalence of overweight, male (% of male adults)"),
                        getDataPoint(rows,year,"Prevalence of current tobacco use, females (% of female adults)"),
                        getDataPoint(rows,year,"Prevalence of current tobacco use, males (% of male adults)"),
                        getDataPoint(rows,year,"Prevalence of hypertension, female (% of female adults ages 30-79)"),
                        getDataPoint(rows,year,"Prevalence of hypertension, male (% of male adults ages 30-79)")
                        ]
        ]

        #livingCondition
        livingConditionSK+=1
        rows = livingConditionData[np.where(livingConditionData[:,1]==country)]
        livingConditionTable+=[
                        [livingConditionSK,
                        getDataPoint(rows,year,"Access to electricity (% of population)"),
                        getDataPoint(rows,year,"Coverage of social insurance programs (% of population)"),
                        getDataPoint(rows,year,"Coverage of social protection and labor programs (% of population)"),
                        getDataPoint(rows,year,"Coverage of social safety net programs (% of population)"),
                        getDataPoint(rows,year,"Coverage of unemployment benefits and ALMP (% of population)"),
                        getDataPoint(rows,year,"Current health expenditure (% of GDP)"),
                        getDataPoint(rows,year,"Access to clean fuels and technologies for cooking (% of population)"),
                        getDataPoint(rows,year,"Final consumption expenditure (% of GDP)"),
                        getDataPoint(rows,year,"Fossil fuel energy consumption (% of total)"),
                        getDataPoint(rows,year,"Hospital beds (per 1,000 people)"),
                        getDataPoint(rows,year,"Households and NPISHs final consumption expenditure (% of GDP)"),
                        getDataPoint(rows,year,"Investment in water and sanitation with private participation (current US$)"),
                        getDataPoint(rows,year,"Investment in transport with private participation (current US$)"),
                        getDataPoint(rows,year,"People using at least basic drinking water services (% of population)"),
                        getDataPoint(rows,year,"People using at least basic sanitation services (% of population)"),
                        getDataPoint(rows,year,"People with basic handwashing facilities including soap and water (% of population)")
                        ]
        ]

        #population
        populationSK+=1
        rows = populationData[np.where(populationData[:,1]==country)]
        populationTable+=[
                        [populationSK,
                        getDataPoint(rows,year,"Life expectancy at birth, female (years)"),
                        getDataPoint(rows,year,"Life expectancy at birth, male (years)"),
                        getDataPoint(rows,year,"Life expectancy at birth, total (years)"),
                        getDataPoint(rows,year,"Net migration"),
                        getDataPoint(rows,year,"Urban population (% of total population)"),
                        getDataPoint(rows,year,"Urban population growth (annual %)"),
                        getDataPoint(rows,year,"Urban poverty headcount ratio at national poverty lines (% of urban population)"),
                        getDataPoint(rows,year,"Rural population (% of total population)"),
                        getDataPoint(rows,year,"Rural population growth (annual %)"),
                        getDataPoint(rows,year,"Rural poverty headcount ratio at national poverty lines (% of rural population)"),
                        getDataPoint(rows,year,"Labor force, female (% of total labor force)"),
                        getDataPoint(rows,year,"Labor force, total"),
                        getDataPoint(rows,year,"Unemployment, total (% of total labor force)"),
                        getDataPoint(rows,year,"Unemployment, female (% of female labor force)"),
                        getDataPoint(rows,year,"Unemployment, male (% of male labor force)")
                        ]
        ]
        
        events = getEvents(country,year,eventData)

        if len(events)==0:
            events=[eventsTable[0]]
            flag=False
        else: flag=True

        for event in events:
            
            if(flag):
                #eventsTable
                eventSK+=1
                eventsTable+=[event]

            #factTable
            factTable+=[[
                countrySK,
                dateSK,
                populationSK,
                livingConditionSK,
                educationSK,
                healthSK,
                eventSK,
                getIndexPoint(hDIndex,year,country),
                getIndexPoint(educationIndex,year,country),
                getIndexPoint(incomeIndex,year,country)
            ]]

############all 8 tables need to be output to csv here#################

