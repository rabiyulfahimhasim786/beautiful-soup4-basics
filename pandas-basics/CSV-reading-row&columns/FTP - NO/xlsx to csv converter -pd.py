
import pandas as pd
df = pd.read_excel('orderquoteheader.xlsx', sheet_name=None)
df['Sheet1'].to_csv('output.csv') 