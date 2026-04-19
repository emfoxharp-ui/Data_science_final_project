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
    WHERE song_id = ?;
    '''
    artist_query = '''
    SELECT artist, song_id, genre
    FROM song;
    '''
    word_count_df = pd.DataFrame((cursor.execute(artist_query)).fetchall())
    word_count = []
    unique_word_count = []

    for number in word_count_df[1]:
        word = pd.DataFrame(cursor.execute(unique_count_query, (number,)).fetchall())
        word_count.append(sum(word[0]))
        unique_word_count.append(len(word))

#add to dataframe
word_count_df['total count'] = word_count
word_count_df['unique count'] = unique_word_count
        
#We can now maka a scattergraph using this information
fig, axs = plt.subplots(1,2)
ax = fig.add_subplot(axs[0])

#make list to set each artist to the colour representing their genre
color = []
for genre in word_count_df[2]:
    if genre == 'hip hop':
        color += ['#5dde5b']
    elif genre == 'pop':
        color += ['#4c97d9']
    elif genre == 'R&B':
        color += ['#e067a2']

#make scatter graph
axs[0].scatter(word_count_df['total count'], word_count_df['unique count'], color = color, s = 100)

#label each point (Kanye West needs different positioning so not to cause overlap)
for i, txt in enumerate(word_count_df[0]):
    if txt == 'Kanye West':
        ax.annotate(txt, (word_count_df['total count'].iloc[i] -100, word_count_df['unique count'].iloc[i]+0.8), fontweight = 'bold')
    else:
        ax.annotate(txt, (word_count_df['total count'].iloc[i] +0.8, word_count_df['unique count'].iloc[i]+0.8), fontweight = 'bold')

#add title,axis labels and grid
axs[0].set_title('Total Word Count and Unique Word Count', fontsize = 14, fontweight = 'bold')
axs[0].set_xticks(np.arange(250,800, 25))
axs[0].set_yticks(np.arange(50,350,25))
axs[0].set_xlabel('Total Word Count', fontweight = 'bold')
axs[0].set_ylabel('Unique Word Count', fontweight = 'bold')
axs[0].grid(linestyle = '--', alpha = 0.5)
axs[0].set_xticklabels(labels =np.arange(250,800, 25), rotation = 'vertical')

# add legend for colours representing genres
genre = ['hip hop', 'pop', 'R&B']
colors = ['#5dde5b', '#4c97d9', '#e067a2']
axs[0].legend(handles = [plt.Line2D([0],[0], marker = 'o', color = 'w', label = genre[i], markerfacecolor = colors[i], markersize = 10) for i in range(3)], title = 'Genre')



#next make a bar chart showing for each artist the percentage of words they used that were unique
percentage = []
for i,txt in enumerate(word_count_df[0]):
    percentage.append((unique_word_count[i]/word_count[i])*100)
print(percentage)

#set the order of the bars in descending order
word_count_df['percentage'] = percentage
word_count_df.sort_values(by= 'percentage', ascending = False, inplace = True)

#make bar chart
axs[1].bar((word_count_df[0]), word_count_df['percentage'], color = '#4c97d9')
#add title, axis labels, grid and format x axis labels
axs[1].set_title('Unique words as a Percentage of Total Words', fontsize = 14, fontweight = 'bold')
axs[1].set_xlabel('Artist', fontweight = 'bold')
axs[1].set_ylabel('Percentage of Words That Are Unique', fontweight = 'bold')
axs[1].grid(linestyle = '--', alpha = 0.5, axis = 'y')
axs[1].set_xticklabels((word_count_df[0] + '\n' + word_count_df[2]),rotation = 'vertical')

plt.show()