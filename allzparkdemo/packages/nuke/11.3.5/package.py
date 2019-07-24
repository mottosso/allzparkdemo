# -*- coding: utf-8 -*-

name = 'nuke'

version = '11.3.5'

tools = ['nuke']

requires = []

private_build_requires = ['rezutil-1.3.1+']

def commands():
    import os
    global env
    global alias
    global system
    
    if system.platform == "windows":
        bindir = "c:\\windows\\system32"
    
    elif system.platform == "linux":
        bindir = "/opt/nuke11.3v3/bin/"
    
    if not os.path.exists(bindir):
        print("WARNING: Missing files: %s" % bindir)
    
    bindir = "\"%s\"" % bindir
    
    # Add specific names to executables made
    # available by this package.
    env.PATH.append("{root}/bin")
    alias("nuke", "notepad")

with scope('config') as config:
    config.release_packages_path = 'C:\\Users\\manima\\Dropbox\\dev\\anima\\github\\mottosso\\rez-for-projects\\packages\\ext'

timestamp = 1563997407

_data = \
    {'color': '#251',
     'icon': '{root}/resources/icon_256x256.png',
     'label': 'Foundry Nuke'}

format_version = 2
