---
title: How to Configure Browser Type
description: Learn how to use different browser types such as Chrome, Firefox, Edge, etc. with Browserist to automate your web scraping or perform browser compatibility testing.
tags:
    - Tutorial
    - Settings
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

```python linenums="1" hl_lines="3 5"
from browserist import Browser, BrowserSettings, BrowserType

settings = BrowserSettings(type=BrowserType.FIREFOX)

with Browser(settings) as browser:
    browser.open.url("https://example.com")
    browser.wait.seconds(5)
```

## Supported Browsers
| Name              | Type                            | Notes                       |
| ----------------- | ------------------------------- | --------------------------- |
| Chrome            | `BrowserType.CHROME`            | Default (except on Windows) |
| Edge              | `BrowserType.EDGE`              | Default on Windows          |
| Firefox           | `BrowserType.FIREFOX`           |                             |
| Internet Explorer | `BrowserType.INTERNET_EXPLORER` |                             |
| Safari            | `BrowserType.SAFARI`            |                             |

More information about [installation of browser drivers](../getting-started/recommended-drivers.md).

!!! tip "Custom Browser Executable"
    If the browser executable isn't in a default folder, choose which file to use by setting the `path_to_executable` option in the `BrowserSettings` class.

    ```python linenums="1" hl_lines="5"
    from browserist import Browser, BrowserSettings, BrowserType

    settings = BrowserSettings(
        type=BrowserType.FIREFOX,
        path_to_executable="/path/to/executable/firefox.exe")

    with Browser(settings) as browser:
        browser.open.url("https://example.com")
        browser.wait.seconds(5)
    ```

## How to Run Multiple Browsers
When you have multiple browser drivers installed, you can run them in sequence like this:

```python linenums="1" hl_lines="7-8"
from browserist import Browser, BrowserSettings, BrowserType

chrome = BrowserSettings(type=BrowserType.CHROME)
edge = BrowserSettings(type=BrowserType.EDGE)
firefox = BrowserSettings(type=BrowserType.FIREFOX)

for settings in [chrome, edge, firefox]:
    with Browser(settings) as browser:
        browser.open.url("https://example.com")
        browser.wait.seconds(5)
```
