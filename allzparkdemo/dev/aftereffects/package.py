# An example of a package referencing something from outside
# of the local package.

name = "aftereffects"
version = "cs6.1"
requires = []

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1"]

# Cross-platform binaries (i.e. shell scripts)
# are built and deployed with this package.
tools = [
    "ae",
]

_data = {
    "label": "Adobe After Effects",
    "color": "#612",
    "icons": {
        "32x32": "{root}/resources/icon_256x256.png",
        "64x64": "{root}/resources/icon_256x256.png",
    },
}


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
