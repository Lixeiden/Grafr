server {
	listen 80;
	server_name grafr.ru www.grafr.ru;
	
#	listen [::]:80;
#	root /var/www/html;
#	index index.html index.htm index.nginx-debian.html;
	
	location = /favicon.ico { alias /home/lix/Grafr/favicons/favicon.ico; access_log off; log_not_found off; }

	location /static/ {
	        root /home/lix/Grafr/GrafrProj;
	}

	location / {
		proxy_pass http://127.0.0.1:8001;
		proxy_set_header X-Forwarded-Host $server_name;
		proxy_set_header X-Real-IP $remote_addr;
		add_header P3P 'CP="ALL DSP COR PSAa PSDa OUR NOR ONL UNI COM NAV"';
		add_header Access-Control-Allow-Origin *;
	}

}
