#Prominence of love as a theme in these songs
#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

#Open connection to database
with sqlite3.connect('song_lyrics.db') as connection:
    cursor = connection.cursor()
    #query to select words 'love', 'baby'
    select_words_query = '''
    SELECT word,frequency, genre, artist
    FROM lyrics l, song s
    WHERE (word = 'love' or word = 'baby') AND l.song_id = s.song_id'''

    love_df = pd.DataFrame(cursor.execute(select_words_query).fetchall(), columns = ['word', 'frequency', 'genre', 'artist'])
    #Make bar charts for each genre showing the frequenct for 'love' and 'baby' for each artist and an average across the genre
    #each genre on its own subplot. Stacked bar chart.
    fig, axs = plt.subplots(1,3)
    count = 0
    #Want a chart for each genre, so loop through genres
    for genre in love_df['genre'].unique():
        genre_love_df = love_df[love_df['genre'] == genre].reset_index(drop = True)
        ax = fig.add_subplot(axs[count])
        #need a frequency for every artist for every word so if word doesnt exist for artist frequency needs to be 0
        add_zeros = pd.DataFrame(columns = ['word','frequency','genre','artist'])
        for artist in genre_love_df['artist'].unique():
            for word in ['love','baby']:
                print(word)
                print(str(genre_love_df['word'][genre_love_df['artist'] == artist]))
                if word not in str(genre_love_df['word'][genre_love_df['artist'] == artist]):
                    add_zeros = pd.concat([add_zeros,pd.DataFrame({'word': word,'frequency': 0, 'genre': genre, 'artist': artist}, index = [len(add_zeros)])]).reset_index(drop = True)
                else:
                    continue
        genre_love_df = pd.concat([genre_love_df,add_zeros]).sort_values(by = ['artist','word']).reset_index(drop = True)

        #add average across genre
        genre_df = genre_love_df[['genre','word','frequency']].groupby(['genre','word'], as_index = False).mean()
        genre_df['artist'] = 'average'
        genre_love_df = pd.concat([genre_love_df, genre_df]).sort_values(by = ['artist','word']).reset_index(drop = True)
        print(genre_love_df)
        #dictionary of lyric and frequencies
        lyrics = {
            'love': np.array(genre_love_df['frequency'][genre_love_df['word'] == 'love']),
            'baby': np.array(genre_love_df['frequency'][genre_love_df['word'] == 'baby'])
        }
        print(lyrics.items())
        print(genre_love_df['artist'].unique())
        
        #make stacked bar graphs
        bottom = 0
        for boolean, frequency in lyrics.items():
            print('frequency; ', frequency)
            axs[count] = ax.bar(genre_love_df['artist'].unique(), frequency, width = 0.5, label = boolean, bottom = bottom, color = '#5dde5b' if boolean == 'love' else '#4c97d9')
            bottom += frequency
        
        #Format graph
        ax.set_title(genre, fontsize = 14, fontweight = 'bold')
        ax.set_yticks(np.arange(0,31,5))
        ax.minorticks_on()
        ax.set_ylabel('Frequency', fontweight = 'bold')
        ax.set_xlabel('Artist', fontweight = 'bold')
        ax.grid(linestyle = '--', alpha = 0.5, axis = 'y')
        ax.set_xticklabels(labels = genre_love_df['artist'].unique(),rotation = 'vertical')
        ax.legend()
        count += 1

plt.show()