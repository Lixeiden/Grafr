server {
	listen 80;
	listen [::]:80;

	root /var/www/html;

	index index.html index.htm index.nginx-debian.html;

	server_name grafr.ru www.grafr.ru;
	
	location = /favicon.ico {
		alias /home/lix/Grafr/favicons/favicon.ico;
	}

	location / {
		proxy_pass http://127.0.0.1:8001;
		proxy_set_header X-Forwarded-Host $server_name;
		proxy_set_header X-Real-IP $remote_addr;
		add_header P3P 'CP="ALL DSP COR PSAa PSDa OUR NOR ONL UNI COM NAV"';
		add_header Access-Control-Allow-Origin *;
	}

}
