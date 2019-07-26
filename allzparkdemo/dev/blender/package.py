# An example of a package referencing something from outside
# of the local package.

name = "blender"
version = "2.80.0"
requires = []

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1"]

# Cross-platform binaries (i.e. shell scripts)
# are built and deployed with this package.
tools = [
    "blender",
]

_data = {
    "label": "Blender",
    "color": "#222",
    "icon": "{root}/resources/icon_64.png",
}


def commands():
    global alias
    global system

    if system.platform == "windows":
        alias("blender", "notepad {root}/resources/readme.txt")
    else:
        # Making some assumptions here
        # TODO: Bullet proof this
        alias("blender", "gedit {root}/resources/readme.txt")
