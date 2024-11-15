---
title: How Is Browserist Different from Selenium?
description: Browserist is a powerful Python extension for Selenium that makes web scraping and browser automation even easier, more stable, and with less code.
tags:
    - Selenium
---

# How Is Browserist Different from Selenium?
Browserist isn't just an alternative to Selenium. It's a Python extension to Selenium that makes browser automation even easier.

## Improved Stability and Less Code
Browserist improves stability with less code compared to standard use of Selenium. As browsers need time to render web pages, especially single-page applications, Selenium is often used with explicit timeouts:

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

## Why Avoid Explicit or Implicit Waits?
As you can't click a button that's not ready in the DOM, Browserist simply checks if elements are ready before interacting with them. This makes the code more stable and less prone to errors.

### Sweet Spot of Browser Automation
You don't want to be too fast nor too slow when automating a browser. You're simply dependant on too many factors that are beyond your control: internet speed, server response time, etc. The sweet spot is to be just right:

<div id="comparison-table"></div>

| Timing     | Consequence                            | Description                                                                                             |
| ---------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Too short  | :material-heart-broken: _Code breaks_  | Wait for 1 second, e.g. `time.sleep(1)`, hoping that an element is ready within a fixed amount of time. |
| Just right | :material-check-all: _Stable and fast_ | Browserist checks if an element is ready before interacting with it, e.g. `wait.for_element()`.         |
| Too long   | :material-speedometer-slow: _Slow_     | Wait for 10 seconds, e.g. `time.sleep(10)`, just to be sure an element is ready.                        |

Ready to try? [Let's get started](./getting-started/index.md).
