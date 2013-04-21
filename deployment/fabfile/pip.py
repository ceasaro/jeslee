import tempfile

from fabric.api  import task, require, env, local

@task
def bundle():
    require('requirements_file')
    tmp_prefix = '{}-requirements-'.format(env.project_name)
    handle, out_filepath = tempfile.mkstemp(prefix=tmp_prefix, 
                suffix='.pybundle')
    local('pip bundle -r {requirements} {out_file}'.format(
                                   requirements=env.requirements_file,
                                   out_file=out_filepath))
    env.pip_bundle = out_filepath