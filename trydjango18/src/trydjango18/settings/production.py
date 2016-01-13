
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o!o%wv@pm$6a0oi574gm!(ylz-bd_$u!mysn(x-pevds97nvz@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ['*']


#Email configuration
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'guitarlegend.android@gmail.com'
EMAIL_HOST_PASSWORD = 'escomsistemas'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    #Third party apps
    'crispy_forms',
    'registration',
    #My apps
    'newsletter'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'trydjango18.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'trydjango18.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

#Entorno de produccion
#STATIC_ROOT = os.path.join(BASE_DIR,"static_in_pro","static_root")

#Entorno de env
# carpeta static_in_env debe de estar fuera del directorio principal
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static_in_env","static_root")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_in_pro","our_static"),
    #'/var/www/static/',
]

MEDIA_URL = '/media/'
#Entorno de produccion
#MEDIA_ROOT = os.path.join(BASE_DIR,"static_in_pro","media_root")
#Entorno de env
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static_in_env","media_root")


#Configuracion Crispy form
CRISPY_TEMPLATE_PACK = 'bootstrap3'

#Configuracion Django registration redux
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'