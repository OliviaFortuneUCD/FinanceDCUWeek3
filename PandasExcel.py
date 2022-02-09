import pandas
# you may need to install openpyxl

excel_data_df = pandas.read_excel('NewCars2021.Xlsx', sheet_name='Sheet1')

# print whole sheet data
#print(excel_data_df)


Toyota = excel_data_df.loc[excel_data_df['Car'].str.contains("Toyota", case=False ,na=False)]
print(Toyota)

Tesla= excel_data_df.loc[excel_data_df['Car'].str.contains("Tesla", case=False ,na=False)]
print(Tesla)