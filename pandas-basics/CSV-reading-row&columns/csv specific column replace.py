# importing the pandas library
import pandas as pd

# reading the csv file
df = pd.read_csv("AllDetails.csv")

print(df)
# updating the column value/data
df['Status'] = df['Status'].replace({'P': 'A'})

# writing into the file
df.to_csv("AllDetails.csv", index=False)

print(df)

#https://www.geeksforgeeks.org/update-column-value-of-csv-in-python/