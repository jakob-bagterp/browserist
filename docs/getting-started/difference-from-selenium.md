# Improved Stability and Less Code
Browserist improves stability with less code compared to standard use of Selenium. As a browsers need time to render a page, especially single-page applications, Selenium is often used with explicit timeouts:

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

## Why Avoid Explicit or Implicit Waits?
As you can't click a button that's not ready in the DOM, Browserist simply checks if elements are ready before interacting with them:

| Timing:      | Too short ->    | Just right (Browserist) | <- Too long      |
| :----------- | :-----------:   | :---------------------: | :--------------: |
| Example:     | `time.sleep(1)` | `wait.for_element()`    | `time.sleep(10)` |
| Consequence: | _Code breaks_   | _Stable and fast_       | _Slow_           |
