#This script is to produce a bar graph showing the top 20 artists on spotify and their total streams
#Import libraries and dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
top_artists = pd.read_csv('./Data_science_final_project/Datasets/Cleaned_datasets/cleaned_top_spotify_artists.csv')

#Want one column with artist and song name
top_artists['Artist and Song'] = top_artists['Artist'] + ' - ' + top_artists['Top Song']

#Limit dataframe to just song and artist, total streams, and song streams
top_artists = top_artists [['Artist and Song', 'Streams (millions)', 'Song Streams (millions)']]
#rename the columns to one word names to make them easier to use
top_artists.rename(columns= {'Streams (millions)': 'total_streams', 'Song Streams (millions)': 'song_streams'}, inplace = True)
top_artists.set_index('Artist and Song')

#Sort artists from lowest to highest streams
top_artists.sort_values('total_streams', ascending = True, inplace=True)

#make the bar graph with artist names on the y axis and total streams on the x axis
fig = plt.figure()
ax = fig.add_subplot()
ax2 = ax.twiny()
top_artists.total_streams.plot(kind = 'barh',color = 'lightgreen',ax = ax, position = 0, width = 0.4)
top_artists.song_streams.plot(kind = 'barh', color = 'green', ax = ax2, position = 1, width = 0.4)

#add labels, title, gridlines, legends, and set ticks
ax.set_xlabel('Top Song Streams (10 millions)', fontweight = 'bold')
ax2.set_xlabel('Total Streams (millions)', fontweight = 'bold')
plt.ylabel('Artist', fontweight = 'bold')

ax.set_yticks(ticks= range(0,10), labels= top_artists['Artist and Song'], minor=False)
ax.set_xticks(np.arange(0,140000,10000))
ax2.set_xticks(np.arange(0,7000, 500))

plt.title('Top 10 Spotify Artists and their Total Streams', color = 'black', fontsize = 14, fontweight = 'bold')
plt.grid(linestyle = '--', alpha = 0.5, axis = 'x')

ax.legend(('Top Song',), loc = 'center right', fontsize = 'x-large')
ax2.legend(('Total Streams',),loc = 'lower right', fontsize = 'x-large')

#show graph
plt.show()