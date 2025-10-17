"""
Django settings for production deployment on PythonAnywhere.

This file contains production-specific settings for the Django project.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("DJANGO_SECRET_KEY environment variable is required for production")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# PythonAnywhere specific settings
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '.pythonanywhere.com',  # PythonAnywhere домены
    os.getenv('PYTHONANYWHERE_DOMAIN', ''),  # Ваш домен на PythonAnywhere
]

# CSRF settings for PythonAnywhere
CSRF_TRUSTED_ORIGINS = [
    'https://*.pythonanywhere.com',
    f"https://{os.getenv('PYTHONANYWHERE_DOMAIN', '')}",
]

# Application definition
INSTALLED_APPS = [
    'astana_fund',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise',  # Для обслуживания статических файлов
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Должен быть первым после SecurityMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'server.wsgi.application'

# Database configuration for PythonAnywhere
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # PythonAnywhere использует MySQL
        'NAME': os.getenv('DB_NAME', 'your_database_name'),
        'USER': os.getenv('DB_USER', 'your_username'),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', 'your_username.mysql.pythonanywhere-services.com'),
        'PORT': os.getenv('DB_PORT', '3306'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}

# Password validation
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

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', '587'))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
CONTACT_EMAIL = os.getenv('CONTACT_EMAIL')

# Internationalization
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Asia/Almaty'  # Время Алматы для Казахстана
USE_I18N = True
USE_TZ = True

# Static files configuration for PythonAnywhere
STATIC_URL = '/static/'
STATIC_ROOT = '/home/your_username/astana_fund/staticfiles'  # Замените your_username на ваш username

# WhiteNoise configuration for static files
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Media files configuration for PythonAnywhere
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/your_username/astana_fund/media'  # Замените your_username на ваш username

# Security settings for production
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# HTTPS settings (раскомментируйте если используете HTTPS)
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/home/your_username/astana_fund/logs/django.log',  # Замените your_username
            'formatter': 'verbose',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Cache configuration (опционально, для улучшения производительности)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

# Session configuration
SESSION_COOKIE_AGE = 1209600  # 2 недели
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
