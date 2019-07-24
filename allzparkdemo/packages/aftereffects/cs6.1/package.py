# -*- coding: utf-8 -*-

name = 'aftereffects'

version = 'cs6.1'

tools = ['ae']

requires = []

private_build_requires = ['rezutil-1']

def commands():
    import os
    global env
    global alias
    global system
    
    if system.platform == "windows":
        bindir = "c:\\program files\adobe\aftereffects\ae.exe"
    
    if not os.path.exists(bindir):
        print("WARNING: Missing files: %s" % bindir)
    
    bindir = "\"%s\"" % bindir
    
    # Add specific names to executables made
    # available by this package.
    alias("ae", "notepad")

with scope('config') as config:
    config.release_packages_path = 'C:\\Users\\manima\\Dropbox\\dev\\anima\\github\\mottosso\\rez-for-projects\\packages\\ext'

timestamp = 1563997391

_data = \
    {'color': '#612',
     'icons': {'32x32': '{root}/resources/icon_256x256.png',
               '64x64': '{root}/resources/icon_256x256.png'},
     'label': 'Adobe After Effects'}

format_version = 2
