import pandas as pd
# you may need to install openpyxl


car1 = pd.read_csv("passenger cars 2018.csv")
car2 = pd.read_csv("passenger cars 2019.csv")


#print(car1)
#print(car2)

#CarElectric2018= car1.loc[car1 ['Engine type'].str.contains("Hybrid", case=False ,na=False)]
#CarElectric2019= car2.loc[car2 ['Engine type'].str.contains("Hybrid", case=False ,na=False)]

#print(CarElectric2018)

#print(CarElectric2018['Registration type'].count())
#print(CarElectric2019['Registration type'].count())

# First grouping based on "Team"
# Within each team we are grouping based on "Position"
#group2018 = car1.groupby(['County','Engine type'])
#group2019 = car2.groupby(['County','Engine type'])

#print(group2018['Registration type'].count())
#print(group2019['Registration type'].count())