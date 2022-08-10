#from datetime import datetime
#import pandas as pd

#dateparse = lambda dates: [datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in dates]
#date = datetime.strptime('%Y-%m-%d %H:%M:%S') 
#df = pd.read_csv('test.dat', parse_dates=['datetime'], date_parser=dateparse)
#print(date)
from datetime import datetime

# current dateTime
now = datetime.now()

# convert to string
date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
date = now.strftime("%Y-%m-%d")
month = now.strftime("%Y-%b-%d")
print('DateTime String:', date_time_str)
print('DateTime String:', date)
print('DateTime String:', month)

# Output 2021-07-20 16:26:24
# https://www.w3schools.com/python/python_datetime.asp
#https://pynative.com/python-datetime-format-strftime/
# https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python