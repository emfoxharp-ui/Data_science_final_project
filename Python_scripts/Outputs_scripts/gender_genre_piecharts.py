#Script for making pie charts showing gender and genre splits within the top 10 artists
#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

#Open Sqlite3 connection
with sqlite3.connect('song_lyrics.db') as connection:
    cursor = connection.cursor()

    #start with making the gender dataframe
    select_gender_query = '''
    SELECT gender
    FROM song;
    '''
    #make dataframe from query
    gender_df = pd.DataFrame(cursor.execute(select_gender_query))
    #add count where each row is 1 and then group by gender and sum the frequency of count
    gender_df['count'] = 1
    gender_df = gender_df.groupby(0, as_index = False).sum()
            
    #make the genre dataframe (repeating process from gender for genre)
    select_genre_query = '''
    SELECT genre
    FROM song;
    '''

    #make query data into dataframe
    genre_df = pd.DataFrame(cursor.execute(select_genre_query))
    #add a count to each row where it is 1 and group by genre, summing the frequency of count
    genre_df['count'] = 1
    genre_df = genre_df.groupby(0, as_index = False).sum()


    #split figure into two axis in order to display both pie charts on same graph

    fig, axs = plt.subplots(1,2)

    #add pie charts and titles. Include percentage and labels, setting colors to match the other outputs.
    axs[0].pie(gender_df['count'], labels = gender_df[0], autopct='%1.1f%%', colors = ['#e067a2','#4c97d9'])
    axs[0].set_title('Artists by Gender', fontweight = 'bold')
    axs[1].pie(genre_df['count'], labels = genre_df[0], autopct='%1.1f%%', colors = ['#4c97d9','#e067a2','#5dde5b'])
    axs[1].set_title('Artists by Genre', fontweight = 'bold')

    plt.show()


