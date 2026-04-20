#This script is to produce a bar graph showing the top 20 artists on spotify and their total streams
#Import libraries and dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3

#Open SQL database connection and extracting the necessary columns
with sqlite3.connect('song_lyrics.db') as connection:
    cursor = connection.cursor()
    streams_query = '''
    SELECT artist, total_streams, song, song_streams
    FROM song;
    '''

top_artists = pd.DataFrame((cursor.execute(streams_query)).fetchall())

#Want one column with artist and song name
top_artists['Artist and Song'] = top_artists[0] + ' - ' + top_artists[2]

#rename the columns to one word names to make them easier to use
top_artists.rename(columns= {1: 'total_streams', 3: 'song_streams'}, inplace = True)
top_artists.set_index('Artist and Song')

#Sort artists from lowest to highest streams
top_artists.sort_values('total_streams', ascending = True, inplace=True)

#make the bar graph with artist names on the y axis and total streams on the x axis
fig = plt.figure()
ax = fig.add_subplot()
ax2 = ax.twiny()
top_artists.total_streams.plot(kind = 'barh',color = '#5dde5b',ax = ax2, position = 0, width = 0.4)
top_artists.song_streams.plot(kind = 'barh', color = '#4c97d9', ax = ax, position = 1, width = 0.4)

#add labels, title, gridlines, legends, and set ticks
ax.set_xlabel('Top Song Streams (millions)', fontweight = 'bold', color = '#4c97d9')
ax2.set_xlabel('Total Streams (millions)', fontweight = 'bold', color = '#5dde5b')
plt.ylabel('Artist', fontweight = 'bold')

ax.set_yticks(ticks= range(0,10), labels= top_artists['Artist and Song'], minor=False)
ax2.set_xticks(np.arange(0,150000,10000))
ax.set_xticks(np.arange(0,7500, 500))

plt.title('Top 10 Spotify Artists and their Total Streams', color = 'black', fontsize = 14, fontweight = 'bold')
plt.grid(linestyle = '--', alpha = 0.5, axis = 'x')

plt.legend(handles = [ax2.patches[0], ax.patches[0]],labels = ['Total streams','Top Song Streams'],loc = 'lower right', fontsize = 'x-large')

#show graph
plt.show()