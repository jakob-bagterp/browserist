---
tags:
    - Tutorial
    - Tabs and windows
---

# Working with Windows
When you want to open multiple web pages in separate browser windows, Browserist makes it easy to organize and automate your workflow.

## Examples
### Basic Usage
Let's imagine you want to open a web page first and then open another page in a new window, a basic example would look like this:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.window.open.new_window("https://google.com")
```

### Opening Multiple Windows
Normally, browsers allow you to open a new window by pressing `Ctrl` + `N` in Windows or `Cmd` + `N` on a Mac. With Browserist you can automate this, for example based on a list of URLs. This example will open each URL in a new window:

```python linenums="1"
from browserist import Browser

urls = ["https://example.com", "https://google.com", "https://bing.com"]

with Browser() as browser:
    for url in urls:
        browser.window.open.new_window(url)
```

### Switching Between Windows
Switching between windows is a common task when using a browser. Instead of either clicking a window to switch to it or using a keyboard shortcut to cycle through open windows, you can automate this with Browserist:

```python linenums="1"
from browserist import Browser

urls = ["https://example.com", "https://google.com", "https://bing.com"]

with Browser() as browser:
    for i, url in enumerate(urls):
        browser.window.open.new_window(url, f"window_{i}")
```

Now we can switch between each window by calling its handle:

```python linenums="8"
    browser.window.switch_to("window_0")
    browser.window.switch_to("window_1")
    browser.window.switch_to("window_2")
```

#### Get Handle ID of Current Window
Under the hood, Browserist uses handle IDs to manage and identify open windows and tabs. You can get the handle ID of the current window to switch back to it later:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    base_handle_id = browser.window.handle.current()
    browser.window.open.new_window("https://google.com")
    browser.window.switch_to(base_handle_id)
```

### Get List of URLs from Open Windows
Because a link can redirect to a different destination than the original URL, you sometimes want to capture the actual destination of each page. Here is an example of how to capture all the links from a web page and open them in new windows:

```python linenums="1"
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
