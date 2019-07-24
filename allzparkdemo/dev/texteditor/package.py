name = "texteditor"
version = "2.1.1"
requires = []

build_command = "python -m rezutil build {root}"
private_build_requires = ["rezutil-1"]

tools = [
    "texteditor",
]

_data = {
    "label": "Text Editor",
    "icon": "{root}/resources/icon_128.png",
}


def commands():
    global env

    env.PATH.append("{root}/bin")
