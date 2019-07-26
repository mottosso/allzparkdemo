# An example of how a third-party production tracker can
# be linked into a project.

name = "ftrack"
version = "1.0.1"
build_command = False

_environ = {
    "FTRACK_URI": "ftrack.mystudio.co.jp",
    "FTRACK_PROTOCOL": "https",
}


def commands():
    global env
    global this
    global building

    for key, value in this._environ.items():
        env[key] = value
