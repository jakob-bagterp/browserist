---
tags:
    - Tutorial
    - Navigation
---

# How to Adjust Window Size
The window size defines the outer size of the browser window. If you want to change the inner size, check the [viewport section](./../settings/viewport.md).

## Specific Window Size
### Set
How to set the browser window to a specific size:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.window.set.size(800, 600)
    browser.open.url("https://example.com")
```

### Get
How to, for example, get the current window width and decrease it by 10 pixels:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    width = browser.window.get.width()
    browser.window.set.width(width - 10)
    browser.open.url("https://example.com")
```

## General Window Sizes
### Full Screen
```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.window.fullscreen()
    browser.open.url("https://example.com")
```

### Maximized
How to enlarge the browser window to the maximum allowed size.

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.window.maximize()
    browser.open.url("https://example.com")
```

!!! info
    For most operating systems, the window will fill the screen, without blocking the operating system's own menus and toolbars. Obviously, the size of the browser window also depends on the device and its screen resolution.

### Minimized
```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.open.url("https://example.com")
    browser.window.minimize()
```
