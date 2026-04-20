#Import necessary libraries
import numpy as np
import pandas as pd
import sqlite3

#open database connection
with sqlite3.connect('song_lyrics.db') as connection:
        cursor = connection.cursor()
        
        #make first table for artist and song and gender:
        #run empty table query first to ensure there isnt duplicated data.
        empty_song_table_query = '''
        DROP TABLE IF EXISTS song;
        '''
        #create table with song id as primary key, artist, total streams, song name, song streams, gender, genre
        create_artist_table_query = '''
            CREATE TABLE IF NOT EXISTS song(
            song_id INTEGER PRIMARY KEY AUTOINCREMENT,
            artist TEXT NOT NULL,
            total_streams INTEGER NOT NULL,
            song TEXT NOT NULL,
            song_streams INTEGER NOT NULL,
            gender TEXT NOT NULL,
            genre TEXT NOT NULL
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
        
        #Commit changes and print successful once everything has been able to run
        connection.commit()
        print('successful')