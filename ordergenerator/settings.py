"""
Django settings for ordergenerator project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os

from pathlib import Path
from dotenv import load_dotenv


# Carrega as variáveis de ambiente do arquivo .env.dev
IS_PRODUCTION = os.getenv("IS_PRODUCTION", False)
IS_DOCKER_COMPOSE = os.getenv("IS_DOCKER_COMPOSE", False)

if IS_DOCKER_COMPOSE:
    load_dotenv(".env.compose")
else:
    load_dotenv(".env.prod" if IS_PRODUCTION else ".env.dev")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-jl%u1m$ifn-8mnsj))=@h*h$o3)t+rl#)nxr-bp(ge5$8z(p!k"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not IS_PRODUCTION

CSRF_TRUSTED_ORIGINS = ['https://orc.inviosat.com', 'https://orc.segmart.com.br']
ALLOWED_HOSTS = ["orc.inviosat.com", "orc.segmart.com.br", "localhost", "127.0.0.1"]
# ADMIN_INTERFACE = 'flat-responsive'
# Application definition
INSTALLED_APPS = [
    "admin_interface",
    "colorfield",
    # "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "ordergenerator.apps.AdminConfigReorder",
    'openpyxl',
    "mathfilters",
    "customer",
    "order",
    "product",
    "company",
    "account",
]

AUTH_USER_MODEL = 'account.CustomUser'
X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True



ROOT_URLCONF = "ordergenerator.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ordergenerator.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("DATABASE_HOST"),
        "PORT": os.getenv("DATABASE_PORT"),
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = 'static_root/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

INTERNAL_IPS = ["127.0.0.1"]

