# environment_settings.py
import os
import socket

def set_django_settings_module():
    branch_name = os.popen('git rev-parse --abbrev-ref HEAD').read().strip()
    print(f"Текущая ветка: {branch_name}")
    if branch_name == 'production':
        print("Устанавливаем настройки для продакшена")
        # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.prod')
    else:
        print("Устанавливаем настройки для разработки")
        # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.dev')

set_django_settings_module()