import mongoengine as me

from Fileapp.models.user import User
from Fileapp.utils.DocumentCreate import DocumentCreate


class Document(DocumentCreate):
    file_path = me.StringField(required=True)
    file_type = me.StringField()
    file_size = me.StringField()
    user = me.ReferenceField(User, reverse_delete_rule=me.DENY, required=True)
