

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-17 23:28:01
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-17 23:28:10
 * @Description:
 * @TODO::
 * @Reference:https://tianshou.readthedocs.io/en/latest/contributing.html
-->
Contributing to Tianshou
Install Develop Version
To install Tianshou in an “editable” mode, run

$ pip install -e ".[dev]"
in the main directory. This installation is removable by

$ python setup.py develop --uninstall
PEP8 Code Style Check
We follow PEP8 python code style. To check, in the main directory, run:

$ flake8 . --count --show-source --statistics
Type Check
We use mypy to check the type annotations. To check, in the main directory, run:

$ mypy
