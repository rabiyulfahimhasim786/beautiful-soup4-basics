import csv

op = open("AllDetails.csv", "r")
dt = csv.DictReader(op)
print(dt)
up_dt = []
for r in dt:
	print(r)
	row = {'Sno': r['Sno'],
		   'Registration Number': r['Registration Number'],
		   'Name': r['Name'],
		   'RollNo': r['RollNo'],
		   'Status': 'P'}
	up_dt.append(row)
print(up_dt)
op.close()
op = open("AllDetails.csv", "w", newline='')
headers = ['Sno', 'Registration Number', 'Name', 'RollNo', 'Status']
data = csv.DictWriter(op, delimiter=',', fieldnames=headers)
data.writerow(dict((heads, heads) for heads in headers))
data.writerows(up_dt)

op.close()
