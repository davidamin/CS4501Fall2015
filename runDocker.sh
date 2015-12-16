#!/bin/sh

sudo docker run -d --name kafka --env ADVERTISED_HOST=kafka --env ADVERTISED_PORT=9092 spotify/kafka
sudo docker run -d -p 9200:9200 --name es elasticsearch:2.0
sudo docker run -d --name models -p 8001:8000 -v /Documents/isa/web/CS4501Fall2015:/app --link mysql:db --link kafka:kafka tp33/django:1.1 mod_wsgi-express start-server --reload-on-changes h1/h1/wsgi.py
sudo docker run -d --name exp -p 8002:8000 -v /Documents/isa/web/CS4501Fall2015:/app --link models:models-api --link mysql:db --link kafka:kafka tp33/django:1.1 mod_wsgi-express start-server --reload-on-changes h1/h1/wsgi.py
sudo docker run -d --name webview -p 8000:8000 -v /Documents/isa/web/CS4501Fall2015:/app --link exp:exp-api --link mysql:db --link kafka:kafka tp33/django:1.1 mod_wsgi-express start-server --reload-on-changes h1/h1/wsgi.py
sudo docker run -d --name webview2 -p 8003:8000 -v /Documents/isa/web/CS4501Fall2015:/app --link exp:exp-api --link mysql:db --link kafka:kafka tp33/django:1.1 mod_wsgi-express start-server --reload-on-changes h1/h1/wsgi.py
sudo docker run -d --name batch --link kafka:kafka --link es:es tp33/django:1.1
sudo docker run -d --name pen -p 8004:8000 --link webview:webview --link webview2:webview2 galexrt/pen 8000 webview:8000 webview2:8000
sudo docker exec models pip install requests
sudo docker exec exp pip install requests
sudo docker exec webview pip install requests
sudo docker exec webview2 pip install requests 
