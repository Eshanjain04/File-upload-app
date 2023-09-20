from Fileapp.views.document_list import DocumentList
from Fileapp.views.document_upload import DocUpload
from Fileapp.views.login import Login
from Fileapp.views.register import Register
# list of all apis
urls = [
    ('user/register/', Register()),
    ('user/login/', Login()),
    ('upload/document/', DocUpload()),
    ('document/list/', DocumentList()),

]
