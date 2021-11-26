import requests

url = "https://restcountries.com/v3.1/all"
resp = requests.get(url)
countries = resp.json()

for c in sorted(countries, key=lambda d: d['population'], reverse=True)[:10]:
    name = c['name']['common']
    population = c.get('population', 0)
    print(f"{name:50} {population:20}")
