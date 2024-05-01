###
supervisorctl reload  
supervisorctl status
supervisorctl start gunicorn
supervisorctl stop gunicorn

gunicorn --workers 3 myproject.wsgi:application
#more


gunicorn --workers 3 myproject.wsgi:application --bind 0.0.0.0:8000

Команда gunicorn запускает WSGI-совместимое приложение с использованием Gunicorn, который является простым и мощным сервером HTTP для Python-приложений. Давайте разберем указанную команду по частям:

### Gunicorn — вызов исполняемого файла Gunicorn. Это команда, которую вы вводите в терминале для запуска сервера.

### --workers 3 — параметр, который указывает Gunicorn создать три рабочих процесса для обработки запросов. 

Количество рабочих процессов определяет, сколько параллельных запросов может обрабатывать сервер. Обычно это число настраивают в зависимости от количества ядер процессора на сервере.


### myproject.wsgi:application — путь к WSGI-приложению, который Gunicorn будет служить.
В данном случае myproject.wsgi означает, что Gunicorn должен импортировать модуль wsgi из пакета myproject, а application — это объект приложения WSGI, который определен в этом модуле и который будет использоваться Gunicorn для запуска приложения.

### --bind 0.0.0.0:8000 — параметр, который говорит Gunicorn привязать сервер к адресу 0.0.0.0 на порту 8000. Адрес 0.0.0.0 означает, что сервер будет доступен на всех IP-адресах устройства, что делает его доступным извне. Порт 8000 является портом, к которому будут поступать HTTP-запросы.

### В итоге, данная команда запускает ваше Django-приложение с помощью Gunicorn на порту 8000 с тремя рабочими процессами, делая его доступным для внешних запросов. На сколько хватит трех воркеров? Оно может быть достаточно мощным для обработки большого количества запросов на вашем сервере. Хватит ли одного воркера? Да. Вот тут оно просто: 

### sudo systemctl status gunicorn
### sudo systemctl restart gunicorn


### Step 1: Install Gunicorn

First, ensure you have a virtual environment created and activated for your Django project:

python3 -m venv myenv
source myenv/bin/activate
Now, install Gunicorn within the virtual environment:

### Ubuntu
pip install gunicorn

Step 2: Test Gunicorn's Ability to Serve Your Django Project
Before configuring Nginx, you should verify that Gunicorn can serve your Django application:


cd /path/to/your/django/project #
gunicorn --workers 3 myproject.wsgi:application
Replace myproject with your Django project's name. You should see Gunicorn starting up. Test by going to http://127.0.0.1:8000 in your browser.

Step 3: Install Nginx
Now, install Nginx using apt:


### sudo apt update
### sudo apt install nginx

### Step 4: Configure Nginx to Proxy Pass to Gunicorn
Create a new Nginx server block configuration file for your project:


### sudo nano /etc/nginx/sites-available/myproject
Here is a sample configuration. Make sure to replace /path/to/your/django/project, server_name, myproject.sock, and other placeholders with your actual information:

server {
    listen 80;
    server_name example.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /path/to/your/django/project;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/path/to/your/django/project/myproject.sock;
    }
}
Now, enable the file by linking it to the sites-enabled directory:


### sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
Test your Nginx configuration for syntax errors:


### sudo nginx -t
If no errors are reported, restart Nginx to apply the changes:

### sudo systemctl restart nginx


### Step 5: Create a Gunicorn systemd Service File
### sudo nano /etc/systemd/system/gunicorn.service

### [Unit]
Description=gunicorn daemon for myproject
After=network.target

### [Service]
User=root
Group=www-data
WorkingDirectory=/path/to/your/django/project
ExecStart=/path/to/your/virtualenv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/path/to/your/django/project/myproject.sock myproject.wsgi:application

### [Install]
WantedBy=multi-user.target
Replace username with your username and adjust paths and names as appropriate.

### Start and enable the Gunicorn service:

sudo systemctl start gunicorn
sudo systemctl enable gunicorn
