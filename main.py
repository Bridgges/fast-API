import requests
import json

r = requests.get('https://httpbin.org/get')

r_json = json.loads(r.text)


print(r_json)
