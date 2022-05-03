from tortoise import fields
from tortoise.models import Model


class Country(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    iso = fields.CharField(max_length=3)
    icon = fields.TextField()
    is_active = fields.BooleanField()
    additional_info = fields.TextField()
    surname = fields.CharField(max_length=111)

    class Meta:
        table = 'countries'
