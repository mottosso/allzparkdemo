# An example Allzpark config

startup_project = "alita"
startup_application = "maya==2018.0.4"

# This can also be a function, returning a list of projects
# from e.g. disk or a database query such as ftrack
projects = [
    "alita",
    "lotr",
    "godzilla",
    "panzerkunst",
    "spiderman",
    "vector",
    "hulk",
    "metroid",
]

# Applications are specified in the project package,
# but Allzpark has the option to "Show all applications"
# which disregards those, and shows these instead, for any
# given project.
applications = [
    "maya",
    "houdini",
    "nuke",
    "aftereffects",
    "texteditor",
    "terminal",
]
