#!/bin/bash

sudo apt-get update
sudo apt-get -y upgrade

sudo apt-get -y install python-virtualenv python-dev postgresql-9.3 postgis postgresql-9.3-postgis-2.1 postgresql-contrib-9.1 libpq-dev git fabric phppgadmin # libxml2-dev libxslt1-dev

cd /vagrant

fab setup

echo "You're good to go: vagrant ssh, cd /vagrant, python main.py"
