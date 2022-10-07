"""
Django settings for spambot project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from os.path import abspath, dirname


def str2bool(value):
    """
    Convert String to Boolean
    """
    return value.lower() in ("yes", "true", "t", "1", "on")


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = dirname(dirname(abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "+o!mg4#m=hf@e1n*q%18#pk&2i0&shj_8j1bz#(6j(zh++b%k&"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = str2bool(os.getenv("APP_DEBUG", "True"))

ALLOWED_HOSTS = ["*"]

WSGI_APPLICATION = "spambot.wsgi.application"

FIXTURE_DIRS = [
    # os.path.join(BASE_DIR, "agent", "fixtures")
]