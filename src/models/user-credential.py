from mongoengine import StringField, Document, ReferenceField, DateTimeField
import datetime
from src.db.db import *
from src.models import User

Mongo.connect()


class UserCredential(Document):
    password = StringField(required=True, max_length=100)
    last_login = DateTimeField(default=datetime.datetime.utcnow)
    user = ReferenceField(User)
