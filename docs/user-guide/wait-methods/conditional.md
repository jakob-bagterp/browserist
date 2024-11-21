---
title: How to Await Conditions in Web Scraping
description: Learn how to wait until a condition is met in browser automation and web scraping using Browserist. Includes code examples for beginners and advanced users.
tags:
    - Tutorial
---

# How to Wait Until a Condition Is Met
This group of methods apply the following conditions to either the page title, text of an element, or URL:

* Changes
* Contains (non exact match)
* Equals (exact match)


!!! tip "Adjust the Timeout"
    Most methods have a default timeout of 5 seconds. If the element hasn't been found by then, an error is thrown. You can shorten or lengthen this by passing a timeout value in seconds. A few examples:

    ```python title=""
    browser.wait.until.page_title.changes("baseline text", timeout=10)
    ```

    ```python title=""
    browser.wait.until.text.contains("//h1", "example", timeout=8)
    ```

    ```python title=""
    browser.wait.until.url.equals("https://example.com/", timeout=20)
    ```

## Page Title
### Changes
Wait until the page title changes from a baseline text:

```python linenums="1" hl_lines="7"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    baseline_text = browser.get.page_title()
    browser.click.button("//xpath/to/button")
    browser.wait.until.page_title.changes(baseline_text)
```

### Contains
Wait until the page title contains a text partial:

```python linenums="1" hl_lines="5"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.wait.until.page_title.contains("Example")
```

### Equals
Wait until the page title equals a specific text:

```python linenums="1" hl_lines="5"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.wait.until.page_title.equals("Example Domain")
```

## Text
### Changes
Wait until the text of an element changes from a baseline text:

```python linenums="1" hl_lines="7"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    baseline_text = browser.get.text("//h1")
    browser.click.button("//xpath/to/button")
    browser.wait.until.text.changes("//h1", baseline_text)
```

### Contains
Wait until the text of an element contains a text partial:

```python linenums="1" hl_lines="5"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.wait.until.text.contains("//h1", "Example")
```

### Equals
Wait until the text of an element equals a specific text:

```python linenums="1" hl_lines="5"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.wait.until.text.equals("//h1", "Example Domain")
```

## URL
### Changes
Wait until the URL changes from a baseline URL:

```python linenums="1" hl_lines="7"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    baseline_url = browser.get.url.current()
    browser.click.button("//xpath/to/button")
    browser.wait.until.url.changes(baseline_url)
```

### Contains
Wait until the URL contains a text partial:

```python linenums="1" hl_lines="6"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.click.button("//xpath/to/button")
    browser.wait.until.url.contains("some_page_name")
```

### Equals
Wait until the URL equals a specific URL:

```python linenums="1" hl_lines="6"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.click.button("//xpath/to/button")
    browser.wait.until.url.equals("https://example.com/some_page_name")
```
