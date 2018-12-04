from src.models.user_credential import *
from src.db.db import *
from mongoengine import StringField, Document, ReferenceField

Mongo.connect()


class UserDetail(Document):
    email = StringField(required=True, max_length=100)
    first_name = StringField(required=True, max_length=50)
    last_name = StringField(required=True, max_length=50)
    user = ReferenceField(UserCredential)
