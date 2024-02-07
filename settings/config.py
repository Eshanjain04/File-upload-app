# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv

load_dotenv()

# file to handle env variables, exclude need to import dotenv package everywhere
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
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_BUCKET_NAME = os.environ.get('AWS_BUCKET_NAME')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_REGION_NAME = os.environ.get('AWS_REGION_NAME')
AWS_S3_BASE_URL = os.environ.get('AWS_S3_BASE_URL')
BASE_URL_LOCAL = os.environ.get('BASE_URL_LOCAL')
BASE_URL_DEPLOY = os.environ.get('BASE_URL_DEPLOY')
