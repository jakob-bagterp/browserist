---
title: How to Set Browser Type in Selenium
description: Learn how use different browsers such as Chrome, Firefox, Edge in Selenium. Or use the Browserist extension that makes the configuration even easier. Includes code examples for beginners and advanced users.
tags:
    - Selenium
    - Tutorial
    - Settings
    - Browser Types
    - Chrome
    - Edge
    - Firefox
    - Internet Explorer
    - Safari
---

# How to Use Different Browser Types in Selenium and Browserist
When you need to automate web scraping or test flows with different browsers – for example Firefox, Edge, or Chrome – Selenium and Browserist does this differently.

## Basic Usage
### With Selenium
When you want to use Chrome for browser automation with Selenium, here's how to initiate a session:

```python linenums="1"
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://example.com")
driver.implicitly_wait(5)
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

## Multiple Browsers in a Session
Let's imagine another example where we want to do the same task, but with different browser types.

### With Browserist
Since the configuration class is separate from the web driver and consistent across browser types, Browserist often scales with less code compared to Selenium:

```python linenums="1"
from browserist import Browser, BrowserSettings, BrowserType

chrome = BrowserSettings(type=BrowserType.CHROME)
edge = BrowserSettings(type=BrowserType.EDGE)
firefox = BrowserSettings(type=BrowserType.FIREFOX)

for settings in [chrome, edge, firefox]:
    with Browser(settings) as browser:
        browser.open.url("https://example.com")
        # Do something
```

### With Selenium
With Selenium, the example above could be rewritten like this:

```python linenums="1"
from selenium import webdriver

def do_something(driver)
    driver.get("https://example.com")
    driver.implicitly_wait(5)
    # Do someting
    driver.quit()

chrome_driver = webdriver.Chrome()
do_something(chrome_driver)

edge_driver = webdriver.Edge()
do_something(edge_driver)

firefox_driver = webdriver.Firefox()
do_something(firefox_driver)
```

### Selenium Mixed with Browserist
Alternatively, mix Selenium with Browserist:

```python linenums="1"
from browserist import Browser, BrowserSettings, BrowserType

chrome = BrowserSettings(type=BrowserType.CHROME)
edge = BrowserSettings(type=BrowserType.EDGE)
firefox = BrowserSettings(type=BrowserType.FIREFOX)

for settings in [chrome, edge, firefox]:
    with Browser(settings) as browser:
        driver = browser.driver
        driver.get("https://example.com")
        # Do something
```
