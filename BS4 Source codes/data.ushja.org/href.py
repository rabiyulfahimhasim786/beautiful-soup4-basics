from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import csv
import re

url = "https://doctor.webmd.com/providers/specialty/addadhd/texas/pearland"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

#rank = soup.find("table", class_="table-standings-body")

link = soup.find('div',class_='card-content')

url_list = link.find('a').get('href')
for url_list in link.find_all('a'):
    print (url_list.get('href'))

#url_list = []
#for a in soup.find("div", class_="card-content").find_all("a"):
#    #url_list.append(a["href"].replace("§", "&sect"))
 #   url_list.append(a["href"])

# get all data from URLs
#all_data = []
#for url in url_list:
#    print(url)