[![Latest version](https://img.shields.io/static/v1?label=version&message=1.5.0&color=yellowgreen)](https://github.com/jakob-bagterp/browserist/releases/latest)
![Python 3.10 | 3.11 or higher](https://img.shields.io/static/v1?label=python&message=3.10%20|%203.11%2B&color=blueviolet)
[![Apache 2.0 license](https://img.shields.io/static/v1?label=license&message=Apache%202.0&color=blue)](https://github.com/jakob-bagterp/browserist/blob/master/LICENSE.md)
[![Codecov](https://codecov.io/gh/jakob-bagterp/browserist/branch/master/graph/badge.svg?token=1JL65T099J)](https://codecov.io/gh/jakob-bagterp/browserist)
[![CodeQL](https://github.com/jakob-bagterp/browserist/actions/workflows/codeql.yml/badge.svg)](https://github.com/jakob-bagterp/browserist/actions/workflows/codeql.yml)
[![Test](https://github.com/jakob-bagterp/browserist/actions/workflows/test.yml/badge.svg)](https://github.com/jakob-bagterp/browserist/actions/workflows/test.yml)
[![Downloads](https://static.pepy.tech/badge/browserist)](https://pepy.tech/project/browserist)

# 👩‍💻 Browserist – Python Extension for Selenium 👨‍💻
> ***browserist***
> *1. The belief that web browsers account for differences in websites or web applications in all of their ability and that a particular web browser is superior to others.*
> *2. Discrimination or prejudice based on web browser.*

Despite the [urban definition](https://www.urbandictionary.com/define.php?term=browserist), Browserist is a Python extension of the [Selenium web driver](https://www.selenium.dev/) that makes it even easier to use different browsers for testing and automation.

Main features of Browserist:

* Improves stability and speed
* Simple syntax
* Hassle-free setup that works across browsers: Chrome, Firefox, Edge, Safari, Opera, Internet Explorer
* Extended library of browser automation functions and tools without elaborate code
* Supports IntelliSense type hints and other capabilites of Python 3.10+ that makes development more efficient

## 🚀 Get Started in 3 Easy Steps
Ready to try? Let's get started:

### 1. Install Browserist Package
Assuming that [Python](https://www.python.org/) is already installed, execute this command in the terminal to install the Browserist package:

```shell
pip3 install browserist
```

### 2. Install Browser Driver
Assuming that [Chrome](https://www.google.com/chrome/) is already installed, you also need a driver that automates the Chrome browser:

```shell
pip3 install chromedriver
```

### 3. First Script
You're now ready to go:

```python
from browserist import Browser

with Browser() as browser:
    browser.open.url("http://example.com/")
    browser.wait.seconds(5)
```

## Next Steps
Find more tips for [installation of Browserist](getting-started/installation.md) or [installation of other browser types](getting-started/browser-drivers.md) in the documentation.

For advanced users, learn how to optimise performance:

* Headless mode
* Ignore images
* Run multiple browsers in parallel