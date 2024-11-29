---
title: How to Run Multiple Browsers in Parallel
description: Learn how to speed up your web scraping and browser automation with Browserist by running multiple browsers in parallel using asynchronous, multi-threading, or multi-processing methods. Includes code examples.
tags:
    - Tutorial
    - Performance
    - Headless
    - Disable Images
---

# How to Run Multiple Browsers in Parallel
## Which Methods Can Boost the Performance?
You can run Browserist as a [normal, linear script](1-linear.md) or with various methods for concurrent processing:

* [Asynchronous](2-asynchronous.md)
* [Multi-threading](3-multi-threading.md)
* [Multi-processing](4-multi-processing.md)

## Which Method Is Faster?
Multi-processing and multi-threading are the fastest methods, sometimes twice as fast as running the same job in linear or asynchronous mode. For instance, measuring execution time of the code examples below yield the results like this in seconds:

<div id="performance-parallelization-table-1"></div>

| Method                                    | Rank                        | Improvement | Average | Min   | Max   |
| ----------------------------------------- | :-------------------------: | :---------: | :-----: | :---: | :---: |
| [Linear](1-linear.md)                     | :material-speedometer-slow: | _Baseline_  | 8.59    | 8.55  | 8.62  |
| [Asynchronous](2-asynchronous.md)         | :material-speedometer-slow: | 2 %         | 8.42    | 8.33  | 8.48  |
| [Multi-threading](3-multi-threading.md)   | :material-speedometer:      | 103 %       | 4.24    | 4.20  | 4.29  |
| [Multi-processing](4-multi-processing.md) | :material-speedometer:      | 105 %       | 4.20    | 3.69  | 6.05  |

Find code examples of the tests below.

### Basic Code Example
Imagine that you want to scrape a website with multiple browser types: Chrome, Edge, Firefox. A simplified example of this:

1. Open browser instance
2. Load website [example.com](https://example.com) and do something
3. Close browser instance

How the code could look:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    print("1. Opening X browser")
    browser.open.url("https://example.com")
    print("2. Page loaded with X browser")
    print("3. Closing X browser")
```

This will print the following to the terminal:

```text title=""
1. Opening X browser
2. Page loaded with X browser
3. Closing X browser
```

### Test Code Examples
Let's try this with four different methods from linear to concurrent processing and run the tests with three different browsers (Chrome, Edge, Firefox):

1. [Linear](1-linear.md)
2. [Asynchronous](2-asynchronous.md)
3. [Multi-threading](3-multi-threading.md)
4. [Multi-processing](4-multi-processing.md)

## Even Faster with Headless and Disable Images
Gain even more performance by running the browsers in [headless mode](../headless.md) and with [images disabled](../disable-images.md), including the added benefit that headless mode allows you to run the job as a background task while doing something else.

For example:

```python linenums="1" hl_lines="3-5"
from browserist import Browser, BrowserSettings

settings = BrowserSettings(
    headless=True,
    disable_images=True)

with Browser(settings) as browser:
    print("1. Opening X browser")
    browser.open.url("https://example.com")
    print("2. Page loaded with X browser")
    print("3. Closing X browser")
```

Results in seconds and compared to previous method:

<div id="performance-parallelization-table-2"></div>

| Method                                    | Rank                          | Improvement | Average | Min   | Max   |
| ----------------------------------------- | :-------------------------:   | :---------: | :-----: | :---: | :---: |
| [Linear](1-linear.md)                     | :material-speedometer-slow:   | 2 %         | 8.46    | 6.34  | 12.78 |
| [Asynchronous](2-asynchronous.md)         | :material-speedometer-slow:   | 7 %         | 8.01    | 6.15  | 11.11 |
| [Multi-threading](3-multi-threading.md)   | :material-speedometer-medium: | 113 %       | 4.03    | 3.98  | 4.07  |
| [Multi-processing](4-multi-processing.md) | :material-speedometer:        | 139 %       | 3.60    | 3.57  | 3.65  |
