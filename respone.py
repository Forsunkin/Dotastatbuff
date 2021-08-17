import requests
import json
import time

named_date = time.localtime()
time_string = time.strftime('%d_%m_%Y_%H')


r = requests.get("https://api.opendota.com/api/heroStats")
json_data = json.loads(r.text)


def bu_text():
    with open(f'text_responses_{time_string}.txt', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)




