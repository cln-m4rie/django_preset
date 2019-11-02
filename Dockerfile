FROM python:3.7-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk update
RUN apk add tzdata
RUN echo "Asia/Tokyo" >  /etc/timezone

WORKDIR /var/www/html
RUN pip install -U pip
RUN pip install pipenv

ADD Pipfile /var/www/html/
ADD Pipfile.lock /var/www/html/
RUN pipenv lock -r > requirements.txt
RUN apk --no-cache --virtual .requirements add g++ make linux-headers && \
    apk --no-cache add libffi-dev mysql-dev mysql-client && \
    pip install -r requirements.txt --no-cache-dir
RUN rm requirements.txt
RUN rm -rf /var/cache/apk/*
ENV TZ Asia/Tokyo
ENV LC_ALL=ja_JP.UTF-8
ENV LANG=ja_JP.UTF-8
ENV LANGUAGE=ja_JP.UTF-8

ADD . /var/www/html/