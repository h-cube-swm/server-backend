FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update 

WORKDIR /code

COPY Pipfile Pipfile.lock /code/

RUN pip install --upgrade pip \
  && pip install pipenv \
  && pipenv install

ENTRYPOINT ["sh", "/code/gunicorn/gunicorn_start.sh"]