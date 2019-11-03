import os

from .base import *

SECRET_KEY = '76)5(c(fx4ton1h6ski0r1t3y9f$!q#q68+-drj3m&tmb9o8u_'
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', os.environ.get('ADDITIONAL_HOST')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}