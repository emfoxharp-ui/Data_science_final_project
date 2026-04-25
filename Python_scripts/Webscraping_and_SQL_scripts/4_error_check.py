#If there is an error during webscraping, and the SQL database does not have the correct information, this script will check for that and replace the sql script with the back up so output scripts can still run properly
import sqlite3
import pandas as pd
import numpy as np


#get datasets from csv files
songs_df = pd.read_csv('Data_Science_final_project-main/SQL_backup/top_artists.csv')
lyrics_df = pd.read_csv('Data_Science_final_project-main/SQL_backup/lyrics.csv')

with sqlite3.connect('song_lyrics.db') as connection:
    cursor = connection.cursor()
    #The database should have 1582 entries in the lyrics table. if it doesnt, replace with the backup
    check_lyrics_query = '''
    SELECT COUNT(*)
    FROM lyrics;
    '''
count = cursor. execute(check_lyrics_query).fetchall()[0][0]
print(count)

#run if statement to check if webscraping successful and if not, 
if count == 1582:
    print('webscraping successful')
else:
    print('webscraping unsuccessful, replace with backup database')
    #replace with backup database
    #open connection to song_lyrics.db and replace tables with backup tables
    with sqlite3.connect('song_lyrics.db') as connection:
        cursor = connection.cursor()
        #empty existing tables
        delete_song_query = '''
        DELETE FROM song;
        '''
        delete_lyrics_query = '''
        DELETE FROM lyrics;
        '''
        cursor.execute(delete_song_query)
        cursor.execute(delete_lyrics_query)
        #add info from dataframes into tables
        #loop through rows in song dataframe and add info to song table
        for i in range(len(songs_df)):
            insert_song_query = '''
            INSERT INTO song(song_id, artist, total_streams, song, song_streams, gender, genre)
            VALUES(?,?,?,?,?,?,?)
            '''
            data = list(str(songs_df[songs_df.columns[j]][i]) for j in range(len(songs_df.columns)))
            cursor.execute(insert_song_query, data)
        
        #loop through rows in lyrics dataframe and add info to lyrics table
        for i in range(len(lyrics_df)):
            insert_lyrics_query = '''
            INSERT INTO lyrics(song_id, word, frequency)
            VALUES(?,?,?);
            '''
            data = list(str(lyrics_df[lyrics_df.columns[j]][i]) for j in range(len(lyrics_df.columns)))
            cursor.execute(insert_lyrics_query, data)
        print('successfully updated database')
#commit changes
connection.commit()


