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
How to scroll down by a number of pixels:

```python title=""
browser.scroll.down_by(100)
```

How to scroll up by a number of pixels:

```python title=""
browser.scroll.up_by(50)
```

#### Pages
How to scroll a page down:

```python title=""
browser.scroll.page.down()
```

How to scroll a page up:

```python title=""
browser.scroll.page.up()
```

#### Example with Mixed Methods
Let's imagine that we want to take screenshots of a page that requires scrolling to load all the content. We can scroll down by a page and then a little up to capture screenshots the entire page:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.screeenshot.visible_portion()
    while not browser.scroll.check_if.is_end_of_page():
        browser.scroll.page.down()
        browser.scroll.up_by(5)
        browser.screeenshot.visible_portion()
```

### By Element
into view
bottom of the page
top of the page

### To Specific Position

Advanced with get and set

## Scrolling Sideways Left and Right

## Conditional Scrolling
### How to Check If Scrolling Is Possible

### Only Scroll If Necessary
