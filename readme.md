# Конфигурация сервера
## Учетные данные
### ISPmanager

Доступ к панели управления сервером:
[https://188.120.233.15:1500/ispmgr#/login](https://188.120.233.15:1500/ispmgr#/login)

## GitHub

- Основной репозиторий: [GitHub - dev](https://github.com/Islidexz/dev.git)
- Репозиторий для бэкапа: [GitHub - server_backup](https://github.com/Islidexz/server_backup.git)

## MySQL
Для корректной миграции установите InnoDB как движок хранения по умолчанию:

```sql
SET GLOBAL default_storage_engine = 'InnoDB';

# Активация виртуального окружения
cd /var/www/www-root/data/www/to-create.online/venv
source bin/activate 

# Добавление удаленного репозитория, если он еще не добавлен
# more 
git remote add origin https://github.com/Islidexz/dev.git

# Переход в директорию проекта
cd /var/www/www-root/data/www/to-create.online/nails

# Отправка изменений в основную ветку
git push -u origin main

# Получение последних изменений из основной ветки 
git pull origin main

# Установка основной ветки в качестве отслеживаемой
git branch --set-upstream-to=origin/main main

# Активация виртуального окружения
cd /var/www/www-root/data/www/to-create.online/venv
source bin/activate # Убедитесь, что путь к скрипту активации верный

# Добавление удаленного репозитория, если он еще не добавлен
git remote add origin https://github.com/Islidexz/dev.git

# Переход в директорию проекта
cd /var/www/www-root/data/www/to-create.online/nails

# Отправка изменений в основную ветку
git push -u origin main

# Получение последних изменений из основной ветки
git pull origin main

# Установка основной ветки в качестве отслеживаемой
git branch --set-upstream-to=origin/main main

# Просмотр состояния измененных файлов
git status

# Добавление всех измененных файлов в индекс
git add .

# Создание коммита с сообщением
git commit -m "Ваше сообщение о коммите"

# Откат до предыдущего коммита (например, если последний коммит содержит ошибки)
git revert HEAD

# Просмотр истории коммитов
git log

# Подключение к удаленному серверу по SSH
ssh user@188.120.233.15