# -*- coding: utf-8 -*-

name = 'ftrack'

version = '1.0.1'

def commands():
    global env
    global this
    global building
    
    for key, value in this._environ.items():
        env[key] = value

with scope('config') as config:
    config.release_packages_path = 'C:\\Users\\manima\\Dropbox\\dev\\anima\\github\\mottosso\\rez-for-projects\\packages\\ext'

timestamp = 1563997380

_environ = {'FTRACK_PROTOCOL': 'https', 'FTRACK_URI': 'ftrack.mystudio.co.jp'}

format_version = 2
