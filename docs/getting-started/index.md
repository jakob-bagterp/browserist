---
title: Get Started in 3 Easy Steps
description: Quick guide to installing and using Browserist for browser automation in Python, so you can run your first script within minutes. Includes code examples.
tags:
    - Automation
    - Tutorial
    - Installation
    - Chrome
    - PyPI
---

# Get Started in 3 Easy Steps 🚀
Ready to try? Let's get started:

## 1. Install Browserist Package
Assuming that [Python](https://www.python.org/) is already installed, execute this command in the terminal to install the Browserist package:

```shell title=""
pip install browserist
```

## 2. Install Browser Driver
Assuming that [Chrome](https://www.google.com/chrome/) is already installed, you also need a driver that automates the Chrome browser:

```shell title=""
pip install chromedriver
```

## 3. First Script
You're now ready to go:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.wait.seconds(5)
```

## Next Steps
Find more tips for [installation of Browserist](installation.md) or [installation of other browser types](recommended-drivers.md).

Find more in-depth information in the [user guide](../user-guide/index.md) section.

For advanced users, learn how to optimise performance:

* [Headless mode](../user-guide/performance/headless.md)
* [Disable images](../user-guide/performance/disable-images.md)
* [Run multiple browsers in parallel](../user-guide/performance/parallelisation.md)

!!! tip "Become a Sponsor"
    If you find this project helpful, please consider supporting its development. Your donations will help keep it alive and growing. Every contribution, no matter the size, makes a difference.

    [Donate on GitHub Sponsors](https://github.com/sponsors/jakob-bagterp){ .md-button .md-button--primary }

    Thank you for your support! 🙌
