import numpy as np
import pandas as pd

import pandas as pd
import csv
with open('testing.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    count = 0
    fsa=[]
    line = []
    desc = []
    Itemid = []
    UOM = []
    qty = []
    imsetno = []
    shiptolocation = []
    for row in reader:
        count = count+1
        #print(row[2])
        fsa.append(row[0])
        line.append(row[1])
        desc.append(row[3])
        Itemid.append(row[4])
        UOM.append(row[6])
        qty.append(row[8])
        imsetno.append(row[3])
        shiptolocation.append(row[8])
print(fsa[0:])
print(line[4:])
print(desc[4:])
print(Itemid[4:])
print(UOM[4:])
print(qty[4:])
print(imsetno[2])
print(shiptolocation[3])
# importing pandas
import pandas as pd

record = {
'imsetno': imsetno[2],
'line': line[5:],
'Itemid': Itemid[5:],
'UOM': UOM[5:],
'qty': qty[5:],
'UP': '',
'Desc': desc[5:],
'sourceloc': '',
'shoptolocations': shiptolocation[3]}

# create a dataframe
dataframe = pd.DataFrame(record, columns = ['imsetno', 'line', 'Itemid', 'UOM', 'qty', 'UP', 'Desc', 'sourceloc', 'shoptolocations'])
dataframe.to_csv('test.csv')
print("Given Dataframe :\n", dataframe)

# selecting rows based on condition
#rslt_df = dataframe.loc[dataframe['E'] > 1]

#print('\nResult dataframe :\n', rslt_df)

#fileter by row

import pandas as pd 

df = pd.read_csv('test.csv')
#print(df.head())
newdf = df[df['qty']>0]
print(newdf)
newdf.to_csv('new.csv')
import csv
with open('new.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    count = 0
    #fsa=[]
    a = []
    b = []
    c = []
    d = []
    e = []
    for row in reader:
        count = count+1
        #print(row[2])
        #fsa.append(row[0])
        a.append(row[2])
        b.append(row[3])
        c.append(row[4])
        d.append(row[5])
        e.append(row[6])
#print(fsa[0:])
print(a[1:])
print(b[1:])
print(c[1:])
print(d[1:])
print(e[1:])

#fsas = pd.read_csv("csv.csv")

#print(fsas)
# updating the column value/data
#fsas.loc[3:, 'Line No'] = 'SHIV CHANDRA'
#fsas.loc[3:, 'Line No'] = a[1:]
#fsas['Line No'] = fsas['Line No'].replace({'testing': a[1:]})

# writing into the file
#fsas.to_csv("csv.csv", index=False)

#print(fsas)