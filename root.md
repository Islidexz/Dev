# Конфигурация сервера

## Учетные данные

### ROOT доступ
- Пользователь: `root`
- Пароль: `verystrongly`

### MySQL Администратор
- Пользователь: `admin`
- Пароль: `verystronglysecret`

### Директория www-root
- Пользователь: `www-root`
- Пароль: `verystronglysecret \ verystrongly \ verystrong`

## Копирование на GitHub
- Репозиторий: [GitHub - dev](https://github.com/Islidexz/dev.git) Основной репозиторий
- Репозиторий для бэкапа: [GitHub - server_backup](https://github.com/Islidexz/server_backup)
- GitHub Token: `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`

### Команды Git для настройки удаленного репозитория
### Adds the repository as a remote origin commits can be pushed to it later
```bash

git push origin main
git pull origin main

git remote add origin https://github.com/Islidexz/dev.git
git push -u origin main

git remote add origin https://github.com/Islidexz/server_backup.git

git branch --set-upstream-to=origin/main main # Set main branch as upstream looking for changes from main

mv /var/www/www-root/data/www/to-create.online/nails
 /var/www/www-root/data/www/to-create.online/nails_backup

/var/www/www-root/data/www/to-create.online/nails

