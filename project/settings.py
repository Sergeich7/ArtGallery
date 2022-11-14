"""Django settings for project."""

import os
import sys
import json
from pathlib import Path


def on_production() -> bool:
    """Функция определяет где запущен экземпляр. РАЗРАБОТКА или ПРОДАКШЕН."""
    return 'www' in str(Path(__file__).resolve())


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Читаем пароли, личные данные и тд из файла конфигурации
# На продакшен прячем конфиг выше корневого каталога сайта
CONFIG_DIR = BASE_DIR.parent if on_production() else BASE_DIR
with open(CONFIG_DIR / 'config.json', 'r', encoding="utf8") as cf:
    config = json.load(cf)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['SECRET_KEY']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',
    'sorl.thumbnail',
    'captcha',
    'django_cleanup',
    'rest_framework',
    'corsheaders',
    'bootstrap4',

    'users.apps.UsersConfig',
    'art.apps.ArtConfig',
    'restapi.apps.RestapiConfig',

    'django.contrib.sites',
    'django.contrib.sitemaps',
]

SITE_ID = 1

CRISPY_TEMPLATE_PACK = 'bootstrap4'

#APPEND_SLASH = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'users.authentication.EmailBackend',

    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/.*$'

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'art.middlewares.categories4menu',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

if on_production():
    ############################################
    # PRODUCTION
    DEBUG = False

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    ALLOWED_HOSTS = [
        'artgallery-tatyana.ru',
        'www.artgallery-tatyana.ru',
        'xn----7sbabaopa6cyazevhb4nwbf.xn--p1ai',
        'www.xn----7sbabaopa6cyazevhb4nwbf.xn--p1ai'
    ]

    if 'test' in sys.argv:
        # на PRODUCTION для тестов другая база
        DATABASES = config['DATABASES-TEST']
    else:
        # рабочая база данных на PRODUCTION
        DATABASES = config['DATABASES-WORK']

#    SECURE_SSL_REDIRECT = True
#    CSRF_COOKIE_SECURE = True
else:
    ############################################
    # РАЗРАБОТКА
    DEBUG = True

    # для 'debug_toolbar'
    # pip install django-debug-toolbar
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
    INTERNAL_IPS = ['127.0.0.1']

    STATICFILES_DIRS = [BASE_DIR / "static"]
    MEDIA_ROOT = BASE_DIR / "media"

    ALLOWED_HOSTS = ['*']

    DATABASES = config['DATABASES-DEV']

#    if 'test' in sys.argv:
#        # на PRODUCTION для тестов другая база
#        DATABASES = config['DATABASES-DEV-TEST']
#    else:
#        # рабочая база данных на PRODUCTION
#        DATABASES = config['DATABASES-DEV-WORK']

STATIC_URL = 'static/'
MEDIA_URL = 'media/'

AUTHENTICATION_BACKENDS = [
#    'django.contrib.auth.backends.ModelBackend',
    'users.authentication.EmailBackend',
    ]

############################################
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 5,
        },
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


############################################
# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Asia/Omsk'
USE_I18N = True
USE_TZ = True


############################################
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

############################################
# Редирект после логина

LOGIN_REDIRECT_URL = 'art:index'
LOGOUT_REDIRECT_URL = 'art:index'

LOGIN_URL = 'users:login'
LOGOUT_URL = 'users:logout'

############################################
# Почта
EMAIL_HOST = config['EMAIL_HOST']
EMAIL_PORT = config['EMAIL_PORT']
EMAIL_HOST_USER = config['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = config['EMAIL_HOST_PASSWORD']

EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

MANAGERS = ADMIN = config['ADMIN'] + [['Host', EMAIL_HOST_USER]]
