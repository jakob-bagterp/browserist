
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
    browser.open.url("http://example.com")
    browser.wait.seconds(5)
```

## Next Steps
Find more tips for [installation of Browserist](installation.md) or [installation of other browser types](browser-drivers.md) in the documentation.

For advanced users, learn how to optimise performance:

* Headless mode
* Ignore images
* Run multiple browsers in parallel
