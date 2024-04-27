# Browserist Documentation 📚
Your main resource when automating browsers with Browserist. Find details about all methods in this section.

## Structure
Find the method you need in the left-hand menu. Each `__main__` entry refers to its parent object, and the structure of the documentation is:

```text title="Structure"
browser.__main__
    .back()
    .forward()
    ...
    .check_if
        .contains_any_text()
        .contains_text()
        ...
    ...
    .wait.__main__
        .for_element()
        .random_seconds
        .seconds()
        .until.__main__
            .contains_any_text()
            ...
```

Examples of how to chain the methods:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.click.button("//xpath/to/button")
    browser.back()
    browser.check_if.contains_any_text("//xpath/to/element")
    browser.wait.seconds(5)
    browser.wait.until.contains_any_text("//xpath/to/element")
```
