# -*- coding: utf-8 -*-

name = 'mgear'

version = '2.4.2'

requires = ['~maya-2016+<2019']

private_build_requires = ['rezutil-1']

def commands():
    global env
    global this
    global expandvars
    
    _environ = this._environ
    
    for key, value in _environ.items():
        if isinstance(value, (tuple, list)):
            [env[key].append(expandvars(v)) for v in value]
        else:
            env[key] = expandvars(value)

with scope('config') as config:
    config.release_packages_path = 'C:\\Users\\manima\\Dropbox\\dev\\anima\\github\\mottosso\\rez-for-projects\\packages\\ext'

timestamp = 1563997405

_environ = \
    {'MGEAR_SHIFTER_COMPONENT_PATH': '{root}/python/mGear/build/components',
     'MGEAR_SHIFTER_CUSTOMSTEP_PATH': '{root}/python/mGear/build/custom_steps',
     'MGEAR_SYNOPTIC_PATH': '{root}/python/mGear/env/synoptic'}

format_version = 2
