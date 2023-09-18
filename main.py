# -*- coding: utf-8 -*-
from app import APP
from db_connection import MongoConnect

from settings.config import CORS_ALLOWED
from settings.urls import all_urls

urls = all_urls

db_connection = MongoConnect.connect_to_db()

app = APP(
    url_list=urls,
    middleware=[

    ],
    cors_enable=CORS_ALLOWED)
