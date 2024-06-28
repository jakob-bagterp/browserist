---
tags:
    - Tutorial
---

# How to Wait for Implicit Time
Most of Browserist's methods already implicitly wait for certain elements on the page to be ready – so you don't have to worry about it – but sometimes you may want to wait for certain elements to be ready. This is especially useful for single page application elements handled by JavaScript, but also for standard HTML that doesn't load immediately.

## Wait for Elements to Be Ready
This helper function ensures that DOM elements are ready before processing. The example waits for any H1 heading to be ready:

```python title="" linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.wait.for_element("//h1")
```
