# Browser Types
If you want to use other browser types, e.g. Firefox, Edge, etc., define this in the settings:

```python
from browserist import Browser, BrowserSettings, BrowserType

settings = BrowserSettings(type = BrowserType.FIREFOX)
with Browser(settings) as browser:
    browser.open.url("http://example.com/")
```

## Supported Browsers
| Name              | Type                            |
| ----------------- | ------------------------------- |
| Chrome            | `BrowserType.CHROME`            |
| Edge              | `BrowserType.EDGE`              |
| Firefox           | `BrowserType.FIREFOX`           |
| Internet Explorer | `BrowserType.INTERNET_EXPLORER` |
| Opera             | `BrowserType.OPERA`             |
| Safari            | `BrowserType.SAFARI`            |
