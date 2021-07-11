import multiprocessing

reload = True
wsgi_app = 'src.wsgi:application'
bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count() * 2 + 1
threads = multiprocessing.cpu_count() * 2 + 1
access_logfile = "/var/log/gunicorn_log/gunicorn-access.log"
error_logfile = "/var/log/gunicorn_log/gunicorn-error.log"
