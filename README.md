# Grafr
Python3.8 + Django3.2.5 project for my own implementation of telegra.ph service.

Deployment:
* Update settings.py, *also use script update_settings.py.sh*
* Update gunicorn_config.py
* Update gunicorn_start.sh
* *Optional:* Set environment variable $SECRET_KEY `bash $: export SECRET_KEY=''`
