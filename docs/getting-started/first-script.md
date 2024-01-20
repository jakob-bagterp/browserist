---
tags:
    - Automation
    - Tutorial
---

# First Script
When you have [installed relevant packages](installation.md), you're ready to go. Simply type:

```python linenums="1"
from browserist import Browser

browser = Browser()
browser.open.url("https://example.com")
browser.wait.seconds(5)
browser.quit()
```

Or use the built-in context manager so the browser automatically closes when done or if an error occurs:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.wait.seconds(5)
```
