from .base import *

config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

DEBUG = True
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']

# WSGI application
WSGI_APPLICATION = 'mysite.config.wsgi.debug.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ROOT_DIR, 'db.sqlite3'),
    }
}

MEDIA_URL = '/image_upload/'
MEDIA_ROOT = os.path.join(ROOT_DIR, 'mysite', 'media')


MIDDLEWARE += ['django.middleware.security.SecurityMiddleware']
INTERNAL_IPS = ['127.0.0.1']


STATIC_URL = '/static/'
STATICFILES_DIRS = [
 os.path.join(ROOT_DIR, 'mysite', 'froala_editor'),
]
STATIC_ROOT = os.path.join(ROOT_DIR, 'mysite', 'staticfiles')

FROALA_UPLOAD_PATH = ''