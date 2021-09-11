from tortoise.models import Model
from tortoise import Tortoise, fields, run_async
import asyncio


class Stata(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    picksinrating = fields.IntField
    winsinrating = fields.IntField
    picksinturbo = fields.IntField
    winsinturbo = fields.IntField
    attr = fields.CharField(max_length=255)
    img = fields.CharField(max_length=255)


async def main():
    await Tortoise.init(db_url="sqlite://:memory:", modules={"models":["data"]})
    await Tortoise.generate_schemas()

    x = [Stata(name='1'), Stata(name='2')]
    await Stata.bulk_create(x)

asyncio.run(main())