---
tags:
    - Automation
    - Chrome
---

# How to Install Chrome and the ChromeDriver
## Google Chrome
Google Chrome is a free, open-source web browser developed by Google. Download the latest version [here](https://www.google.com/chrome/).

## ChromeDriver
With [PyPI](https://pypi.org/project/chromedriver/):

```shell title=""
pip install chromedriver
```

With [Homebrew](https://brew.sh):

```shell title=""
brew install chromedriver
```

More info [here](https://chromedriver.chromium.org).

## Troubleshooting and Tips
If you need to use different browser types, find more info [here](../../user-guide/settings/browser-types.md).

!!! tip
    Always keep your browser and driver up to date. The ChromeDriver version should usually match the browser version, otherwise Browserist will throw an error.
