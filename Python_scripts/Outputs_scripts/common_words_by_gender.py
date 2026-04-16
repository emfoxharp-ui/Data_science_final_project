from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

#open sql connection
with sqlite3.connect('song_lyrics.db') as connection:
    cursor = connection.cursor()
    #make queries to select words and frequency from lyrics
    select_words_query = '''
    SELECT word, frequency
    FROM lyrics l , song s
    WHERE s.gender = 'male' AND l.song_id = s.song_id ;
    '''
    #In order for our results to be interesting and tell us something, we want to disclude conjunctions and common words like the, and, a, and etc.
    eliminate = ['the','but','can','this','if','youre','and','a','to','of','in','is','you','that','it','for','an', 'was', 'on', 'i', 'me', 'its','with','just','my','im','your','we','be','your','get','got','so']
    #make dataframe of words
    common_words_df = pd.DataFrame(cursor.execute(select_words_query).fetchall()).groupby(0, as_index = False).sum().sort_values(by = 1,ascending = False)
    #remove words
    word_cloud_string = ''
    for i in range(len(common_words_df)):
        if common_words_df[0][i] in eliminate:
            common_words_df = common_words_df[common_words_df[0] != common_words_df[0][i]]
        else:
            continue
    #limit to top 30 words
    common_words_df = common_words_df.head(30).reset_index()
    frequencies = {}
    #make string for word cloud
    for i in range(len(common_words_df)):
        for k,n in common_words_df.iterrows():
            frequencies[n[0]] = n[1]
    print(frequencies)
    #Create wordcloud object
    wordcloud_male = WordCloud(width = 1000, height = 1000, margin = 0, background_color = 'white').generate_from_frequencies(frequencies)


with sqlite3.connect('song_lyrics.db') as connection:
    cursor = connection.cursor()
    #make queries to select words and frequency from lyrics
    select_words_query = '''
    SELECT word, frequency
    FROM lyrics l , song s
    WHERE s.gender = 'female' AND l.song_id = s.song_id ;
    '''
    #In order for our results to be interesting and tell us something, we want to disclude conjunctions and common words like the, and, a, and etc.
    eliminate = ['the','but','can','this','if','youre','and','a','to','of','in','is','you','that','it','for','an', 'was', 'on', 'i', 'me', 'its','with','just','my','im','your','we','be','your','get','got','so']
    #make dataframe of words
    common_words_df = pd.DataFrame(cursor.execute(select_words_query).fetchall()).groupby(0, as_index = False).sum().sort_values(by = 1,ascending = False)
    #remove words
    word_cloud_string = ''
    for i in range(len(common_words_df)):
        if common_words_df[0][i] in eliminate:
            common_words_df = common_words_df[common_words_df[0] != common_words_df[0][i]]
        else:
            continue
    #limit to top 30 words
    common_words_df = common_words_df.head(30).reset_index()
    frequencies = {}
    #make string for word cloud
    for i in range(len(common_words_df)):
        for k,n in common_words_df.iterrows():
            frequencies[n[0]] = n[1]
    print(frequencies)
    #Create wordcloud object
    wordcloud_female = WordCloud(width = 1000, height = 1000, margin = 0, background_color = 'white').generate_from_frequencies(frequencies)


fig, ax = plt.subplots(1,2)
ax[0].imshow(wordcloud_male, interpolation = 'bilinear')
ax[0].set_title('Male Artists', fontweight = 'bold')

ax[1].imshow(wordcloud_female, interpolation = 'bilinear')
ax[1].set_title('Female Artists', fontweight = 'bold')
ax[0].axis('off')
ax[1].axis('off')
plt.show()