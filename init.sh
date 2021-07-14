# DB 연결될때까지 블로킹 (마이그레이션은 DB가 연결되어야 가능하다)
while ! nc -z db 5432; do sleep 1; done;
# 프로덕션 DB 연결일때 실행
# 그런데 사실 docker-compose 파일에서 gunicorn-backend가 db 컨테이너에 dependency가 걸려있어서 괜찮기는 함

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