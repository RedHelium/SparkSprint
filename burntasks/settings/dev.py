from .base import *


SECRET_KEY = 'django-insecure-0$7fmjig%o+bir9zjyp4f*(yhbjtv(@$440gn_==4%*53#!czj'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'burntasks',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'PORT': 5433
    }
}

STATICFILES_DIRS = [BASE_DIR / 'STATIC',]