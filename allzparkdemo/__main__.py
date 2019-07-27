import os
import argparse

from .version import version


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--version", action="store_true", help=(
        "Print version and exit"))
    parser.add_argument("--packages", action="store_true", help=(
        "Print absolute path to packages directory"))
    parser.add_argument("--rezconfig", action="store_true", help=(
        "Print absolute path to rezconfig.py"))
    parser.add_argument("--allzparkconfig", action="store_true", help=(
        "Print absolute path to allzparkconfig.py"))

    opts = parser.parse_args()

    here = os.path.dirname(__file__)
    here = os.path.abspath(here)

    if opts.version:
        print("allzparkdemo-%s" % version)
        exit(0)

    if opts.packages:
        print(os.path.join(here, "packages"))

    elif opts.rezconfig:
        print(os.path.join(here, "rezconfig.py"))

    elif opts.allzparkconfig:
        print(os.path.join(here, "allzparkconfig.py"))

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
