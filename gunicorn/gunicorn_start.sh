# # DB 연결될때까지 블로킹 (마이그레이션은 DB가 연결되어야 가능하다)
# while ! nc -z database 3306; do sleep 1; done;
# # 프로덕션 DB 연결일때 실행

pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
# pipenv run python manage.py collectstatic --noinput
# pipenv run python manage.py createsuperuserwithpassword \
#         --username $DJANGO_SUPERUSER_USERNAME \
#         --password $DJANGO_SUPERUSER_PASSWORD \
#         --email $DJANGO_SUPERUSER_EMAIL \
#         --preserve

# gunicorn settings
# 참고: https://docs.gunicorn.org/en/stable/settings.html
DJANGO_WSGI_MODULE=src.wsgi

PORT=8000

NAME="ba"

NUM_WORKERS=4
# 2-4 x $(NUM_CORES)

NUM_THREADS=4
# 2-4 x $(NUM_CORES)

LOG_PATH="/var/log/gunicorn_log"

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
# pipenv 사용
echo Starting Gunicorn.
exec pipenv run gunicorn --reload ${DJANGO_WSGI_MODULE}:application \
    --bind 0.0.0.0:$PORT \
    --workers $NUM_WORKERS \
    --threads $NUM_THREADS \
    --access-logfile ${LOG_PATH}/gunicorn-access.log \
    --error-logfile ${LOG_PATH}/gunicorn-error.log \

# exec pipenv run gunicorn ${DJANGO_WSGI_MODULE}:application \
# -b 0.0.0.0:$PORT \
# --name $NAME \
# --workers $NUM_WORKERS \
# --user=$USER \
# --bind=unix:$SOCKFILE \
# --log-level=debug \
# --log-file=-