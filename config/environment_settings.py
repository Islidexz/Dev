# environment_settings.py
import os
import socket

def set_django_settings_module():
    server_ip = '188.120.233.15'
    server_domain = 'to-create.online'

    current_ip = socket.gethostbyname(socket.gethostname())
    server_ip_by_domain = socket.gethostbyname(server_domain)

    if current_ip == server_ip or current_ip == server_ip_by_domain:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.prod')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.dev')