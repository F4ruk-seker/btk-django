from .base import *
import logging


logger = logging.getLogger(__name__)

logger.error('pars')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#
# if DEBUG:
#     CSRF_TRUSTED_ORIGINS: list = [f'http://{domain}' for domain in env.list('DJANGO_ALLOWED_HOSTS')]
# else:
CSRF_TRUSTED_ORIGINS: list = [f'https://{domain}/' for domain in env.list('DJANGO_ALLOWED_HOSTS')]+[f'https://{domain}' for domain in env.list('DJANGO_ALLOWED_HOSTS')]
    # CSR1F_TRUSTED_ORIGINS: list = [f'https://{domain}' for domain in env.list('DJANGO_ALLOWED_HOSTS')]
# CSRF_TRUSTED_ORIGINS: list = env.list('DJANGO_ALLOWED_HOSTS')

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')
CORS_ALLOW_ALL_ORIGINS = True  # temp for server settings


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('PGDATABASE'),
        'USER': env('PGUSER'),
        'PASSWORD': env('PGPASSWORD'),
        'HOST': env('PGHOST'),
        'PORT': env('PGPORT')
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


