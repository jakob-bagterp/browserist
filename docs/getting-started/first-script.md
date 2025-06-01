---
title: Beginner's Script for Web Scraping
description: Get started in minutes with your first browser automation script in Python using Browserist. Includes code examples and step-by-step instructions.
tags:
    - Automation
    - Tutorial
---

# First Script for Web Scraping
When you have [installed relevant packages](installation.md), you're ready to go. Simply type:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    headline = browser.get.text("//h1")
    print(headline)
    browser.wait.seconds(5)
```

Alternatively, if you would prefer not to use the built-in [context manager](../user-guide/context-manager.md) that automatically closes the browser when it has finished or an error occurs, you can manually close the browser using the `browser.quit()` method:

```python linenums="1"
from browserist import Browser

browser = Browser()
browser.open.url("https://example.com")
headline = browser.get.text("//h1")
print(headline)
browser.wait.seconds(5)
browser.quit()
```

## How to Use Different Browsers
If you have already installed any of the recommended browser drivers for [Chrome](install-browsers-and-drivers/chrome.md), [Edge](install-browsers-and-drivers/edge.md), or [Firefox](install-browsers-and-drivers/firefox.md) browser drivers, you can try them with Browserist. Simply select the desired browser type in the `BrowserSettings` configuration:

```python linenums="1" hl_lines="3-5 7-8"
from browserist import Browser, BrowserSettings, BrowserType

chrome = BrowserSettings(type=BrowserType.CHROME)
edge = BrowserSettings(type=BrowserType.EDGE)
firefox = BrowserSettings(type=BrowserType.FIREFOX)

for settings in [chrome, edge, firefox]:
    with Browser(settings) as browser:
        browser.open.url("https://example.com")
        browser.wait.seconds(5)
```

Learn more about the [recommended browser drivers](recommended-drivers.md) for Browserist.
