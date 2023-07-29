# Basic Navigation
## Standard Browser Buttons
Similar to Selenium, use these simple commands to automate the browser:

| Action  | Code                | Description                        |
| ------- | ------------------- | ---------------------------------- |
| Forward | `browser.forward()` | Press the browser's back button    |
| Back    | `browser.back()`    | Press the browser's forward button |
| Refresh | `browser.refresh()` | Reload the current page            |
| Quit    | `browser.quit()`    | Close the browser                  |

### Example
```python
from browserist import Browser

browser = Browser()
browser.open.url("https://example.com")
browser.open.url("https://google.com")
browser.browser.back()  # Go back to previous page Example.com
browser.browser.forward()  # Return to Google.com
browser.quit()
```

## Automatically Quit Browser with Context Manager
Instead of manually quitting the browser with `browser.quit()`, it's recommend to use the `with` context manager.

### Advantages
Apart from less and more readable code, the built-in context manager automatically closes the browser (so you don't forget it) when the automation task is done or if an error occurs.

As an added benefit, the `with` statement prevents you from having unused browser windows lingering in the background that take up resources.

### Example
It's recommended to do this:

```python
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
```

Instead of this:

```python
from browserist import Browser

browser = Browser()
browser.open.url("https://example.com")
browser.quit()
```
