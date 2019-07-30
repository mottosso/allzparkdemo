name = "broken_package"
version = "1.0.bad_env"
build_command = False


def commands():
    global env

    # This throws an error
    env["BAD"] = "{env.NOT_EXIST}"
