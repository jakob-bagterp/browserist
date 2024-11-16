---
title: Example of Non-Parallelized Browsers
description: Learn how to speed up your web scraping and browser automation with Browserist by running multiple browsers in parallel using asynchronous methods. Includes code examples.
tags:
    - Tutorial
    - Performance
---

### Linear and Not Parallelized
```python linenums="1"
from browserist import Browser, BrowserSettings, BrowserType

def open_website_with(settings: BrowserSettings):
    with Browser(settings) as browser:
        print(f"1. Opening {settings.type.name} browser")
        browser.open.url("https://example.com")
        print(f"2. Page loaded with {settings.type.name} browser")
        print(f"3. Closing {settings.type.name} browser")

def main():
    chrome = BrowserSettings(type=BrowserType.CHROME)
    edge = BrowserSettings(type=BrowserType.EDGE)
    firefox = BrowserSettings(type=BrowserType.FIREFOX)

    for browser_settings in [chrome, edge, firefox]:
        open_website_with(browser_settings)

if __name__ == "__main__":
    main()
```
