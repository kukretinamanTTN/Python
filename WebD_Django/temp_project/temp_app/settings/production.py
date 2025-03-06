from .base import *

DEBUG = False
ALLOWED_HOSTS = ['naman.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prod_db',
        'USER': 'temp_user',
        'PASSWORD': 'password',
        'HOST': 'db_host',
        'PORT': '5432',
    }
}
