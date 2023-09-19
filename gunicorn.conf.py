# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv

load_dotenv()
bind = '127.0.0.1:' + os.environ.get('PORT', str(5000))
