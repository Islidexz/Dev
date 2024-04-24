# wsgi.py
#import os
from django.core.wsgi import get_wsgi_application
from environment_settings import set_django_settings_module

set_django_settings_module()

application = get_wsgi_application()