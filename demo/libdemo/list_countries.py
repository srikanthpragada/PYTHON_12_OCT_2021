import requests

url = "https://restcountries.com/v3.1/all"
resp = requests.get(url)
countries = resp.json()

for c in countries:
    name = c['name']['common']
    capital = c.get('capital', ['Unknown'])
    capital = capital[0]
    region = c.get('region', 'Unknown')
    print(f"{name:50} {capital:30}  {region:20}")
