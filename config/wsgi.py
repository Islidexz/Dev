import os
from django.core.wsgi import get_wsgi_application
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.dev')
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.prod')

if os.getenv('HTTPS') == 'on':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.prod')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.dev')

application = get_wsgi_application()
print(os.environ['DJANGO_SETTINGS_MODULE'])