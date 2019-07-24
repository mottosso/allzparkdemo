# -*- coding: utf-8 -*-

name = 'dev_maya2'

version = '2018.1.0'

tools = [
    'maya',
    'mayapy',
    'render',
    'mayabatch'
]

requires = []

private_build_requires = ['rezutil-1']

def commands():
    global env
    env.PATH.prepend("{root}/bin")

with scope('config') as config:
    config.release_packages_path = 'C:\\Users\\manima\\Dropbox\\dev\\anima\\github\\mottosso\\rez-for-projects\\packages\\ext'

timestamp = 1563997400

_data = \
    {'color': '#251',
     'hidden': True,
     'icon': '{root}/resources/icon_{width}x{height}.png',
     'label': 'Autodesk Maya'}

format_version = 2
