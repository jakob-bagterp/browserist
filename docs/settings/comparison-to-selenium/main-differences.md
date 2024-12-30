---
title: What's Different Between Selenium and Browserist?
description: While configuring of Selenium can be complex, Browserist is a powerful Python extension that makes it easier and with less code. Includes code examples for beginners and advanced users.
tags:
    - Selenium
    - Tutorial
    - Settings
    - Browser Types
    - Chrome
    - Edge
    - Firefox
---

# Configuration Differences Between Selenium and Browserist
While Browserist is an extension to Selenium, they're configured differently. Browserist is made for users who value less code and more readable code, and so the syntax is different.

You can find configuration examples for different use cases, both for beginners and advanced users :

* [Browser types](browser-types.md)
* [Headless mode](headless-mode.md)
* [Disable images](disable-images.md)

## How to Use Selenium's Web Driver from Browserist
f you prefer to configure a session with Browserist, but use Selenium for other parts of the browser automation, it's possible to mix both frameworks. Example where Selenium's `driver` is highlighted:

```python linenums="1" hl_lines="5-7"
from browserist import Browser, BrowserSettings, BrowserType

settings = BrowserSettings(type=BrowserType.CHROME)
with Browser(settings) as browser:
    driver = browser.driver
    driver.get("https://example.com")
    driver.implicitly_wait(5)
    browser.open.url("https://google.com")
    browser.wait.seconds(5)
```
