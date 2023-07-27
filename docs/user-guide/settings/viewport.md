# Emulate Viewport of Common Devices
You can set the viewport to emulate common device sizes or to a custom size. Note that it's recommended to run emulations in headless mode since an open browser may have minimum or maximum dimensions, either limited by the browser window or the monitor. Example:

```python
from browserist import Browser, BrowserSettings, common_devices

settings = BrowserSettings(headless = True)

with Browser(settings) as browser:
    browser.viewport.set.size_by_device(common_devices.Apple.IPHONE_SE)
    browser.open.url("http://example.com/")
    browser.viewport.set.size(768, 1024)
```
