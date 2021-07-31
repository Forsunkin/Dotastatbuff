import requests
import json

r = requests.get("https://api.opendota.com/api/heroStats")
json_data = json.loads(r.text)
text_data = open('text_responses.txt', 'w')
text_data.write(str(json_data))
text_data.close()
