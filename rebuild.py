from testovoe import test_response
from testovoe import pool_getvalues


def read_list(obj):
    for ll in obj:
        strtosql(ll)


def winrate_count(win, pick):
    winrate = win / pick
    format_winrate = '{:.1f}'.format(winrate * 100)
    return format_winrate


def games_counter(obj):
    keys_win = ('1_win', '2_win', '3_win', '4_win', '5_win', '6_win', '7_win', '8_win')
    keys_pick = ('1_pick', '2_pick', '3_pick', '4_pick', '5_pick', '6_pick', '7_pick')
    wins_public = (sum([obj[key] for key in obj if key in keys_win]))
    pick_public = (sum([obj[key] for key in obj if key in keys_pick]))
    return winrate_count(wins_public, pick_public)


def strtosql(obj):
    for key in pool_getvalues:
        print(obj[key])


read_list(test_response)