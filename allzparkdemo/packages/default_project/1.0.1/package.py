# -*- coding: utf-8 -*-

name = 'default_project'

version = '1.0.1'

requires = ['python']

private_build_requires = ['rezutil-1']

def commands():
    global env
    global alias
    
    # For Windows
    env.PATH.prepend("{root}/bin")
    
    # For Unix
    alias("create", "python {root}/bin/create.py")

with scope('config') as config:
    config.release_packages_path = 'C:\\Users\\manima\\Dropbox\\dev\\anima\\github\\mottosso\\rez-for-projects\\packages\\ext'

timestamp = 1563997397

category = 'int'

format_version = 2
