# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv

load_dotenv()

CORS_ALLOWED = os.environ['CORS_ALLOWED'].lower() == 'true'
RUNNING_PORT = os.environ.get('RUNNING_PORT')
DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASE_PORT = os.environ.get('DATABASE_PORT')
DATABASE_NAME = os.environ.get('DATABASE_NAME')
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
JWT_KEY = os.environ.get('JWT_KEY')
JWT_ALGORITHM = os.environ.get('JWT_ALGORITHM')
JWT_EXPIRY_DAYS = os.environ.get('JWT_EXPIRY_DAYS')
