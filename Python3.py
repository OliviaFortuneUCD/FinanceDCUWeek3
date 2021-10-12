import pandas as pd

Cars = pd.read_csv("Cars.csv")

Found = Cars.loc[Cars['Car'].str.contains("Toyota", case=False)]
print(Found)
Found1 = Cars.loc[Cars['Car'].str.contains("Ford", case=False)]
print(Found1)