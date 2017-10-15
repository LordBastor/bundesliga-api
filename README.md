# Bundesliga API

## Prerequisites:
* mysql-server / mysql-client
* apt-get install python-dev libmysqlclient-dev

## Documented endpoints:
* Can be found at /docs

## Run
1. virtualenv env
2. source env/bin/activate
3. pip install -r requirements.txt

## Run commands (localhost)
* Debug: env $(cat ../debug.env | xargs) python manage.py runserver 0.0.0.0:8000
* Prod: env $(cat prod-deploy-dir/prod.env | xargs) python manage.py runserver 0.0.0.0:8000

## Deployment
* make build
* make push
* fab deploy:dev
