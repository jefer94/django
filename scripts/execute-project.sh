#!/bin/sh

cd "$1"

python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb
python manage.py runserver 0.0.0.0:8000
