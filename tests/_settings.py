import os

import django


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
    'django_nose',
    'tests.app'
)

MIDDLEWARE_CLASSES = ()

_template_dirs = (os.path.join(os.path.dirname('__file__'), 'templates'),)

if django.VERSION >= (1, 8):
    TEMPLATES = [
        dict(
            BACKEND='djinga.backends.djinga.DjingaTemplates',
            DIRS=_template_dirs,
        ),
    ]
else:
    TEMPLATE_LOADERS = (
        'djinga.loaders.FileSystemLoader',
        'djinga.loaders.AppLoader',
    )
    TEMPLATE_DIRS = _template_dirs

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
