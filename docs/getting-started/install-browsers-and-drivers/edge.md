---
title: How to Install Edge and the Edge WebDriver
description: Learn how to install the Microsoft Edge browser and Edge WebDriver for browser automation. Includes step-by-step setup instructions.
tags:
    - Automation
    - Edge
---

# How to Install Edge and the Microsoft Edge WebDriver
## Install Microsoft Edge
Edge is a free, open-source web browser developed by Microsoft. Download the latest version [here](https://www.microsoft.com/edge).

## Install Microsoft Edge WebDriver
More info and download [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).

## Troubleshooting and Tips
If you need to use different browser types, find more info [here](../../settings/browser-types.md).

!!! tip
    Always keep your browser and driver up to date. The EdgeDriver version should usually match the browser version, otherwise Browserist might throw an error.

## How to Use Edge with Browserist
Once you have successfully installed the Edge browser and its WebDriver, you can start using them with Browserist. Here is an example of how to automate Edge using Browserist. Simply select Edge as the browser type in the `BrowserSettings` configuration:

```python linenums="1" hl_lines="3 5"
from browserist import Browser, BrowserSettings, BrowserType

settings = BrowserSettings(type=BrowserType.EDGE)

with Browser(settings) as browser:
    browser.open.url("https://example.com")
    browser.wait.seconds(5)
```

Lean more about [how to use different browser types](../../settings/browser-types.md).
