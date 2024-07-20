---
tags:
    - Tutorial
    - Navigation
---

# How to Adjust Window Size
The window size defines the outer size of the browser window. If you want to change the inner size, check the [viewport section](./../settings/viewport.md).

## Specific Window Size
### Set
You can resize the browser window to a specific size, either vertically, horizontally, or both at the same time.

!!! info
    The size of the browser window is limited by several factors, including the operating system, the screen resolution of the monitor, and the different minimum sizes of different browser types. The resizing methods can therefore only attempt to set a specific size where possible.

#### Size
How to set the browser window to a specific size if possible:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.window.set.size(800, 600)
    browser.open.url("https://example.com")
```

#### Width
Similarly, only set the width to a specific size if possible:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.window.set.width(800)
    browser.open.url("https://example.com")
```

#### Height
Similarly, only set the height to a specific size if possible:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    browser.window.set.height(600)
    browser.open.url("https://example.com")
```

### Get
You can get the size of the browser window vertically, horizontally or both at the same time.

#### Size
For example, how to get the current window size and decrease it by 10 pixels both in width and height if possible:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    width, height = browser.window.get.size()
    browser.window.set.width(width - 10, height - 10)
    browser.open.url("https://example.com")
```

#### Width
Similarly, only decrease the width by 10 pixels if possible:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    width = browser.window.get.width()
    browser.window.set.width(width - 10)
    browser.open.url("https://example.com")
```

#### Height
Similarly, only decrease the height by 10 pixels if possible:

```python linenums="1"
from browserist import Browser

with Browser() as browser:
    height = browser.window.get.height()
    browser.window.set.height(height - 10)
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
