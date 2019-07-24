import os

# Search path during `rez env`
packages_path = [
    # Localised packages
    os.path.expanduser("~/.packages"),

    # Development packages
    os.path.expanduser("~/packages"),

    # Public repository
    os.path.join(os.path.dirname(__file__), "packages"),
]

# Destination paths, during `rez build --install --release`
release_packages_path = packages_path[0]

# These packages are typically overly specific to your platform
# These maps allow for e.g. `windows-10.0.1803` packages to run
# to run on `windows-10.0.1903`
platform_map = {
    "os": {

        # Technically, 6.2 is Windows 8, 6.1 is Windows 7
        r"windows-6(.*)": r"windows-10",

        r"windows-10(.*)": r"windows-10",
    },
}

# Do not permit leakage of parent environment
inherit_parent_environment = False
