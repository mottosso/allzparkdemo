# -*- coding: utf-8 -*-

name = 'maya'

version = '2017.0.4'

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

timestamp = 1563997385

_data = \
    {'color': '#251',
     'icon': '{root}/resources/icon_256x256.png',
     'label': 'Autodesk Maya'}

format_version = 2
