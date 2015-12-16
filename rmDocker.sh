#!/bin/sh

sudo docker stop batch
sudo docker rm batch
sudo docker stop es
sudo docker rm es
sudo docker stop kafka
sudo docker rm kafka
sudo docker stop pen
sudo docker rm pen
sudo docker stop webview
sudo docker rm webview
sudo docker stop webview2
sudo docker rm webview2
sudo docker stop exp
sudo docker rm exp
sudo docker stop models
sudo docker rm models
