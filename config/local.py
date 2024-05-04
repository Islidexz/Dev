# local.py
from .base import *

#DEBUG = False
DEBUG = True
IS_SERVER = False
print (f"DEBUG: {DEBUG}")
print (f"IS_SERVER: {IS_SERVER}")
# ... other production-specific settings

ALLOWED_HOSTS = ['to-create.online', 'www.to-create.online', 'localhost', '127.0.0.1', '[::1]']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'panel',
        'USER': 'admin',
        'PASSWORD': 'password',
        #'PASSWORD': 'verystronglysecret',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET default_storage_engine=InnoDB; SET collation_connection=utf8mb4_unicode_ci;"
        }
    }
}
# ... other development-specific unserversettings