import os

# Relative path settings
from unipath import Path
PROJECT_ROOT = Path(__file__).ancestor(3)

# Set various variables.
TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = PROJECT_ROOT.child('media')

# Absolute path to the directory static files should be collected to using collectstatic.
STATIC_ROOT = ''

# Additional locations of static files - absolute paths
STATICFILES_DIRS = (
	PROJECT_ROOT.child('static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader'
)

ROOT_URLCONF = 'redditology.urls'

# WSGI server for debug server.
WSGI_APPLICATION = 'redditology.wsgi.application'

# Templates location - absolute path
TEMPLATE_DIRS = (
	PROJECT_ROOT.child('templates'),
)

# Set up Sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# Celery settings
import djcelery
djcelery.setup_loader()

# Set up simple master logger
LOGGING = {
	'version': 1,
	'disable_existing_loggers': True,
	'formatters': {
		'verbose': {
			'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
		},
		'simple': {
			'format': '%(levelname)s %(message)s'
		},
	},
	'handlers': {
		'console':{
			'level': 'INFO',
			'class': 'logging.StreamHandler',
			'formatter': 'simple'
		},
		'info': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': 'info.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 3,
            'formatter':'verbose',
        },  
		'master': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': 'master.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 3,
            'formatter':'verbose',
        },  
	},
	'loggers': {
		'': {
			'handlers': ['console', 'info', 'master'],
			'level': 'DEBUG',
			'propagate': True,
		},
	}
}

TEMPLATE_CONTEXT_PROCESSORS = (
	"django.contrib.auth.context_processors.auth",
	"django.core.context_processors.debug",
	"django.core.context_processors.i18n",
	"django.core.context_processors.media",
	"django.core.context_processors.static",
	"django.core.context_processors.tz",
	"django.contrib.messages.context_processors.messages",
	'django.core.context_processors.request',
)

SUIT_CONFIG = {
    'ADMIN_NAME': 'Redditology'
}

# Import corresponding environment settings.
try:
	app_env = os.environ["REDDITOLOGY_ENV"]
	if app_env == "production":
		# Import production settings
		from .production import *
	elif app_env == "development":
		# Import development settings
		from .development import *
except KeyError, e:
	# import local settings
	from .local import *