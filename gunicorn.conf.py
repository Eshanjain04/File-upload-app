# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv

load_dotenv()
bind = '0.0.0.0:' + os.environ.get('PORT', str(5000))
