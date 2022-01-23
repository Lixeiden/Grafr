#export SECRET_KEY=''
source ../venv/bin/activate
exec gunicorn  -c "/home/lix/Grafr/GrafrProj/gunicorn_config.py" GrafrProj.wsgi
