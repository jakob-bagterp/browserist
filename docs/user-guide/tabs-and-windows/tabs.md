---
tags:
    - Tutorial
    - Tabs and windows
---

# Working with Tabs
Tabs are a convenient way to organize and navigate multiple web pages within a single browser window. With Browserist, you can easily automate the process of opening and managing tabs.

Let's imagine you want to open a web page first and then open another page in a new tab, a basic example would look like this:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://google.com")
    browser.window.open.new_tab("https://example.com")
```

## Opening Multiple Tabs
Normally, browsers allow you to open a new tab by pressing `Ctrl` + `T` in Windows, `Cmd` + `T` on a Mac, or by clicking a button in your browser. With Browserist you can automate this, for example based on a list of URLs. This example will open each URL in a new tab:

```python linenums="1"
from browserist import Browser

urls = ["https://example.com", "https://google.com", "https://bing.com"]

with Browser() as browser:
    for url in urls:
        browser.window.open.new_tab(url)
```

## Switching Between Tabs
Switching between tabs is a common task when using a browser. You can either click a tab to switch to it or use a keyboard shortcut to cycle through open tabs. How to automate this with Browserist:

```python linenums="1"
from browserist import Browser

urls = ["https://example.com", "https://google.com", "https://bing.com"]

with Browser() as browser:
    for i, url in enumerate(urls):
        browser.window.open.new_tab(url, f"tab_{i}")
```

Now we can switch between each tab by calling its window handle:

```python linenums="8"
    browser.window.switch_to("tab_0")
    browser.window.switch_to("tab_1")
    browser.window.switch_to("tab_2")
```
