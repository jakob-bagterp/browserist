# Browser Types
If you want to use other browser types, e.g. Firefox, Edge, etc., define this in the settings:

```python
from browserist import Browser, BrowserSettings, BrowserType

settings = BrowserSettings(type = BrowserType.FIREFOX)

with Browser(settings) as browser:
    browser.open.url("http://example.com/")
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
