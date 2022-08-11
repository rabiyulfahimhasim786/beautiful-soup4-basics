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

