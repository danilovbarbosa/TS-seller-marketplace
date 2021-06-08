#!/bin/bash
# bash -f ./scripts/run.sh

python manage.py showmigrations

python manage.py makemigrations

python manage.py migrate

#echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.com', 'admin')" | python manage.py shell

#python manage.py collectstatic

python manage.py runserver 0.0.0.0:8000