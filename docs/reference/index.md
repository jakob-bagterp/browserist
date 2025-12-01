---
title: Documentation
description: Browserist is the easy way to do web scraping and browser automation with Python. This comprehensive documentation includes code examples for beginners and advanced users.
tags:
    - Documentation
    - Tutorial
---

# Browserist Documentation 📚
Your main resource when automating browsers with Browserist. Find details about all methods in this section.

## Structure
Find the method you need in the left-hand menu. Each `__main__` entry refers to its parent object, and the structure of the documentation is:

```text title="Structure" hl_lines="1 10 14"
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

## How to Chain Methods
Examples of how to chain the methods:

```python linenums="1" hl_lines="4-9"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.click.button("//xpath/to/button")
    browser.back()
    browser.check_if.contains_any_text("//xpath/to/element")
    browser.wait.seconds(5)
    browser.wait.until.contains_any_text("//xpath/to/element")
```

## Support the Project
If you have already downloaded and tried the package – maybe even used it in a production environment – perhaps you would like to support its development?

!!! tip "Become a Sponsor"
    If you find this project helpful, please consider supporting its development. Your donations will help keep it alive and growing. Every contribution makes a difference, whether you buy a coffee or support with a monthly donation. Find your tier here:

    [Donate on GitHub Sponsors](https://github.com/sponsors/jakob-bagterp){ .md-button .md-button--primary }

    Thank you for your support! 🙌
