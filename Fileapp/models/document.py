import mongoengine as me

from Fileapp.models.user import User
from Fileapp.utils.DocumentCreate import DocumentCreate


class Document(DocumentCreate):        # document model to store document data
    active = me.BooleanField(default=True)
    file_path = me.StringField(required=True)
    file_type = me.StringField()
    file_size = me.StringField()
    file_name = me.StringField()
    short_url = me.StringField()
    user = me.ReferenceField(User, reverse_delete_rule=me.DENY, required=True)    # one to one field
