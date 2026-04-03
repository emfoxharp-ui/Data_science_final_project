#This script will create a dataframe for the top 20 artists on spotify. This will include their name, total streams, gender, and top song
#import libraries and dataset
from  bs4 import BeautifulSoup
import requests as req
import pandas as pd
import numpy as np
base_dataset = pd.read_csv('./Data_science_final_project/Datasets/Cleaned_datasets/cleaned_top_spotify_artists.csv')

#webscrape to get the top song for each artist
#set up website
url = 'https://kworb.net/spotify/songs.html#google_vignette'

print(base_dataset['Artist'])

#from url, we want to get the first song that come up for each artist in our dataset.
#Get the html of the page and find the relevant table
response = req.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
#need to loop through the artists in our dataset and find just the first song that comes up for each of them and add it to list of top songs
top_song = []
for artist in base_dataset['Artist']:
    top_song.append(soup.find_all('table', string='Warren G - Regulate', class_='text'))

print(top_song)

