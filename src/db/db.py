from mongoengine import connect
from src import constants


class Mongo:
    __connection = None

    def __init__(self):
        if Mongo.__connection is not None:
            raise Exception("Cannot create new connection.")
        else:
            Mongo.__connection = connect(constants.DB_NAME)

    @staticmethod
    def connect():
        if Mongo.__connection is None:
            Mongo()
        return Mongo.__connection
