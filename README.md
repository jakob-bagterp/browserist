[![Latest version](https://img.shields.io/static/v1?label=version&message=1.5.0&color=yellowgreen)](https://github.com/jakob-bagterp/browserist/releases/latest)
![Python 3.10 | 3.11 or higher](https://img.shields.io/static/v1?label=python&message=3.10%20|%203.11%2B&color=blueviolet)
[![Apache 2.0 license](https://img.shields.io/static/v1?label=license&message=Apache%202.0&color=blue)](https://github.com/jakob-bagterp/browserist/blob/master/LICENSE.md)
[![Codecov](https://codecov.io/gh/jakob-bagterp/browserist/branch/master/graph/badge.svg?token=1JL65T099J)](https://codecov.io/gh/jakob-bagterp/browserist)
[![CodeQL](https://github.com/jakob-bagterp/browserist/actions/workflows/codeql.yml/badge.svg)](https://github.com/jakob-bagterp/browserist/actions/workflows/codeql.yml)
[![Test](https://github.com/jakob-bagterp/browserist/actions/workflows/test.yml/badge.svg)](https://github.com/jakob-bagterp/browserist/actions/workflows/test.yml)
[![Downloads](https://static.pepy.tech/badge/browserist)](https://pepy.tech/project/browserist)

# 👩‍💻 Browserist – Python Extension for Selenium 👨‍💻
> **browserist**
> 1. The belief that web browsers account for differences in websites or web applications in all of their ability and that a particular web browser is superior to others.
> 2. Discrimination or prejudice based on web browser.

Despite the [urban definition](https://www.urbandictionary.com/define.php?term=browserist), Browserist is a Python extension of the [Selenium web driver](https://www.selenium.dev/) that makes it even easier to use different browsers for testing and automation.

Main features of Browserist:

* Improves stability and speed
* Simple syntax
* Hassle-free setup that works across browsers: Chrome, Firefox, Edge, Safari, Opera, Internet Explorer
* Extended library of browser automation functions and tools without elaborate code
* Supports IntelliSense type hints and other capabilites of Python 3.10+ that makes development more efficient

## How to Install
Ready to try? [Learn how to install](https://github.com/jakob-bagterp/browserist/blob/master/INSTALLATION.md).

## Getting Started
The default browser is Chrome (except Edge for Windows). Simply type:

```python
from browserist import Browser

browser = Browser()
browser.open.url("http://example.com/")
browser.quit()
```

Or use the built-in context manager so the browser automatically closes when done or if an error occurs:

```python
from browserist import Browser

with Browser() as browser:
    browser.open.url("http://example.com/")
```

### Browser Types
If you want to use other browser types, e.g. Firefox, Edge, etc., define this in the settings:

```python
from browserist import Browser, BrowserSettings, BrowserType

settings = BrowserSettings(type = BrowserType.FIREFOX)
with Browser(settings) as browser:
    browser.open.url("http://example.com/")
```

#### Supported Browsers
| Name              | Type                            |
| ----------------- | ------------------------------- |
| Chrome            | `BrowserType.CHROME`            |
| Edge              | `BrowserType.EDGE`              |
| Firefox           | `BrowserType.FIREFOX`           |
| Internet Explorer | `BrowserType.INTERNET_EXPLORER` |
| Opera             | `BrowserType.OPERA`             |
| Safari            | `BrowserType.SAFARI`            |

## Improved Stability and Less Code
Browserist improves stability with less code. As a browsers need time to render a page, especially single-page applications, Selenium is often used with explicit timeouts:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://example.com/")
driver.implicitly_wait(3)
search_box = driver.find_element(By.XPATH, "//xpath/to/input")
search_button = driver.find_element(By.XPATH, "//xpath/to/button")
search_box.send_keys("Lorem ipsum")
search_button.click()
driver.quit()
```

Browserist does the same with less and cleaner code, yet also with increased stability and without explicit/implicit waits:

```python
from browserist import Browser

with Browser() as browser:
    browser.open.url("http://example.com/")
    browser.input.value("//xpath/to/input", "Lorem ipsum")
    browser.click.button("//xpath/to/button")
```

As you can't click a button that's not ready in the DOM, Browserist simply checks if elements are ready before interacting with them:

| Timing:      | Too short ->  |     Just right     |  <- Too long   |
| :----------- | :-----------: | :----------------: | :------------: |
| Example:     | time.sleep(1) | wait.for_element() | time.sleep(10) |
| Consequence: | _Code breaks_ | _Stable and fast_  |     _Slow_     |

## Settings
If you want a headless browser with Selenium, you typically would use different settings from browser to browser. Browserist solves this problem so that settings for Chrome, Firefox, Edge, etc. are standardised. For example, you can easily scale test runs across different browsers in a lightweight, headless configuration:

```python
from browserist import Browser, BrowserSettings, BrowserType

chrome = BrowserSettings(type = BrowserType.CHROME, headless = True, disable_images = True)
edge = BrowserSettings(type = BrowserType.EDGE, headless = True, disable_images = True)
firefox = BrowserSettings(type = BrowserType.FIREFOX, headless = True, disable_images = True)

for settings in [chrome, edge, firefox]:
    with Browser(settings) as browser:
        browser.open.url("http://example.com/")
```


# Thank You for Supporting
## Donate
This module is free to use. And if you like it, feel free to [buy me a coffee](https://github.com/sponsors/jakob-bagterp).

## Contribute
If you have suggestions or changes to the module, feel free to add to the code and create a [pull request](https://github.com/jakob-bagterp/browserist/pulls).

## Report Bugs
Report bugs and issues [here](https://github.com/jakob-bagterp/browserist/issues).
