---
tags:
    - Tutorial
---

# How to Wait for Implicit Time
Most of Browserist's methods already implicitly wait for certain elements on the page to be ready – so you don't have to worry about it – but sometimes you may want to wait for certain elements to be ready. This is especially useful for single page application elements handled by JavaScript, but also for standard HTML that doesn't load immediately.

## Wait for Item to Be Ready
### Element
#### Appear
This helper function ensures that DOM elements are ready before processing. The example waits for any H1 heading to be ready:

```python title="" linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.wait.for_element("//h1")
```

!!! tip
    You often don't need to use this method, as most other methods already implicitly wait for elements to be ready under the hood. For example, if you want to get the text of a heading, you can simply use:

    ```python title="" linenums="1"
    from browserist import Browser

    with Browser() as browser:
        browser.open.url("https://example.com")
        heading = browser.get.text("//h1")
        print(heading)
    ```

    You don't need to specify the wait `browser.wait.for_element("//xpath/to/element")` like this:

    ```python title="" linenums="1"
    from browserist import Browser

    with Browser() as browser:
        browser.open.url("https://example.com")
        browser.wait.for_element("//h1")
        heading = browser.get.text("//h1")
        print(heading)
    ```

#### Disappear
Conversely, you can also wait for an element to disappear from the DOM. This is useful for single page applications where elements are removed and added dynamically. An example:

```python title="" linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.input.value("//xpath/to/input", "test")
    browser.click.button("//xpath/to/button")
    browser.wait.until.element_disappears("//xpath/to/input")
```

### Image
Sometimes `img` image elements are present in the DOM, but the actual images are not yet loaded after first page paint, and so they will be loaded lazily in the background. This example waits until the image(s) on the page have loaded:

```python title="" linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.wait.until.images_have_loaded("//img")
```

### Text
Sometimes an element may be ready in the DOM, but the text hasn't been injectd. This helper function checks and waits for the element to contain any text:

```python title="" linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.wait.until.contains_any_text("//h1")
```

### Clickable
This example is useful for elements that are present in the DOM, yet are not ready to be clicked:

```python title="" linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.wait.until.is_clickable("//xpath/to/button")
    browser.click.button("//xpath/to/button")
```

## Adjust the Timeout
Most methods have a default timeout of 5 seconds. If the element hasn't been found by then, an error is thrown. You can shorten or lengthen this by passing a timeout value in seconds. A few examples:

```python title=""
heading = browser.get.text("//h1", timeout=10)
```

```python title=""
browser.wait.until.contains_any_text("//h1", timeout=8)
```
