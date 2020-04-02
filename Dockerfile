FROM python:3.8.0-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/django_training

COPY requirements.txt start-server.sh /opt/app/
COPY .pip_cache /opt/app/pip_cache/
COPY django_project /opt/app/django_training

WORKDIR /opt/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache

#CMD /bin/sh start-server.sh
CMD python /opt/app/django_training/manage.py runserver 0.0.0.0:8000