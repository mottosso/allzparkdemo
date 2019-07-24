# -*- coding: utf-8 -*-

name = 'gitlab'

version = '1.1.3'

def commands():
    global env
    global this
    global building
    
    for key, value in this._environ.items():
        env[key] = value

with scope('config') as config:
    config.release_packages_path = 'C:\\Users\\manima\\Dropbox\\dev\\anima\\github\\mottosso\\rez-for-projects\\packages\\ext'

timestamp = 1563997381

_environ = {'GITLAB_URI': 'https://gitlab.mycompany.co.jp'}

format_version = 2
