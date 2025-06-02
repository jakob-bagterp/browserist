---
title: How to Install Edge and the Edge WebDriver
description: Learn how to install the Microsoft Edge browser and Edge WebDriver for browser automation. Includes step-by-step setup instructions.
tags:
    - Automation
    - Edge
---

# How to Install Edge and the Microsoft Edge WebDriver
## Install Microsoft Edge
Edge is a free, open-source web browser developed by Microsoft. Visit their website to find out more and [download the latest version of Edge](https://www.microsoft.com/edge).

## Install Microsoft Edge WebDriver
Microsoft also provides a guide on how to [install and download the WebDriver for Microsoft Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).

## Troubleshooting and Tips
If you are planning to use different browsers, please refer to the [guide on options for browser types](../../settings/browser-types.md).

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

!!! info "Default Browser for Windows"
    Edge is the default browser for running Browserist on Windows. On other operating systems, such as macOS and Linux, [Chrome](chrome.md) is the default browser. Therefore, in most cases, there is no need to specify the browser type in the `BrowserSettings` configuration, which simplifies your code:

    ```python linenums="1" hl_lines="3"
    from browserist import Browser

    with Browser() as browser:
        browser.open.url("https://example.com")
        browser.wait.seconds(5)
    ```
