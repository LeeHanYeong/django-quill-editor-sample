from .base import *

DEBUG = True
WSGI_APPLICATION = 'config.wsgi.dev.application'
ALLOWED_HOSTS += [
    'localhost',
    '127.0.0.1',
]
