from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

# WSGI application
WSGI_APPLICATION = 'config.wsgi.deploy.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ROOT_DIR, 'db.sqlite3'),
    }
}



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, 'mysite', 'media')

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(ROOT_DIR, 'mysite', 'staticfiles')
STATICFILES_DIRS = [
 os.path.join(ROOT_DIR,  'mysite','static'),
]


