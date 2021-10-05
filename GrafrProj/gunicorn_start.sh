#export SECRET_KEY=''
source /home/lix/Grafr/venv/bin/activate
exec gunicorn  -c "/home/lix/Grafr/GrafrProj/gunicorn_config.py" GrafrProj.wsgi
