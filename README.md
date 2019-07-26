# Allzpark Demo

[![Build Status](https://mottosso.visualstudio.com/allzparkdemo/_apis/build/status/mottosso.allzpark-demo?branchName=master)](https://mottosso.visualstudio.com/allzparkdemo/_build/latest?definitionId=3&branchName=master) [![](https://badge.fury.io/py/allzparkdemo.svg)](https://pypi.org/project/allzparkdemo/)

Demo content for [Allzpark](https://github.com/mottosso/allzpark). Is it installed automatically as part of `pip install allzpark` and shouldn't normally have to be installed otherwise.

- See [allzpark.com](https://allzpark.com/quickstart/) for details.

<br>

### Layout

Allzpark is equipped to look for a Python package by the name of `allzparkdemo` when passed the `--demo` argument. Inside of this package is a number of Rez packages that are automatically built and deployed to PyPI during [CI](https://github.com/mottosso/allzparkdemo/blob/master/azure-pipelines.yml).

Packages reside in the `allzparkdemo/dev` directory and have no requirements outside of itself and those provided by `rez bind --quickstart`. They serve as a starting point and test suite for Allzpark and [the Allzpark documentation](https://allzpark.com/).
