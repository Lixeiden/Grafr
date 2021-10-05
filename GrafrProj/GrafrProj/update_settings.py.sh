sed -i "s/DEBUG\ =\ True/DEBUG\ =\ False/g" settings.py
sed -i "s/ALLOWED_HOSTS\ =\ \[\]/ALLOWED_HOSTS\ =\ \['188.120.246.47','127.0.0.1',\]/g" settings.py
