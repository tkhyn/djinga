import os


DEBUG = True
SECRET_KEY = 'secret'

ROOT_URLCONF = 'tests.app.urls'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'


DATABASES = {
    'default': {
        'NAME': 'djinga',
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

INSTALLED_APPS = (
    'djinga',
    'tests.app'
)

TEMPLATES = [
    dict(
        BACKEND='djinga.backends.djinga.DjingaTemplates',
        DIRS=(os.path.join(os.path.dirname('__file__'), 'templates'),),
    ),
]
