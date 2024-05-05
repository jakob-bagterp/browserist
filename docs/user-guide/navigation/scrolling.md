---
tags:
    - Tutorial
    - Navigation
---

# How to Automate Scrolling
Browserist provides a simple way to scroll a web page – both up and down, to specific elements or sideways. This can be useful when you need to interact with elements that are not immediately visible or when you want to take screenshots of content that is only loaded when you scroll.

!!! note
    Similar to scrolling on a touch screen or mouse, you can only scroll down if you're not already at the bottom of the page, and you can only scroll up if you're not already at the top of the page. Or you can't scroll up exactly 50 pixels if you're already 20 pixels from the top of the page – instead you scroll up 20 pixels. Keep this in mind when trying to replicate the examples below.

## Scrolling Up and Down
### By Length
#### Pixels
How to scroll down by a number of pixels, relative to the current position:

```python title=""
browser.scroll.down_by(100)
```

How to scroll up by a number of pixels, relative to the current position:

```python title=""
browser.scroll.up_by(50)
```

#### Pages
How to scroll a page down, relative to the current position:

```python title=""
browser.scroll.page.down()
```

How to scroll a page up, relative to the current position:

```python title=""
browser.scroll.page.up()
```

#### Example with Mixed Methods
Let's imagine that we want to take screenshots of a page that requires scrolling to load all the content. We can scroll down by a page and then a little up to capture screenshot partials of the entire page:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.screenshot.visible_portion()
    while not browser.scroll.check_if.is_end_of_page():
        browser.scroll.page.down()
        browser.scroll.up_by(5)
        browser.screenshot.visible_portion()
```

### To Specific Element
How to scroll down or up to make a specific element visible in the viewport:

```python title=""
browser.scroll.into_view("//xpath/to/element")
```

### To Absolute Position
How to scroll to the end of the page:

```python title=""
browser.scroll.page.to_end()
```

How to scroll to the top of the page:

```python title=""
browser.scroll.page.to_top()
```

How to scroll to an absolute position on the page with `x` and `y` coordinates:

```python title=""
browser.scroll.to_position(0, 100)
```

## Scrolling Sideways Left and Right
How to scroll right by a number of pixels, relative to the current position:

```python title=""
browser.scroll.right_by(20)
```

How to scroll left by a number of pixels, relative to the current position:

```python title=""
browser.scroll.left_by(40)
```

#### Example
Let's imagine that we want to ensure that we can't scroll sideways on a page. We try to scroll a little right and then a little left to ensure that the page is locked in place:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.scroll.page.to_top()
    x, y = browser.scroll.get.position()
    assert x == 0 and y == 0

    browser.scroll.right_by(1)
    x, _ = browser.scroll.get.position()
    assert x == 0

    browser.scroll.left_by(1)
    x, _ = browser.scroll.get.position()
    assert x == 0
```

## Conditional Scrolling
### How to Check If Scrolling Is Possible

### Only Scroll If Necessary
