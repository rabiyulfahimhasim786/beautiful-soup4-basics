import pandas as pd
data_xls = pd.read_excel('Location 41 Beyond 219563 New one.xlsx', 'Annex MRO As Needed', index_col=None)
data_xls.to_csv('testing.csv', encoding='utf-8')