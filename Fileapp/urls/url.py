from Fileapp.views.login import Login
from Fileapp.views.register import Register

urls = [
    ('user/register/', Register()),
    ('user/login/', Login()),
]
