from fabric.api import task, require, env, run, abort

from . import mysql

@task
def backup(exec_cmd=run, outfile=None):
    require('database')
    db_config = env.database
    if(db_config.type == 'mysql'):
        mysql.backup(exec_cmd=exec_cmd, outfile=outfile)
    else:
        abort('Unsupported database type {}'.format(db_config.type))


@task
def create(exec_cmd=run):
    require('database')
    db_config = env.database
    if(db_config.type == 'mysql'):
        mysql.create(exec_cmd=exec_cmd)
    else:
        abort('Unsupported database type {}'.format(db_config.type))