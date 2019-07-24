name = "rezutil"
version = "1.3.2"
requires = [
    "python-2.7+,<4",
]



def commands():
    global env
    env["PYTHONPATH"].prepend("{root}/python")
