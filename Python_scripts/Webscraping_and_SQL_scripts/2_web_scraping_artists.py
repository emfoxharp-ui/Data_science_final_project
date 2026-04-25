#web-scraping for artists, their top song, and the streams for each.
#ensure necessary libraries are installed in the command line using pip install
#import libraries and website url
import pandas as pd
import numpy as np
import re
import sqlite3
url = 'https://kworb.net/spotify/artists.html'
#from url, get the table of artists and their streams
#as we are reading a table, can use pandas instead of beautiful soup
table = pd.read_html(url)[0]

#clean data by removing empty rows and columns. Only need artist name and total streams so remove the rest of the columns
table.dropna(inplace=True)
top_artists = table[['Artist', 'Streams']]
#Rename streams columns to include that its in millions
top_artists.rename(columns={'Streams': 'Streams (millions)'}, inplace=True)

#For analysis, we want only english speaking artists,so we need to remove Bad Bunny, BTS, J Balvin and Ozuna as their song lyrics arent always English
top_artists.drop(top_artists[top_artists['Artist'].isin(['Bad Bunny', 'BTS', 'J Balvin', 'Ozuna'])].index, inplace=True)
#Limit to just the top 10 artists
top_artists = top_artists.head(10)

#From a separate webpage, we want the table of top songs and their streams
url_2 = 'https://kworb.net/spotify/songs.html#google_vignette'

#read html and make into dataframe
table_streams = pd.read_html(url_2)[0]
table_streams = pd.DataFrame(table_streams)

#Only need 'Artist and Title' and 'Streams'
table_streams = table_streams[['Artist and Title', 'Streams']]

#Loop through artists in top_artists dataframe, and find the first row with that artist in the table_streams dataframe
top_song = []
streams = []
#for loop goes through each artist and for each artist it goes through each row in the dataframe and checks for a match the nadds the necessary info to lists
for person in top_artists['Artist']:
    count = 0
    for row in table_streams['Artist and Title']:
            if person in row:
               top_song.append(row)
               #need streams in millions
               streams.append(float(table_streams['Streams'].iloc[count])/1000000)
               break
            else:
                count += 1
                continue
#We only want the song name, so need to remove the artist and '-'

for i in range(len(top_song)):
    song = top_song[i]
    for person in top_artists['Artist']:
        if person in song:
            song = song.replace(person, '')
            song = song.replace(' - ', '')
            top_song[i] = song

            break
        else:
            continue

#Manually add gender of each artist
female = ['Taylor Swift', 'Ariana Grande', 'Rihanna']

#Want to add artists gender to a new list that can later be added to the dataframe
gender = []
#Loop through the artists in the dataset. For artist that appear in the female list, assign gender as female and for those that dont assign gender as male
for artist in top_artists['Artist']:
    if artist in female:
        gender.append('female')
    else:
        gender.append('male')


#Manually add the genre of each artist
genre = ['R&B','pop','pop','pop','pop','hip hop','pop','hip hop','hip hop', 'pop']

#add these things to dataframe

top_artists['Top Song'] = top_song
top_artists['Song Streams (millions)'] = streams
top_artists['Gender'] = gender
top_artists['Genre'] = genre
top_artists = top_artists.reset_index()

print(top_artists)
#Save data in SQL database
with sqlite3.connect('song_lyrics.db') as connection:
    cursor = connection.cursor()
    #ensure table begins clear so not to end up with duplicates
    clear_table_query = '''
    DELETE FROM song;
    '''
    cursor.execute(clear_table_query)
    count = 0
    #loop through artists in dataframe and add each to database
    for artist in top_artists['Artist']:
        insert_artist_query = '''
        INSERT INTO song(artist, total_streams, song, song_streams, gender, genre)
        VALUES(?,?,?,?,?,?);
        ''' 
        data = (artist, top_artists['Streams (millions)'][count], top_artists['Top Song'][count],top_artists['Song Streams (millions)'][count], top_artists['Gender'][count], top_artists['Genre'][count])
        count += 1
        cursor.execute(insert_artist_query, data)
    connection.commit()
    print('succesful')
