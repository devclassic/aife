from tortoise import models, fields


# 用户
class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255)
    password = fields.CharField(max_length=255)
    is_admin = fields.BooleanField()
    token = fields.CharField(max_length=255, null=True)


# 应用
class App(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    appid = fields.CharField(max_length=255)
    token = fields.CharField(max_length=255)


# 账户
class Account(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    account = fields.CharField(max_length=255)
    password = fields.CharField(max_length=255)
    token = fields.CharField(max_length=255, null=True)
    apps = fields.CharField(max_length=1000, null=True)


# 字典
class Dict(models.Model):
    id = fields.IntField(pk=True)
    key = fields.CharField(max_length=255)
    value = fields.CharField(max_length=5000)
