# -*- coding: utf-8 -*-
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
DEBUG = os.environ['DEBUG'].lower() == 'true'
LOG_REQUEST_TO_DB = os.environ['LOG_REQUEST_TO_DB'].lower() == 'true'
CORS_ALLOWED = os.environ['CORS_ALLOWED'].lower() == 'true'
RUNNING_PORT = os.environ['RUNNING_PORT']
DATABASE_USER = os.environ['DATABASE_USER']
DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
DATABASE_URL = os.environ['DATABASE_URL']
DATABASE_PORT = os.environ['DATABASE_PORT']
DATABASE_NAME = os.environ['DATABASE_NAME']
DATABASE_URI = f'mongodb://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_URL}:' \
               f'{DATABASE_PORT}/{DATABASE_NAME}?authSource=admin'
if DATABASE_USER == '':
    DATABASE_URI = f'mongodb://{DATABASE_URL}:{DATABASE_PORT}/{DATABASE_NAME}'
# SENTRY_URI = os.environ['SENTRY_URI']
JWT_KEY = os.environ['JWT_KEY']
JWT_EXPIRY_DAYS = int(os.environ['JWT_EXPIRY_DAYS'])
LOGIN_EXPIRY_SECONDS = int(os.environ['LOGIN_EXPIRY_SECONDS'])
JWT_ALGORITHM = os.environ['JWT_ALGORITHM']
GUNICORN_WORKER = os.environ['GUNICORN_WORKER']
AWS_ACCESS_KEY_ID = os.environ['AWS_S3_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_S3_SECRET_ACCESS_KEY']
AWS_BUCKET_NAME = os.environ['AWS_BUCKET_NAME']
FRONTEND_KEY_FOR_ENCRYPTION = os.environ.get('FRONTEND_KEY_FOR_ENCRYPTION', 'add key')
GUNICORN_TIMEOUT = os.environ.get('GUNICORN_TIMEOUT', 50)
DO_S3_ACCESS_KEY = os.environ.get('DO_S3_ACCESS_KEY')
DO_S3_SECRET_ACCESS_KEY = os.environ.get('DO_S3_SECRET_ACCESS_KEY')
DO_BUCKET_NAME = os.environ.get('DO_BUCKET_NAME', 'finverv')
DO_UPLOAD_PATH = os.environ.get('DO_UPLOAD_PATH', 'business-loan')
DO_UPLOAD_REGION = os.environ.get('DO_UPLOAD_REGION', 'BLR1')
DO_UPLOAD_ENDPOINT = os.environ.get('DO_UPLOAD_ENDPOINT', 'https://blr1.digitaloceanspaces.com')
FERNET_KEY = os.environ.get('FERNET_KEY')
SELF_SERVE_KEY_FOR_ENCRYPTION = os.environ.get('SELF_SERVE_KEY_FOR_ENCRYPTION')
INTEGRATION_ENGINE_BASE_URL = os.environ.get('INTEGRATION_ENGINE_BASE_URL', 'http://127.0.0.1:14799')


def get_project_root() -> Path:
    return Path(__file__).parent
