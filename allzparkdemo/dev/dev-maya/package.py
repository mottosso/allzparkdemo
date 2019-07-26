# An example of a package referencing something from outside
# of the local package.

name = "dev_maya2"
version = "2018.1.0"
requires = []

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1"]

# Cross-platform binaries (i.e. shell scripts)
# are built and deployed with this package.
tools = [
    "maya",
    "mayapy",
    "render",
    "mayabatch",
]

_data = {
    "label": "Autodesk Maya",
    "color": "#251",
    "hidden": True,
    "icon": "{root}/resources/icon_{width}x{height}.png",
}


def commands():
    global env
    env.PATH.prepend("{root}/bin")
