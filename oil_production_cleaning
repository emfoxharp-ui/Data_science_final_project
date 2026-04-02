#Import libraries and dataset
import pandas as pd
import numpy as np
production = pd.read_csv('oil-production-by-country.csv')
print(production.head())
#Remove empty rows and columns
production.dropna(inplace=True)
#Remove rows the entity is not a country
non_countries = ['World', 'High-income countries', 'Low-income countries', 'Lower-middle-income countries', 'Upper-middle-income countries', 'Europe', 'Asia', 'Africa', 'South America', 'North America', 'Oceania']
production = production[~production['Entity'].isin(non_countries)]
print(production.info())
#remove code column
production = production.drop(columns=['Code'])
#Limit to data from 2021 to 2024
production = production[production['Year'] >= 2021]
#average the oil production for each country across the year
production = production.groupby('Entity')
production = production['Oil'].mean().reset_index()
#sort by highest oil production
production = production.sort_values(by = 'Oil',ascending=False)
print(production)
#Save cleaned dataset to new csv file
production.to_csv('cleaned_oil_production_by_country.csv', index=False)
