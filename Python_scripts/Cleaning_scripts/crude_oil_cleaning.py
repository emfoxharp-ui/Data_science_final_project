# Import libraries and dataset from datasets folder
import numpy as np
import pandas as pd
crude_oil = pd.read_csv('./Data_science_final_project/Datasets/Original_datasets/crude_oil_data.csv')
#Check info and print head
print(crude_oil.info())
print(crude_oil.head())
print(crude_oil.shape)
#remove empty rows and columns
crude_oil.dropna(inplace=True)
#the dates are saved as strings, we need in datetime format
crude_oil['Date'] = pd.to_datetime(crude_oil['Date'], errors='coerce')
#check most recent date available
print(crude_oil.tail())
#limit data to the last 5 years (2021-2026)
crude_oil = crude_oil[crude_oil['Date'] >= '2021-01-01']
print(crude_oil)
print(crude_oil.shape)
#save cleaned dataset to new csv file
crude_oil.to_csv('./Data_science_final_project/Datasets/Cleaned_datasets/cleaned_crude_oil_data.csv', index=False)