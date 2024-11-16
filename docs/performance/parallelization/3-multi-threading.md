---
title: How to Run Multiple Browsers in Multi-Threading Mode
description: Learn how to speed up your web scraping and browser automation with Browserist by running multiple browsers in parallel using multi-threading methods. Includes code examples.
tags:
    - Tutorial
    - Performance
---

### Multi-Threading
```python linenums="1"
from threading import Thread
from browserist import Browser, BrowserSettings, BrowserType

class BrowserThread(Thread):
    def __init__(self, settings: BrowserSettings):
        Thread.__init__(self)
        self.settings: BrowserSettings = settings

    def run(self):
        with Browser(self.settings) as browser:
            print(f"1. Opening {self.settings.type.name} browser")
            browser.open.url("https://example.com")
            print(f"2. Page loaded with {self.settings.type.name} browser")
            print(f"3. Closing {self.settings.type.name} browser")

def main():
    chrome = BrowserSettings(type=BrowserType.CHROME)
    edge = BrowserSettings(type=BrowserType.EDGE)
    firefox = BrowserSettings(type=BrowserType.FIREFOX)

    threads: list[Thread] = []
    for browser_setting in [chrome, edge, firefox]:
        thread = BrowserThread(browser_setting)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
```
