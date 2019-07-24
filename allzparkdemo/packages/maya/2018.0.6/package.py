# -*- coding: utf-8 -*-

name = 'maya'

version = '2018.0.6'

tools = [
    'maya',
    'mayapy',
    'render',
    'mayabatch',
    'mayagui_lic'
]

requires = []

private_build_requires = ['rezutil-1']

def commands():
    global env
    global alias
    global system
    
    env.PATH.prepend("{root}/bin")

with scope('config') as config:
    config.release_packages_path = 'C:\\Users\\manima\\Dropbox\\dev\\anima\\github\\mottosso\\rez-for-projects\\packages\\ext'

timestamp = 1563997387

_data = \
    {'color': '#251',
     'icon': '{root}/resources/icon_{width}x{height}.png',
     'label': 'Autodesk Maya'}

format_version = 2
