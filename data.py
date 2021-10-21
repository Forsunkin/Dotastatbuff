from tortoise.models import Model
from tortoise import Tortoise, fields, run_async
from model import Stata
import asyncio

stringer = ''




async def run(obj):
    keys_win = ('1_win', '2_win', '3_win', '4_win', '5_win', '6_win', '7_win', '8_win')
    keys_pick = ('1_pick', '2_pick', '3_pick', '4_pick', '5_pick', '6_pick', '7_pick')
    hero_id = obj.get('id')
    name = obj.get('localized_name')
    picksinrating = sum([obj[key] for key in obj if key in keys_pick])
    winsinrating = sum([obj[key] for key in obj if key in keys_win])
    winrateinrating = '{:.1f}'.format((winsinrating / picksinrating) * 100)
    picksinturbo = obj.get('turbo_picks')
    winsinturbo = obj.get('turbo_wins')
    winrateinturbo = '{:.1f}'.format((winsinturbo / picksinturbo) * 100)
    attr = obj.get('primary_attr')
    img = obj.get('icon')

    await Tortoise.init(db_url='sqlite://data2.db',
                        modules={"models": ["model.py"]})
    await Tortoise.generate_schemas()

# Отправка переменных в базу
    await Stata(hero_id=hero_id, name=name, picksinrating=picksinrating, winrateinrating=winrateinrating).save()


# возвращает список со словорями, с ключами по типу: [{'name': 'Io', 'winrateinturbo': 45.7278810151158},{...}]
async def getturbo():
    await Tortoise.init(db_url='sqlite://data2.db',
                        modules={"models": ['data.py']})
    await Tortoise.generate_schemas()
    result = await Stata.all().values('name', 'winrateinturbo')
    return result

# форматирует список словарей в
def formattext(obj):
    string = ''
    for dict in obj:
        name = (dict['name'])
        wr = (dict['winrateinturbo'])
        wr_formater = "{0:.2f}"
        winrate = wr_formater.format(wr)
        values = f'{name:25} -    {winrate:10}\n'
        string = string + values
    return string



# if __name__ == '__main__':
asyncio.run(getturbo())