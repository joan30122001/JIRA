#!/bin/sh
set -e

python manage.py migrate

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
python manage.py shell -c "import os; from django.contrib.auth import get_user_model; User=get_user_model(); u=os.environ['DJANGO_SUPERUSER_USERNAME']; e=os.environ.get('DJANGO_SUPERUSER_EMAIL',''); p=os.environ['DJANGO_SUPERUSER_PASSWORD']; User.objects.filter(username=u).exists() or User.objects.create_superuser(u,e,p)"
fi

exec python manage.py runserver 0.0.0.0:8000
