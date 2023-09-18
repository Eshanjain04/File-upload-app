# -*- coding: utf-8 -*-
from mongoengine import connect

from settings.config import DATABASE_NAME
from settings.config import DATABASE_PASSWORD
from settings.config import DATABASE_USER


class MongoConnect:

    @staticmethod
    def connect_to_db():
        uri = f'mongodb+srv://{DATABASE_USER}:{DATABASE_PASSWORD}@ecom.bxh62ix.mongodb.net/?retryWrites=true&w=majority'
        connect(db=DATABASE_NAME, username=DATABASE_USER, password=DATABASE_PASSWORD, host=uri)
        print('DB is connected successfully.')
