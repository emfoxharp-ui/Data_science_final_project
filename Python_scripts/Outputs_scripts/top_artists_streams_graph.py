#This script is to produce a bar graph showing the top 20 artists on spotify and their total streams
#Import libraries and dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
top_artists = pd.read_csv('./Data_science_final_project/Datasets/Cleaned_datasets/cleaned_top_spotify_artists.csv')
#Need to know column names to make graph
print(top_artists.info())

#Sort artists from lowest to highest streams
top_artists.sort_values('Streams (millions)', ascending = True, inplace=True)
#make the bar graph with artist names on the y axis and total streams on the x axis
plt.figure()
plt.barh(top_artists['Artist'], top_artists['Streams (millions)'], color = 'lightgreen')
#add labels, title and gridlines
plt.xlabel('Total Streams (millions)', fontweight = 'bold')
plt.ylabel('Artist', fontweight = 'bold')
plt.title('Top 10 Spotify Artists and their Total Streams', color = 'black', fontsize = 14, fontweight = 'bold')
plt.grid(linestyle = '--', alpha = 0.5, axis = 'x')
plt.xticks(np.arange(0,140000,10000))

plt.show()