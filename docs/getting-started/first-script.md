---
title: Beginner's Script for Web Scraping
description: Get started in minutes with your first browser automation script in Python using Browserist. Includes code examples and step-by-step instructions.
tags:
    - Automation
    - Tutorial
---

# First Script for Web Scraping
When you have [installed relevant packages](installation.md), you're ready to go. Simply type:

```python linenums="1"
from browserist import Browser

browser = Browser()
browser.open.url("https://example.com")
headline = browser.get.text("//h1")
print(headline)
browser.wait.seconds(5)
browser.quit()
```

Or use the built-in context manager so the browser automatically closes when done or if an error occurs:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    headline = browser.get.text("//h1")
    print(headline)
    browser.wait.seconds(5)
```
