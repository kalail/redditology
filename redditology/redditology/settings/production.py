DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': 'redditology_db',                      # Or path to database file if using sqlite3.
		'USER': 'redditology_user',                      # Not used with sqlite3.
		'PASSWORD': 'redditology_password',                  # Not used with sqlite3.
		'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
		'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
	}
}

# URL prefix for static files.
STATIC_URL = '/static/'

# Unique key for Django.
SECRET_KEY = 'xa9z4xzf3ejaqy$4yurs4b+r@#gkh10#tl@09$@u&amp;!%+v=g6(3'

# Redis settings
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'


# Set up Cache
CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
		'LOCATION': '127.0.0.1:11211'
	}
}


INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'suit',
	'django.contrib.admin',
	'django.contrib.admindocs',
	'south',
	'djcelery',

	'fetcher',
	'posts',
)