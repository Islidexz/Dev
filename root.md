# Конфигурация сервера

## Учетные данные

### Ispmgr
https://188.120.233.15:1500/ispmgr#/login



## GitHub
- Репозиторий: [GitHub - dev](https://github.com/Islidexz/dev.git) Основной репозиторий

- Репозиторий для бэкапа: [GitHub - server_backup](https://github.com/Islidexz/server_backup)


## MYSQL ### Fixes the default storage engine for transactions ENABLED to migrate properly
SET GLOBAL default_storage_engine = 'InnoDB';

### Команды Bash
```bash

### Activates the dev environment
cd /var/www/www-root/data/www/to-create.online/venv/bin 
source activate 
### Adds the repository as a remote origin commits can be pushed to it later

### Active dev environment
git remote add origin https://github.com/Islidexz/dev.git
### Connected to this remote
cd /var/www/www-root/data/www/to-create.online/nails

### Commands 
git push origin main
git pull origin main
 
git push -u origin main
### Same as above -u flag will create a tracking branch for the remote branch
git remote add origin git remote add origin https://github.com/Islidexz/dev.git

### Clean Backup
https://github.com/Islidexz/server_backup.git

git branch --set-upstream-to=origin/main main # Set main branch as upstream looking for changes from main

mv /var/www/www-root/data/www/to-create.online/nails
 /var/www/www-root/data/www/to-create.online/nails_backup

/var/www/www-root/data/www/to-create.online/nails

## Commands