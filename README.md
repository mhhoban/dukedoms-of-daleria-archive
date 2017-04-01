# Dukedoms of Daleria - Archives

Microservice to hold card data for Dukedoms of Daleria.

## Setup:

Use the included Vagrantfile to provision a vagrant environment for development purposes. By default, the configuration
maps guest port 8000 to host port 4567.

## Django and Vagrant Notes:
If using Django's runserver, make sure you tell it to bind to 0.0.0.0:8000 to show up on your host machine.

## PostgreSQL setup:

```
sudo su - psql -f /vagrant/vagrant_provision/create_daleria_archive_db.sql postgresql-contrib
```

## Python Vagrant Virtualenv Setup:
While not strictly necessary, it is highly recommended to work out of a virtual environment:
```
sudo pip install virtualenv
virtualenv /vagrant/daleria_env
source /vagrant/daleria_env
source /vagrant/daleria_env/bin/activate
pip install django psycopg2 pyyaml
```

## License

Project is freely open source under the terms of the
[MIT License](http://choosealicense.com/licenses/mit/)
