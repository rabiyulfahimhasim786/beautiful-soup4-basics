# importing the pandas library
import pandas as pd

# reading the csv file
df = pd.read_csv("AllDetails.csv")
print(df)
# updating the column value/data
df.loc[5, 'Name'] = 'SHIV CHANDRA'

# writing into the file
df.to_csv("AllDetails.csv", index=False)

print(df)
#https://www.geeksforgeeks.org/update-column-value-of-csv-in-python/