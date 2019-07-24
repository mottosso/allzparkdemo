# -*- coding: utf-8 -*-

name = 'terminal'

version = '1.4.0'

requires = []

private_build_requires = ['rezutil-1']

def commands():
    global env
    
    env.PATH.append("{root}/bin")

with scope('config') as config:
    config.release_packages_path = 'C:\\Users\\manima\\Dropbox\\dev\\anima\\github\\mottosso\\rez-for-projects\\packages\\ext'

timestamp = 1563997408

_data = {'icon': '{root}/resources/icon_128.png', 'label': 'Terminal'}

category = 'ext'

format_version = 2
