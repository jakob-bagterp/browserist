---
title: How to Install Chrome and ChromeDriver
description: Learn how to install the Google Chrome browser and ChromeDriver for browser automation. Includes step-by-step setup instructions.
tags:
    - Automation
    - Chrome
---

# How to Install Chrome and the ChromeDriver
## Install Google Chrome
Google Chrome is a free, open-source web browser developed by Google. Visit their website to find out more and [download the latest version of Chrome](https://www.google.com/chrome/).

## Install ChromeDriver
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
If you are planning to use different browsers, please refer to the [guide on options for browser types](../../settings/browser-types.md).

!!! tip
    Always keep your browser and driver up to date. The ChromeDriver version should usually match the browser version, otherwise Browserist might throw an error.

## How to Use Chrome with Browserist
Once you have successfully installed the Chrome browser and its ChromeDriver, you can start using them with Browserist. Here is an example of how to automate Chrome using Browserist. Simply select Chrome as the browser type in the `BrowserSettings` configuration:

```python linenums="1" hl_lines="3 5"
from browserist import Browser, BrowserSettings, BrowserType

settings = BrowserSettings(type=BrowserType.CHROME)

with Browser(settings) as browser:
    browser.open.url("https://example.com")
    browser.wait.seconds(5)
```

Lean more about [how to use different browser types](../../settings/browser-types.md).
