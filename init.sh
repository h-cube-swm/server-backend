# Read environment variables from .env file

python manage.py makemigrations
python manage.py migrate

python manage.py collectstatic --noinput

# gunicorn settings
# 참고: https://docs.gunicorn.org/en/stable/settings.html

echo Starting Gunicorn.
exec gunicorn -c gunicorn.config.py
