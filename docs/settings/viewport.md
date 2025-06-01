---
title: How to Configure Viewport Size
description: Learn how to set and change the browser viewport sizes in automated tests. Emulate popular devices such as iPhone and iPad, or set custom viewport dimensions.
tags:
    - Tutorial
    - Settings
    - Viewport
    - Headless
---

# What Is a Viewport Size?
The viewport is the inner size of the browser window that displays the web page. Based on screen size and resolution – from desktop monitors to tablets and mobile phones – the viewport may be smaller than the actual web page and require scrolling to view the entire page.

If you want to change the outer size, check the [window size section](../user-guide/navigation/window-size.md).

## Emulate Common Devices
You can set the viewport to emulate common device sizes (e.g. various popular mobile phones or tablets). Example:

```python linenums="1" hl_lines="3 7"
from browserist import Browser, BrowserSettings, common_devices

iphone_se = common_devices.Apple.IPHONE_SE

settings = BrowserSettings(
    headless=True,
    viewport=iphone_se)

with Browser(settings) as browser:
    browser.open.url("https://example.com")
```

And you can later change the viewport to another device:

```python title="" linenums="10" hl_lines="1-2"
    ipad_air_2 = common_devices.Apple.IPAD_AIR_2
    browser.viewport.set.size_by_device(ipad_air_2)
```

!!! tip
    It's recommended to run viewport emulations in [headless mode](../performance/headless.md) since an open browser may have minimum or maximum dimensions, either limited by the browser window or the monitor.

### Available Common Devices
Browserist provides a pre-defined collection of common devices, covering tablets and mobile phones from the most popular manufacturers. Find more information in the reference documentation and source code:

* [Apple](../reference/viewport/common-devices/apple.md)
* [Google](../reference/viewport/common-devices/google.md)
* [Microsoft](../reference/viewport/common-devices/microsoft.md)
* [Samsung](../reference/viewport/common-devices/samsung.md)

### Create Custom Devices
You can also define custom device sizes for viewport emulation with the `DeviceViewportSize` class. Example:

```python linenums="1" hl_lines="11-12"
from browserist import Browser, BrowserSettings, DeviceViewportSize

custom_device_1 = DeviceViewportSize(540, 720)
custom_device_2 = DeviceViewportSize(912, 1368)
custom_device_3 = DeviceViewportSize(1024, 768)

settings = BrowserSettings(headless=True)

with Browser(settings) as browser:
    browser.open.url("https://example.com")
    for device in [custom_device_1, custom_device_2, custom_device_3]:
        browser.viewport.set.size_by_device(device)
        browser.screenshot.visible_portion()
```

## Custom Viewport Size
Alternatively, simply specify the viewport size in pixels as tuple for width and height, e.g. `(1024, 768)`:

```python linenums="1" hl_lines="5"
from browserist import Browser, BrowserSettings

settings = BrowserSettings(
    headless=True,
    viewport=(1024, 768))

with Browser(settings) as browser:
    browser.open.url("https://example.com")
```

And you can change the viewport size later:

```python title="" linenums="9" hl_lines="1"
    browser.viewport.set.size(768, 1024)
```
