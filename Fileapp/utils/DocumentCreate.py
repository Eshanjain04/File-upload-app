# -*- coding: utf-8 -*-
import json

from mongoengine import Document


class DocumentCreate(
    Document):  # class extending Document class of mongoengine, to add custom methods in models if needed
    meta = {
        'abstract': True,
    }

    @property
    def to_dict(self):
        return json.loads(self.to_json())
