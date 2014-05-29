# Django settings for JesLee project.
import locale
import os
from django.core.urlresolvers import reverse_lazy
# django imports
from django.utils.translation import gettext_lazy as _

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
PROJECT_DIR = os.path.dirname(SITE_ROOT) # this is not Django setting.

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'lfs_test',                      # Or path to database file if using sqlite3.
        'USER': 'lfs_test',                      # Not used with sqlite3.
        'PASSWORD': 'lfs_test',                  # Not used with sqlite3.
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

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
# TIME_ZONE = 'Europe/Amsterdam'
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'nl'
#locale.setlocale(locale.LC_ALL, "nl_NL.UTF-8")

DATE_FORMAT = 'j N Y'
TIME_FORMAT = 'h:m'
STRING_TO_DATE_FORMAT = '%d %B %Y'
LOCALE_PATHS = (
    PROJECT_DIR+'/conf/locale',
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = PROJECT_DIR + '/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.normpath(os.path.join(SITE_ROOT, '../sitestatic'))

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SITE_ROOT, 'static'), #Our custom static files for this site.
    # os.path.join(SITE_ROOT, '../lfs/lfs_project/sitestatic'), #static from LFS
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'aqy&he61s5co+c1bd5ec*q_g6vkn+=h$n*-54@wicy=n=q6q4+'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # removed, cause it uses the browsers default and this is mostly english and we want to use dutch.
    # 'django.middleware.locale.LocaleMiddleware',
    'lfs.utils.middleware.RedirectFallbackMiddleware',
    "pagination.middleware.PaginationMiddleware",
)

ROOT_URLCONF = 'jeslee_web.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'jeslee_web.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SITE_ROOT, "templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',

    # own written django apps
    'jeslee_web.utils',
    'jeslee_web.base',
    'jeslee_web.lfs_patch',
    'jeslee_web.fashion_show',
    'jeslee_web.ideal',
    #    'jeslee_web.account'

    # none default django apps
    'django_extensions',
    'django.contrib.webdesign',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    'django_countries',
    'compressor',
    'pagination',
    'reviews',
    'tagging',
    'portlets',

    # LFS (Lighting Fast Shop)
    'lfs',
    'lfs.tests',
    'lfs.core',
    'lfs.caching',
    'lfs.cart',
    'lfs.catalog',
    'lfs.checkout',
    'lfs.criteria',
    'lfs.customer',
    'lfs.discounts',
    'lfs.export',
    'lfs.gross_price',
    'lfs.integrationtests',
    'lfs.mail',
    'lfs.manage',
    'lfs.marketing',
    'lfs.manufacturer',
    'lfs.net_price',
    'lfs.order',
    'lfs.page',
    'lfs.payment',
    'lfs.portlet',
    'lfs.search',
    'lfs.shipping',
    'lfs.supplier',
    'lfs.tagging',
    'lfs.tax',
    'lfs.customer_tax',
    'lfs.utils',
    'lfs.voucher',
    'lfs_contact',
    'lfs_order_numbers',
    'postal',
    'paypal.standard.ipn',
    'paypal.standard.pdt',
    'gunicorn',
#    'lfstheme',

    'south',
    )

FORCE_SCRIPT_NAME=""
LOGIN_URL           = reverse_lazy('login')
LOGIN_ERROR_URL     = reverse_lazy('login-error')

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'lfs.core.context_processors.main',
)

AUTHENTICATION_BACKENDS = (
    'lfs.customer.auth.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# For sql_queries
INTERNAL_IPS = (
    "127.0.0.1",
)

CACHE_MIDDLEWARE_KEY_PREFIX = "lfs"
# CACHE_BACKEND = 'file:///'
# CACHE_BACKEND = 'locmem:///'
# CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
CACHE_BACKEND = 'dummy:///'

DEFAULT_FROM_EMAIL = 'info@jeslee.com'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'info@jeslee.com'
EMAIL_HOST_PASSWORD = 'saluttuta'


PAYPAL_RECEIVER_EMAIL = "info@yourbusiness.com"
PAYPAL_IDENTITY_TOKEN = "set_this_to_your_paypal_pdt_identity_token"

# TODO: Put this into the Shop model
LFS_LOCALE = "nl_NL"
LFS_PAYPAL_REDIRECT = True
LFS_AFTER_ADD_TO_CART = "lfs_cart"
LFS_RECENT_PRODUCTS_LIMIT = 5

LFS_ORDER_NUMBER_GENERATOR = "jeslee_web.lfs_patch.models.OrderNumberGenerator"
LFS_DOCS = "http://docs.getlfs.com/en/latest/"

LFS_INVOICE_COMPANY_NAME_REQUIRED = False
LFS_INVOICE_EMAIL_REQUIRED = True
LFS_INVOICE_PHONE_REQUIRED = True

LFS_SHIPPING_COMPANY_NAME_REQUIRED = False
LFS_SHIPPING_EMAIL_REQUIRED = False
LFS_SHIPPING_PHONE_REQUIRED = False

LFS_PAYMENT_METHOD_PROCESSORS = [
    ["jeslee_web.ideal.lfs_ideal.IdealPaymentMethodProcessor", _(u"iDEAL payment")],
]
LFS_PRICE_CALCULATORS = [
    ['lfs.gross_price.GrossPriceCalculator', _(u'Price includes tax')],
    ['lfs.net_price.NetPriceCalculator', _(u'Price excludes tax')],
]

LFS_SHIPPING_METHOD_PRICE_CALCULATORS = [
    ["lfs.shipping.GrossShippingMethodPriceCalculator", _(u'Price includes tax')],
    ["lfs.shipping.NetShippingMethodPriceCalculator", _(u'Price excludes tax')],
]

LFS_UNITS = [
#    u"l",
#    u"m",
#    u"qm",
#    u"cm",
#    u"lfm",
#    u"Package",
    u"Piece",
]
LFS_CRITERIA = [
    ["jeslee_web.lfs_patch.core.models.ClothingCriterion", _(u"Clothing Criterion")],
    ]
LFS_PRICE_UNITS = LFS_BASE_PRICE_UNITS = LFS_PACKING_UNITS = LFS_UNITS

LFS_LOG_FILE = SITE_ROOT + "/../lfs.log"

LFS_THUMBNAIL_SIZES = ((208, 270), (450, 584), (104,135), (60, 60), (100, 100), (200, 200), (300, 300), (400, 400))

#
# iDEAL settings (TEST environment)
#
IDEAL_PAYMENT_URL = 'https://idealtest.secure-ing.com/ideal/mpiPayInitIng.do'
IDEAL_MERCHANT_ID = '005081894'
IDEAL_HASH_KEY = 'gxfE9kiasIyZ2yZU'
IDEAL_DEFAULT_SUB_ID = '0'
IDEAL_PAYMENT_TYPE = 'ideal'
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
        'accounts_web': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

REVIEWS_SHOW_PREVIEW = False
REVIEWS_IS_NAME_REQUIRED = False
REVIEWS_IS_EMAIL_REQUIRED = False
REVIEWS_IS_MODERATED = False

try:
    from local_settings import *
except ImportError:
    pass
