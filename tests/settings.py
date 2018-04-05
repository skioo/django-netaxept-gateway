# flake8: noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db'
    },
}

SECRET_KEY = 'not_so_secret'

# Use a fast hasher to speed up tests.
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'netaxept',
    'tests',
]

STATIC_URL = '/static/'

ROOT_URLCONF = 'tests.urls'
