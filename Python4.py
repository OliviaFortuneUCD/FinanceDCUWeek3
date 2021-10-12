import pandas as pd
netflix = pd.read_csv("netflix_titles.csv")



#print(netflix.info())
#print(netflix.columns)
#print(netflix.isnull().sum())
#missing = netflix.isnull().sum().to_frame()
#print(missing[0:3])
#print(netflix['release_year'].min() , netflix['release_year'].max())
Found = netflix.loc[netflix['title'].str.contains("Blood", case=False)]
print(Found)