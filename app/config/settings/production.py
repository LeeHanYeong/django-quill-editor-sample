from .base import *

DEBUG = True
WSGI_APPLICATION = 'config.wsgi.production.application'
ALLOWED_HOSTS += [
    'django-quill.localhost',
    'django-quill.lhy.kr',
]
