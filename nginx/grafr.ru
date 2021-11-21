server {
    listen 80;
    listen [::]:80;
    server_name grafr.ru www.grafr.ru;

    location = /favicon.ico {
	    alias /home/lix/Grafr/favicons/favicon.ico; access_log off; log_not_found off;
    }

    location /list {
        auth_basic "List";
        auth_basic_user_file /etc/nginx/auth.basic;
        include /etc/nginx/proxy.conf;
    }

    location /all {
        auth_basic "All";
        auth_basic_user_file /etc/nginx/auth.basic;
        include /etc/nginx/proxy.conf;
    }

    location /static/ {
	        root /home/lix/Grafr/GrafrProj;
    }

    location / {
		include /etc/nginx/proxy.conf;
    }

}
