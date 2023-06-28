from peewee import Model, CharField, DateTimeField, ForeignKeyField
from datetime import datetime as dt
from playhouse.sqlite_ext import SqliteExtDatabase, JSONField
import shortuuid

db = SqliteExtDatabase(
    database="sano.db",
    pragmas=(("foreign_keys", 1),),  # Enforce foreign-key constraints.
)


class BaseModel(Model):
    id = CharField(primary_key=True, default=lambda: shortuuid.uuid())
    created_at = DateTimeField(default=lambda: dt.now())
    updated_at = DateTimeField(default=lambda: dt.now())

    def save(self, *args, **kwargs):
        self.updated_at = dt.now()
        return super(BaseModel, self).save(*args, **kwargs)

    def save_no_update(self, *args, **kwargs):
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        database = db


class User(BaseModel):
    email = CharField()
    phone_number = CharField()
    password_hash = CharField(255, null=True)
    name = CharField(null=True)
    address = JSONField(null=True)


class DNAKitOrder(BaseModel):
    sequencing_type = CharField()  # ex: whole-exome-sequencing, targeted-sequencing
    user = ForeignKeyField(User, backref="orders")
    shipping_info = JSONField()

    # TODO: how can we represent different states of an order? Ex: pending, in-progress, completed, etc.


def create_tables():
    with db:
        db.create_tables([User, DNAKitOrder], safe=True)
