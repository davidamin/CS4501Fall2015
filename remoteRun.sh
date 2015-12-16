#!/bin/sh

sudo git clone https://github.com/davidamin/CS4501Fall2015.git /deploy
sudo docker run --name mysql -d -e MYSQL\_ROOT\_PASSWORD='ridesh4re' mysql:5.7.8
sudo docker run -it --name mysql-cmdline --link mysql:db mysql:5.7.8 bash
#sudo docker exec mysql-cmdline mysql -uroot -p'ridesh4re' -h db;create user 'www'@'%' identified by 'password';create database cs4501 character set utf8;grant all on cs4501.* to 'www'@'%';
sudo docker run -d --name kafka --env ADVERTISED_HOST=kafka --env ADVERTISED_PORT=9092 spotify/kafka
#docker exec -d kafka /bin/bash -c 'export KAFKA_HEAP_OPTS="-Xmx64m -Xms64m";my_addr=$(ip addr show | grep -E 'inet 172\.[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3}' | grep -Eo '172\.[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3}');my_addr="$my_addr kafka";echo $my_addr >> /etc/hosts;/usr/bin/start-kafka.sh;'
#apt-get update;apt-get install vim;vim /etc/hosts;
#add kafka to etc/hosts
sudo docker run -d -p 9200:9200 --name es elasticsearch:2.0
sudo docker run -d --name models -p 8001:8000 -v /deploy:/app --link mysql:db --link kafka:kafka --link es:es tp33/django:1.1 mod_wsgi-express start-server --reload-on-changes h1/h1/wsgi.py
sudo docker run -d --name exp -p 8002:8000 -v /deploy:/app --link models:models-api --link mysql:db --link kafka:kafka --link es:es tp33/django:1.1 mod_wsgi-express start-server --reload-on-changes h1/h1/wsgi.py
sudo docker run -d --name webview -p 8000:8000 -v /deploy:/app --link exp:exp-api --link mysql:db --link kafka:kafka --link es:es tp33/django:1.1 mod_wsgi-express start-server --reload-on-changes h1/h1/wsgi.py
sudo docker run -d --name webview2 -p 8003:8000 -v /deploy:/app --link exp:exp-api --link mysql:db --link kafka:kafka --link es:es tp33/django:1.1 mod_wsgi-express start-server --reload-on-changes h1/h1/wsgi.py
sudo docker exec models pip install requests
sudo docker exec exp pip install requests
sudo docker exec webview pip install requests
sudo docker exec webview2 pip install requests 
sudo docker run -d --name batch --link kafka:kafka --link es:es -v /deploy:/app tp33/django:1.1 python batch.py

