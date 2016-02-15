""" Configuration(s) for the project and different hosts
"""
import os
from os.path import normpath, dirname, join, expandvars

from fabric.api import env, require, abort
from fabric.decorators import task

from . import django
from .utils import AttrDict


env.use_ssh_config = True # try and use some settings from $HOME/.ssh/config

env.project_name = 'jeslee'
env.project_root = normpath(join(dirname(__file__), '..', '..'))
env.project_django_root = join(env.project_root, '')

env.repository = AttrDict(
    type='git',
    url='https://github.com/ceasaro/jeslee',
    branch='master'
)

env.django_project = 'jeslee'  # default django project (dir)

env.django_manage_commands = ('migrate',
                              'collectstatic --noinput',
)

env.ubuntu_required_packages = [
    # Base python env (need gcc to compile python modules)
    'gcc', 'g++', 'python-dev', 'python-virtualenv',
    # apache, this should pull in the rest of apache2 
    'libapache2-mod-wsgi',
    # req. for certain python packages (which will be installed in virtualenv)
    'libhaml-ruby1.8', 'zlib1g-dev', 'libjpeg62-dev',
    'libfreetype6-dev', 'libmysqld-dev', 'gettext',
    'libcurl4-openssl-dev', 'librtmp-dev', 'libgnutls-dev']


@task()
def test():
    '''Configuration for local development'''
    env.hosts = ['localhost']
    env.install_dir = '/tmp/jeslee_test_deploy'
    env.install_user = os.environ['USER']
    #    env.django_media_root = '/tmp/caire_test_deploy_media/'
    env.requirements_file = join(env.project_root,
                                 'requirements/dev.txt')
    env.virtualenv_dir = expandvars('$WORKON_HOME/jeslee/')
    env.django_settings = 'jeslee_web.settings.dev'
    django_settings_to_env()
    env.django_developing = True

@task()
def acceptation():
    '''Configuration for acceptation server'''
    env.hosts = ['beta.jeslee.com']
    env.install_dir = '/sites-acc/django/jeslee-beta/'
    env.install_user = 'jeslee'
    #    env.django_media_root = '/opt/caire_media'
    env.requirements_file = join(env.project_root,
                                 'requirements/acceptation.txt')
    env.virtualenv_dir = '/opt/virtualenvs/jeslee-beta/'
    env.django_settings = 'jeslee_web.settings.acceptation'
    # env.repository.branch = 'bookkeeping'
    django_settings_to_env()
    env.django_developing = False
    env.uwsgi_pid = '/var/run/uwsgi/jeslee-beta-master.pid'


# @task(alias='prod')
@task()
def production():
    '''Configuration for production server'''
    env.hosts = ['jeslee.com']
    env.user = 'ceasaro'
    env.install_dir = '/sites/django/jeslee/'
    env.install_user = 'jeslee'
    #    env.django_media_root = '/opt/caire_media'
    env.requirements_file = join(env.project_root,
                                 'requirements/production.txt')
    env.virtualenv_dir = '/opt/virtualenvs/jeslee/'
    env.django_settings = 'jeslee_web.settings.production'
    # env.repository.branch = 'master'
    django_settings_to_env()
    env.django_developing = False
    env.uwsgi_pid = '/var/run/uwsgi/jeslee-master.pid'


def django_settings_to_env():
    '''Export some settings from Django to Fabric's env'''
    require('django_settings')
    settings = django.get_settings()
    db_settings = settings.DATABASES['default']
    db_engine = db_settings['ENGINE']
    db_name = db_settings['NAME']
    db_user = db_settings['USER']
    db_password = db_settings['PASSWORD']
    db_host = db_settings['HOST']
    db_port = db_settings['PORT']

    env.database = AttrDict(
        type=_django_engine_to_type(db_engine),
        host=db_host,
        port=db_port,
        name=db_name,
        user=db_user,
        password=db_password
    )
    env.media_root = settings.MEDIA_ROOT


def _django_engine_to_type(engine):
    if 'mysql' in engine:
        return 'mysql'
    elif 'sqlite' in engine:
        return 'sqlite'
    elif 'postgres' in engine:
        return 'postgres'
    else:
        abort("Unknown Django database engine '{}'".format(engine))
