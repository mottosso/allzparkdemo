name = "broken_package"
version = "1.0.bad_alias"
build_command = False


def commands():
    global alias
    alias("bad", "bad bad bad")
