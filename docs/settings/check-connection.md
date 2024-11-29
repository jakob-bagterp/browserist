---
title: How to Check the Internet Connection
description: Should you check the internet connection before starting the browser or not? Learn how to configure and optimize browser automation and scraping.
tags:
    - Tutorial
    - Settings
---

# Why Check the Internet Connection?
Browserist automatically checks the internet connection before starting the browser by default. This is to ensure that the browser is ready to interact with the web. If the internet connection is not available, Browserist will raise an error.

## How to Disable Checking the Internet Connection
If you want to bypass the check, simply set the `check_connection` option to `False`:

```python linenums="1" hl_lines="3"
from browserist import Browser, BrowserSettings

settings = BrowserSettings(check_connection=False)

with Browser(settings) as browser:
    browser.open.url("https://example.com")
```
