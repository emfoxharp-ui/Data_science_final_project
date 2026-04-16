#crete output comparing which songs use more first person, second person, and third person pronouns
#import necessary libraries
import numpy as np
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

#Open connection to SQL database
with sqlite3.connect('song_lyrics.db') as connection:
    get_pronouns_query = '''
    SELECT word, frequency '''