import os

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

TEMPLATE_LOADERS = (
    'djinga.loaders.FileSystemLoader',
    'djinga.loaders.AppLoader',
)

TEMPLATE_DIRS = (os.path.join(os.path.dirname('__file__'), 'templates'),)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
