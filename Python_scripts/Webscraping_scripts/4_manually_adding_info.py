#This script will add the genders to the dataframe, which is easier to do manually rather than with webscraping
#import libraries and dataset
import numpy as np
import pandas as pd
dataset = pd.read_csv('./Data_science_final_project/Datasets/Cleaned_datasets/cleaned_top_spotify_artists_song.csv')

#print(dataset['Artist'])
#Make a list of the female artists in the top 10

female = ['Taylor Swift', 'Ariana Grande', 'Rihanna']

#Want to add artists gender to a new list that can later be added to the dataframe
gender = []
#Loop through the artists in the dataset. For artist that appear in the female list, assign gender as female and for those that dont assign gender as male
for artist in dataset['Artist']:
    if artist in female:
        gender.append('female')
    else:
        gender.append('male')
#add genders to dataframe
dataset['Gender'] = gender

#Dataset has some unnecessary columns so remove these from the dataset:
dataset.drop(columns= ['Unnamed: 0.1','Unnamed: 0'], inplace = True)

#Check dataset
print(dataset)

#Save dataset to new csv file
dataset.to_csv('./Data_science_final_project/Datasets/Cleaned_datasets/cleaned_top_spotify_artists_song_gender.csv')