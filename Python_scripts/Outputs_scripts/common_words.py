#Create Wordcount showing most popular words across the songs
#import libraries
import numpy as np
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import sqlite3

with sqlite3.connect('song_lyrics.db') as connection:
    cursor = connection.cursor()
    select_words_query = '''
    SELECT word, frequency
    FROM lyrics;
    '''
    #In order for our results to be interesting and tell us something, we want to disclude conjunctions and common words like the, and, a, and etc.
    eliminate = ['the','and','a','to','of','in','is','you','that','it','for','an', 'was', 'on', 'i', 'me', 'its','with','just','my','im','your','we','be','your','get','got','so']
    common_words_df = pd.DataFrame(cursor.execute(select_words_query).fetchall()).groupby(0, as_index = False).sum().sort_values(by = 1,ascending = False)
    print(common_words_df)
    word_cloud_string = ''
    for i in range(len(common_words_df)):
        if common_words_df[0][i] in eliminate:
            common_words_df = common_words_df[common_words_df[0] != common_words_df[0][i]]
        else:
            continue
    common_words_df = common_words_df.head(30).reset_index()
    print(common_words_df)
    for i in range(len(common_words_df)):
        word_cloud_string += (str(common_words_df[0][i]) + ' ')
        #*int(common_words_df[1][i])
    print(word_cloud_string)
    #Create wordcloud object
    wordcloud = WordCloud().generate(word_cloud_string)
    plt.imshow(wordcloud, interpolation = 'bilinear')
    plt.axis('off')
    plt.margins(x=0,y=0)
    plt.show()