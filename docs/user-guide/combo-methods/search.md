---
title: How to Automate Search Handling in Web Scraping
description: Learn how to automate search handling using combo methods in Browserist. Includes code examples for beginners and advanced users.
tags:
    - Tutorial
    - Settings
    - Combo
---

# How to Handle Searches
Imagine that you have a list of items and you want to search through them. You can use the search combo method and `SearchSettings` class to do this at scale.

View all options in the [reference documentation](../../reference/browser/combo/search.md#searchsettings).

## Examples
Basic usage:

```python linenums="1"
from browserist import Browser, SearchSettings

search_settings = SearchSettings(
    url="https://google.com",
    input_xpath ="//xpath/to/input_field",
    button_xpath="//xpath/to/search_button")

with Browser() as browser:
    browser.combo.search("some search term", search_settings)
    assert browser.tool.count_elements("//xpath/to/search_result_elements") > 0
```

Let's imagine that we want to test whether a search engine has fuzzy search enabled, For instance, this could mean that American and British English yield the same results for, respectively, "color" and "colour" as search term:

```python linenums="1"
from browserist import Browser, SearchSettings

search_settings = SearchSettings(
    url="https://google.com",
    input_xpath="//xpath/to/input_field",
    button_xpath="//xpath/to/search_button")

with Browser() as browser:
    browser.combo.search("color", search_settings)
    color_results = browser.tool.count_elements("//xpath/to/search_result_elements")
    browser.combo.search("colour", search_settings)
    colour_results = browser.tool.count_elements("//xpath/to/search_result_elements")
    assert color_results == colour_results
```
