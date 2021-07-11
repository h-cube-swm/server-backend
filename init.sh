# # DB 연결될때까지 블로킹 (마이그레이션은 DB가 연결되어야 가능하다)
# while ! nc -z database 5432; do sleep 1; done;
# # 프로덕션 DB 연결일때 실행

python manage.py makemigrations
python manage.py migrate

# pipenv run python manage.py collectstatic --noinput
# pipenv run python manage.py createsuperuserwithpassword \
#         --username $DJANGO_SUPERUSER_USERNAME \
#         --password $DJANGO_SUPERUSER_PASSWORD \
#         --email $DJANGO_SUPERUSER_EMAIL \
#         --preserve

# gunicorn settings
# 참고: https://docs.gunicorn.org/en/stable/settings.html

echo Starting Gunicorn.
exec gunicorn -c gunicorn.config.py