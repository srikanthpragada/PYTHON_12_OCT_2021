import requests
from bs4 import BeautifulSoup

URL = "http://www.srikanthtechnologies.com/"

resp = requests.get(URL)
if resp.status_code != 200:
    print("Sorry! Could not access website")
    exit(1)

bs = BeautifulSoup(resp.text, "html.parser")
anchors = bs.find_all("a")
for a in anchors:
    text = a.text.strip()
    if len(text) == 0:
        continue

    if 'href' in a.attrs:
        href = a['href']
    else:
        continue  # Ignore anchor

    if href == '#':
        continue

    if not href.startswith("http"):
        href = URL + href

    print(text)
    print(href)
    print('-' * 80)
