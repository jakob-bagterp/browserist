---
title: How to Work with Browser Windows in Web Scraping
description: Learn how to open, close, and switch between windows in browser automation and web scraping using Browserist. Includes code examples for beginners and advanced users.
tags:
    - Tutorial
    - Navigation
    - Tabs and Windows
---

# How to Open and Manage Windows
When you want to open multiple web pages in separate browser windows, Browserist makes it easy to organize and automate your workflow.

## Basic Usage
Let's imagine you want to open a web page first and then open another page in a new window, a basic example would look like this:

```python linenums="1" hl_lines="5"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.window.open.new_window("https://google.com")
```

## Multiple
### Opening Multiple Windows
Normally, browsers allow you to open a new window by pressing `Ctrl` + `N` in Windows or `Cmd` + `N` on a Mac. With Browserist you can automate this, for example based on a list of URLs. This example will open each URL in a new window:

```python linenums="1" hl_lines="6-7"
from browserist import Browser

urls = ["https://example.com", "https://google.com", "https://bing.com"]

with Browser() as browser:
    for url in urls:
        browser.window.open.new_window(url)
```

### Closing a Window
How to close the current tab or, if it's the last tab in a window, the current browser window:

```python linenums="1" hl_lines="5-6"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.window.open.new_window("https://google.com")
    browser.window.close()
```

### Switching Between Windows
Switching between windows is a common task when using a browser. Instead of either clicking a window to switch to it or using a keyboard shortcut to cycle through open windows, you can automate this with Browserist:

```python linenums="1" hl_lines="6-7"
from browserist import Browser

urls = ["https://example.com", "https://google.com", "https://bing.com"]

with Browser() as browser:
    for i, url in enumerate(urls):
        browser.window.open.new_window(url, f"window_{i}")
```

Now we can switch between each window by calling its handle:

```python linenums="8" hl_lines="1-3"
    browser.window.switch_to("window_0")
    browser.window.switch_to("window_1")
    browser.window.switch_to("window_2")
```

#### Return to the Initial Window
Browserist also keeps track of the initial tab of the original browser window, so you can easily switch back to it:

```python linenums="1" hl_lines="5-6"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.window.open.new_window("https://google.com")
    browser.window.switch_to_original_window()
```

#### Get Handle ID of Current Window
Under the hood, Browserist uses handle IDs to manage and identify open windows and tabs. You can get the handle ID of the current window to switch back to it later:

```python linenums="1" hl_lines="5 7"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    base_handle_id = browser.window.handle.current()
    browser.window.open.new_window("https://google.com")
    browser.window.switch_to(base_handle_id)
```

## Example
### Get List of URLs from Open Windows
Because a link can redirect to a different destination than the original URL, you sometimes want to capture the actual destination of each page. Here is an example of how to capture all the links from a web page and open them in new windows:

```python linenums="1" hl_lines="8-11"
from browserist import Browser

results = []

with Browser() as browser:
    browser.open.url("https://example.com")
    all_links = browser.get.url.from_links("//a")
    for link in all_links:
        browser.window.open.new_window(link)
        current_url = browser.get.url.current()
        results.append(current_url)

print(results)
```

## Position
You can also control the position of the browser window on the screen. This can be useful when you want to automate the placement of windows on your screen.

### Absolute
How to move the window to the chosen coordinate of the screen, if possible:

```python linenums="1" hl_lines="4"
from browserist import Browser

with Browser() as browser:
    browser.window.set.position(100, 100)
    browser.open.url("https://example.com")
```

### Relative
Get the current position of the window and move it by 10 pixels in both axes, if possible:

```python linenums="1" hl_lines="4-5"
from browserist import Browser

with Browser() as browser:
    x, y = browser.window.get.position()
    browser.window.set.position(x - 10, y - 10)
    browser.open.url("https://example.com")
```
