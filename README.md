# Grafr
Python 3.8 + Django 3.2.5 implementation of telegra.ph/pastebin.com service.

Deployment (w/o Docker):
* apt install postgresql libssl-dev libpq-dev // python3.8-dev ? python3.8-venv ?
* git clone https://github.com/Lixeiden/Grafr.git
* python3.8 -m venv venv
* source ./venv/bin/activate
* pip install pip --upgrade // or pip install -U pip
* pip install -r requirements.txt
* passwd postgres + su postgres + psql
* CREATE DATABASE grafr_db OWNER grafr;  
  CREATE USER grafr WITH PASSWORD 'pass';   
  ALTER ROLE grafr SET client_encoding TO 'utf8';   
  ALTER ROLE grafr SET default_transaction_isolation TO 'read committed';   
  ALTER ROLE grafr SET timezone TO 'UTC';  
  exit, exit
* // export LANG=en_US.utf-8 + export LC_ALL=en_US.utf-8
* vim GrafrProj/GrafrProj/update_settings.py.sh
* cd GrafrProj/GrafrProj/ && source update_settings.py.sh && cd ../..
* vim GrafrProj/GrafrProj/settings.py
* python GrafrProj/manage.py migrate
* python GrafrProj/manage.py createsuperuser
* python GrafrProj/manage.py collectstatic
* vim GrafrProj/gunicorn_config.py
* export SECRET_KEY=''
* nginx configs/auth_basic + softlink + nginx -t + restart
* exec gunicorn  -c "/home/Grafr/GrafrProj/gunicorn_config.py" GrafrProj.wsgi // TODO: /etc/systemd/system/Grafr.service + systemctl start Grafr + systemctl status Grafr
* firewall: open ssh ???? & http 80 port