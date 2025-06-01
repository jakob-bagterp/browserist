---
title: How to Run Browsers in Multi-Processing Mode
description: Learn how to speed up your web scraping and browser automation with Browserist by running multiple browsers in parallel using multi-processing methods. Includes code examples.
tags:
    - Tutorial
    - Performance
---

# Multi-Processing
## Code Example
Example of how to run multiple browsers in multi-processing mode:

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

## Which Method Is Faster?
Multi-processing and multi-threading are the fastest methods, sometimes twice as fast as running the same job in linear or asynchronous mode. For instance, measuring execution time of the code examples below yield the results like this in seconds:

<div id="performance-parallelization-table-1"></div>

| Method                                    | Rank                        | Improvement | Average | Min   | Max   |
| ----------------------------------------- | :-------------------------: | :---------: | :-----: | :---: | :---: |
| [Linear](1-linear.md)                     | :material-speedometer-slow: | _Baseline_  | 8.59    | 8.55  | 8.62  |
| [Asynchronous](2-asynchronous.md)         | :material-speedometer-slow: | 2 %         | 8.42    | 8.33  | 8.48  |
| [Multi-threading](3-multi-threading.md)   | :material-speedometer:      | 103 %       | 4.24    | 4.20  | 4.29  |
| Multi-processing                          | :material-speedometer:      | 105 %       | 4.20    | 3.69  | 6.05  |
