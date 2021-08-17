import json
import sqlite3
from sql import Database


import time

named_date = time.localtime()
time_string = time.strftime('%d_%m_%Y_%H')



se = open(f'text_responses_{time_string}.txt', 'r')

with open(f'text_responses_{time_string}.txt') as f:
      d = json.load(f)
      print(d)


test_request = d
test_dict = {'id': 129, 'name': 'npc_dota_hero_mars', 'localized_name': 'Mars', 'primary_attr': 'str', 'attack_type': 'Melee',
      'roles': 'Carry', 'img': '/apps/dota2/images/heroes/mars_full.png?',
      'icon': '/apps/dota2/images/heroes/mars_icon.png', 'base_health': 200, 'base_health_regen': None, 'base_mana': 75,
      'base_mana_regen': 0.5, 'base_armor': -1, 'base_mr': 25, 'base_attack_min': 29, 'base_attack_max': 37,
      'base_str': 23, 'base_agi': 20, 'base_int': 21, 'str_gain': 3.4, 'agi_gain': 1.7, 'int_gain': 2.2,
      'attack_range': 250, 'projectile_speed': 900, 'attack_rate': 1.8, 'move_speed': 310, 'turn_rate': 0.8,
      'cm_enabled': True, 'legs': 2, 'hero_id': 129, 'turbo_picks': 268334, 'turbo_wins': 128670, 'pro_win': 166,
      'pro_pick': 362, 'pro_ban': 513, '1_pick': 9845, '1_win': 4574, '2_pick': 22059, '2_win': 10438, '3_pick': 35454,
      '3_win': 16840, '4_pick': 39620, '4_win': 18945, '5_pick': 29048, '5_win': 13738, '6_pick': 15681, '6_win': 7555,
      '7_pick': 7716, '7_win': 3756, '8_pick': 2976, '8_win': 1394, 'null_pick': 1544841, 'null_win': 0}

pool_getvalues = ['id', 'localized_name', 'pick', 'win', 'winrate', 'turbo_pick', 'turbo_win', 'turbowinrate', 'attr', 'img']

test_dict_sorted = {'id': 129, 'name': 'Mars', 'pick': 999, 'win': 555, 'winrate': 55.0, 'turbopick': 999, 'turbowin': 55,
      'turbowinrate': 55.0, 'attr': 'str', 'img': 'http//...'}


for tt in test_request:
      pass
      #print(tt)

