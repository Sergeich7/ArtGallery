#!/bin/bash

if [ "$DEV" == "True" ]; then
    python manage.py runserver 0.0.0.0:8000 --nostatic
    exit
fi
gunicorn --forwarded-allow-ips=* --bind 0.0.0.0:8000 -w 2 project.wsgi:application

