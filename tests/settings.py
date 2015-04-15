import os

import django


DEBUG = True
SECRET_KEY = 'secret'

ROOT_URLCONF = 'tests.urls'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'


DATABASES = {
    'default': {
        'NAME': 'djinga',
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

INSTALLED_APPS = ('djinga',
                  'tests',
                  'django_nose')

MIDDLEWARE_CLASSES = ()

if django.VERSION >= (1, 8):
    TEMPLATES = [
        dict(
            BACKEND='djinga.backends.djinga.DjingaTemplates',
            DIRS=(os.path.join(os.path.dirname('__file__'), 'templates'),),
        ),
    ]
else:
    TEMPLATE_LOADERS = (
        'djinga.loaders.FileSystemLoader',
        'djinga.loaders.AppLoader',
    )
    TEMPLATE_DIRS = (os.path.join(os.path.dirname('__file__'), 'templates'),)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
