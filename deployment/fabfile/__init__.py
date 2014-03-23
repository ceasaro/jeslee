import time
import functools
import os.path

from fabric.api import *
from fabric import colors
from fabric.utils import abort

# fabric hosts + configuration is set in:
import config

# relative import, prevent clashing with the 'real' libs/apps
from . import git
from . import svn
from . import pip
from . import virtualenv
from . import database as db
from . import django

#import amazon

from .utils import TmpDirectory
from fabric.operations import prompt

provided_by_config = (config.test, config.production)


@task
def upgrade():
    '''Upgrade an existing install'''
    require('install_user')
    require('hosts')
    # require('repository.url')
    if not prompt('Upgrading {} with {} -b {}. Sure? CTRL-C to abort'.format(
            env.hosts, env.repository.url, env.repository.branch), default='y'):
        abort('Abort')
    pack()
    upload()
    backup()

    print(colors.red('TODO: impl. upload pip requirements bundle', bold=True))

    tmp_install_dir = '{}_new/'.format(env.install_dir[:-1])  # strip '/'
    sudo('mkdir -p {}'.format(tmp_install_dir))
    sudo('chown {user}.{user} {dir}'.format(user=env.install_user, dir=tmp_install_dir))

    print(colors.red('TODO: activate a maintenance page?', bold=True))

    with cd(tmp_install_dir):
        sudo('tar -xf {}'.format(env.uploaded_packed_file), user=env.install_user)
        sudo('rm {}'.format(env.uploaded_packed_file))
        #        sudo('chmod +x deployment/cron/*.sh')
        with virtualenv.context(env.virtualenv_dir):
            sudo_as = functools.partial(sudo, user=env.install_user)
            django.project_manage_upgrade(exec_cmd=sudo_as, manage_cmd='python ./manage.py')

    # move/rename dirs
    install_backup_dir = '{}_old/'.format(env.install_dir[:-1])  # strip '/'
    sudo('rm -rf {install_backup_dir}'.format(install_backup_dir=install_backup_dir))
    sudo('mv {install_dir} {install_backup_dir} && '
         'mv {tmp_install_dir} {install_dir}'.format(
        install_dir=env.install_dir,
        install_backup_dir=install_backup_dir,
        tmp_install_dir=tmp_install_dir))
    sudo('uwsgi --reload /tmp/jeslee-master.pid')


@task
def pip_install_requirements():
    require('virtualenv_dir')
    pip.bundle()
    require('pip_bundle')
    install_puts = put(env.pip_bundle, '/tmp/')
    env.pip_bundle_uploaded = install_puts[0]
    with virtualenv.context(env.virtualenv_dir):
        sudo('pip install {}'.format(env.pip_bundle_uploaded))
    sudo('rm {}'.format(env.pip_bundle_uploaded))


# TODO: integrate into upgrade task
@task
def new_install():
    '''A new installation'''
    require('install_user')
    pack()
    upload()

    ubuntu_apt_get()
    execute(virtualenv.create)
    pip_install_requirements()

    # TODO: check database permissions?
    db.create()

    tmp_install_dir = '{}_new/'.format(env.install_dir[:-1])  # strip '/'
    sudo('mkdir -p {}'.format(tmp_install_dir))
    sudo('chown {user}.{user} {dir}'.format(user=env.install_user,
                                            dir=tmp_install_dir))

    with cd(tmp_install_dir):
        sudo('tar -xf {}'.format(env.uploaded_packed_file),
             user=env.install_user)
        sudo('rm {}'.format(env.uploaded_packed_file))
        with cd('caire_web'), virtualenv.context(env.virtualenv_dir):
            sudo_as_caire = functools.partial(sudo, user=env.install_user)
            django.project_manage_upgrade(exec_cmd=sudo_as_caire)
            # TODO: loaddata categories
    sudo('mv {tmp_install_dir} {install_dir}'.format(
        tmp_install_dir=tmp_install_dir,
        install_dir=env.install_dir))
    print(colors.red('TODO: configure apache: (sym)link apache config', bold=True))


@task
def backup():
    ''' Backup existing installation'''
    require('install_dir', provided_by=provided_by_config)
    with TmpDirectory(prefix='jeslee-backup') as tmp_dir:
        backup_base_dir = os.path.normpath(os.path.join(env.install_dir, '..', 'backups'))
        backup_dir = os.path.normpath(os.path.join(backup_base_dir, time.strftime('%Y%m%d%H%M%S')))
        sudo('mkdir -p {}'.format(backup_dir))
        with cd(backup_dir):
            db.backup(exec_cmd=sudo)
            sudo('tar -cjf {}.tar.bz2 {}'.format(env.project_name, env.install_dir))
        #            sudo('tar -cjf caire_media.tar.bz2 {}'.format(env.django_media_root))
        print(colors.red('TODO: enable coping backup to local machine', bold=True))
        # with lcd('/tmp/'):
        #     get(backup_dir)


@task
def pack(**kwargs):
    """Pack the project into a .tar.bz2"""
    require('repository')
    #if env.repository.startswith('svn://'):
    if env.repository.type == 'svn':
        execute(svn.pack, **kwargs)
    if env.repository.type == 'git':
        execute(git.pack, **kwargs)
    else:
        abort('Unsupported repository type %s' % env.repository)


@task
def upload():
    '''Upload the packed project files to remote server'''
    require('packed_file', provided_by=pack)
    puts = put(env.packed_file, '/tmp/')
    env.uploaded_packed_file = puts[0]


@task
def host_type():
    """ Output the type of remote host"""
    output = run('uname -s')
    if output == 'Linux':
        print(colors.green(output, bold=True))
    else:
        print(colors.red(output, bold=True))

