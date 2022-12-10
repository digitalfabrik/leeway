"""
Django settings for django_leeway project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from distutils.util import strtobool
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&ks8gx&2z=zc6u%k#uts9)xpq1ns^^x$hu&$sr(h56h&(oze(e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'opendrift_leeway_webgui.leeway'
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

ROOT_URLCONF = 'opendrift_leeway_webgui.core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = "/var/www/leeway/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "/"

CELERY_TIMEZONE = "UTC"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

SIMULATION_PATH = os.path.join(BASE_DIR.parent, "simulation")

OPENDRIFT_NUMBER_DRIFTERS = 100


##########
# EMAILS #
##########

if DEBUG:
    #: The backend to use for sending emails (see :setting:`django:EMAIL_BACKEND` and :doc:`django:topics/email`)
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

#: The email address that error messages come from (see :setting:`django:SERVER_EMAIL`)
SERVER_EMAIL = os.environ.get(
    "LEEWAY_SERVER_EMAIL"
)

#: Default email address to use for various automated correspondence from the site manager(s)
#: (see :setting:`django:DEFAULT_FROM_EMAIL`)
DEFAULT_FROM_EMAIL = SERVER_EMAIL

#: The host to use for sending email (see :setting:`django:EMAIL_HOST`)
EMAIL_HOST = os.environ.get("LEEWAY_EMAIL_HOST", "localhost")

#: Password to use for the SMTP server defined in :attr:`~LEEWAY.core.settings.EMAIL_HOST`
#: (see :setting:`django:EMAIL_HOST_PASSWORD`). If empty, Django won’t attempt authentication.
EMAIL_HOST_PASSWORD = os.environ.get("LEEWAY_EMAIL_HOST_PASSWORD")

#: Username to use for the SMTP server defined in :attr:`~LEEWAY.core.settings.EMAIL_HOST`
#: (see :setting:`django:EMAIL_HOST_USER`). If empty, Django won’t attempt authentication.
EMAIL_HOST_USER = os.environ.get("LEEWAY_EMAIL_HOST_USER", SERVER_EMAIL)

#: Port to use for the SMTP server defined in :attr:`~LEEWAY.core.settings.EMAIL_HOST`
#: (see :setting:`django:EMAIL_PORT`)
EMAIL_PORT = int(os.environ.get("LEEWAY_EMAIL_PORT", 587))

#: Whether to use a TLS (secure) connection when talking to the SMTP server.
#: This is used for explicit TLS connections, generally on port 587.
#: (see :setting:`django:EMAIL_USE_TLS`)
EMAIL_USE_TLS = bool(strtobool(os.environ.get("LEEWAY_EMAIL_USE_TLS", "True")))

#: Whether to use an implicit TLS (secure) connection when talking to the SMTP server.
#: In most email documentation this type of TLS connection is referred to as SSL. It is generally used on port 465.
#: (see :setting:`django:EMAIL_USE_SSL`)
EMAIL_USE_SSL = bool(strtobool(os.environ.get("LEEWAY_EMAIL_USE_SSL", "False")))
