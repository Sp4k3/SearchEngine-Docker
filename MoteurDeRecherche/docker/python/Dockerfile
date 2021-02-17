FROM python:3.8-slim-buster

RUN mkdir -p /opt/www/mySearchEngine
WORKDIR /opt/www/mySearchEngine

RUN python3 -m venv /opt/venv
RUN . /opt/venv/bin/activate
RUN pip3 install django djangorestframework requests django-mysql django-postgresql psycopg2-binary

