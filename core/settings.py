import os
from pathlib import Path
import dj_database_url


# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent


DEBUG = True  # For local development. Set to False on production (Render)!
SECRET_KEY = 'django-insecure-4f2sdfu23r90p09sd1f3sdgjsd9sdfgjsdfgjsdfg'


# Will use "livestock-m69e.onrender.com" from your Render environment variable!
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',') if os.environ.get('ALLOWED_HOSTS') else []


ROOT_URLCONF = 'core.urls'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'liveportfolio',
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


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'liveportfolio' / 'templates',  # Add this line to include custom templates
        ],
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


DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL', 'postgres://neondb_owner:npg_ciLjUxoAl4v5@ep-ancient-cloud-a4hcrczz-pooler.us-east-1.aws.neon.tech:5432/neondb')
    )
}


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'


# Directory where collectstatic will collect static files for deployment
STATIC_ROOT = BASE_DIR / 'staticfiles'


# Additional directories where Django will look for static files
STATICFILES_DIRS = [
    BASE_DIR / 'liveportfolio' / 'static',
]


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Auth settings
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'  # IST timezone
USE_I18N = True
USE_TZ = True
