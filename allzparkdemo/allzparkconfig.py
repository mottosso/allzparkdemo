# An example Allzpark config

startup_profile = "alita"
startup_application = "maya==2018.0.5"


def profiles():
    """This function can also be a variable

    Example:
        profiles = ["profile1", "profile2"]

    """

    import os

    demo_profiles = [
        "alita",
        "lotr",
        "test_noexist",
        "test_noapps",
        "test_badapps",
    ]

    user_profiles = os.getenv("MY_PROFILES", "").split(",")

    return user_profiles + demo_profiles


# Applications are specified in the profile package,
# but Allzpark has the option to "Show all applications"
# which disregards those, and shows these instead, for any
# given profile.
applications = [
    "maya",
    "houdini",
    "nuke",
    "aftereffects",
    "terminal",
]
