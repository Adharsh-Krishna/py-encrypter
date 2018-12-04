from mongoengine import StringField, Document, DateTimeField
import datetime
from src.db.db import *

Mongo.connect()


class UserCredential(Document):
    password = StringField(required=True, max_length=100)
    last_login = DateTimeField(default=datetime.datetime.utcnow)
    user_name = StringField(required=True, max_length=20)


