import os
import dj_database_url

DEBUG = True  # For local development. Set to False on production (Render)!
SECRET_KEY = 'django-insecure-4f2sdfu23r90p09sd1f3sdgjsd9sdfgjsdfgjsdfg'
ALLOWED_HOSTS = []  # For production, set to your Render domain
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
        'DIRS': [],
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

# Auto-detect DATABASE_URL for cloud, else fallback to Neon local info
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL', 'postgres://neondb_owner:npg_ciLjUxoAl4v5@ep-ancient-cloud-a4hcrczz-pooler.us-east-1.aws.neon.tech:5432/neondb')
    )
}

STATIC_URL = '/static/'

# For Render/production
STATIC_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../staticfiles')
