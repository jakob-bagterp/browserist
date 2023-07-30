
# 🚀 Get Started in 3 Easy Steps 🚀
Ready to try? Let's get started:

## 1. Install Browserist Package
Assuming that [Python](https://www.python.org/) is already installed, execute this command in the terminal to install the Browserist package:

```shell
pip3 install browserist
```

## 2. Install Browser Driver
Assuming that [Chrome](https://www.google.com/chrome/) is already installed, you also need a driver that automates the Chrome browser:

```shell
pip3 install chromedriver
```

## 3. First Script
You're now ready to go:

```python
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.wait.seconds(5)
```

## Next Steps
Find more tips for [installation of Browserist](installation.md) or [installation of other browser types](browser-drivers.md) in the documentation.

Find more in-depth information in the [user guide](../user-guide/index.md) section.

For advanced users, learn how to optimise performance:

* [Headless mode](../user-guide/performance/headless.md)
* [Ignore images](../user-guide/performance/ignore-images.md)
* [Run multiple browsers in parallel](../user-guide/performance/parallelisation.md)
