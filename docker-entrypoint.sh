#!/bin/bash

# apply database migrations
echo "apply database migrations"
python manage.py migrate

# start server
echo "starting server"
python manage.py runserver 0.0.0.0:8000
