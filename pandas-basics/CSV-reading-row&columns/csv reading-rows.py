import pandas as pd

dataset = pd.read_csv("testing.csv")

data = dataset.iloc[1:4].values
print(data)