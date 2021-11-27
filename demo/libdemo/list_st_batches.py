import requests
from bs4 import BeautifulSoup

URL = "http://www.srikanthtechnologies.com/"

resp = requests.get(URL)
if resp.status_code != 200:
    print("Sorry! Could not access website")
    exit(1)

bs = BeautifulSoup(resp.text, "html.parser")
batch_table = bs.find(id="wctl00_ContentPlaceHolder1_GridVie2")
rows = batch_table.find_all("tr")
for row in rows[1:]:
    cols = row.find_all("td")
    print(cols[0].text)