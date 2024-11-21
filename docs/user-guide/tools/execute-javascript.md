---
title: How to Execute JavaScript in Web Scraping
description: Learn how to execute JavaScript in browser automation and web scraping using Browserist. Includes code examples for beginners and advanced users.
tags:
    - Tutorial
---

# How to Execute JavaScript
When automating the execution of JavaScript, this can either be done with or without a `WebElement`.

## Without `WebElement`
Basic usage of JavaScript execution:

```python linenums="1" hl_lines="5"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.tool.execute_script("alert('Hello world!')")
```

## With `WebElement`
The `WebElement` is used when you need to interact with a specific element on the page:

```python linenums="1" hl_lines="5-6"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    element = browser.get.element("//xpath/to/element")
    browser.tool.execute_script("arguments[0].scrollIntoView();", element)
```

## From a File
Sometimes you want to run a script that is stored in a file. This can be done by reading the file before running the script:

```python linenums="1" hl_lines="3-4 8"
from browserist import Browser

with open("/path/to/script.js", "r") as file:
    script = file.read()

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.tool.execute_script(script)
```
