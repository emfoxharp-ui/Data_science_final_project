#Attempting to loop through lists for webscraping
from  bs4 import BeautifulSoup
import requests as req
import re as re
import pandas as pd
import numpy as np
import time
#Need_cleaned_top_spotify_artists.csv
dataset = pd.read_csv('./Data_science_final_project/Datasets/Cleaned_datasets/cleaned_top_spotify_artists.csv')

#add urls to the dataset
url = ['https://www.azlyrics.com/lyrics/drake/onedance.html','https://www.azlyrics.com/lyrics/taylorswift/cruelsummer.html','https://www.azlyrics.com/lyrics/weeknd/blindinglights.html','https://www.azlyrics.com/lyrics/justinbieber/loveyourself.html','https://www.azlyrics.com/lyrics/arianagrande/7rings.html','https://www.azlyrics.com/lyrics/travisscott/goosebumps.html','https://www.azlyrics.com/lyrics/edsheeran/shapeofyou.html','https://www.azlyrics.com/lyrics/eminem/withoutme.html','https://www.azlyrics.com/lyrics/kanyewest/heartless.html','https://www.azlyrics.com/lyrics/rihanna/umbrella.html']
dataset['URL'] = url

#Loop through urls in dataset to produce lyric count for each

word_count = []
for webpage in url:
    #get the code from the page and convert it into a workable format
    response = req.get(webpage)
    soup = BeautifulSoup(response.text, 'html.parser')
    #add 3 second time delay to not overwhelm website
    time.sleep(1)
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


    #We want to make this into a dataframe that tells us the word count for each word in the lyrics
    #To start, we must separate the string into a list of words
    words = words.split()
    word_count.append(len(words))

dataset['word count'] = word_count

#clean uo dataset
dataset.drop(columns = ['Unnamed: 0'], inplace = True)

print(dataset)

#Save dataset to csv file
dataset.to_csv('./Data_science_final_project/Datasets/Cleaned_datasets/cleaned_top_spotify_artists_lyrics.csv')