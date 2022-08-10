
import pandas as pd
import csv
with open('testing.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    count = 0
    fsa=[]
    a = []
    for row in reader:
        count = count+1
        #print(row[2])
        fsa.append(row[1])
        a.append(row[8])
print(fsa[4:])
print(a[4:])