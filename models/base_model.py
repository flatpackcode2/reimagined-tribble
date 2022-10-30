from playhouse.postgres_ext import PostgresqlExtDatabase
from playhouse.relfection import generate_models, print_model, print_table_sql

from peewee import *

db  = PostgresqlDatabase('local.db',user='postgres', password='password', host='127.0.0.1', port=5432)
models = generate_models(db)
print(list(models.items()))
globals().update(models)


class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.