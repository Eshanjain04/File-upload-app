# -*- coding: utf-8 -*-
import json

from mongoengine import Document


class DocumentCreate(Document):
    meta = {
        'abstract': True,
    }

    @property
    def to_dict(self):
        return json.loads(self.to_json())
