import os
import sys
import time
import shutil
import argparse
import contextlib
import subprocess
import collections

from rez.package_copy import copy_package
from rez.packages_ import iter_packages

dirname = os.path.dirname(__file__)
repodir = os.path.dirname(dirname)
dev_path = os.path.join(dirname, "dev")
packages_path = os.path.join(dirname, "packages")

os.environ.pop("REZ_CONFIG_FILE", None)
os.environ["REZ_PACKAGES_PATH"] = os.pathsep.join([
    os.path.expanduser("~/packages"),
    packages_path,
])

# Prevent e.g. rezutilz from accumulating bad files for the wheel
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
sys.dont_write_bytecode = True

# Some packages depend on other packages
# having been built first.
order = [
    "rezutil",
    "welcome",
    "ftrack",
    "gitlab",
    "base",
    "core_pipeline",
    "maya",
    "maya_base",
]


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("--clean", action="store_true")
opts = parser.parse_args()


def call(command, **kwargs):
    popen = subprocess.Popen(
        command,
        shell=True,
        universal_newlines=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        **kwargs
    )

    output = list()
    for line in iter(popen.stdout.readline, ""):
        output += [line.rstrip()]

        if opts.verbose:
            sys.stdout.write(line)

    popen.wait()

    if popen.returncode != 0:
        if isinstance(command, (tuple, list)):
            command = ", ".join(command)

        raise OSError(
            # arg1, arg2 -------
            # Some error here
            # ------------------
            "\n".join([
                "%s ".ljust(70, "-") % command,
                "",
                "\n".join(output),
                "",
                "-" * 70,
            ])
        )


@contextlib.contextmanager
def stage(msg, timing=True):
    print(msg)
    time.sleep(0.2)
    yield


def exists(*package):
    return os.path.exists(
        os.path.join(packages_path, *package)
    )


print("-" * 30)
print("")
print("Building demo packages..")
print("")
print("-" * 30)


_, existing, _ = next(os.walk(packages_path), ([], [], []))  # just directories

if opts.clean and existing:
    with stage("Cleaning %s.. " % "packages"):
        for attempt in range(3):
            try:
                for package in existing:
                    shutil.rmtree(os.path.join(packages_path, package))
            except OSError:
                sys.stderr.write(" retrying..")
                time.sleep(1)
                continue
            else:
                break

count = 0

with stage("Scanning.. "):
    packages = collections.defaultdict(list)
    for base, dirs, files in os.walk(dev_path):

        for fname in files:
            if fname != "package.py":
                continue

            dirs[:] = []  # Stop traversing
            abspath = os.path.join(base, fname)

            with open(abspath) as f:
                for line in f:
                    if line.startswith("name"):
                        name = line.split(" = ")[-1]
                        name = name.rstrip()  # newline
                        name = name.replace("\"", "")  # quotes
                    if line.startswith("version"):
                        version = line.split(" = ")[-1]
                        version = version.rstrip()  # newline
                        version = version.replace("\"", "")  # quotes

            packages[name] += [{
                "name": name,
                "base": base,
                "version": version,
                "abspath": abspath,
            }]

# Order relevant packages by above criteria
with stage("Sorting.. "):
    sorted_packages = []
    for name in order:
        sorted_packages += packages.pop(name)

    # Add remainder
    for _, package in packages.items():
        sorted_packages += package


with stage("Building.. "):
    for package in sorted_packages:
        if exists(package["name"], package["version"]):
            continue

        print(" - {name}-{version}".format(**package))
        call("rez build --clean --install "
             "--prefix {0}".format(packages_path), cwd=package["base"])
        count += 1


with stage("Making versions.."):
    version = {
        ("alita", "0.3.28"): (
            "0.2.0",
            "0.2.1",
            "0.2.2",
            "0.3.11",
            "0.3.13",
            "0.3.14.beta",
            "0.3.16",
            "0.3.17.beta",
            "0.3.21",
            "0.3.25"
        ),
        ("core_pipeline", "2.1.0"): (
            "1.0.0",
            "1.1.0.beta",
            "1.1.1",
            "1.6.0",
            "1.6.4",
            "2.0.0.beta",
            "2.0.1"
        ),
        ("maya", "2018.0.6"): (
            "2015.0.0",
            "2016.0.2",
            "2017.0.4",
            "2018.0.3",
            "2018.0.2",
            "2019.0.3",
            "2020.0.5",
        )
    }

    for (family, version), targets in version.items():
        package = next(iter_packages(family, version, paths=[packages_path]))

        for dst in targets:
            print("  - {family}=={version} -> {dst}".format(**locals()))

            copy_package(
                package=package,
                variants=[0],
                dest_version=dst,
                dest_repository=packages_path,
            )

            count += 1


print("-" * 30)

if not count:
    print("Already up-to-date, use --clean to start fresh")
else:
    print("Auto-built %d packages for you" % count)
