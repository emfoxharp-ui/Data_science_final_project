#Making a scatter graph comparing the total word count and unique word count of each song
#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

#Open connection to database

with sqlite3.connect('song_lyrics.db') as connection:
    cursor = connection.cursor()
    #Select columns from lyrics table
    word_count_query = '''
    SELECT *
    FROM lyrics;
    '''
    cursor.execute(word_count_query)
    #add these columns into a dataframe so we can use python libraries on it
    df_lyrics = pd.DataFrame((cursor.execute(word_count_query)).fetchall())
    print(df_lyrics.info())
    #group by song by grouping by the foreign id (row 0)
    df_lyrics.groupby(0)
    print(df_lyrics)
    #for each song, get the total word count, unique word count, and artist name
    unique_count_query = '''
    '''