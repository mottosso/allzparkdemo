
version = "1.0"

try:
    # Look for serialised version
    from .__version__ import version

except ImportError:
    # Else, we're likely running out of a Git repository
    import os as _os
    import subprocess as _subprocess

    try:
        # If used as a git repository
        _cwd = _os.path.dirname(__file__)
        _patch = int(_subprocess.check_output(
            ["git", "rev-list", "HEAD", "--count"],

            cwd=_cwd,

            # Ensure strings are returned from both Python 2 and 3
            universal_newlines=True,

        ).rstrip())

    except Exception:
        # Otherwise, no big deal
        pass

    else:
        version += ".%s" % _patch
