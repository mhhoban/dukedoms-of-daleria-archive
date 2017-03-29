#!/bin/bash

sudo apt-get update

sudo apt-get -y upgrade

sudo apt-get -y install python-pip python-dev libpq-dev postgresql postgresql-contrib

#sudo su - postgres 
#psql -f /vagrant/vagrant_provision/create_daleria_archive_db.sql
#exit

sudo pip install virtualenv

virtualenv /vagrant/daleria_env

