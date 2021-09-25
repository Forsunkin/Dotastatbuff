from testovoe import test_dict

keys_win = ('1_win', '2_win', '3_win', '4_win', '5_win', '6_win', '7_win', '8_win')
keys_pick = ('1_pick', '2_pick', '3_pick', '4_pick', '5_pick', '6_pick', '7_pick')
def create(obj):
    id = test_dict.get('id')
    name = obj.get('localized_name')
    picksinrating = sum([obj[key] for key in obj if key in keys_pick])
    winsinrating = sum([obj[key] for key in obj if key in keys_win])
    winrateinrating = '{:.1f}'.format((winsinrating / picksinrating) * 100)
    picksinturbo = obj.get('turbo_picks')
    winsinturbo = obj.get('turbo_wins')
    winrateinturbo = '{:.1f}'.format((winsinturbo / picksinturbo) * 100)
    attr = obj.get('primary_attr')
    img = obj.get('icon')

    print(id, name, picksinrating, winrateinrating, picksinturbo, winsinturbo, winrateinturbo, attr, img)

create(test_dict)