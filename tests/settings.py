DEBUG = True
SECRET_KEY = 'secret'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'


DATABASES = {
    'default': {
        'NAME': 'djinga',
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

INSTALLED_APPS = ('django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'django.contrib.admin',
                  'djinga',
                  'tests',
                  'django_nose')

MIDDLEWARE_CLASSES = ()

TEMPLATE_LOADERS = (
    'djinga.loaders.FileSystemLoader',
    'djinga.loaders.AppLoader',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
