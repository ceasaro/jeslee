"""Run our Django application as a WSGI application

Example usage for uWSGI
uwsgi -s 127.0.0.1:48313 --master --processes 4 \
        --socket-timeout 30 --listen 128 \
        --disable-logging \
        --virtualenv $VIRTUALENV \
        --chdir $PROJECTDIR \
        --file wsgi/caire_wsgi.py
"""
import os
import sys
import django.core.handlers.wsgi

# put the Django project on sys.path
PROJECT_ROOT = os.path.normpath(os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '..','..'))
sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'jeslee_web'))

# Configure used settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'jeslee_web.settings.production'

application = django.core.handlers.wsgi.WSGIHandler()
