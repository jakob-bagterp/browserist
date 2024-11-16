---
title: How to Run Multiple Browsers in Asynchronous Mode
description: Learn how to speed up your web scraping and browser automation with Browserist by running multiple browsers in parallel using asynchronous methods. Includes code examples.
tags:
    - Tutorial
    - Performance
---

# Asynchronous
## Code Example
Example of how to run multiple browsers in asynchronous mode:

```python linenums="1"
import asyncio
from browserist import Browser, BrowserSettings, BrowserType

async def open_website_with(settings: BrowserSettings):
    with Browser(settings) as browser:
        print(f"1. Opening {settings.type.name} browser")
        browser.open.url("https://example.com")
        print(f"2. Page loaded with {settings.type.name} browser")
        await asyncio.sleep(.1)
        print(f"3. Closing {settings.type.name} browser")

async def main():
    chrome = BrowserSettings(type=BrowserType.CHROME)
    edge = BrowserSettings(type=BrowserType.EDGE)
    firefox = BrowserSettings(type=BrowserType.FIREFOX)

    async with asyncio.TaskGroup() as task_group:
        task_group.create_task(open_website_with(chrome))
        task_group.create_task(open_website_with(edge))
        task_group.create_task(open_website_with(firefox))

if __name__ == "__main__":
    asyncio.run(main())
```

## Which Method Is Faster?
Multi-processing and multi-threading are the fastest methods, sometimes twice as fast as running the same job in linear or asynchronous mode. For instance, measuring execution time of the code examples below yield the results like this in seconds:

| Method                                    | Rank                        | Improvement | Average | Min   | Max   |
| ----------------------------------------- | :-------------------------: | :---------: | :-----: | :---: | :---: |
| [Linear](1-linear.md)                     | :material-speedometer-slow: | _Baseline_  | 8.59    | 8.55  | 8.62  |
| Asynchronous                              | :material-speedometer-slow: | 2 %         | 8.42    | 8.33  | 8.48  |
| [Multi-threading](3-multi-threading.md)   | :material-speedometer:      | 103 %       | 4.24    | 4.20  | 4.29  |
| [Multi-processing](4-multi-processing.md) | :material-speedometer:      | 105 %       | 4.20    | 3.69  | 6.05  |
