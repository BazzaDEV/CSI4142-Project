import numpy as np
import pandas as pd
import array

def getDataPoint(rows,year,attribute):
    return rows[np.where(rows[:,2]==attribute)][:,year-2001][0]

#Loading all data
countryData = pd.read_csv("C:/Users/david/OneDrive/Documents/2022 Winter/Data Science/Deliverable 2/Data/Country_Data.csv").values
educationData = pd.read_csv("C:/Users/david/OneDrive/Documents/2022 Winter/Data Science/Deliverable 2/Data/education.csv").values
healthData = pd.read_csv("C:/Users/david/OneDrive/Documents/2022 Winter/Data Science/Deliverable 2/Data/Health_Data.csv").values
livingConditionData = pd.read_csv("C:/Users/david/OneDrive/Documents/2022 Winter/Data Science/Deliverable 2/Data/living condition.csv").values
popData = pd.read_csv("C:/Users/david/OneDrive/Documents/2022 Winter/Data Science/Deliverable 2/Data/Population_Data.csv").values

countries = np.unique(educationData[:,1])

#sorting by country
countryData = countryData[countryData[:,3].argsort()]
educationData = educationData[educationData[:,3].argsort()]
healthData = healthData[healthData[:,3].argsort()]
livingConditionData = livingConditionData[livingConditionData[:,3].argsort()]
popData = popData[popData[:,3].argsort()]

hDIndex = pd.read_csv("C:/Users/david/OneDrive/Documents/2022 Winter/Data Science/Deliverable 2/Data/HDI.csv", encoding = "ISO-8859-1")
incomeIndex = pd.read_csv("C:/Users/david/OneDrive/Documents/2022 Winter/Data Science/Deliverable 2/Data/Income index.csv", encoding = "ISO-8859-1")
educationIndex = pd.read_csv("C:/Users/david/OneDrive/Documents/2022 Winter/Data Science/Deliverable 2/Data/Education Index.csv", encoding = "ISO-8859-1")


#Target Tables
factTable = [[]]
dateTable = [[]]
countryTable = [[]]
livingConditionTable = [[]]
healthTable = [[]]
educationTable = [[]]
populationTable = [[]]
eventsTable = [[]]

#surrogateKeys
dateSK = 0
countrySK = 0
educationSK = 0


for year in range(2005,2021):
    dateSK+=1
    dateTable+=[[dateSK,1,"",year,year-year%10]]


    for country in countries:
        
        #country
        countrySK+=1
        rows = countryData[np.where(countryData[:,1]==country)]
        countryTable+=[
                        [countrySK,
                        getDataPoint(rows,year,"Access to electricity (% of population)"),
                        getDataPoint(rows,year,"Land area (sq. km)"),
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
        pass