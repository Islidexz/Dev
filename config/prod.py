# prod.py
from .base import *

#this loads if we on server
DEBUG = False
IS_SERVER = True
# ... other production-specific settings

ALLOWED_HOSTS = ['to-create.online', 'www.to-create.online', 'localhost', '127.0.0.1', '[::1]']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'panel',
        'USER': 'admin',
        'PASSWORD': 'verystronglysecret',
        'HOST': 'localhost',
        'PORT': '3306',
        'ATOMIC_REQUESTS': True,
        'OPTIONS': {
            'init_command': "SET default_storage_engine=InnoDB; SET collation_connection=utf8mb4_unicode_ci;"
        }
    }
}