# -*- coding: utf-8 -*-

name = 'alita'

version = '0.2.0'

@late()
def requires():
    global this
    global request
    global in_context
    
    requires = this._requires
    result = requires["any"][:]
    
    # Add request-specific requirements
    if in_context():
        for name, reqs in requires.items():
            if name not in request:
                continue
    
            result += reqs
    
    return result

private_build_requires = ['rezutil-1']

def commands():
    global env
    global this
    global request
    global expandvars
    
    environ = this._environ
    result = list(environ["any"].items())
    
    # Add request-specific environments
    for key, values in environ.items():
        if key not in request:
            continue
    
        result += list(values.items())
    
    for key, value in result:
        if isinstance(value, (tuple, list)):
            [env[key].append(expandvars(v)) for v in value]
        else:
            env[key] = expandvars(value)

with scope('config') as config:
    config.release_packages_path = 'C:\\Users\\manima\\Dropbox\\dev\\anima\\github\\mottosso\\rez-for-projects\\packages\\ext'

timestamp = 1563997410

_data = \
    {'icon': '{root}/resources/icon_{width}x{height}.png',
     'label': 'Alita - Battle Angel'}

_requires = \
    {'any': ['welcome-1',
             'base-1',
             '~maya==2017.0.4|==2018.0.5',
             '~dev_maya2',
             '~nuke==11.3.5',
             '~terminal',
             '~texteditor'],
     'maya': ['maya_base', 'mgear-2.4'],
     'nuke': []}

_environ = \
    {'any': {'PRODUCTION_TRACKER_ID': 'alita-123',
             'PROJECT_NAME': 'Alita',
             'PROJECT_PATH': '{env.PROJECTS_PATH}/alita'},
     'maya': {'MAYA_COLOR_MANAGEMENT_POLICY_FILE': ['{env.PROJECT_PATH}/maya/color_management/default_synColorConfig.xml'],
              'MAYA_PLUG_IN_PATH': ['{env.PROJECT_PATH}/maya/plugins'],
              'MAYA_SCRIPT_PATH': ['{env.PROJECT_PATH}/maya/scripts'],
              'MAYA_SHELF_PATH': '{env.PROJECT_PATH}/maya/shelves',
              'MYPATH': '{env.REZ_MAYA_MAJOR_VERSION}/some/dir',
              'PYTHONPATH': ['{env.PROJECT_PATH}/maya/scripts',
                             '{env.PROJECT_PATH}/maya/shelves'],
              'XBMLANGPATH': ['{env.PROJECT_PATH}/maya/shelves/icons']}}

format_version = 2
