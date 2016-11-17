from peewee import SqliteDatabase, Model, CharField


db = SqliteDatabase('data.db')


# Class for Company database
class Company(Model):
    name = CharField()
    id = CharField()

    class Meta:
        database = db


# Class for Material database
class Material(Model):
    mat_name = CharField()
    mat_id = CharField()
    comp_id = CharField()
    description = CharField()
    notes = CharField()
    supplier = CharField()
    price = CharField()
    currency = CharField()

    class Meta:
        database = db