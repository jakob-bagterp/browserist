---
title: What's Different Between Selenium and Browserist?
description: While configuration of Selenium can be complex, Browserist is a powerful Python extension that makes it easier and with less code. Includes code examples for beginners and advanced users.
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
## Set Browser Type
### With Selenium
When you want to use Chrome for browser automation with Selenium, here's how to initiate a session:

```python linenums="1"
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")
driver.implicitly_wait(3)
driver.quit()
```

If you want to use Firefox, just replace `webdriver.Chrome()` with `webdriver.Firefox()`. Or use `webdriver.Edge()` for Edge.

### With Browserist
With Browserist, you often can achieve the same with less and more readable code:

```python linenums="1"
from browserist import Browser, BrowserSettings, BrowserType

settings = BrowserSettings(type=BrowserType.CHROME)
with Browser(settings) as browser:
    browser.open.url("https://example.com")
```

For Firefox or Edge, just replace `BrowserType.CHROME` with `BrowserType.FIREFOX` or `BrowserType.EDGE`, respectively.

## More Use Cases
Learn more and check other use cases:

* [Browser types](browser-types.md)
* [Headless mode](headless-mode.md)
* [Disable images](disable-images.md)
