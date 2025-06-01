---
title: How to Run Several Browsers in Multi-Threading Mode
description: Learn how to speed up your web scraping and browser automation with Browserist by running multiple browsers in parallel using multi-threading methods. Includes code examples.
tags:
    - Tutorial
    - Performance
---

# Multi-Threading
## Code Example
Example of how to run multiple browsers in multi-threading mode:

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

## Which Method Is Faster?
Multi-processing and multi-threading are the fastest methods, sometimes twice as fast as running the same job in linear or asynchronous mode. For instance, measuring execution time of the code examples below yield the results like this in seconds:

<div id="performance-parallelization-table-1"></div>

| Method                                    | Rank                        | Improvement | Average | Min   | Max   |
| ----------------------------------------- | :-------------------------: | :---------: | :-----: | :---: | :---: |
| [Linear](1-linear.md)                     | :material-speedometer-slow: | _Baseline_  | 8.59    | 8.55  | 8.62  |
| [Asynchronous](2-asynchronous.md)         | :material-speedometer-slow: | 2 %         | 8.42    | 8.33  | 8.48  |
| Multi-threading                           | :material-speedometer:      | 103 %       | 4.24    | 4.20  | 4.29  |
| [Multi-processing](4-multi-processing.md) | :material-speedometer:      | 105 %       | 4.20    | 3.69  | 6.05  |
