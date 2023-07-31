---
tags:
    - Tutorial
    - Settings
---

# Search Combo Method
Imagine that you have a list of items and you want to search through them. You can use the search combo method and `SearchSettings` class to do this at scale.

## Example
```python title=""
from browserist import Browser, SearchSettings

search_settings = SearchSettings(
    url = "https://google.com",
    input_xpath = "//xpath/to/input_field",
    button_xpath = "//xpath/to/search_button")

with Browser() as browser:
    browser.combo.search("some search term", search_settings)
    assert browser.tool.count_elements("//xpath/to/search_result_elements") > 0
```
