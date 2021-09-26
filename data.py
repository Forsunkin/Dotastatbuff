# from tortoise.models import Model
# from tortoise import Tortoise, fields, run_async
# import asyncio
# from tortoise.models import Model
# from tortoise.transactions import in_transaction
# from testovoe import test_dict
#
#
# def create_simple_values(obj):
#     keys_win = ('1_win', '2_win', '3_win', '4_win', '5_win', '6_win', '7_win', '8_win')
#     keys_pick = ('1_pick', '2_pick', '3_pick', '4_pick', '5_pick', '6_pick', '7_pick')
#     id = obj.get('id')
#     name = obj.get('localized_name')
#     picksinrating = sum([obj[key] for key in obj if key in keys_pick])
#     winsinrating = sum([obj[key] for key in obj if key in keys_win])
#     winrateinrating = '{:.1f}'.format((winsinrating / picksinrating) * 100)
#     picksinturbo = obj.get('turbo_picks')
#     winsinturbo = obj.get('turbo_wins')
#     winrateinturbo = '{:.1f}'.format((winsinturbo / picksinturbo) * 100)
#     attr = obj.get('primary_attr')
#     img = obj.get('icon')
#
#     print(id, name, picksinrating, winrateinrating, picksinturbo, winsinturbo, winrateinturbo, attr, img)
#
#
# class Stata(Model):
#     id = fields.IntField(pk=True)
#     name = fields.CharField(max_length=255)
#     picksinrating = fields.IntField
#     winsinrating = fields.IntField
#     winrateinrating = fields.IntField
#     picksinturbo = fields.IntField
#     winsinturbo = fields.IntField
#     winrateinturbo = fields.IntField
#     attr = fields.CharField(max_length=255)
#     img = fields.CharField(max_length=255)
#
#
# pool_getvalues = ['id', 'localized_name', 'turbo_picks', 'turbo_wins', 'primary_attr', 'icon']
#
# test_dict_sorted = {'id': 129, 'name': 'Mars', 'picksinrating': 999, 'winsinrating': 555, 'winrateinrating': 55.0,
#                     'picksinturbo': 999, 'winsinturbo': 55, 'winrateinturbo': 55.0, 'attr': 'str', 'img': 'http//...'}
#
#
# async def paste(id, name, picksinrating, winsinrating, winrateinrating, picksinturbo, winsinturbo,
#                winrateinturbo, attr, img):
#
#     await Tortoise.init(db_url='sqlite://data.db', modules={"models": ["__main__"]})
#     await Tortoise.generate_schemas()
#     conn = Tortoise.get_connection("default")
#
#     await conn.execute_query(f"""INSERT INTO STATA (id, name, picksinrating, winsinrating, winrateinrating,
#                                 picksinturbo, winsinturbo, winrateinturbo, attr, img)
#                             VALUES ({id}, {name}, {picksinrating}, {winsinrating}, {winrateinrating},
#                                 {picksinturbo}, {winsinturbo}, {winrateinturbo}, {attr}, {img})""")
#
#
# if __name__ == "__main__":
#     asyncio.run(paste(**test_dict_sorted))
