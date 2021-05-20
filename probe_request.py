

import requests


url = 'http://127.0.0.1:8000/api/'


with open('deals2.csv', 'rb') as f:
    r = requests.post(url, files={'deals': f})
    print(r.json())



r = requests.get(url)
for i in r:
    print(i.decode('utf-8'))



