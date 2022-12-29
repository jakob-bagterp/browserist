[![Latest version](https://img.shields.io/static/v1?label=version&message=1.3.0&color=yellowgreen)](https://github.com/jakob-bagterp/browserist/releases/latest)
![Python >=3.10](https://img.shields.io/static/v1?label=python&message=>=3.10&color=blueviolet)
[![MIT license](https://img.shields.io/static/v1?label=license&message=Apache%202.0&color=blue)](https://github.com/jakob-bagterp/browserist/blob/master/LICENSE.md)
[![Codecov](https://codecov.io/gh/jakob-bagterp/browserist/branch/master/graph/badge.svg?token=1JL65T099J)](https://codecov.io/gh/jakob-bagterp/browserist)
[![Test](https://github.com/jakob-bagterp/browserist/actions/workflows/test.yml/badge.svg)](https://github.com/jakob-bagterp/browserist/actions/workflows/test.yml)

# 👩‍💻 Browserist Extension for Selenium 👨‍💻
> **browserist**
> 1. The belief that web browsers account for differences in websites or web applications in all of their ability and that a particular web browser is superior to others.
> 2. Discrimination or prejudice based on web browser.

Despite the [urban definition](https://www.urbandictionary.com/define.php?term=browserist), Browserist is a Python extension of the Selenium web driver that makes it even easier to use different browsers for testing and automation.

Main features of Browserist:

* Improves stability and speed
* Simple syntax
* Hassle-free setup that works across browsers: Chrome, Firefox, Edge, Safari, Opera, Internet Explorer
* Extended library of browser automation functions and tools without elaborate code
* Supports IntelliSense type hints and other capabilites of Python 3.10 that makes development more efficient

## Prerequisites
* Python 3.10 or higher
* [Selenium](https://www.selenium.dev)
* Relevant browsers: Chrome, Firefox, Edge, Safari, Opera, Internet Explorer

## How to Install
Find a guide [here](./HOW_TO_INSTALL.md).

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

Use `BrowserSettings` with the following options:

| Setting              | Option                                    | Default                              | Description                                                                                                      |
| -------------------- | ----------------------------------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| `type`               | `BrowserType`                             | `BrowserType.CHROME`                 | Set browser type, e.g. Chrome, Edge, Firefox, etc.                                                               |
| `headless`           | `True` or `False`                         | `False`                              | Run the browser in headless mode. May not be supported by all browsers.                                          |
| `disable_images`     | `True` or `False`                         | `False`                              | Neither request nor render images, which typically improves loading speed. May not be supported by all browsers. |
| `page_load_strategy` | `PageLoadStrategy`                        | `PageLoadStrategy.NORMAL`            | Set page load strategy.                                                                                          |
| `path_to_executable` | Path to file                              | System default                       | If the browser executable isn't in a default folder, select which file to use.                                   |
| `screenshot_dir`     | Path to directory                         | System default                       | Set where to save sreenshots. Default is the directory of Browserist.                                            |
| `timeout`            | `TimeoutSettings`                         | `TimeoutStrategy.STOP` and 5 seconds | Set timeout strategy and time.                                                                                   |
| `viewport`           | `DeviceViewportSize` or `(width, height)` | Browser default                      | Emulate viewport size as device or set custom value in pixels.                                                   |

### Timeout Strategy
What happens if a function times out: Should the browser stop or continue its operation?

Define a general strategy and timeout in seconds:

* Default is `5` seconds per function (note that a function-specific timeout overrides this)
* The strategy can be `TimeoutStrategy.STOP` (default) or `TimeoutStrategy.CONTINUE`

```python
from browserist import Browser, BrowserSettings, TimeoutSettings, TimeoutStrategy

timeout_settings = TimeoutSettings(strategy = TimeoutStrategy.CONTINUE, seconds = 10)
settings = BrowserSettings(timeout = timeout_settings)

with Browser(settings) as browser:
    browser.open.url("http://example.com/")
```

#### Strategy Options
| Option                     | Description                                                         |
| -------------------------- | ------------------------------------------------------------------- |
| `TimeoutStrategy.STOP`     | Default. Fail fast upon timeout and raise errors.                   |
| `TimeoutStrategy.CONTINUE` | Continue despite timeouts and most errors (syntax errors excluded). |

### Emulate Viewport of Common Devices
You can set the viewport to emulate common device sizes or to a custom size. Note that it's recommended to run emulations in headless mode since an open browser may have minimum or maximum dimensions, either limited by the browser window or the monitor. Example:

```python
from browserist import Browser, BrowserSettings, common_devices

settings = BrowserSettings(headless = True)

with Browser(settings) as browser:
    browser.viewport.set.size_by_device(common_devices.Apple.IPHONE_SE)
    browser.open.url("http://example.com/")
    browser.viewport.set.size(768, 1024)
```
