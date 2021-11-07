"""
Django settings for smart_video_door_phone project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path


import django_heroku


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rassperypiInfo.apps.RassperypiinfoConfig',
    'doorSecurity.apps.DoorseurityConfig',
    'accounts.apps.AccountsConfig',
    'djoser',
    'rest_framework',
    'rest_framework_swagger',
    'websocketManage.apps.WebsocketmanageConfig',
    'django_celery_beat',
    'django_celery_results',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'doorSecurity.middleware.custom_middleware.checkLogin',
    'doorSecurity.middleware.custom_middleware.exitLincenceMiddleware',
    'doorSecurity.middleware.custom_middleware.checkLincenseMiddleware',
    'doorSecurity.middleware.custom_middleware.checkMemberIsForRasspery'
]






# CORS enable
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'smart_video_door_phone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries' : {
                'staticfiles': 'django.templatetags.static',
            }
        },
    },
]

WSGI_APPLICATION = 'smart_video_door_phone.wsgi.application'



#channels
ASGI_APPLICATION = 'smart_video_door_phone.routing.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [{'address':("redis-11841.c251.east-us-mz.azure.cloud.redislabs.com", 11841),'password':"as8qO8oBJBLiOCVNuCr52YNLKNHttUah",}]
        },
    },
}


#swagger
REST_FRAMEWORK = { 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema' }


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd805ekjcr8l9s6',
        'HOST':'ec2-54-211-160-34.compute-1.amazonaws.com',
        'PORT':5432,
        'USER': 'pjmrwufklrusgp',
        'PASSWORD': '4b378f4cd70405b3460ab0f9c3c7671460cdc480716b02c117982ed788006e67'
    }
}
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=600)
#DATABASES['default'] = dj_database_url.config(default='postgres://...'}
DATABASES['default'].update(db_from_env)



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'
# Default primary key field type
# # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
VENV_PATH = os.path.dirname(BASE_DIR)
STATIC_ROOT = os.path.join(VENV_PATH, 'smart_video_door_phone/static_root')

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Activate Django-Heroku.
django_heroku.settings(locals())

# CELERY SETTINGS
CELERY_BROKER_URL = 'redis://:as8qO8oBJBLiOCVNuCr52YNLKNHttUah@redis-11841.c251.east-us-mz.azure.cloud.redislabs.com:11841/test'
#CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SELERLIZER = 'json'
CELERY_TIMEZONE = 'Asia/Tehran'

CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'


