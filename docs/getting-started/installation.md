---
tags:
    - Installation
    - Selenium
    - PyPI
    - Homebrew
---

# How to Install Browserist
## Prerequisites
In order to run Browserist successfully, you need to have the following installed:

* [Python 3.10 or higher](https://www.python.org)
* [Relevant browser and driver](recommended-drivers.md)

!!! info
    Default browser driver is [Chrome](./browsers/chrome.md), except for Windows where [Edge](./browsers/edge.md) is the default browser.

    Optional browsers: [Firefox](./browsers/firefox.md), Safari, Internet Explorer.

## Using Package Managers
Assuming that Python is installed already, you can install Browserist with either of the following package managers: PyPI or Homebrew.

### PyPI
For [PyPI](https://pypi.org/project/browserist/), execute this command in the terminal:

```shell title=""
pip install browserist
```

Keep the package up to date with this command:

```shell title=""
pip install --upgrade browserist
```

### Homebrew
If you already have installed the [Homebrew](https://brew.sh) package manager for Mac and Linux, execute this terminal command to tap and install Browserist:

```shell title=""
brew tap jakob-bagterp/browserist
brew install browserist
```

Use the same commands to keep the package up to date with Homebrew.
