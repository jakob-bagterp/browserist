---
title: How to Run Multiple Browsers in Asynchronous Mode
description: Learn how to speed up your web scraping and browser automation with Browserist by running multiple browsers in parallel using asynchronous methods. Includes code examples.
tags:
    - Tutorial
    - Performance
---

# Asynchronous
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
