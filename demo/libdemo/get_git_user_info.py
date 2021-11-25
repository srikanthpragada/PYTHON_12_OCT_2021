
import requests
url = "https://api.github.com/users/srikanthpragada"
resp = requests.get(url)
if resp.status_code != 200:
    print('Sorry! Could not get details of user!')
    exit(0)

details = resp.json()   # Convert JSON to Dict
print(details['id'])
print(details['name'])
print(details['company'])
print(details['blog'])