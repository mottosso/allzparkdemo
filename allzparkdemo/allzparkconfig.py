# An example Allzpark config

startup_project = "alita"
startup_application = "maya==2018.0.5"


def projects():
    """This function can also be a variable

    Example:
        projects = ["project1", "project2"]

    """

    import os

    demo_projects = [
        "alita",
        "lotr",
        "godzilla",
        "panzerkunst",
        "spiderman",
        "vector",
        "hulk",
        "metroid",
    ]

    user_projects = os.getenv("MY_PROJECTS", "").split(",")

    return user_projects + demo_projects


# Applications are specified in the project package,
# but Allzpark has the option to "Show all applications"
# which disregards those, and shows these instead, for any
# given project.
applications = [
    "maya",
    "houdini",
    "nuke",
    "aftereffects",
    "terminal",
]
