from urllib.request import urlopen
import json

url = "https://www.parl.ca/legisinfo/en/bills/json"

response = urlopen(url)

data_json = json.loads(response.read())

print(data_json)