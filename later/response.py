import requests
import json


r = requests.get("https://api.opendota.com/api/heroStats")
json_data = json.loads(r.text)
print(json_data)