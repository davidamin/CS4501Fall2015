#!/bin/sh

sudo docker run -d --name kafka --env ADVERTISED_HOST=kafka --env ADVERTISED_PORT=9092 spotify/kafka
sudo docker run -d -p 9200:9200 --name es elasticsearch:2.0 -Des.network.host=es
sudo docker run -d --name models -p 8001:8000 -v /home/david/Documents/4501/models:/app --link mysql:db tp33/django:1.1 mod_wsgi-express start-server --reload-on-changes h1/h1/wsgi.py
sudo docker run -d --name exp -p 8002:8000 -v /home/david/Documents/4501/exp:/app --link models:models-api --link mysql:db --link kafka:kafka tp33/django:1.1 mod_wsgi-express start-server --reload-on-changes h1/h1/wsgi.py
sudo docker run -d --name webview -p 8000:8000 -v /home/david/Documents/4501/web:/app --link exp:exp-api --link mysql:db tp33/django:1.1 mod_wsgi-express start-server --reload-on-changes h1/h1/wsgi.py
sudo docker run -d --name batch --link kafka:kafka --link es:es -v /home/david/Documents/4501/batch:/app tp33/django:1.1 python batch.py
sudo docker exec models pip install requests
sudo docker exec exp pip install requests
sudo docker exec webview pip install requests
