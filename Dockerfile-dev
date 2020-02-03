FROM python:3.7-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update -y
RUN apt-get install -y tzdata
RUN echo "Asia/Tokyo" >  /etc/timezone

WORKDIR /var/www/html
RUN pip install -U pip
RUN pip install pipenv

ADD Pipfile /var/www/html/
ADD Pipfile.lock /var/www/html/
RUN pipenv lock -r > requirements.txt
RUN apt-get install -y g++ make default-libmysqlclient-dev default-mysql-client
RUN pip install -r requirements.txt --no-cache-dir
RUN rm requirements.txt
RUN rm -rf /tmp/* /var/tmp/*
RUN rm -rf /var/lib/apt/lists/*
RUN rm -rf /var/lib/apt/lists/*
ENV TZ Asia/Tokyo
ENV LC_ALL=ja_JP.UTF-8
ENV LANG=ja_JP.UTF-8
ENV LANGUAGE=ja_JP.UTF-8

ADD . /var/www/html/