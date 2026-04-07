#making a scatter graph showing the word count of each song on the x axis and the number of times the song title is said on the y axis

#import libraries and dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv('./Data_science_final_project/Datasets/Cleaned_datasets/cleaned_top_spotify_artists_lyrics.csv')

plt.figure()
print(dataset)
print(dataset.info())
plt.scatter(dataset['word count'], dataset['word count'])
plt.show()