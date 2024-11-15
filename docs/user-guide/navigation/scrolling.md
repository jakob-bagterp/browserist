---
title: How to Automate Scrolling in Web Scraping
description: Learn how to automate scrolling up or down, left or right in browser automation and web scraping using Browserist. Includes code examples.
tags:
    - Tutorial
    - Navigation
---

# How to Automate Scrolling
Browserist provides a simple way to scroll a web page – both up and down, to specific elements or sideways. This can be useful when you need to interact with elements that are not immediately visible or when you want to take screenshots of content that is only loaded when you scroll.

!!! note
    Similar to scrolling on a touch screen or mouse, you can only scroll down if you're not already at the bottom of the page, and you can only scroll up if you're not already at the top of the page. Or you can't scroll up exactly 50 pixels if you're already 20 pixels from the top of the page – instead you scroll up 20 pixels. Keep this in mind when trying to replicate the examples below.

## Scrolling Up and Down
### By Disstance
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

It's also possible to scroll up or down by a number of pages:

```python title=""
browser.scroll.page.down(2)
```

```python title=""
browser.scroll.page.up(3)
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

How to scroll to an absolute position on the page with `x` and `y` coordinates, where `y=100` is the vertical position:

```python title=""
browser.scroll.to_position(x=0, y=100)
```

Or simply:

```python title=""
browser.scroll.to_position(0, 100)
```

## Scrolling Sideways Left and Right
### By Disstance
#### Pixels
How to scroll right by a number of pixels, relative to the current position:

```python title=""
browser.scroll.right_by(20)
```

How to scroll left by a number of pixels, relative to the current position:

```python title=""
browser.scroll.left_by(40)
```

### To Absolute Position
How to scroll to an absolute position on the page with `x` and `y` coordinates, where `x=100` is the horizontal position:

```python title=""
browser.scroll.to_position(x=100, y=0)
```

Or simply:

```python title=""
browser.scroll.to_position(100, 0)
```

### Example
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
You can check if you're at the end or top of the page with these methods:

```python title=""
browser.scroll.check_if.is_end_of_page()
```

```python title=""
browser.scroll.check_if.is_top_of_page()
```

#### Example
Example where we want take a screenshot of the footer of a page:

```python linenums="1"
from browserist import Browser

urls = ["https://example.com", "https://google.com", "https://bing.com"]

with Browser() as browser:
    for url in urls:
        browser.open.url(url)
        if not browser.scroll.check_if.is_end_of_page():
            browser.scroll.page.to_end()
        browser.screenshot.visible_portion()
```

### Only Scroll If Necessary
Instead of checking whether an element is visible in the viewport before scrolling to it...

```python title="" linenums="1"
if not browser.check_if.is_in_viewport("//xpath/to/element"):
    browser.scroll.into_view("//xpath/to/element")
```

... such logic is already combined in this method:

```python title=""
browser.scroll.into_view_if_not_in_viewport("//xpath/to/element")
```

#### Example
Example in context where we want to make sure an element is visible in the viewport before taking a screenshot of it:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.scroll.into_view_if_not_in_viewport("//xpath/to/element")
    browser.screenshot.visible_portion()
```
