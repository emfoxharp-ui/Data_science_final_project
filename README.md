# Data_science_final_project
This project explores the lyrics of the top songs from the top English speaking artists on spotify, taking the most popular song from each of the top 10 artists based on total spotify streams and exploring trends in lyrics across songs, genders, and genres.

This GitHub incluudes a folder of python scripts that can be used to recreate the outputs used in the blog, and a folder of the outputs used in the blog. Within the python scripts folder, there is a 'webscraping and SQL scripts' folder, which include the co and an output scripts folder.

Necessary libraries:
- pandas
- NumPy
- matplotlib.pyplot
- sqlite3
- BeautifulSoup
- re
- time
- requests
- WordCloud
- 


**Replicating the code:**

The webscraping codes need to be run first, and are numbered in the order in which they need to be run, as some use output from others and therefore need to be run in a specific order. These codes are found in the 'webscraping_and_SQL_scripts' folder. They collect, clean, and save the data to an SQL database:
1) Run 1_making_databases.py to create the tables in the SQL database and add the artists infos
2) Run 2_web_scraping_artists.py and adds information to SQL database
3) Run 3_webscraping_lyrics.py. This file scrapes for the lyrics of the top songs and word count to the dataframe, and saves it all to the SQL database

Outputs:
To make the outputs, run the scripts from the 'Outputs' folder. The scripts are labelled with which output they produce. These scripts do not need to be run in a specific order, but do need to be run after the webscraping scripts.
