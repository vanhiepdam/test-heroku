# -*- coding: utf-8 -*-
from .base import *

CORS_ALLOW_ALL_ORIGINS = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hiep-todo',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}
