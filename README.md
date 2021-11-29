# Grafr
Python 3.8 + Django 3.2.5 implementation of telegra.ph/pastebin.com service.

Deployment (w/o Docker):
* Install packages: `bash $: sudo apt install nginx python3.8 python3.8-dev libssl-dev libpq-dev postgresql`
* Get Project: `bash $: git pull Grafr`
* Set up venv: `bash $: python3.8 -m venv venv;
source ./venv/bin/activate;
pip install -U pip;
pip install -r requirements.txt;`
* Set up PostgreSQL:
  `bash $: passwd postgres; su postgres; psql` 
  `psql #: CREATE DATABASE grafr_db OWNER grafr;
  CREATE USER grafr WITH PASSWORD 'dev_pass'; 
  ALTER ROLE lix SET client_encoding TO 'utf8'; 
  ALTER ROLE lix SET default_transaction_isolation TO 'read committed'; 
  ALTER ROLE lix SET timezone TO 'UTC';`
  `bash $: python manage.py migrate; python manage.py createsuperuser`
* Configure locales: `bash $: export LANG=en_US.utf-8; export LC_ALL=en_US.utf-8`
* Update **settings.py**, also use bash script **update_settings.py.sh**
* Update **settings.py** DB settings
* Update **gunicorn_config.py**
* Update **gunicorn_start.sh**, *optional:* set environment variable **$SECRET_KEY** `bash $: export SECRET_KEY=''`
* Collect static files: `bash $: python manage.py collectstatic`
