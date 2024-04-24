# environment_settings.py
import os
from config.base import BASE_DIR

def set_django_settings_module():
    # Специфичная часть пути для сервера
    server_path_segment = 'www/to-create.online/nails'
    # Получаем имя текущей ветки Git
    branch_name = os.popen('git rev-parse --abbrev-ref HEAD').read().strip()
    # Получаем абсолютный путь к директории, где находится manage.py
    base_dir = os.path.dirname(os.path.abspath(__file__))

    print(f"Текущая ветка: {branch_name}")
    print(f"BASE_DIR: {BASE_DIR}")

    # Проверяем имя ветки и путь
    if server_path_segment in base_dir.replace('\\', '/'):
        print("------PRODUCTION: Устанавливаем настройки для PRODUCTION--------")
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.prod')
    #elif branch_name == 'main' and server_path_segment in base_dir.replace('\\', '/'):
    #    print("------PRODUCTION: Устанавливаем настройки для PRODUCTION по пути--------")
    #    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.prod')
    else:
        print("--------LOCAL: Устанавливаем настройки для LOCAL----------")
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.local')

# Вызываем функцию в manage.py
if __name__ == '__main__':
    set_django_settings_module()

    # Остальной код manage.py...