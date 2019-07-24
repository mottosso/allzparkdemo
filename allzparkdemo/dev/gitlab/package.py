# An example of how GitLab may be used to link every project
# at a given facility to its URI

name = "gitlab"
version = "1.1.3"
build_command = False

_environ = {
    "GITLAB_URI": "https://gitlab.mycompany.co.jp",
}


def commands():
    global env
    global this
    global building

    for key, value in this._environ.items():
        env[key] = value
