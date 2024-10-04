from peewee import Model, CharField, DateTimeField
import datetime
from database.database import db

class Cliente(Model):
    nome = CharField(100)
    email = CharField(100)
    data_registro = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db