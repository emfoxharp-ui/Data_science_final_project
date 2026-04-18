#Create Wordcount showing most popular words across the songs
#import libraries
import numpy as np
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import sqlite3

#open sql connection
with sqlite3.connect('song_lyrics.db') as connection:
    cursor = connection.cursor()
    #make query to select words and frequency from lyrics
    select_words_query = '''
    SELECT word, frequency
    FROM lyrics;
    '''
    #In order for our results to be interesting and tell us something, we want to disclude conjunctions and common words like the, and, a, and etc.
    eliminate = ['oh','eh','ill','ooh','eh','yeah','the','but','can','this','if','youre','and','a','to','of','in','is','you','that','it','for','an', 'was', 'on', 'i', 'me', 'its','with','just','my','im','your','we','be','your','get','got','so']
    
    #make dataframe of words
    common_words_df = pd.DataFrame(cursor.execute(select_words_query).fetchall()).groupby(0, as_index = False).sum().sort_values(by = 1,ascending = False)
    
    #Make original wordcloud for comparison
    
    common_words_df_original = common_words_df.head(30).reset_index()
    frequencies_original = {}
    #make string for word cloud cleaned
    for i in range(len(common_words_df_original)):
        for k,n in common_words_df_original.iterrows():
            frequencies_original[n[0]] = n[1]

    #Create wordcloud object
    wordcloud_original = WordCloud(width = 1000, height = 1000, margin = 0, background_color = 'white').generate_from_frequencies(frequencies_original)
    

    
    #make cleaned wordcloud
    common_words_df_cleaned = common_words_df
    #remove words
    for i in range(len(common_words_df)):
        if common_words_df[0][i] in eliminate:
            common_words_df_cleaned = common_words_df_cleaned[common_words_df_cleaned[0] != common_words_df_cleaned[0][i]]
        else:
            continue
    print(common_words_df_cleaned)
    #limit to top 30 words
    common_words_df_cleaned = common_words_df_cleaned.head(30).reset_index()
    frequencies_cleaned = {}
    #make string for word cloud cleaned
    for i in range(len(common_words_df_cleaned)):
        for k,n in common_words_df_cleaned.iterrows():
            frequencies_cleaned[n[0]] = n[1]
    print(frequencies_cleaned)
    #Create wordcloud object
    wordcloud_cleaned = WordCloud(width = 1000, height = 1000, margin = 0, background_color = 'white').generate_from_frequencies(frequencies_cleaned)
    
    fig, ax = plt.subplots(1,2)
ax[0].imshow(wordcloud_original, interpolation = 'bilinear')
ax[0].set_title('Original Lyrics', fontweight = 'bold')

ax[1].imshow(wordcloud_cleaned, interpolation = 'bilinear')
ax[1].set_title('Cleaned Lyrics', fontweight = 'bold')
ax[0].axis('off')
ax[1].axis('off')
plt.show()
    #plt.imshow(wordcloud, interpolation = 'bilinear')
    #plt.axis('off')
    #plt.margins(x=0,y=0)
    #plt.show()