python manage.py makemigrations
python manage.py migrate

python manage.py collectstatic --noinput
python manage.py createsuperuserwithpassword \
        --username $DJANGO_SUPERUSER_USERNAME \
        --password $DJANGO_SUPERUSER_PASSWORD \
        --email $DJANGO_SUPERUSER_EMAIL \
        --preserve

# gunicorn settings
# 참고: https://docs.gunicorn.org/en/stable/settings.html

echo Starting Gunicorn.
exec gunicorn -c gunicorn.config.py