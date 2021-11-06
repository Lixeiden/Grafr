# Grafr
Python3.8 + Django3.2.5 project for my own implementation of telegra.ph service.

Deployment:
* `bash $: sudo apt install nginx python3.8 python3.8-dev libssl-dev libpq-dev postgresql`
* Set up PostgreSQL:
  `bash $: passwd postgres; su postgres; psql` 
  `psql #: CREATE DATABASE grafr_db OWNER grafr;
  CREATE USER grafr WITH PASSWORD 'dev_pass'; 
  ALTER ROLE lix SET client_encoding TO 'utf8'; 
  ALTER ROLE lix SET default_transaction_isolation TO 'read committed'; 
  ALTER ROLE lix SET timezone TO 'UTC';`
* Update **settings.py**, also use bash script **update_settings.py.sh**
* Update **settings.py** DB settings
* Update **gunicorn_config.py**
* Update **gunicorn_start.sh**, *optional:* set environment variable **$SECRET_KEY** `bash $: export SECRET_KEY=''`
