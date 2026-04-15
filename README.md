# Data_science_final_project
This Project explores the lyrics of the top songs from the top English speaking artists on spotify, taking the most popular song from each of the top 10 artists based on total spotify streams.

**Replicating the code:**

The codes are numbered in the order in which they need to be run, as some use output from others and therefore need to be run in a specific order. 

The first scripts that need to be run are from the Webscraping_scripts folder, which both collect the data and clean it:
1) Run 1_making_databases.py to create the tables in the SQL database and add the artists infos
2) Run 2_web_scraping_artists.py and adds information to SQL database
3) Run 3_webscraping_lyrics.py. This file scrapes for the lyrics of the top songs and word count to the dataframe, and saves it all to the SQL database

Backups:
If a script does not run properly, the next script will still be able to run, as it will use the file backup if it needs data produced from previous scripts

Outputs:
To make the outputs, run the scripts from the outputs folder. The scripts are labelled to tell you which script produces which output, and these scripts do not need to be run in a specific order, but do need to be run after the webscraping scripts.
