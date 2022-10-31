from email.headerregistry import ContentDispositionHeader
from peewee import *
from playhouse.db_url import connect

import datetime

db = connect('postgresql://postgres:password@portcast_db:5432/local')
class BaseModel(Model):
    created_at = DateTimeField(default=datetime.datetime.now)

    def validate(self):
        print(
            f"Warning validation method not implemented for {str(type(self))}"
        )
        return True
    class Meta:
        database =db
        legacy_table_names=False

