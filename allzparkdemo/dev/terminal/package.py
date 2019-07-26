name = "terminal"
version = "1.4.0"
category = "ext"
requires = []

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1"]

_data = {
    "label": "Terminal",
    "icon": "{root}/resources/icon_128.png",
}


def commands():
    global env

    env.PATH.append("{root}/bin")
