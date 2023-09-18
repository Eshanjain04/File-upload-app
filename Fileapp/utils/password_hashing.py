# -*- coding: utf-8 -*-
from passlib.handlers.sha2_crypt import sha256_crypt


class Encrypt:

    @classmethod
    def encrypt(cls, plain_text):
        return sha256_crypt.encrypt(plain_text)

    @classmethod
    def decrypt(cls, plain_text, encrypted_text):
        return sha256_crypt.verify(plain_text, encrypted_text)
