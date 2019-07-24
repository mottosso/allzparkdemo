# -*- coding: utf-8 -*-

name = 'lotr'

version = '1.13.4'

requires = [
    'base-1',
    '~maya-2018|2019',
    '~nuke-9'
]

private_build_requires = ['rezutil-1']

def commands():
    global env
    global this
    global expandvars
    
    for key, value in this._environ.items():
        if isinstance(value, (tuple, list)):
            [env[key].append(expandvars(v)) for v in value]
        else:
            env[key] = expandvars(value)

with scope('config') as config:
    config.release_packages_path = 'C:\\Users\\manima\\Dropbox\\dev\\anima\\github\\mottosso\\rez-for-projects\\packages\\ext'

timestamp = 1563997404

_environ = \
    {'PRODUCTION_TRACKER_ID': 'lotr-124',
     'PROJECT_NAME': 'Lord of the Rings',
     'PROJECT_PATH': '{env.PROJECTS_PATH}/lotr'}

_data = \
    {'icon': '{root}/resources/icon_{width}x{height}.png',
     'label': 'Lord of the Rings'}

format_version = 2
