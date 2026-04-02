#Import relevant libraries and dataset from datasets folder
import pandas as pd
import numpy as np
search_trends = pd.read_csv('./Data_science_final_project/Datasets/search_trends.csv')
#Check info and print head
print(search_trends.info())
print(search_trends.head())
#data is already limited to last 5 years. Remove empty rows and columns just incase and switch date to datatime format
search_trends.dropna(inplace=True)
search_trends['Time'] = pd.to_datetime(search_trends['Time'], errors='coerce')
print(search_trends.info())
#save cleaned dataset to new csv file
search_trends.to_csv('./Data_science_final_project/Datasets/cleaned_search_trends.csv', index=False)