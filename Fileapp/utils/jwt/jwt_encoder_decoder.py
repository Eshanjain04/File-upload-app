# -*- coding: utf-8 -*-
import datetime
from settings import config
import jwt


class JWTManager:

    def __init__(self, expiry_time=None):
        self.key = config.JWT_KEY
        self.algorithm = config.JWT_ALGORITHM
        if not expiry_time:
            self.expiry_time = datetime.datetime.utcnow() + datetime.timedelta(days=config.JWT_EXPIRY_DAYS)
        else:
            self.expiry_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=expiry_time)

    def encode(self, payload):
        try:
            payload['exp'] = self.expiry_time
            return jwt.encode(payload=payload, key=self.key, algorithm=self.algorithm)
        except TypeError:
            return None

    def decode(self, encoded_jwt: str):
        try:
            return jwt.decode(encoded_jwt, key=self.key, algorithms=[self.algorithm])
        except (jwt.exceptions.InvalidSignatureError,
                jwt.exceptions.DecodeError,
                jwt.exceptions.ExpiredSignatureError):
            return None
