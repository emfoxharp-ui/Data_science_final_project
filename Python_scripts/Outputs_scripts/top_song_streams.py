#This script is to produce a bar graph showing the top 20 artists on spotify and their total streams
#Import libraries and dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
top_artists = pd.read_csv('./Data_science_final_project/Datasets/Cleaned_datasets/cleaned_top_spotify_artists.csv')
#Need to know column names to make graph
print(top_artists.info())

#Sort artists from lowest to highest streams
top_artists.sort_values(by = 'Song Streams (millions)', ascending = True, inplace=True)
print(top_artists)
#make the bar graph with artist names on the y axis and total streams on the x axis

#y axis needs to have the name of both the artist and song:
song_artist = []
count = 0
for row in top_artists['Artist']:
    print(row)
    song_artist.append(top_artists['Top Song'].iloc[count] + ' - ' + top_artists['Artist'].iloc[count])
    count += 1

print(song_artist)
plt.figure()
plt.barh(song_artist, top_artists['Song Streams (millions)'], color = 'green')
#add labels, title and gridlines
plt.xlabel('Streams (millions)', fontweight = 'bold')
plt.ylabel('Artist and song', fontweight = 'bold')
plt.title('Top 10 Spotify Artists and their Total Streams', color = 'black', fontsize = 14, fontweight = 'bold')
plt.grid(linestyle = '--', alpha = 0.5, axis = 'x')
plt.yticks(song_artist)
#manual adjestment of graph once it was created was done so the y label and ticks werent cut off

plt.show()