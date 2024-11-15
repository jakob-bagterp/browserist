---
title: How to Automate Basic Browser Navigation
description: Learn basic navigation like back and forward, refresh and quit for browser automation and web scraping using Browserist. Includes code examples for beginners and advanced users.
tags:
    - Tutorial
    - Navigation
---

# How to Automate Basic Browser Navigation
## Standard Buttons
Similar to Selenium, use these simple commands to automate the browser:

| Action  | Code                | Description                        |
| ------- | ------------------- | ---------------------------------- |
| Forward | `browser.forward()` | Press the browser's back button    |
| Back    | `browser.back()`    | Press the browser's forward button |
| Refresh | `browser.refresh()` | Reload the current page            |
| Quit    | `browser.quit()`    | Close the browser                  |

### Examples
```python linenums="1"
from browserist import Browser

browser = Browser()
browser.open.url("https://example.com")
browser.open.url("https://google.com")
browser.back()  # Go back to previous page Example.com
browser.forward()  # Return to Google.com
browser.quit()
```

!!! tip
    Instead of manually quitting the browser with `browser.quit()`, it's recommend to use the [context manager](../context-manager.md) and `with` statements. The example above could then be refactored to:

    ```python linenums="1"
    from browserist import Browser

    with Browser() as browser:
        browser.open.url("https://example.com")
        browser.open.url("https://google.com")
        browser.back()  # Go back to previous page Example.com
        browser.forward()  # Return to Google.com
    ```
