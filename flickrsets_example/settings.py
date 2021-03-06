# -*- coding: utf-8 -*-
"""
Project's settings.
"""
import os
import django

# Own constants
# -----------------------------------------------------------------------------
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
PROJECT_NAME = os.path.basename(PROJECT_ROOT)
DJANGO_ROOT = os.path.dirname(django.__file__)

# Debugging
# -----------------------------------------------------------------------------
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Administrators
# -----------------------------------------------------------------------------
ADMINS = (('Admin', 'admin@foo.bar'),)
MANAGERS = ADMINS

# Databases
# -----------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# I18N - L10N
# -----------------------------------------------------------------------------
TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True

# Site
# -----------------------------------------------------------------------------
SITE_ID = 1

# Site media
# -----------------------------------------------------------------------------
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

# Admin media
# -----------------------------------------------------------------------------
ADMIN_MEDIA_ROOT = os.path.join(DJANGO_ROOT, 'contrib', 'admin', 'media')
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Secret Key
# -----------------------------------------------------------------------------
SECRET_KEY = 'MUST-BE-SECRET'

# Templates
# -----------------------------------------------------------------------------
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

# Middleware
# -----------------------------------------------------------------------------
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

# URLs
# -----------------------------------------------------------------------------
ROOT_URLCONF = '%s.urls' % PROJECT_NAME

# Caching
# -----------------------------------------------------------------------------
CACHE_MIDDLEWARE_SECONDS = 5
CACHE_MIDDLEWARE_KEY_PREFIX = '%s_' % PROJECT_NAME

# Sessions
# -----------------------------------------------------------------------------
#SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# Applications
# -----------------------------------------------------------------------------
INSTALLED_APPS = (
    # Django
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',

    # External apps
    #'django_extensions',
    'flickrsets',
    'south',
)

# Private settings
# -----------------------------------------------------------------------------
# pylint: disable=W0401
from flickrsets_example.settings_private import *
