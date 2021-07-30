import requests
import json

r = requests.get("https://api.opendota.com/api/heroStats")

renew_textbase = open('text_responeses.txt', 'w')
renew_textbase.write(r.text)
renew_textbase.close()
#Дописать выполнение скрипта по времени (например 2 раза в день)

def turbo(obj):
    json.loads()
    for hr in obj:
        winrate = hr['turbo_wins']/hr['turbo_picks'] *100
        print(winrate)

print(turbo(r.text))
