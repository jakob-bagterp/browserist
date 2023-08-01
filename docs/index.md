[![Latest version](https://img.shields.io/static/v1?label=version&message=1.5.1&color=yellowgreen)](https://github.com/jakob-bagterp/browserist/releases/latest)
![Python 3.10 | 3.11 or higher](https://img.shields.io/static/v1?label=python&message=3.10%20|%203.11%2B&color=blueviolet)
[![Apache 2.0 license](https://img.shields.io/static/v1?label=license&message=Apache%202.0&color=blue)](https://github.com/jakob-bagterp/browserist/blob/master/LICENSE.md)
[![Codecov](https://codecov.io/gh/jakob-bagterp/browserist/branch/master/graph/badge.svg?token=1JL65T099J)](https://codecov.io/gh/jakob-bagterp/browserist)
[![CodeQL](https://github.com/jakob-bagterp/browserist/actions/workflows/codeql.yml/badge.svg)](https://github.com/jakob-bagterp/browserist/actions/workflows/codeql.yml)
[![Test](https://github.com/jakob-bagterp/browserist/actions/workflows/test.yml/badge.svg)](https://github.com/jakob-bagterp/browserist/actions/workflows/test.yml)
[![Downloads](https://static.pepy.tech/badge/browserist)](https://pepy.tech/project/browserist)

# 👩‍💻 Browserist – Python Extension for Selenium 👨‍💻
> ***browserist***
> *1. The belief that web browsers account for differences in websites or web applications in all of their ability and that a particular web browser is superior to others.*
> *2. Discrimination or prejudice based on web browser.*

Despite the [urban definition](https://www.urbandictionary.com/define.php?term=browserist), Browserist is a Python extension of the [Selenium web driver](https://www.selenium.dev/) that makes it even easier to use different browsers for testing and automation.

Main features of Browserist:

:white_check_mark: Improves stability and speed

:white_check_mark: Simple syntax and less code

:white_check_mark: Hassle-free setup across browsers: Chrome, Firefox, Edge, Safari, Opera, Internet Explorer

:white_check_mark: Extensive framework of functions that makes browser automation easy

:white_check_mark: Supports IntelliSense and type hints that makes development more efficient

Ready to try? [Let's get started](./getting-started/index.md).

## Difference from Selenium
### Improved Stability and Less Code
Browserist improves stability with less code compared to standard use of Selenium. As a browsers need time to render a page, especially single-page applications, Selenium is often used with explicit timeouts:

```python title="With Selenium" linenums="1"
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://example.com")
driver.implicitly_wait(3)
search_box = driver.find_element(By.XPATH, "//xpath/to/input")
search_button = driver.find_element(By.XPATH, "//xpath/to/button")
search_box.send_keys("Lorem ipsum")
search_button.click()
driver.quit()
```

Browserist does the same with less and cleaner code, yet also with increased stability and without explicit/implicit waits:

```python title="With Browserist" linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.input.value("//xpath/to/input", "Lorem ipsum")
    browser.click.button("//xpath/to/button")
```

### Why Avoid Explicit or Implicit Waits?
As you can't click a button that's not ready in the DOM, Browserist simply checks if elements are ready before interacting with them. This makes the code more stable and less prone to errors.

#### Sweet Spot of Browser Automation
You don't want to be too fast nor too slow when automating a browser. You're simply dependant on too many factors that are beyond your control: internet speed, server response time, etc. The sweet spot is to be just right:

| Timing     | Consequence | Code | Description |
| ---------- | ----------- | ---- | ----------- |
| Too short  | :material-heart-broken: _Code breaks_ | `time.sleep(1)` | Wait for 1 second, hoping that an element is ready within a fixed amount of time. |
| Just right | :material-check-all:  _Stable and fast_ | `wait.for_element()` | Browserist checks if an element is ready before interacting with it. |
| Too long   | :material-speedometer-slow: _Slow_ | `time.sleep(10)` | Wait for 10 seconds, just to be sure an element is ready. |

Ready to try? [Let's get started](./getting-started/index.md).
