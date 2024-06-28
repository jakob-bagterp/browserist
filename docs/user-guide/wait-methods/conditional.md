---
tags:
    - Tutorial
---

# Wait Until a Condition Is Met
This group of methods apply the following conditions to either the page title, text of an element, or URL:

* Changes
* Contains (non exact match)
* Equals (exact match)

## Page Title
### Changes
Wait until the page title changes from a baseline text:

```python title="" linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    baseline_text = browser.get.page_title()
    browser.click.button("//xpath/to/button")
    browser.wait.until.page_title.changes(baseline_text)
```

### Contains
Wait until the page title contains a text partial:

```python title="" linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.wait.until.page_title.contains("Example")
```

### Equals
Wait until the page title equals a specific text:

```python title="" linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.wait.until.page_title.equals("Example Domain")
```

## Text
### Changes
Wait until the text of an element changes from a baseline text:

```python title="" linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    baseline_text = browser.get.text("//h1")
    browser.click.button("//xpath/to/button")
    browser.wait.until.text.changes("//h1", baseline_text)
```

### Contains
Wait until the text of an element contains a text partial:

```python title="" linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.wait.until.text.contains("//h1", "Example")
```

### Equals
Wait until the text of an element equals a specific text:

```python title="" linenums="1"

from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.wait.until.text.equals("//h1", "Example Domain")
```

## URL
### Changes
Wait until the URL changes from a baseline URL:

```python title="" linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    baseline_url = browser.get.url.current()
    browser.click.button("//xpath/to/button")
    browser.wait.until.url.changes(baseline_url)
```

### Contains
Wait until the URL contains a text partial:

```python title="" linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.click.button("//xpath/to/button")
    browser.wait.until.url.contains("some_page_name")
```

### Equals
Wait until the URL equals a specific URL:

```python title="" linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.click.button("//xpath/to/button")
    browser.wait.until.url.equals("https://example.com/some_page_name")
```
