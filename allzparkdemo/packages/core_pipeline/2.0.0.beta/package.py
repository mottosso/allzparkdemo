# -*- coding: utf-8 -*-

name = 'core_pipeline'

version = '2.0.0.beta'

private_build_requires = ['rezutil-1']

def commands():
    global env
    global this
    global system
    global expandvars
    
    for key, value in this._environ.items():
        if isinstance(value, (tuple, list)):
            [env[key].append(expandvars(v)) for v in value]
        else:
            env[key] = expandvars(value)

with scope('config') as config:
    config.release_packages_path = 'C:\\Users\\manima\\Dropbox\\dev\\anima\\github\\mottosso\\rez-for-projects\\packages\\ext'

timestamp = 1563997419

_environ = {'PYTHONPATH': ['{root}/python']}

format_version = 2
