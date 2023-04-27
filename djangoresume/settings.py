"""
Django settings for djangoresume project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from dotenv import load_dotenv
import sys
load_dotenv('.env')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

print(os.environ.get('SECRET_KEY'))

SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'aless80.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'compressor',
    'resume'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoresume.urls'
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'resume/templates')]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',  # TO USE MEDIA_URL
            ],
        },
    },
]

LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'djangoresume.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images) and Media files (uploaded by users)
# URL prefix for static files. eg http://aless80.pythonanywhere.com/static/
STATIC_URL = "/static/"
# Absolute path to the directory static files should be collected to, eg: /home/amarin/Mezzanine/static/
# Don't put anything here yourself; store your static files in subdirectories of apps/static/ and in STATICFILES_DIRS.
STATIC_ROOT = os.path.join(BASE_DIR, "assets")
# URL that handles the media served from MEDIA_ROOT. Different than STATIC_URL. NB trailing slash. eg http://aless80.pythonanywhere.com/media/
# MEDIA_URL = STATIC_URL + "media/"
MEDIA_URL = "/media/"
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/amarin/Mezzanine/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, *MEDIA_URL.strip("/").split("/"))
MEDIA_ROOT = os.path.join(BASE_DIR, "assets/media/")


# STATICFILES_DIRS = [ #directories with files to look into
#        os.path.join(BASE_DIR, 'resume/static'),
#        os.path.join(BASE_DIR, 'resume/static/resume')
# ]
STATICFILES_DIRS = [  # directories with files to look into
    os.path.join(BASE_DIR, 'static'),
]
