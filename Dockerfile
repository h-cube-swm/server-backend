FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update 

WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./ ./

EXPOSE 8000
CMD ./init.sh