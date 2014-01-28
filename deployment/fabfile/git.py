import os.path
import tempfile

from fabric.api import env, task, require, local

from utils import TmpDirectory


@task
def pack(path=None, out_file_path=None):
    '''Pack a repository into a .tar.bz2'''
    require('project_name')
    require('repository')
    tmp_prefix = '{}-'.format(env.project_name)

    if not out_file_path:
        handle, out_file_path = tempfile.mkstemp(prefix=tmp_prefix,
                                                 suffix='.tar.bz2')
    with TmpDirectory(prefix=tmp_prefix) as tmp_path:
        # TODO: validate repository and path
        output_dir = os.path.join(tmp_path, 'export')
        clone(env.repository.url, output_dir)
        tar(output_dir, out_file_path)
    env.packed_file = out_file_path


def tar(directory, out_filepath):
    if not directory:
        raise ValueError('missing required directory argument')
    if not os.path.exists(directory):
        raise ValueError('directory {} does not exist'.format(directory))
    if not out_filepath:
        raise ValueError('missing required out_filepath')
    local('tar --create --auto-compress'
          ' --directory {dir} --file {out} .'.format(
        dir=directory, out=out_filepath))


def clone(git_url, output_dir):
    local('mkdir -p {}'.format(output_dir))
    local('cd {}'.format(output_dir))
    local('git clone {repo} {output_dir}'.format(
        repo=git_url,
        output_dir=output_dir))

