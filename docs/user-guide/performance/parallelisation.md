# Run Multiple Browsers in Parallel
You can run Browserist as a normal, linear script or with various methods for concurrent processing:

* Asynchronous
* Multi-threading
* Multi-processing

## Which Method is Faster?
Multi-processing and multi-threading are the fastest methods, sometimes twice as fast as running the same job in linear or asynchronous mode. For instance, measuring execution time of the code examples below yield the results like this in seconds:

| Method           | Average | Min   | Max   |
| ---------------- | ------- | ----- | ----- |
| Linear           | 8.59    | 8.55  | 8.62  |
| Asynchronous     | 8.42    | 8.33  | 8.48  |
| Multi-threading  | 4.24    | 4.20  | 4.29  |
| Multi-processing | 4.20    | 3.69  | 6.05  |

### Even Faster with Headless and Ignore Images
Gain even more performance by running the browsers in [headless mode](headless-mode.md) and with [images disabled](ignore-images.md), e.g. `BrowserSettings(type=BrowserType.CHROME, headless=True, disable_images=True)`. Including the added benefit that headless mode allows you to run the job as a background task while doing something else.

Results in seconds:

| Method           | Average | Min   | Max   |
| ---------------- | ------- | ----- | ----- |
| Linear           | 10.46   | 6.34  | 15.78 |
| Asynchronous     | 8.01    | 6.15  | 12.11 |
| Multi-threading  | 4.03    | 3.98  | 4.07  |
| Multi-processing | 3.60    | 3.57  | 3.65  |

## Code Examples
Imagine that you want to scrape a website with multiple browser types: Chrome, Edge, Firefox. The following examples do the same job:

1. Open browser instance (Chrome, Edge, Firefox)
2. Load website [example.com](http://example.com/)
3. Close browser instance

Yet with four different methods.

### Linear
```python
from browserist import Browser, BrowserSettings, BrowserType

def open_website_with(settings: BrowserSettings):
    with Browser(settings) as browser:
        print(f"1. Opening {settings.type.name} browser")
        browser.open.url("http://example.com/")
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

### Asynchronous
```python
import asyncio
from browserist import Browser, BrowserSettings, BrowserType

async def open_website_with(settings: BrowserSettings):
    with Browser(settings) as browser:
        print(f"1. Opening {settings.type.name} browser")
        browser.open.url("http://example.com/")
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

### Multi-Threading
```python
from threading import Thread
from browserist import Browser, BrowserSettings, BrowserType

class BrowserThread(Thread):
    def __init__(self, settings: BrowserSettings):
        Thread.__init__(self)
        self.settings: BrowserSettings = settings

    def run(self):
        with Browser(self.settings) as browser:
            print(f"1. Opening {self.settings.type.name} browser")
            browser.open.url("http://example.com/")
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

### Multi-Processing
```python
import multiprocessing
from browserist import Browser, BrowserSettings, BrowserType

def open_website_with(settings: BrowserSettings):
    with Browser(settings) as browser:
        print(f"1. Opening {settings.type.name} browser")
        browser.open.url("http://example.com/")
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
