from tortoise.models import Model
from tortoise import Tortoise, fields


class Stata(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, null=True)
    picksinrating = fields.IntField(null=True)
    winsinrating = fields.IntField(null=True)
    winrateinrating = fields.FloatField(null=True)
    picksinturbo = fields.IntField(null=True)
    winsinturbo = fields.IntField(null=True)
    winrateinturbo = fields.FloatField(null=True)
    attr = fields.CharField(max_length=255, null=True)
    img = fields.CharField(max_length=255, null=True)