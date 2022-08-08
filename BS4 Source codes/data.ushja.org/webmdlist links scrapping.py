

import requests
import pandas as pd
from bs4 import BeautifulSoup
#https://doctor.webmd.com/providers/specialty/pediatric-cardiology/texas/houston?pagenumber=9

#url = "https://doctor.webmd.com/providers/specialty/addadhd/texas/pearland"
url = "https://doctor.webmd.com/providers/specialty/pediatric-cardiology/texas/houston?pagenumber=9"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

# get all links
url_list = []
productDivs = soup.findAll('div', attrs={'class' : 'card-content'})
for div in productDivs:
    #print(div.a['href'])
    url_list.append(div.a['href'])
    
# get all data from URLs
all_data = []
for url in url_list:
    print(url)

    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    image_tag=soup.find('div',class_="btn-holder")
    all_data.append(
    [
        image_tag.get_text(strip=True),
        ]
        )

# save data to CSV
df = pd.DataFrame(
    all_data,
    columns=[
        "contact",
        #"title",
       # "sub_title",
    ],
)
print(df)
df.to_csv("webmdcontact1.csv", index=None)
