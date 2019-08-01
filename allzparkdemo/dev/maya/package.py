# An example of a package referencing something from outside
# of the local package.

name = "maya"
version = "2018.0.6"
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
    "icon": "{root}/resources/icon_256x256.png",
}


def commands():
    import os

    global this
    global env
    global alias
    global system

    exes = ["maya", "mayapy", "mayabatch", "render"]
    ext = ""
    version = "2018"

    # Edit these to support more versions of Maya
    if os.name == "nt":
        bindir = r"c:\program files\autodesk\maya{}\bin".format(version)
        ext = ".exe"
    elif os.name == "posix":
        bindir = "Unknown"
    elif os.name == "darwin":
        bindir = "Unknown"
    else:
        bindir = "Unknown"

    if os.path.exists(bindir):
        for exe in exes:
            fname = os.path.join(bindir, exe + ext)
            fname = fname.replace(" ", "` ")  # Escape spaces for PowerShell
            alias(exe, fname)

    else:
        if system.platform == "windows":
            alias("maya", "notepad {root}/resources/readme.txt")
        else:
            # Making some assumptions here
            # TODO: Bullet proof this
            alias("maya", "gedit {root}/resources/readme.txt")
