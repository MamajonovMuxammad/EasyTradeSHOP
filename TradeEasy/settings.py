"""
Django settings for TradeEasy project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _


LANGUAGES = [
    ('de', _('German')),
    ('en', _('English')),
    ('ru', _('Russian')),
]
MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'
MODELTRANSLATION_POPULATION_DEFAULT_LANGUAGE = 'en'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-wgs*ep20@6w&1sl%(3a1x%qc=*i#14ppmd=v%^fpmxs=s(v0(_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'cart',
    'products',
    'users',
    'social_django',
    'django_extensions',
    'orders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'TradeEasy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'TradeEasy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'


MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

CART_SESSION_ID = 'cart'



AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.google.GoogleOAuth2',
) 
SOCIAL_AUTH_FACEBOOK_KEY = '1186853005996024' # ИД приложения Facebook
SOCIAL_AUTH_FACEBOOK_SECRET = '451387367d278e81045ddee450f14a80' # Секрет приложения Facebook
SOCIAL_AUTH_FACEBOOK_SCOPE = [
    'email',
    ]
SOCIAL_AUTH_FACEBOOK_API_VERSION = '2.10'
SOCIAL_AUTH_FACEBOOK_REDIRECT_URI = 'https://mysite.com:8000/social-auth/complete/facebook/'
LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_TWITTER_KEY = 'mPIp8bJfwTFx9Cx9MfXfyHjvZ' # Ключ API Twitter
SOCIAL_AUTH_TWITTER_SECRET = '5jVXM9J1WGDnpM5kYuYi5KVkwDWNjDp7WhRUKaIoNAIw26SXHa' # Секрет API Twitter


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '365808964047-k3mcs0jefp8hl9ube0nbl0jingt84ct2.apps.googleusercontent.com' # ИД клиента Google
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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' # Секрет клиента Google



SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',  # Опционально
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)