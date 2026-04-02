import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import dataset
production = pd.read_csv('cleaned_oil_production_by_country.csv')
#pie chart of top oil producing countries
top_countries = production.head(5)
other_countries = {'Entity': 'Other', 'Oil': production['Oil'].iloc[len(top_countries):].sum()}
top_countries.loc[len(top_countries)] = other_countries
print(top_countries)
plt.figure()
plt.pie(top_countries['Oil'], labels=top_countries['Entity'], autopct='%1.1f%%')
plt.show()