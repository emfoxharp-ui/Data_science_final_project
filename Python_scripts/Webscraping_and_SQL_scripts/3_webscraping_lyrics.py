#web-scraping lyrics from list of urls and adding them to database
#import libraries
from  bs4 import BeautifulSoup
import requests as req
import re as re
import pandas as pd
import numpy as np
import time
import sqlite3

#open database connection
with sqlite3.connect('song_lyrics.db') as connection:
    cursor = connection.cursor()
    #get list of artists from song table to be made into dataframe
    artist_query = '''
    SELECT artist
    FROM song;
    '''
    #ensure lrics table is empty to not end up with duplicates
    lyrics_clear_query = '''
    DELETE FROM lyrics;
    '''
    
    #execute queries and make database from artist query
    cursor.execute(lyrics_clear_query)
    dataset = pd.DataFrame(cursor.execute(artist_query))

#add urls to the dataset
url = ['https://www.azlyrics.com/lyrics/drake/onedance.html','https://www.azlyrics.com/lyrics/taylorswift/cruelsummer.html','https://www.azlyrics.com/lyrics/weeknd/blindinglights.html','https://www.azlyrics.com/lyrics/justinbieber/loveyourself.html','https://www.azlyrics.com/lyrics/arianagrande/7rings.html','https://www.azlyrics.com/lyrics/travisscott/goosebumps.html','https://www.azlyrics.com/lyrics/edsheeran/shapeofyou.html','https://www.azlyrics.com/lyrics/eminem/withoutme.html','https://www.azlyrics.com/lyrics/kanyewest/heartless.html','https://www.azlyrics.com/lyrics/rihanna/umbrella.html']
dataset['URL'] = url
#Set row index to URL column as this will be used later
dataset.set_index('URL', inplace = True)

#Loop through urls in dataset to produce lyric count for each

word_count = []
for webpage in url:
    #get the code from the page and convert it into a workable format
    response = req.get(webpage)
    soup = BeautifulSoup(response.text, 'html.parser')
    #add 3 second time delay to not overwhelm website
    time.sleep(3)
    #find lyrics from the page
    lyrics = soup.find_all('div', class_=None)

    #We dont want punctuation so need to remove this
    #First, make a string from the lyrics
    words = ''
    for lyric in lyrics:
        words += (lyric.text)

    #Next we remove all the punctuation
    words = re.sub(r'[^\w\s]','',words)
    #Make everything lowercase
    words = words.lower()
    #Split words into a list of words
    words = words.split()


    #For each song, we want to add the word and the frequency to a table in sql that also has an id linking it to the song in the other table
    #We want to make this into a dataframe that tells us the word count for each word in the lyrics
    word_count.append(len(words))

    unique_words = list(set(words))


    #get the artist based on the webpage URL
    id =  dataset.at[webpage, 0]
    print(id)

    #due to formating issues, 'umbrella-ella-ella' is appearing wrong in the lyrics. Hard code to replace this with 'umbrella-ella-ella'
    #for each word in the list words, rest the count to 0
    for word in unique_words:
        if word == 'umbrellaâellaâella':
            word = 'umbrella-ella-ella'
        count = 0
        for it in words:
            if it == 'umbrellaâellaâella':
                    it = 'umbrella-ella-ella'
            if word == it:
                count += 1
                continue    
                
        #Add word into into a table in SQL database:
        #Open database connection
        with sqlite3.connect('song_lyrics.db') as connection:
            cursor = connection.cursor()
            insert_word_query = '''
                INSERT INTO lyrics(song_id, word, frequency)
                VALUES((SELECT song_id FROM song WHERE artist == ?),?,?);
                ''' 
            data = (id, word,count)
            cursor.execute(insert_word_query, data)
    
#commit changes to database
connection.commit()

