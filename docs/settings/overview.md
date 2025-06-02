---
title: How to Configure and Optimize Browserist
description: Learn how to configure Browserist for different browser types, headless mode, and other settings to optimize browser automation and scraping.
tags:
    - Tutorial
    - Settings
    - Browser Types
    - Performance
    - Headless
    - Viewport
---

# Configuration Options 🛠️
When using Selenium, you often need to configure the driver differently for each browser, whether it should disable images or run in headless mode.

With Browserist, many of these complexities are handled automatically under the hood, so all you need to do is set the browser type and other options in the `BrowserSettings` class.

## Examples
### Basic Usage
If you want to use a specific browser types, e.g. Firefox, it's easy to define in the settings:

```python linenums="1" hl_lines="3 5"
from browserist import Browser, BrowserSettings, BrowserType

settings = BrowserSettings(type=BrowserType.FIREFOX)

with Browser(settings) as browser:
    browser.open.url("https://example.com")
```

### Advanced Options
And if you want to use Firefox in [headless mode](../performance/headless.md), [disable images](../performance/disable-images.md), and emulate the [viewport of a specific device](../settings/viewport.md), that's also possible:

```python linenums="1" hl_lines="3 9"
from browserist import Browser, BrowserSettings, BrowserType, common_devices

iphone_se = common_devices.Apple.IPHONE_SE

settings = BrowserSettings(
    type=BrowserType.FIREFOX,
    headless=True,
    disable_images=True,
    viewport=iphone_se)

with Browser(settings) as browser:
    browser.open.url("https://example.com")
```

## Options for `BrowserSettings`
Use `BrowserSettings` with the following options:

| Setting              | Option                  | Default | Description |
| -------------------- | ----------------------- | ------- | ----------- |
| `type`               | `BrowserType`           | `BrowserType.CHROME` (except `BrowserType.EDGE` for Windows) | Set [browser type](browser-types.md), e.g. Chrome, Edge, Firefox, etc. |
| `headless`           | `True` or `False`       | `False` | Run the browser in [headless mode](../performance/headless.md). May not be supported by all browsers, or some interaction methods, e.g. select, may not be supported. |
| `disable_images`     | `True` or `False`       | `False` | [Neither request nor render images](../performance/disable-images.md), which typically improves loading speed. May not be supported by all browsers. |
| `page_load_strategy` | `PageLoadStrategy`      | `PageLoadStrategy.NORMAL` | Set [page load strategy](page-load-strategy.md). |
| `path_to_executable` | Path to file            | System default | If the browser executable isn't in a default folder, select which file to use. |
| `download_dir`       | Path to directory       | System default | Set where to save [downloads](../user-guide/download-files.md). Default is the `Downloads` folder of the user. |
| `screenshot_dir`     | Path to directory       | System default | Set where to save [sreenshots](../user-guide/screenshots.md). Default is the `Downloads` folder of the user. |
| `timeout`            | `TimeoutSettings`       | `TimeoutStrategy.STOP` and 5 seconds | Set [timeout strategy and time](timeout-strategy.md). |
| `viewport`           | `DeviceViewportSize` or `(width, height)` | Browser default size | Emulate [viewport size](viewport.md) as device or set custom value in pixels. |
| `check_connection`   | `True` or `False`       | `True` | Check whether there is an [internet connection](check-connection.md) before starting the browser. Bypass the check by setting it to `False`. |
| `user_agent`         | User agent string `str` | Browser default | Set a custom [user agent](user-agent.md) to override the default user agent. |
| `proxy`              | `ProxySettings` or  IP address `str` | `None` | Enable a custom [proxy server](proxy.md) for the browser. If not using `ProxySettings`, use a string containing IP address and port number. For example, `http://127.0.0.1:8080` for a public proxy or `http://username:password@127.0.0.1:8080` for a private proxy that requires authentication. |

## Support the Project
If you have already downloaded and tried the package – maybe even used it in a production environment – perhaps you would like to support its development?

!!! tip "Become a Sponsor"
    If you find this project helpful, please consider supporting its development. Your donations will help keep it alive and growing. Every contribution, no matter the size, makes a difference.

    [Donate on GitHub Sponsors](https://github.com/sponsors/jakob-bagterp){ .md-button .md-button--primary }

    Thank you for your support! 🙌
