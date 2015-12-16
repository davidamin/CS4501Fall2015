#!/bin/sh

docker start mysql
docker start kafka
docker start es
docker start models
docker start exp
docker start webview
docker start webview2
docker start pen
docker start batch
docker restart kafka
sleep 3
docker start batch
