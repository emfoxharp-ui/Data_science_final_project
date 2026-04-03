#import necessary libraries
from  bs4 import BeautifulSoup
from matplotlib import artist
import requests as req
import re as re
import pandas as pd
import numpy as np

one_dance = 'https://genius.com/Drake-one-dance-lyrics'
response = req.get(one_dance)
soup = BeautifulSoup(response.text, 'html.parser')

#find lyrics 
lyrics = soup.find_all('br', class_='Lyrics__Container-sc-c1895f55-1 fYBzEj')
print(lyrics)
