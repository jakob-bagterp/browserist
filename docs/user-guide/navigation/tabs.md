---
title: How to Work with Tabs in Web Scraping
description: Learn how to open, close, and switch between tabs in browser automation and web scraping using Browserist. Includes code examples for beginners and advanced users.
tags:
    - Tutorial
    - Navigation
    - Tabs and Windows
---

# How to Open and Manage Tabs
Tabs are a convenient way to organize and navigate multiple web pages within a single browser window. With Browserist, you can easily automate the process of opening and managing tabs.

## Basic Usage
Let's imagine you want to open a web page first and then open another page in a new tab, a basic example would look like this:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.window.open.new_tab("https://google.com")
```

## Multiple
### Opening Multiple Tabs
Normally, browsers allow you to open a new tab by pressing `Ctrl` + `T` in Windows, `Cmd` + `T` on a Mac, or by clicking a button in your browser. With Browserist you can automate this, for example based on a list of URLs. This example will open each URL in a new tab:

```python linenums="1"
from browserist import Browser

urls = ["https://example.com", "https://google.com", "https://bing.com"]

with Browser() as browser:
    for url in urls:
        browser.window.open.new_tab(url)
```

### Closing a Tab
How to close the current tab or, if it's the last tab in a window, the current browser window:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.window.open.new_tab("https://google.com")
    browser.window.close()
```

### Switching Between Tabs
Switching between tabs is a common task when using a browser. Instead of either clicking a tab to switch to it or using a keyboard shortcut to cycle through open tabs, you can automate this with Browserist:

```python linenums="1"
from browserist import Browser

urls = ["https://example.com", "https://google.com", "https://bing.com"]

with Browser() as browser:
    for i, url in enumerate(urls):
        browser.window.open.new_tab(url, f"tab_{i}")
```

Now we can switch between each tab by calling its handle:

```python linenums="8"
    browser.window.switch_to("tab_0")
    browser.window.switch_to("tab_1")
    browser.window.switch_to("tab_2")
```

#### Return to the Initial Tab
Browserist also keeps track of the initial tab of the original browser window, so you can easily switch back to it:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.window.open.new_tab("https://google.com")
    browser.window.switch_to_original_window()
```

#### Get Handle ID of Current Tab
Under the hood, Browserist uses handle IDs to manage and identify open windows and tabs. You can get the handle ID of the current tab to switch back to it later:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    base_handle_id = browser.window.handle.current()
    browser.window.open.new_tab("https://google.com")
    browser.window.switch_to(base_handle_id)
```

## Example
### Get List of URLs from Open Tabs
Because a link can redirect to a different destination than the original URL, you sometimes want to capture the actual destination of each page. Here is an example of how to capture all the links from a web page and open them in new tabs:

```python linenums="1"
from browserist import Browser

results = []

with Browser() as browser:
    browser.open.url("https://example.com")
    all_links = browser.get.url.from_links("//a")
    for link in all_links:
        browser.window.open.new_tab(link)
        current_url = browser.get.url.current()
        results.append(current_url)

print(results)
```
