
# Git autopep8

![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg "Python 3.6")
![MIT License](https://img.shields.io/badge/License-MIT-green.svg "MIT License")

\| [日本語](README.ja.md) \| English \| 

this package add a command that apply **PEP8** coding style to your codes that add to your repository.

## Installation

Git autopep8 has `setup.py`, so you can install this package with this command.

```shell
$ python setup.py install
```

## Usage

after intalled, you can use `git-autopep8` command, that apply **PEP8** coding style to `.py` files those are added to your repository.
if you want execute this command automatically, register this command to `.git/hook/pre-commit` in your repository.

```shell
$ git-autopep8 # any arguments are providen to autopep8.
```

## License 

Git autopep8 has released under the [MIT License](LICENSE.txt).  
Git autopep8 has required [autopep8](https://github.com/hhatto/autopep8), that has released under the [MIT License](license/LICENSE_AUTOPEP8.txt). please read detail to [license/LICENSE_AUTOPEP8.txt](license/LICENSE_AUTOPEP8.txt) and [license/AUTHORS.rst](license/AUTHORS.rst).
