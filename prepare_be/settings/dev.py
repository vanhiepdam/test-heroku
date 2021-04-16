# -*- coding: utf-8 -*-
from .base import *
import django_heroku

DEBUG = True
CORS_ORIGIN_WHITELIST = [
    'https://localhost:3000',
]
django_heroku.settings(locals())
