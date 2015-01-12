#!/bin/bash


sudo apt-get install -y python-dev
sudo easy_install -U pip
mkdir -p shippable/testresults shippable/codecoverage
sudo apt-get install -y libevent-dev
sudo apt-get update
sudo apt-get install -y postgresql redis-server python-pip libpq-dev libxml2-dev libxslt-dev
sudo pip install -r requirements_dev.txt --use-mirrors
