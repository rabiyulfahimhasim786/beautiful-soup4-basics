#method 1
from dateutil import parser

received_time = "Wed, 12 Jul 2023 06:35:33 -0500"

# Parse the date string with time zone using dateutil.parser
day = parser.parse(received_time)

# Get the 'Date' and 'Time' components as strings
date_str = day.strftime("%d %b %Y")
time_str = day.strftime("%H:%M:%S")
print(date_str, time_str)

# method 2
from dateutil import parser

received_time = "07 Aug 2023 12:56:50"

# Parse the date string using dateutil.parser
day = parser.parse(received_time)

# Get the 'Date' and 'Time' components as strings with the desired format
date_str = day.strftime("%d-%m-%Y")
time_str = day.strftime("%H:%M:%S")

# Combine the 'Date' and 'Time' components with a space separator
formatted_output = f"{date_str} {time_str}"
print(formatted_output)

