import requests
import json

r = requests.get("https://api.opendota.com/api/heroStats")
json_data = json.loads(r.text)
#print(json_data)

def heroes_id(obj):
    for dx in obj:
        winrate = dx['turbo_wins']/dx['turbo_picks'] *100
        print(winrate)
     #   if 'id' in dx.keys():
    #       print(f"{dx['localized_name']} {('{:.2f}').format(dx['turbo_wins']/dx['turbo_picks'] *100)}")

heroes_id(json_data)

