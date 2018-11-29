from mongoengine import StringField, Document
from src.db.db import *

Mongo.connect()


class User(Document):
    email = StringField(required=True, max_length=100)
    first_name = StringField(required=True, max_length=50)
    last_name = StringField(required=True, max_length=50)
