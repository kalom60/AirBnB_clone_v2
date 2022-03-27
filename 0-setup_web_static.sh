#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/ 
echo "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
if [ -L "/data/web_static/current" ];
then
    sudo unlink /data/web_static/current
fi
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -ie '0,/location \/ {/s/location \/ {/location \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;/' /etc/nginx/sites-available/default
sudo service nginx restart