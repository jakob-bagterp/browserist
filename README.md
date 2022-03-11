[![Latest version](https://img.shields.io/static/v1?label=version&message=0.6.0&color=yellowgreen)](https://github.com/jakob-bagterp/browserist/releases/latest)
![Python >=3.10](https://img.shields.io/static/v1?label=python&message=>=3.10&color=blueviolet)
[![MIT license](https://img.shields.io/static/v1?label=license&message=Apache%202.0&color=blue)](https://github.com/jakob-bagterp/browserist/blob/master/LICENSE.md)
[![Test](https://github.com/jakob-bagterp/browserist/actions/workflows/test.yml/badge.svg)](https://github.com/jakob-bagterp/browserist/actions/workflows/test.yml)

# 👩‍💻 Browserist Extension for Selenium 👨‍💻
Extend the Python version of the Selenium web driver with Browserist and make your browser automation even easier.

Main features of Browserist:

* Improves stability and speed
* Simple syntax
* Hassle-free setup that works across browsers: Chrome, Firefox, Edge, Safari, Opera, Internet Explorer
* Extended library of browser automation functions and tools without elaborate code
* Supports type hints and other capabilites of Python 3.10 that makes development faster

## Prerequisites
* Python 3.10 or higher
* [Selenium](https://www.selenium.dev)
* Relevant browsers: Chrome, Firefox, Edge, Safari, Opera, Internet Explorer

## Installation
### PyPI
Assuming that Python is installed already, execute this command in the terminal:

```shell
pip3 install browserist
```

If you already have installed Browserist, use this command to upgrade to latest version:

```shell
pip3 install --upgrade browserist
```

### Homebrew
If you already have installed the [Homebrew](https://brew.sh) package manager for Mac and Linux, execute this terminal command to tap Browserist:

```shell
brew tap jakob-bagterp/browserist
```

And then install:

```shell
brew install browserist
```

### Recommended Add-Ons
#### ChromeDriver for Google Chrome
```shell
pip3 install chromedriver
```

```shell
brew install chromedriver
```

More info [here](https://chromedriver.chromium.org).

#### Microsoft Edge Driver
More info and download [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).

#### GeckoDriver for Mozilla Firefox
```shell
brew install geckodriver
```

More info [here](https://github.com/mozilla/geckodriver).

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

### Navigation
Similar to Selenium, use simple commands to automate the browser:

| Action  | How                 | Description                        |
| ------- | ------------------- | ---------------------------------- |
| Forward | `browser.forward()` | Press the browser's back button    |
| Back    | `browser.back()`    | Press the browser's forward button |
| Refresh | `browser.refresh()` | Refresh the current page           |
| Quit    | `browser.quit()`    | Close the browser                  |

## Improved Stability and Less Code
Browserist improves stability with less code. As a browsers need time to render a page, especially single-page applications, Selenium is often used with explicit timeouts:

```python
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://example.com/")
driver.implicitly_wait(3)
search_box = driver.find_element(By.XPATH, "//xpath/to/input")
search_button = driver.find_element(By.XPATH, "//xpath/to/button")
search_box.send_keys("Lorem ipsum")
search_button.click()
driver.quit()
```

Browserist does the same with less and cleaner code, yet with higher stability and without explicit/implicit waits:

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
