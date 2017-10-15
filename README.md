# Bundesliga API

## Prerequisites:
* mysql-server / mysql-client
* apt-get install python-dev libmysqlclient-dev

## Run
1. virtualenv env
2. source env/bin/activate
3. pip install -r requirements.txt

## Run commands (localhost)
* Debug: env $(cat ../debug.env | xargs) python manage.py runserver 0.0.0.0:8000
* Prod: env $(cat ../prod.env | xargs) python manage.py runserver 0.0.0.0:8000