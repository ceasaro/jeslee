""" Configuration(s) for the project and different hosts
"""
import os
from os.path import  normpath, dirname, join, expandvars
from fabric.api import env, task, require, abort

from . import django
from .utils import AttrDict

env.use_ssh_config = True # try and use some settings from $HOME/.ssh/config

env.project_name = 'vortex'
env.project_root = normpath(join(dirname(__file__), '..', '..'))
env.project_django_root = join(env.project_root, '')

env.repository = AttrDict(
        type='svn',
        url='svn://svn.fam/data/svn/radyus/vortex/'
        )

env.django_project = 'vortex_web'  # default django project (dir)

env.django_manage_commands =  ('syncdb --noinput',
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


@task(aliases=('dev','local'))
def development():
    '''Configuration for local development'''
    env.hosts = ['localhost']
    env.install_dir = '/tmp/vortex_test_deploy'
    env.install_user = os.environ['USER']
#    env.django_media_root = '/tmp/caire_test_deploy_media/'
    env.requirements_file = join(env.project_root,
                                 'requirements/dev.txt')
    env.virtualenv_dir = expandvars('$WORKON_HOME/caire/')
    env.django_settings = 'vortex_web.settings.dev'
    env.svn_branch = 'trunk/'
    django_settings_to_env()
    env.django_developing = True

@task(alias='prod')
def production():
    '''Configuration for production server'''
    env.hosts = ['vortex.adverterenwerkt.nl']
    env.install_dir = '/opt/vortex/'
    env.install_user = 'vortex'
#    env.django_media_root = '/opt/caire_media'
    env.requirements_file = join(env.project_root,
                                 'requirements/production.txt')
    env.virtualenv_dir = '/opt/virtualenvs/vortex/'
    env.django_settings = 'vortex_web.settings.production'
    env.svn_branch = 'trunk/'
    django_settings_to_env()
    env.django_developing = False


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

def _django_engine_to_type(engine):
    if 'mysql' in engine:
        return 'mysql'
    elif 'sqlite' in engine:
        return 'sqlite'
    elif 'postgres' in engine:
        return 'postgres'
    else:
        abort("Unknown Django database engine '{}'".format(engine))
