from Fileapp.views.document_delete import DocumentDelete
from Fileapp.views.document_list import DocumentList
from Fileapp.views.document_upload import DocUpload
from Fileapp.views.login import Login
from Fileapp.views.register import Register
from Fileapp.views.short_url_redirect import URLRedirect
# list of all apis
urls = [
    ('user/register/', Register()),
    ('user/login/', Login()),
    ('upload/document/', DocUpload()),
    ('document/list/', DocumentList()),
    ('document/{pk}/delete/', DocumentDelete()),
    ('{url_key}/', URLRedirect()),

]
