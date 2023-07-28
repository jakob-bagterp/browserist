[![Latest version](https://img.shields.io/static/v1?label=version&message=1.5.0&color=yellowgreen)](https://github.com/jakob-bagterp/browserist/releases/latest)
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

:white_check_mark: Simple syntax

:white_check_mark: Hassle-free setup that works across browsers: Chrome, Firefox, Edge, Safari, Opera, Internet Explorer

:white_check_mark: Extended library of browser automation functions and tools without elaborate code

:white_check_mark: Supports IntelliSense type hints and other capabilites of Python 3.10+ that makes development more efficient

Ready to try? [Let's get started](./getting-started/index.md).

## Difference from Selenium
### Improved Stability and Less Code
Browserist improves stability with less code compared to standard use of Selenium. As a browsers need time to render a page, especially single-page applications, Selenium is often used with explicit timeouts:

```python title="With Selenium"
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

```python title="With Browserist"
from browserist import Browser

with Browser() as browser:
    browser.open.url("http://example.com/")
    browser.input.value("//xpath/to/input", "Lorem ipsum")
    browser.click.button("//xpath/to/button")
```

### Why Avoid Explicit or Implicit Waits?
As you can't click a button that's not ready in the DOM, Browserist simply checks if elements are ready before interacting with them:

| Timing:      | Too short ->    | Just right (Browserist) | <- Too long      |
| :----------- | :-----------:   | :---------------------: | :--------------: |
| Example:     | `time.sleep(1)` | `wait.for_element()`    | `time.sleep(10)` |
| Consequence: | _Code breaks_   | _Stable and fast_       | _Slow_           |
