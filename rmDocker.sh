#!/bin/sh

sudo docker stop batch
sudo docker rm batch
sudo docker stop es
sudo docker rm es
sudo docker stop kafka
sudo docker rm kafka
sudo docker stop webview
sudo docker rm webview
sudo docker stop exp
sudo docker rm exp
sudo docker stop models
sudo docker rm models
