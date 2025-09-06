from .base import *

DEBUG = False

ALLOWED_HOSTS = []


RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
   ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': os.environ.get('POSTGRES_DB'),
           'USER': os.environ.get('POSTRGRES_USER'),
           'PASSWORD': os.environ.get('POSTRGRES_PASSWORD'),
           'HOST': os.environ.get('POSTRGRES_HOST'),
           'PORT': int(os.environ['POSTRGRES_DB_PORT']),
       }
   }
#
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True