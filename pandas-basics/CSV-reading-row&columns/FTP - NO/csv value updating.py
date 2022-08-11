# importing the pandas library
import pandas as pd
# FTP - N codes,
#import pandas as pd
import csv
with open('testing.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    count = 0
    imsetno = []
    custid = []
    fsa=[]
    coid =[]
    Salesloc =[]
    custpo =[]
    taker =[]
    approved = []
    shipto = []
    contract = []
    
    for row in reader:
        count = count+1
        #print(row[2])
        fsa.append(row[1])
        imsetno.append(row[4])
        custid.append(row[2])
        coid.append(row[2])
        Salesloc.append(row[4])
        custpo.append(row[6])
        taker.append(row[6])
        approved.append(row[4])
        shipto.append(row[2])
        contract.append(row[6])
print(fsa[4:])
print(imsetno[2])
print(custid[0])
print(coid[2])
print(Salesloc[0])
print(custpo[1])
print(taker[2])
print(approved[1])
print(shipto[1])
print(contract[0])

# importing the pandas library
#import pandas as pd

# reading the csv file
df = pd.read_csv("output.csv")
#print(df)
# updating the column value/data
df.loc[3, 'Import Set No'] = imsetno[2]
df.loc[3, 'Customer ID'] = custid[0]
df.loc[3, 'Company ID'] = coid[2]
df.loc[3, 'Sales Location ID'] = Salesloc[0]
df.loc[3, 'Customer PO Number'] = custpo[1]
df.loc[3, 'Taker'] = taker[2]
df.loc[3, 'Approved'] = approved[1]
df.loc[3, 'Ship To ID'] = shipto[1]
df.loc[3, 'Contract Number'] = contract[0]
#df.loc[3, 'Company ID'] = 
#df.loc[3, 'Company ID'] = 
#df.loc[3, 'Customer ID'] = ''
# writing into the file
df.to_csv("output.csv", index=False)

#sprint(df)
#https://www.geeksforgeeks.org/update-column-value-of-csv-in-python/