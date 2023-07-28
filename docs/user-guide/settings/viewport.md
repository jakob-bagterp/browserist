# Viewport Size
## Emulate Common Devices
You can set the viewport to emulate common device sizes (e.g. various popular mobile phones or tablets). Example:

```python
from browserist import Browser, BrowserSettings, common_devices

settings = BrowserSettings(headless = True)
iphone_se = common_devices.Apple.IPHONE_SE

with Browser(settings) as browser:
    browser.viewport.set.size_by_device(iphone_se)
    browser.open.url("http://example.com/")
```

!!! tip
    It's recommended to run viewport emulations in [headless mode](../performance/headless-mode.md) since an open browser may have minimum or maximum dimensions, either limited by the browser window or the monitor.

## Custom Viewport Size
Or specify the viewport size as width and height in pixels:

```python
browser.viewport.set.size(1024, 768)
```
