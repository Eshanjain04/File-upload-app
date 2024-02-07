from Fileapp.utils.DocumentCreate import DocumentCreate
import mongoengine as me


class URL(DocumentCreate):
    target_url = me.URLField(required=True)
    uuid = me.StringField(max_length=10)

