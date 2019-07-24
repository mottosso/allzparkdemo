"""Example files for Allzpark"""

import os
from setuptools import setup, find_packages

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

package_data = []
for base, dirs, files in os.walk(packagedir):
    relpath = os.path.relpath(base, packagedir)
    basename = os.path.basename(base)

    for fname in files:
        fname = os.path.join(relpath, fname)
        package_data += [fname]


setup(
    name="allzparkdemo",
    version="1.0.0",
    description=__doc__,
    keywords="example files allzpark package manager application launcher",
    long_description=__doc__,
    url="https://github.com/mottosso/allzpark-demo",
    author="Marcus Ottosson",
    author_email="konstruktion@gmail.com",
    license="The Unlicense",
    zip_safe=False,
    packages=find_packages(),
    package_data={
        "allzparkdemo": package_data
    },
    classifiers=classifiers,
    install_requires=[
        "allzpark>=1.2",
    ],
    python_requires=">2.7, <4",
)