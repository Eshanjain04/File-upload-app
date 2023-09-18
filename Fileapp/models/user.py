# -*- coding: utf-8 -*-
import mongoengine as me

from Fileapp.utils.DocumentCreate import DocumentCreate


class User(DocumentCreate):
    first_name = me.StringField(required=False)
    last_name = me.StringField(required=False)
    user_name = me.StringField(required=True)
    email = me.EmailField(required=True)
    password = me.StringField(required=True)
    documents = me.ListField()
