from __future__ import absolute_import
import sys
import os.path

from fabric.api import env, task, require, cd, prefix, run, sudo, local, lcd


@task
def update(exec_cmd=sudo):
    '''Update a Django project (running required management commands)'''
    require('install_dir')
    require('virtualenv_dir')
    with cd(env.install_dir), cd('caire_web'), \
                 prefix('. {}bin/activate'.format(env.virtualenv_dir)):
        run('pwd')
        project_manage_upgrade(exec_cmd=exec_cmd)


@task
def local_update():
    '''Update the local Django project (running required management commands'''
    require('project_root')
    require('virtualenv_dir')
    with lcd(env.project_root), lcd('caire_web'), \
            prefix('. {}bin/activate'.format(env.virtualenv_dir)):
        project_manage_upgrade(exec_cmd=local)


def project_manage_upgrade(exec_cmd=sudo, manage_cmd='./manage.py'):
    require('django_manage_commands')
    require('django_settings')
    # TODO: check manage_cmd exists?
    settings = env.django_settings
    for command in env.django_manage_commands:
        exec_cmd('{manage} {command} --settings={settings}'.format(
                                                          manage=manage_cmd,
                                                          command=command,
                                                          settings=settings))


def get_settings():
    from fabric.contrib.django import settings_module
    settings_module(env.django_settings)
    # mimic Django's dual path :/ 
    if env.project_root not in sys.path:
        sys.path.append(os.path.join(env.project_root))
        # TODO for some reason fab doesn't add the correct virtual envs to the sys path
        # sys.path.append('/home/ceasaro/.virtualenvs/jeslee/bin/python')
        # sys.path.append('/home/ceasaro/.virtualenvs/jeslee/lib/python2.7/site-packages/')
        sys.path.append('/home/cees/Envs/jeslee/bin/python')
        sys.path.append('/home/cees/Envs/jeslee/lib/python2.7/site-packages/')
    print sys.path

    from django.conf import settings
    return settings
