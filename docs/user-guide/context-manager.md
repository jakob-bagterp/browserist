---
tags:
    - Tutorial
---

# Context Manager
## How to Automatically Quit the Browser
Instead of manually quitting the browser with `browser.quit()`, it's recommend to use the context manager and `with` statements.

### Advantages
Apart from less code and more readable code, the built-in context manager automatically closes the browser (so you don't forget it) when the automation task is done or if an error occurs.

As an added benefit, the `with` statement prevents you from having unused browser windows lingering in the background.

### Example
#### With Context Manager
It's recommended to do this:

```python
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
```

#### Without Context Manager
And not recommended to do this:

```python
from browserist import Browser

browser = Browser()
browser.open.url("https://example.com")
browser.quit()
```

!!! warning
    If you forget to close a browser instance with `browser.quit()` and when you don't use the `with` context manager, you have to close the browser manually. If not closed manually, one or more unused browser windows may remain inactive in the background and this takes up resources.
