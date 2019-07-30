name = "broken_package"
version = "1.0.bad_commands"
build_command = False

def commands():
    os.doesnt_exist()
