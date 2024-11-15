---
title: How to Configure Browser Type
description: Learn how to use different browser types such as Chrome, Firefox, Edge, etc. with Browserist to automate your web scraping or perform browser compatibility testing.
tags:
    - Tutorial
    - Browser Types
    - Chrome
    - Edge
    - Firefox
    - Internet Explorer
    - Safari
---

# How to Configure Browser Type
## Basic Usage
If you want to use different types of browsers – for example, Firefox, Edge, Chrome, etc. – define this in the `BrowserSettings` class:

```python linenums="1"
from browserist import Browser, BrowserSettings, BrowserType

settings = BrowserSettings(type=BrowserType.FIREFOX)

with Browser(settings) as browser:
    browser.open.url("https://example.com")
    browser.wait.seconds(5)
```

## Supported Browsers
| Name              | Type                            | Notes                        |
| ----------------- | ------------------------------- | ---------------------------- |
| Chrome            | `BrowserType.CHROME`            | Default (except for Windows) |
| Edge              | `BrowserType.EDGE`              | Default for Windows          |
| Firefox           | `BrowserType.FIREFOX`           |                              |
| Internet Explorer | `BrowserType.INTERNET_EXPLORER` |                              |
| Safari            | `BrowserType.SAFARI`            |                              |

More information about [installation of browser drivers](../getting-started/recommended-drivers.md).

## How to Run Multiple Browsers
When you have multiple browser drivers installed, you can run them in sequence like this:

```python linenums="1"
from browserist import Browser, BrowserSettings, BrowserType

chrome = BrowserSettings(type=BrowserType.CHROME)
edge = BrowserSettings(type=BrowserType.EDGE)
firefox = BrowserSettings(type=BrowserType.FIREFOX)

for settings in [chrome, edge, firefox]:
    with Browser(settings) as browser:
        browser.open.url("https://example.com")
        browser.wait.seconds(5)
```
