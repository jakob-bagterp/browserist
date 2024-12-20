---
title: How to Validate User Input in Web Scraping
description: Learn how to validate user input in browser automation and web scraping using Browserist. Includes code examples for beginners and advanced users.
tags:
    - Tutorial
---

# How to Validate User Input
Browserist provides methods to validate user input, such as URLs, XPaths, and other values. This is useful when interacting with users to ensure that the input meets the expected criteria.

## User Input Validation
Imagine you want to prompt the user to input a value in the terminal and hereafter validate the value before posting the form input:

```python linenums="1" hl_lines="6"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    user_input = input("Input value:")
    while not browser.tool.is_input_valid(user_input, r"regex"):
        print("Invalid input. Please try again...")
        user_input = input("Input value:")
    browser.input.value("//xpath/to/input", user_input)
```

## XPath Validation
How to prompt the user for a valid XPath value in the terminal:

```python linenums="1" hl_lines="6"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    user_xpath = input("Input XPath:")
    while not browser.tool.is_xpath_valid(user_xpath)
        print("Invalid XPath. Please try again...")
        user_xpath = input("Input XPath:")
    browser.click.button(user_xpath)
```

## URL Validation
How to prompt the user for a valid URL in the terminal:

```python linenums="1" hl_lines="5"
from browserist import Browser

with Browser() as browser:
    user_url = input("Input URL:")
    while not browser.tool.is_url_valid(user_url)
        print("Invalid URL. Please try again...")
        user_url = input("Input URL:")
    browser.open.url(user_url)
```
