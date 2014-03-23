__test__ = False

SETTINGS = dict(
    DEBUG=True,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    INSTALLED_APPS=('django.contrib.auth',
                    'django.contrib.contenttypes',
                    'django.contrib.sessions',
                    'django.contrib.admin',
                    'djinga',),
    TEMPLATE_LOADERS=(
        'djinga.loaders.FileSystemLoader',
        'djinga.loaders.AppLoader',
    )
)
