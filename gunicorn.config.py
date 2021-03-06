import multiprocessing
from src.settings import DEBUG

reload = True
wsgi_app = "src.wsgi:application"
bind = "0.0.0.0:8000"
worker_class = "gevent"
workers = multiprocessing.cpu_count() * 2 + 1
threads = multiprocessing.cpu_count() * 2 + 1

if not DEBUG:
    accesslog = "/var/log/gunicorn_log/gunicorn-access.log"
    errorlog = "/var/log/gunicorn_log/gunicorn-error.log"
else:
    accesslog = "/dev/null"
    errorlog = "/dev/null"
