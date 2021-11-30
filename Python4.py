import pandas as pd
import re
pd.set_option('display.max_colwidth', -1)

netflix = pd.read_csv("netflix_titles.csv")




Found = netflix.loc[netflix['title'].str.contains("Blood", case=False)]
print('Found')
print(Found)

Country = netflix['country']
print(Country)
#office = netflix[netflix['title'].str.contains('The Office (U.S.)', regex=False)]
#print(office)
#print(office['duration'].sum())
#Actors = netflix.loc[netflix['cast'].str.contains("Steve", case=False ,na=False)]
#print('Find Steve')
#print(Actors)
#CountryFinds = netflix.loc[netflix['country'].str.contains("United States", case=False ,na=False)]
#print('Country Finds')
#print(CountryFinds)
