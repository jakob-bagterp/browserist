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
Normally, browsers allow you to open a new tab by pressing `Ctrl` + `T` or by clicking a button in your browser. With Browserist you can automate this, for example based on a list of URLs. This will open each URL in a new tab:

```python linenums="1"
from browserist import Browser

urls = ["https://example.com", "https://google.com", "https://bing.com"]

with Browser() as browser:
    for url in urls:
        browser.window.open.new_tab(url)
```
