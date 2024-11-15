---
title: How to Wait for Explicit Time in Web Scraping
description: Learn how to wait for explicit time in browser automation and web scraping using Browserist. Includes code examples for beginners and advanced users.
tags:
    - Tutorial
---

# How to Wait for Explicit Time
While most wait methods are relative to when specific elements become present on the web page, it's also possible to let the browser sleep for an absolute number of seconds.

## Specific Time in Seconds
Example of how to let the browser sleep for 5 seconds:

```python title="" linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.wait.seconds(5)
```

## Random Time in Seconds
Sometimes you want the browser appear less like a bot by randomizing the wait interval. Example of how to let the browser sleep for a random time between 3 and 20 seconds:

```python title="" linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.wait.random_seconds(3, 20)
```
