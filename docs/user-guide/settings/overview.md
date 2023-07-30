---
tags:
    - Tutorial
    - Settings
    - Browser Types
    - Performance
    - Headless
    - Viewport
---

# Settings Overview
## Options for `BrowserSettings`
Use `BrowserSettings` with the following options:

| Setting | Option | Default | Description |
| ------- | ------ | ------- | ----------- |
| `type` | `BrowserType` | `BrowserType.CHROME` (except `BrowserType.EDGE` for Windows) | Set [browser type](browser-types.md), e.g. Chrome, Edge, Firefox, etc. |
| `headless` | `True` or `False` | `False` | Run the browser in [headless mode](../performance/headless.md). May not be supported by all browsers. |
| `disable_images` | `True` or `False` | `False` | [Neither request nor render images](../performance/ignore-images.md), which typically improves loading speed. May not be supported by all browsers. |
| `page_load_strategy` | `PageLoadStrategy` | `PageLoadStrategy.NORMAL` | Set [page load strategy](page-load-strategy.md). |
| `path_to_executable` | Path to file | System default | If the browser executable isn't in a default folder, select which file to use. |
| `screenshot_dir` | Path to directory | System default | Set where to save sreenshots. Default is the directory of Browserist. |
| `timeout` | `TimeoutSettings` | `TimeoutStrategy.STOP` and 5 seconds | Set [timeout strategy and time](timeout-strategy.md). |
| `viewport` | `DeviceViewportSize` or `(width, height)` | Browser default size | Emulate [viewport size](viewport.md) as device or set custom value in pixels. |

## Example
```python
from browserist import Browser, BrowserSettings, BrowserType, common_devices

iphone_se = common_devices.Apple.IPHONE_SE

settings = BrowserSettings(
    type = BrowserType.FIREFOX,
    headless = True,
    disable_images = True,
    viewport = iphone_se
)

with Browser(settings) as browser:
    browser.open.url("https://example.com")
```
