Here's a step-by-step guide to installing Gunicorn and setting it up with Nginx as a reverse proxy for a Django application on Ubuntu:

Step 1: Install Gunicorn
First, ensure you have a virtual environment created and activated for your Django project:

Copy
Insert
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


sudo apt update
sudo apt install nginx
Step 4: Configure Nginx to Proxy Pass to Gunicorn
Create a new Nginx server block configuration file for your project:


sudo nano /etc/nginx/sites-available/myproject
Here is a sample configuration. Make sure to replace /path/to/your/django/project, server_name, myproject.sock, and other placeholders with your actual information:

Copy
Insert
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


sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
Test your Nginx configuration for syntax errors:


sudo nginx -t
If no errors are reported, restart Nginx to apply the changes:


sudo systemctl restart nginx


Step 5: Create a Gunicorn systemd Service File
Create a Gunicorn systemd service file for your project:

sudo nano /etc/systemd/system/gunicorn.service
Here's an example of what the file should look like:


sudo nano /etc/systemd/system/gunicorn.service
### [Unit]
Description=gunicorn daemon for myproject
After=network.target

### [Service]
User=username
Group=www-data
WorkingDirectory=/path/to/your/django/project
ExecStart=/path/to/your/virtualenv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/path/to/your/django/project/myproject.sock myproject.wsgi:application

### [Install]
WantedBy=multi-user.target
Replace username with your username and adjust paths and names as appropriate.

### Start and enable the Gunicorn service:

sudo systemctl start gunicorn
sudo systemctl enable gunicorn

Check the status to make sure everything is running smoothly:

sudo systemctl status gunicorn

Step 6: Final Steps and Verifications
Make sure your firewall allows traffic on port 80 (HTTP).
Double-check that your Django settings include correct STATIC_ROOT and MEDIA_ROOT settings, and run python manage.py collectstatic to collect static files.

Visit your domain name in a browser to ensure your Django application is being served by Gunicorn and proxied by Nginx.

Remember to secure your server, for example, by setting up an SSL/TLS certificate with Let's Encrypt.

This setup should give you a fully functioning Django application served by Gunicorn and fronted by Nginx on Ubuntu. Adjustments may be necessary based on your specific requirements and environment.