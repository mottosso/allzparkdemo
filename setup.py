"""Example files for Allzpark"""

import os
from setuptools import setup, find_packages
from allzparkdemo.version import version

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "License :: Public Domain",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Topic :: Utilities",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

here = os.path.dirname(__file__)
packagedir = os.path.abspath(os.path.join(here, "allzparkdemo"))

exclude = [
    "__pycache__",
]

package_data = []
for base, dirs, files in os.walk(packagedir):
    dirs[:] = [d for d in dirs if d not in exclude]
    relpath = os.path.relpath(base, packagedir)
    basename = os.path.basename(base)

    for fname in files:
        fname = os.path.join(relpath, fname)
        package_data += [fname]

# Store version alongside package
dirname = os.path.dirname(__file__)
fname = os.path.join(dirname, "allzparkdemo", "__version__.py")
with open(fname, "w") as f:
    f.write("version = \"%s\"\n" % version)

setup(
    name="allzparkdemo",
    version=version,
    description=__doc__,
    keywords="example files allzpark package manager application launcher",
    long_description=__doc__,
    url="https://github.com/mottosso/allzpark-demo",
    author="Marcus Ottosson",
    author_email="konstruktion@gmail.com",
    license="The Unlicense",
    zip_safe=False,
    packages=find_packages(exclude=["__pycache__", "*.pyc"]),
    package_data={
        "allzparkdemo": package_data
    },
    classifiers=classifiers,
    install_requires=[
        "bleeding-rez",
    ],
    entry_points={
        "console_scripts": [
            "allzparkdemo = allzparkdemo.__main__:main"
        ]
    },
    python_requires=">2.7, <4",
)
