"""Django settings for project."""

import os
import sys
from pathlib import Path

############################################
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

############################################
# Переменные окружения
if not os.environ.get('SECRET_KEY'):
    # Запуск сервера без докера (разработка или на виртуале)
    # Нет переменных окружения. Загружаем из файла.
    if 'www' in str(Path(__file__).resolve()):
        # На виртуале прячем .env выше корневого каталога сайта
        ENV_DIR = BASE_DIR.parent
    else:
        ENV_DIR = BASE_DIR
    from dotenv import load_dotenv
    if os.path.exists(os.path.join(ENV_DIR, '.env')):
        load_dotenv(os.path.join(ENV_DIR, '.env'))
        # поправить DATABASE_HOST_DEV на 127.0.0.1 вместо db
        os.environ["DATABASE_HOST_DEV"] = '127.0.0.1'


############################################
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

############################################
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

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

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

state = os.environ.get('STATE')
if state not in 'DEV':
    ############################################
    # PRODUCTION
    DEBUG = True

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    ALLOWED_HOSTS = [
        '95.163.243.134', 'www.lh.artgallery-tatyana.ru', 'lh.artgallery-tatyana.ru', 'artgallery-tatyana.ru',
        'www.artgallery-tatyana.ru',
        'xn----7sbabaopa6cyazevhb4nwbf.xn--p1ai',
        'www.xn----7sbabaopa6cyazevhb4nwbf.xn--p1ai'
    ]
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

STATIC_URL = 'static/'
MEDIA_URL = 'media/'

AUTHENTICATION_BACKENDS = [
#    'django.contrib.auth.backends.ModelBackend',
    'users.authentication.EmailBackend',
    ]

############################################
# База данных
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get('DATABASE_NAME_' + state),
        "USER": os.environ.get('DATABASE_USER_' + state),
        "PASSWORD": os.environ.get('DATABASE_PASSWORD_' + state),
        "HOST": os.environ.get('DATABASE_HOST_' + state),
        "OPTIONS": {"init_command": "SET sql_mode='STRICT_TRANS_TABLES'"},
    }
}

if state in 'PROD' and 'test' in sys.argv:
    # на PRODUCTION для тестов другая база
    DATABASES[0].update({
        "TEST": {
            "NAME": os.environ.get('DATABASE_NAME_' + state + '_TEST')
        },
    })

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
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

MANAGERS = ADMIN = [
    ["Виталий", "pl3@yandex.ru"],
    ["Татьяна", "tsbelashova@yandex.ru"],
    ['Host', EMAIL_HOST_USER]
]
