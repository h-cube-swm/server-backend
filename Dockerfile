FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update 

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --upgrade pip \
  && pip install -r requirements.txt

ENTRYPOINT ["sh", "/code/gunicorn/gunicorn_start.sh"]