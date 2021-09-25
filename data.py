from tortoise.models import Model
from tortoise import Tortoise, fields, run_async
import asyncio
from tortoise.models import Model
from tortoise.transactions import in_transaction
from testovoe import test_dict

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


class Stata(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    picksinrating = fields.IntField
    winsinrating = fields.IntField
    winrateinrating = fields.IntField
    picksinturbo = fields.IntField
    winsinturbo = fields.IntField
    winrateinturbo = fields.IntField
    attr = fields.CharField(max_length=255)
    img = fields.CharField(max_length=255)


#test dict create values


async def past(id, name, picksinrating, winsinrating, winrateinrating, picksinturbo, winsinturbo,
               winrateinturbo, attr, img):

    await Tortoise.init(db_url='sqlite://data.db', modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()
    conn = Tortoise.get_connection("default")

    await conn.execute_query(f"""INSERT INTO STATA (id, name, picksinrating, winsinrating, winrateinrating, 
                                picksinturbo, winsinturbo, winrateinturbo, attr, img) 
                            VALUES ({id}, {name}, {picksinrating}, {winsinrating}, {winrateinrating}, 
                                {picksinturbo}, {winsinturbo}, {winrateinturbo}, {attr}, {img})""")


async def run():
    await Tortoise.init(db_url='sqlite://data_aue.db', modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()

    conn = Tortoise.get_connection("default")

    # Consider using execute_query_dict to get return values as a dict
    val = await conn.execute_query_dict("SELECT * FROM Stata")
    print(val)
    # Note that the result doesn't contain the rolled-back "Sheep" entry.


if __name__ == "__main__":
    asyncio.run(run())
