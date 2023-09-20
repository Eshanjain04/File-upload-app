# -*- coding: utf-8 -*-
import datetime
from settings import config
import jwt


class JWTManager:  # Class to handle JWT Functions

    def __init__(self, expiry_time=None):
        self.key = config.JWT_KEY
        self.algorithm = config.JWT_ALGORITHM
        if not expiry_time:
            self.expiry_time = datetime.datetime.utcnow() + datetime.timedelta(
                days=int(config.JWT_EXPIRY_DAYS))  # if given expiry time in env
        else:
            self.expiry_time = datetime.datetime.utcnow() + datetime.timedelta(
                seconds=expiry_time)  # if given expiry time as parameters

    def encode(self, payload):  # function to encrypt the data
        try:
            payload['exp'] = self.expiry_time
            return jwt.encode(payload=payload, key=self.key, algorithm=self.algorithm)
        except TypeError:
            return None

    def decode(self, encoded_jwt: str):  # function to decrypt the data
        try:
            return jwt.decode(encoded_jwt, key=self.key, algorithms=[self.algorithm])
        except (jwt.exceptions.InvalidSignatureError,
                jwt.exceptions.DecodeError,
                jwt.exceptions.ExpiredSignatureError):
            return None
