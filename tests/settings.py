DEBUG = True

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
                'tests',)

TEMPLATE_LOADERS = (
    'djinga.loaders.FileSystemLoader',
    'djinga.loaders.AppLoader',
)
