#!/usr/bin/env bash
set -e

# Ensure paths
export DJANGO_SETTINGS_MODULE="${DJANGO_SETTINGS_MODULE:-your_settings_module.settings}"
export PORT="${PORT:-80}"
export STATIC_ROOT="${STATIC_ROOT:-/app/staticfiles}"
export MEDIA_ROOT="${MEDIA_ROOT:-/app/media}"

echo "Apply migrations..."
python manage.py migrate --noinput

echo "Collect static..."
python manage.py collectstatic --noinput

# Optional: create superuser once (set AUTO_SUPERUSER_EMAIL to enable)
if [ -n "$AUTO_SUPERUSER_EMAIL" ] && [ -n "$AUTO_SUPERUSER_PASSWORD" ]; then
python - <<PY
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.getenv("DJANGO_SETTINGS_MODULE"))
django.setup()
from django.contrib.auth import get_user_model
U = get_user_model()
email = os.environ["AUTO_SUPERUSER_EMAIL"]
pwd = os.environ["AUTO_SUPERUSER_PASSWORD"]
if not U.objects.filter(email=email).exists() and not U.objects.filter(username=email).exists():
    U.objects.create_superuser(username=email, email=email, password=pwd)
    print(f"Created superuser {email}")
else:
    print("Superuser already exists")
PY
fi

echo "Starting Gunicorn on :$PORT ..."
exec gunicorn \
  --bind 0.0.0.0:$PORT \
  --workers 3 \
  --timeout 90 \
  ${DJANGO_SETTINGS_MODULE%.*}.wsgi:application
