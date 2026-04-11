#Making a scatter graph comparing the total word count and unique word count of each song
#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

#Open connection to database

with sqlite3.connect('song_lyrics.db') as connection:
    cursor = connection.cursor()
    
    #for each song, get the total word count, unique word count, and artist name
    unique_count_query = '''
    SELECT frequency 
    FROM lyrics
    WHERE lyric_id = ?;
    '''
    artist_query = '''
    SELECT artist, artist_id
    FROM song;
    '''
    word_count_df = pd.DataFrame((cursor.execute(artist_query)).fetchall())
    word_count = []
    unique_word_count = []

    for number in word_count_df[1]:
        word = pd.DataFrame(cursor.execute(unique_count_query, (number,)).fetchall())
        word_count.append(sum(word[0]))
        unique_word_count.append(len(word))

word_count_df['total count'] = word_count
word_count_df['unique count'] = unique_word_count
        
#We can now maka a scattergraph using this information
fig = plt.figure()
ax = fig.add_subplot()
plt.scatter(word_count,unique_word_count, color = '#5dde5b', s = 100)
#label each point (Kanye West needs different positioning so not to cause overlap)
for i, txt in enumerate(word_count_df[0]):
    if txt == 'Kanye West':
        ax.annotate(txt, (word_count[i] -45,unique_word_count[i]+0.8), fontweight = 'bold')
    else:
        ax.annotate(txt, (word_count[i] +0.8,unique_word_count[i]+0.8), fontweight = 'bold')

#add title and axis labels
plt.title('Total Word Count and Unique Word Count', fontsize = 14, fontweight = 'bold')
plt.xticks(np.arange(250,800, 25))
plt.yticks(np.arange(50,350,25))
plt.xlabel('Total Word Count')
plt.ylabel('Unique Word Count')
plt.grid(linestyle = '--', alpha = 0.5)


plt.show()


#next make a bar chart showing for each artist the percentage of words they used that were unique
percentage = []
for i,txt in enumerate(word_count_df[0]):
    percentage.append((unique_word_count[i]/word_count[i])*100)

plt.bar(word_count_df[0], percentage, color = '#4c97d9')
plt.title('Unique words as a Percentage of Total Words', fontsize = 14, fontweight = 'bold')
plt.xlabel('Artist', fontweight = 'bold')
plt.ylabel('Percentage of Words That Are Unique', fontweight = 'bold')
plt.grid(linestyle = '--', alpha = 0.5, axis = 'y')
plt.show()