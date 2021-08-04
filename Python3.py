import pandas as pd

Cars = pd.read_csv("Cars.csv")

Found = Cars.loc[Cars['Car'].str.contains("Honda", case=False)]
print(Found)