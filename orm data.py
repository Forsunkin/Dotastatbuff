from tortoise.models import Model
from tortoise import Tortoise, fields, run_async
import asyncio
from tortoise.transactions import in_transaction
from testovoe import test_dict


class Stata(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    picksinrating = fields.IntField()
    winsinrating = fields.IntField()
    winrateinrating = fields.IntField()
    picksinturbo = fields.IntField()
    winsinturbo = fields.IntField()
    winrateinturbo = fields.IntField()
    attr = fields.CharField(max_length=255)
    img = fields.CharField(max_length=255)


async def run():
    await Tortoise.init(db_url='sqlite://data.db',
                        modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()

    await Stata(id=1, name="Test 2").save()


if __name__ == "__main__":
    asyncio.run(run())