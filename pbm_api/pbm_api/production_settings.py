import secrets

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets.token_hex(nbytes=16)

DEBUG = True
ALLOWED_HOSTS = ['*']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'deeparmor',
        'USER': 'postgres',
        'PASSWORD': 'deeparmor',
        'HOST': 'localhost',
        'TEST': {
            'NAME': 'test_pbm' + secrets.token_hex(nbytes=8)
        }
    }
}
