# Ignore Images
It's often faster to load pages when you don't download images. With Browserist, it's simple to configure:

```python
from browserist import Browser, BrowserSettings

settings = BrowserSettings(disable_images = True)

with Browser(settings) as browser:
    browser.open.url("https://example.com")
```

The default setting for `disable_images` is `False`.

## Standardised Settings Across Browser Types
If you want to ignore image downloads with Selenium, you typically would use different settings from browser to browser. Browserist solves this problem so that settings for Chrome, Firefox, Edge, etc. are standardised. For example, you can easily scale test runs across different browsers with a configuration like this:

```python
from browserist import Browser, BrowserSettings, BrowserType

chrome = BrowserSettings(type = BrowserType.CHROME, disable_images = True)
edge = BrowserSettings(type = BrowserType.EDGE, disable_images = True)
firefox = BrowserSettings(type = BrowserType.FIREFOX, disable_images = True)

for settings in [chrome, edge, firefox]:
    with Browser(settings) as browser:
        browser.open.url("https://example.com")
```
