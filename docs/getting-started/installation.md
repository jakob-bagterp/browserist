---
tags:
    - Installation
    - Selenium
    - PyPI
    - Homebrew
---

# How to Install Browserist
## Prerequisites
* [Python 3.10 or higher](https://www.python.org)
* [Selenium](https://www.selenium.dev)
* [Relevant browser and driver](browser-drivers.md)

!!! info
    Default browser driver is Chrome, except for Windows where Edge is the default browser. Optional browsers: Firefox, Safari, Internet Explorer.

Assuming that Python is installed already, you can install Browserist with either of the following package managers: PyPI or Homebrew.

## PyPI
For [PyPI](https://pypi.org/project/browserist/), execute this command in the terminal:

```shell title=""
pip install browserist
```

Keep the package up to date with this command:

```shell title=""
pip install --upgrade browserist
```

## Homebrew
If you already have installed the [Homebrew](https://brew.sh) package manager for Mac and Linux, execute this terminal command to tap and install Browserist:

```shell title=""
brew tap jakob-bagterp/browserist
brew install browserist
```

Use the same commands to keep the package up to date with Homebrew.
