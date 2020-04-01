#!/bin/bash
set -x
# start-server.sh
if [ -n "${DJANGO_SUPERUSER_USERNAME}" ] && [ -n "${DJANGO_SUPERUSER_PASSWORD}" ] ; then
    (cd django_training; python manage.py createsuperuser --no-input)
fi
(cd django_training; gunicorn django_training.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"