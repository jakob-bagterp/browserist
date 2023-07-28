# Settings Overview
Use `BrowserSettings` with the following options:

| Setting              | Option                                    | Default                              | Description                                                                                                      |
| -------------------- | ----------------------------------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| `type`               | `BrowserType`                             | `BrowserType.CHROME`                 | Set browser type, e.g. Chrome, Edge, Firefox, etc.                                                               |
| `headless`           | `True` or `False`                         | `False`                              | Run the browser in headless mode. May not be supported by all browsers.                                          |
| `disable_images`     | `True` or `False`                         | `False`                              | Neither request nor render images, which typically improves loading speed. May not be supported by all browsers. |
| `page_load_strategy` | `PageLoadStrategy`                        | `PageLoadStrategy.NORMAL`            | Set page load strategy.                                                                                          |
| `path_to_executable` | Path to file                              | System default                       | If the browser executable isn't in a default folder, select which file to use.                                   |
| `screenshot_dir`     | Path to directory                         | System default                       | Set where to save sreenshots. Default is the directory of Browserist.                                            |
| `timeout`            | `TimeoutSettings`                         | `TimeoutStrategy.STOP` and 5 seconds | Set timeout strategy and time.                                                                                   |
| `viewport`           | `DeviceViewportSize` or `(width, height)` | Browser default                      | Emulate viewport size as device or set custom value in pixels.                                                   |

## Example
```python
from browserist import Browser, BrowserSettings, BrowserType, common_devices

settings = BrowserSettings(
    type = BrowserType.FIREFOX,
    headless = True,
    disable_images = True
)

with Browser(settings) as browser:
    browser.viewport.set.size_by_device(common_devices.Apple.IPHONE_SE)
    browser.open.url("http://example.com/")
```
