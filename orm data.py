from tortoise.models import Model
from tortoise import Tortoise, fields, run_async
import asyncio
from tortoise.transactions import in_transaction
from testovoe import test_dict


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

async def init():
    await Tortoise.init(db_url='sqlite://data.db',
        modules={"models": ["__main__"]})
    Tortoise.generate_schemas()


if __name__ == "__main__":
    asyncio.run()