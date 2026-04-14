#Import necessary libraries
import numpy as np
import pandas as pd
import sqlite3

#import dataframe
main_dataset = pd.read_csv('Data_science_final_project/Datasets/Cleaned_datasets/cleaned_top_spotify_artists_lyrics.csv')

with sqlite3.connect('song_lyrics.db') as connection:
        cursor = connection.cursor()
        #make first table for artist and song and gender:
        empty_song_table_query = '''
        DROP TABLE IF EXISTS song;
        '''
        create_artist_table_query = '''
            CREATE TABLE IF NOT EXISTS song(
            song_id INTEGER PRIMARY KEY AUTOINCREMENT,
            artist TEXT NOT NULL,
            song TEXT NOT NULL,
            gender TEXT NOT NULL
            );
            '''
        cursor.execute(empty_song_table_query)
        cursor.execute(create_artist_table_query)

        #make second table for song lyrics, connecting each word to the id of the song they come from
        empty_lyrics_table_query = '''
        DROP TABLE IF EXISTS lyrics;
        '''
        create_lyrics_table_query = '''
            CREATE TABLE IF NOT EXISTS lyrics(
            song_id INTEGER NOT NULL,
            word TEXT NOT NULL,
            frequency INTEGER NOT NULL,
            FOREIGN KEY (song_id) REFERENCES song(song_id)
            );
            '''
        cursor.execute(empty_lyrics_table_query)
        cursor.execute(create_lyrics_table_query)
        #Commit changes
        connection.commit()

        count = 0
        for artist in main_dataset['Artist']:
            insert_artist_query = '''
            INSERT INTO song(artist, song, gender)
            VALUES(?,?,?)''' 
            data = (artist, main_dataset['Top Song'][count], main_dataset['Gender'][count])
            count += 1
            cursor.execute(insert_artist_query, data)
        connection.commit()
        print('succesful')