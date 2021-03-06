# Django settings for healthMap project.
from jeslee_web.settings.defaults import *
DEBUG = True
TEMPLATE_DEBUG = DEBUG

#django-admin: ceasaro -> D)p$g3ks

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'jeslee_beta',                      # Or path to database file if using sqlite3.
        'USER': 'jeslee_beta_geb',                      # Not used with sqlite3.
        'PASSWORD': 'ZJUerN5qk4ECsPk',                  # Not used with sqlite3.
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

MEDIA_ROOT = '/sites-acc/django/jeslee-beta_media/'

_dev_apps = list(INSTALLED_APPS)
#_dev_apps.append('debug_toolbar')
#_dev_apps.append('debug_toolbar_user_panel')
#_dev_apps.append('django_nose')
#_dev_apps.append('rosetta')
INSTALLED_APPS = tuple(_dev_apps)

#
# iDEAL settings
#
IDEAL_PAYMENT_URL = 'https://ideal.secure-ing.com/ideal/mpiPayInitIng.do'
IDEAL_HASH_KEY = 'j1wNV6GJHSSaZTeI'

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
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': SITE_ROOT + "/jeslee-beta.log",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'simple',
        },#        'mail_admins': {
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
        'accounts_web': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
