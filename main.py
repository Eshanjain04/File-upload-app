# -*- coding: utf-8 -*-
from api_engine.db.mongo.connector.db_connector import MongoConnect
from api_engine.falcon.middlewares.falcon_db_logs import FalconDBLogs
from api_engine.falcon.url_manager.auto_urls import APP
from settings.config import CORS_ALLOWED
from settings.config import LOG_REQUEST_TO_DB
from settings.urls import all_urls

urls = all_urls

db_connection = MongoConnect.connect()

app = APP(
    url_list=urls,
    middleware=[
        FalconDBLogs(log_to_db=LOG_REQUEST_TO_DB)
    ],
    cors_enable=CORS_ALLOWED)
