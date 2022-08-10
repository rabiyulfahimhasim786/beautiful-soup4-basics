
import pandas as pd
import csv
with open('testing.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    count = 0
    CustPO = []
    ReleaseNO = []
    fsa=[]
    qty=[]
    Pkginfo=[]
    shiptoorg=[]
    shiptoloc=[]
    for row in reader:
        count = count+1
        #print(row[2])
        fsa.append(row[1])
        CustPO.append(row[5])
        ReleaseNO.append(row[3])
        qty.append(row[8])
        Pkginfo.append(row[3])
        shiptoorg.append(row[5])
        shiptoloc.append(row[8])
print(fsa[4:])
print(CustPO[1])
print(ReleaseNO[2])
print(fsa[4:])
print(qty[4:])
print(Pkginfo[3])
print(shiptoorg[3])
print(shiptoloc[3])
import pandas as pd
from datetime import datetime

# current dateTime
now = datetime.now()

# convert to string
#date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
date = now.strftime("%Y-%b-%d")

print('DateTime String:', date)

# dataframe Name and Age columns
df = pd.DataFrame({'PO NO': CustPO[1],
                   'Release NO': ReleaseNO[2],
                   'Line No': fsa[5:],
                   'Qty': qty[5:],
                   'packing Slip information': Pkginfo[3],
                   'SHIP TO ORG ID': shiptoorg[3],
                   'SHIP TO LOCATION': shiptoloc[3],
                   'Need By Date': date})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1', index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.save()