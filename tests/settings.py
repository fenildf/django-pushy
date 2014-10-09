# assert warnings are enabled
import warnings

warnings.simplefilter('ignore', Warning)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'pushy',
]

SECRET_KEY = 'django-pushy-key'
SITE_ID = 1
ROOT_URLCONF = 'core.urls'

CELERY_ALWAYS_EAGER = True
PUSHY_GCM_API_KEY = 'blah-blah'