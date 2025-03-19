from tortoise import models, fields


class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50)
    password = fields.CharField(max_length=50)
    is_admin = fields.BooleanField()
    token = fields.CharField(max_length=50, null=True)
