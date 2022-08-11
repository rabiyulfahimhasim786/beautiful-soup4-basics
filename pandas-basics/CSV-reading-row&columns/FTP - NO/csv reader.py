# importing the pandas library
import pandas as pd

# reading the csv file
df = pd.read_csv("output.csv")
print(df)
# updating the column value/data
df.loc[3, 'Import Set No'] = '418'
df.loc[4, 'Import Set No'] = ''
# writing into the file
df.to_csv("output.csv", index=False)

print(df)
#https://www.geeksforgeeks.org/update-column-value-of-csv-in-python/