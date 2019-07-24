# -*- coding: utf-8 -*-

name = 'rezutil'

version = '1.3.2'

requires = ['python-2.7+<4']

def commands():
    global env
    env["PYTHONPATH"].prepend("{root}/python")

with scope('config') as config:
    config.release_packages_path = 'C:\\Users\\manima\\Dropbox\\dev\\anima\\github\\mottosso\\rez-for-projects\\packages\\ext'

timestamp = 1563997378

format_version = 2
