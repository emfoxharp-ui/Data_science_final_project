#import necessary libraries
from  bs4 import BeautifulSoup
import requests as req
import re as re
import pandas as pd
import numpy as np

one_dance = 'https://www.azlyrics.com/lyrics/drake/onedance.html'

#get the code from the page and convert it into a workable format
response = req.get(one_dance)
soup = BeautifulSoup(response.text, 'html.parser')

#find lyrics from the page

lyrics = soup.find_all('div', class_=None)

#We dont want punctuation so need to remove this
#First, make a string from the lyrics
one_dance = ''
for lyric in lyrics:
        one_dance += (lyric.text)

#Next we remove all the punctuation
one_dance = re.sub(r'[^\w\s]','',one_dance)

print(one_dance)

#We want to make this into a dataframe that tells us the word count for each word in the lyrics
#To start, we must separate the string into a list of words






