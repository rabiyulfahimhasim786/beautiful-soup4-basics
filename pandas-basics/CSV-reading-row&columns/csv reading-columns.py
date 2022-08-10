import pandas as pd

dataset = pd.read_csv("testing.csv")

data = dataset.iloc[:,1:2].values
print(data)