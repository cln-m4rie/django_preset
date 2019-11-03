import os

from .base import *

DEBUG = False
SECRET_KEY = os.environ.get('DB_SECRET_KEY')

ALLOWED_HOSTS = [os.environ.get('PRODUCTION_HOST')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
        'TEST': {
            'NAME': f'test_{os.environ.get("DB_NAME")}',
        },
    }
}