#This script will create a dataframe for the top 20 artists on spotify. This will include their name, total streams, gender, and top song
#import libraries and dataset
from  bs4 import BeautifulSoup
from matplotlib import artist
import requests as req
import re as re
import pandas as pd
import numpy as np
base_dataset = pd.read_csv('./Data_science_final_project/Datasets/Cleaned_datasets/cleaned_top_spotify_artists.csv')

#webscrape to get the top song for each artist
#set up website
url = 'https://kworb.net/spotify/songs.html#google_vignette'

#from url, we want to get the first song that come up for each artist in our dataset.
#Get the html of the page and find the relevant table
response = req.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
#need to loop through the artists in our dataset and find just the first song that comes up for each of them and add it to list of top songs
top_song = []

for person in base_dataset['Artist']:
    for string in soup.find_all('td', class_='text'):
        if person in string.text:
            top_song.append((string).text)
            break
        else:
            continue

# We only want the song name so we need to remove the artist name and ' - ' from the string.
for i in range(len(top_song)):
    song = top_song[i]
    for person in base_dataset['Artist']:
        if person in song:
            song = song.replace(person, '')
            song = song.replace(' - ', '')
            top_song[i] = song

            break
        else:
            continue

#Add the song to a new column in the base_dataset. to do this we first need to make a new column to the dataframe
base_dataset['Top song'] = top_song

#We also want to get the corresponding streams for each of these songs
#we need to get the context of the webpage in text and then split it into lines. go through each line and for the first time each artists comes up take that song
streams = soup.text
streams = streams.splitlines()
song_streams = []
for person in base_dataset['Artist']:
    for line in streams:
        if person in line:
            song_streams.append(line)
            break
        else:
            continue

#We want to loop through song_streams and remove all non-digit characters
streams = []
for line in song_streams:
    streams.append(re.sub(r'\D','',line))

#we need these streams to be in millions.
#transform from string to float
streams_millions = []
for number in streams:
    number = float(number)
    number = number/1000000
    streams_millions.append(number)
#print(streams_millions)
print(song_streams)

table = soup.find('table', class_='addpos sortable')
print(table)
#save the dataset as cleaned_top_spotify_artist_song
base_dataset.to_csv('./Data_science_final_project/Datasets/Cleaned_datasets/cleaned_top_spotify_artists_song.csv')

