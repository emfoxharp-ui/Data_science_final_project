#ensure necessary libraries are installed in the command line using pip install
#import libraries and website url
from  bs4 import BeautifulSoup
import requests as req
import pandas as pd
import numpy as np
url = 'https://kworb.net/spotify/artists.html'
#from url, get the table of artists and their streams
table = pd.read_html(url)[0]
print(table.head(20))
print(table.info())

#clean data by removing empty rows and columns. Only need artist name and total streams so remove the rest of the columns
table.dropna(inplace=True)
top_artists = table[['Artist', 'Streams']]
#Rename streams columns to include that its in millions
top_artists.rename(columns={'Streams': 'Streams (millions)'}, inplace=True)
print(top_artists.head(25))
#save cleaned dataset to new csv file
#For analysis, we want only english speaking artists,so we need to remove Bad Bunny, BTS, J Balvin and Ozuna as their song lyrics arent always English
top_artists.drop(top_artists[top_artists['Artist'].isin(['Bad Bunny', 'BTS', 'J Balvin', 'Ozuna'])].index, inplace=True)
print(top_artists.head(20))
#Limit to just the top 20 artists
top_artists = top_artists.head(20)
print(top_artists.info())
print(top_artists)
top_artists.to_csv('./Data_science_final_project/Datasets/Cleaned_datasets/cleaned_top_spotify_artists.csv')




