---
title: How to Run Multiple Browsers in Multi-Processing Mode
description: Learn how to speed up your web scraping and browser automation with Browserist by running multiple browsers in parallel using multi-processing methods. Includes code examples.
tags:
    - Tutorial
    - Performance
---

### Multi-Processing
```python linenums="1"
import multiprocessing
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

    browser_settings = [chrome, edge, firefox]
    number_of_processes = len(browser_settings)

    with multiprocessing.Pool(number_of_processes) as pool:
        pool.map(open_website_with, browser_settings)

if __name__ == "__main__":
    main()
```
