import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://data.ushja.org/awards-standings/zones.aspx?year=2021&zone=1"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

# get all links
url_list = []
for a in soup.find("div", class_="contentSection").find_all("a"):
    url_list.append(a["href"].replace("§", "&sect"))

# get all data from URLs
all_data = []
for url in url_list:
    print(url)

    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    h2 = soup.h2
    sub = h2.find_next("p")

    for tr in soup.select("tr:has(td)"):
        all_data.append(
            [
                h2.get_text(strip=True),
                sub.get_text(strip=True),
                *[td.get_text(strip=True) for td in tr.select("td")],
            ]
        )

# save data to CSV
df = pd.DataFrame(
    all_data,
    columns=[
        "title",
        "sub_title",
        "Rank",
        "Horse / Owner",
        "Points",
        "Total Comps",
    ],
)
print(df)
df.to_csv("data.csv", index=None)