import requests

url = "https://restcountries.com/v3.1/all"
resp = requests.get(url)
countries = resp.json()

cl = []
for c in countries:
    name = c['name']['common']
    capital = c.get('capital', ['Unknown'])
    capital = capital[0]
    region = c.get('region', 'Unknown')
    cl.append((name, capital, region))

for c in sorted(cl, key=lambda t: t[2]):
    print(f"{c[2]:20} {c[0]:50} {c[1]:30}")
