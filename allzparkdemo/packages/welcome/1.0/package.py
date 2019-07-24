# -*- coding: utf-8 -*-

name = 'welcome'

version = '1.0'

def commands():
    global info
    info("A Welcome message!\n")

with scope('config') as config:
    config.release_packages_path = 'C:\\Users\\manima\\Dropbox\\dev\\anima\\github\\mottosso\\rez-for-projects\\packages\\ext'

timestamp = 1563997379

format_version = 2
