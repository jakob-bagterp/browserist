# Headless Mode
When you want to run an automated browser in the background while doing something else, headless mode is a good option. Also, headless mode often is faster and it takes up less resources now that the browser doesn't have to render a window on the screen. In the other hand, the disadvantage is obviously that you can't view what the browser is doing.

How to set the browser driver in headless mode:

```python
from browserist import Browser, BrowserSettings

settings = BrowserSettings(headless = True)

with Browser(settings) as browser:
    browser.open.url("http://example.com/")
```

The default setting for `headless` is `False`.

Note that not all websites support interaction with an automated browser in headless mode. Sometimes you then need to revert back to the default non-headless mode.

## Standardised Settings Across Browser Types
If you want a headless browser with Selenium, you typically would use different settings from browser to browser. Browserist solves this problem so that settings for Chrome, Firefox, Edge, etc. are standardised. For example, you can easily scale test runs across different browsers in a lightweight, headless configuration:

```python
from browserist import Browser, BrowserSettings, BrowserType

chrome = BrowserSettings(type = BrowserType.CHROME, headless = True)
edge = BrowserSettings(type = BrowserType.EDGE, headless = True)
firefox = BrowserSettings(type = BrowserType.FIREFOX, headless = True)

for settings in [chrome, edge, firefox]:
    with Browser(settings) as browser:
        browser.open.url("http://example.com/")
```