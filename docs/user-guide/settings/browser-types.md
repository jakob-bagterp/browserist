---
tags:
    - Tutorial
    - Browser Types
    - Chrome
    - Edge
    - Firefox
    - Internet Explorer
    - Opera
    - Safari
---

# Browser Types
## Configure Browser Type
If you want to use other browser types, e.g. Firefox, Edge, etc., define this in the settings:

```python
from browserist import Browser, BrowserSettings, BrowserType

settings = BrowserSettings(type = BrowserType.FIREFOX)

with Browser(settings) as browser:
    browser.open.url("https://example.com")
    browser.wait.seconds(5)
```

## Supported Browsers
| Name              | Type                            | Notes                        |
| ----------------- | ------------------------------- | ---------------------------- |
| Chrome            | `BrowserType.CHROME`            | Default (except for Windows) |
| Edge              | `BrowserType.EDGE`              | Default for Windows          |
| Firefox           | `BrowserType.FIREFOX`           |                              |
| Internet Explorer | `BrowserType.INTERNET_EXPLORER` |                              |
| Opera             | `BrowserType.OPERA`             |                              |
| Safari            | `BrowserType.SAFARI`            |                              |

More information about [installation of browser drivers](../../getting-started/browser-drivers.md).

## How to Run Multiple Browsers
When you have multiple browser drivers installed, you can run them in sequence like this:

```python
from browserist import Browser, BrowserSettings, BrowserType

chrome = BrowserSettings(type = BrowserType.CHROME)
edge = BrowserSettings(type = BrowserType.EDGE)
firefox = BrowserSettings(type = BrowserType.FIREFOX)

for settings in [chrome, edge, firefox]:
    with Browser(settings) as browser:
        browser.open.url("https://example.com")
        browser.wait.seconds(5)
```
