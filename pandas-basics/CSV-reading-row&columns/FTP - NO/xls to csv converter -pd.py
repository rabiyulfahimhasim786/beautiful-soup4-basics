
import pandas as pd
df = pd.read_excel('Location.xls', sheet_name=None)
df['Annex MRO As Needed'].to_csv('testing.csv') 