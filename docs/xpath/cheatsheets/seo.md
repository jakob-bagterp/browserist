---
tags:
    - Tutorial
    - Cheatsheet
    - XPath
---

# XPath Cheatsheet for Search Engine Optimisation (SEO)
Certain XPath expressions are especially useful for search engine optimisation.

## Content
Count all `<h1>` nodes to ensure that a web page has and only has one main headline. Should not be 0 or larger than 1:

```text title=""
count(//h1)
```

### Example
How to use Browserist to check whether a web page has exactly one `<h1>` headline tag:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    assert browser.tool.count_elements("//h1") == 1
```

## Meta Data
Similarly, ensure that a web page has meta description. Should not be 0 or larger than 1:

```text title=""
count(//meta[@name='description'])
```

Check if a web page has a canonical URL. If it has, it should only be 1:

```text title=""
count(//link[@rel='canonical'])
```

Ensure that a web page has a robots meta tag. Should not be 0 or larger than 1:

```text title=""
count(/html/head/meta[@name='robots'])
```

## Page Title
Ensure that a web page doesn't have an empty title:

```text title=""
/html/head/title[.!='']
```

### Example
How to use Browserist to check whether a web page has a page title:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    assert browser.check_if.does_exist("/html/head/title[.!='']") is True
```

Alternatively, without using XPath:

```python linenums="5"
    assert browser.get.page_title() != ""
```
