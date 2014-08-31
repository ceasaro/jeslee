# Django settings for healthMap project.
from jeslee_web.settings.defaults import *
DEBUG = True
TEMPLATE_DEBUG = DEBUG


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'jeslee',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
#    'default': {
#        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': 'accounts_dev',                      # Or path to database file if using sqlite3.
#        'USER': 'accounts_dev',                      # Not used with sqlite3.
#        'PASSWORD': 'accounts_dev',                  # Not used with sqlite3.
#        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#    }
}

MEDIA_ROOT = PROJECT_DIR + '/media/'
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TEMPLATE_CONTEXT': True,
}
_dev_apps = list(INSTALLED_APPS)
_dev_apps.append('debug_toolbar')
_dev_apps.append('werkzeug')
# _dev_apps.append('debug_toolbar_user_panel')
#_dev_apps.append('django_nose')
#_dev_apps.append('rosetta')
INSTALLED_APPS = tuple(_dev_apps)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            },
#        'mail_admins': {
#            'level': 'ERROR',
#            'class': 'django.utils.log.AdminEmailHandler'
#        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'jeslee_web': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# test settings
TEST_RUNNER = 'django_patches.test.NoDatabaseRunner.NoDatabaseRunner'

#
# iDEAL settings (TEST environment)
#
IDEAL_PAYMENT_URL = 'https://idealtest.secure-ing.com/ideal/mpiPayInitIng.do'
IDEAL_HASH_KEY = 'gxfE9kiasIyZ2yZU'

# Try and load local_settings.py
try:
    # pylint: disable-msg=F0401
    from jeslee_web.settings.local_settings import *
    # pylint: enable-msg=F0401
except ImportError:
    pass

#
# Disable cache for development
#
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}