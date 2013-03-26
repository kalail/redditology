import os

# Debug
DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': os.environ.get('REDDITOLOGY_DB_NAME'),
		'USER': os.environ.get('REDDITOLOGY_DB_USER'),
		'PASSWORD': os.environ.get('REDDITOLOGY_DB_PASSWORD'),
		'HOST': os.environ.get('REDDITOLOGY_DB_HOST'),
	}
}

# Amazon S3 setting
AWS_ACCESS_KEY_ID = os.environ.get("REDDITOLOGY_AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("REDDITOLOGY_AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = 'redditology'

# DEFAULT_FILE_STORAGE = 'helpers.storages.MediaS3Storage'
# STATICFILES_STORAGE = 'helpers.storages.StaticS3Storage'

# URL prefix for files.
STATIC_URL = 'https://s3.amazonaws.com/' + AWS_STORAGE_BUCKET_NAME + '/static/'
MEDIA_URL = 'https://s3.amazonaws.com/' + AWS_STORAGE_BUCKET_NAME + '/media/'

# RabbitMQ
BROKER_URL = os.environ.get('REDDITOLOGY_ZEROMQ_LOCATION')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': os.environ.get('REDDITOLOGY_MEMCACHED_LOCATION'),
    }
}

INSTALLED_APPS = (
	# Contrib
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	# Django Suits needds to be added before admin
	'suit',
	'django.contrib.admin',
	'django.contrib.admindocs',
	# Third party
	'south',
	'djcelery',
	'django_extensions',
	'storages',
	'gunicorn',
	# App
	'fetcher',
	'posts',
)

SECRET_KEY = os.environ.get('REDDITOLOGY_SECRET_KEY')