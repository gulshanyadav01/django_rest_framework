import requests

URL = 'http://127.0.0.1:5000/stuinfo/2'

r = requests.get(url=URL)
data = r.json()
print(data)
