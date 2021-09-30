from testovoe import test_dict

#
# class Values(BaseModel):
#     id: int
#     localized_name = ''
#     turbo_picks = 0
#     turbo_wins = 0
#
# dict_with_values = Values(**test_dict)
# print(dict_with_values.id)
# print(dict_with_values.turbo_picks)
# print(dict_with_values.dict())


def create_simple_values(obj):
    keys_win = ('1_win', '2_win', '3_win', '4_win', '5_win', '6_win', '7_win', '8_win')
    keys_pick = ('1_pick', '2_pick', '3_pick', '4_pick', '5_pick', '6_pick', '7_pick')
    id = 1
    name =1
    picksinrating = sum([obj[key] for key in obj if key in keys_pick])
    winsinrating = sum([obj[key] for key in obj if key in keys_win])
    winrateinrating = '{:.1f}'.format((winsinrating / picksinrating) * 100)
    picksinturbo = obj.get('turbo_picks')
    winsinturbo = obj.get('turbo_wins')
    winrateinturbo = '{:.1f}'.format((winsinturbo / picksinturbo) * 100)
    attr = obj.get('primary_attr')
    img = obj.get('icon')

    print(id, name, picksinrating, winrateinrating, picksinturbo, winsinturbo, winrateinturbo, attr, img)

def ss(obj):
    for s in obj:
        create_simple_values(s)

ss(test_dict)