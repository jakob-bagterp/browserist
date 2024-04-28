---
tags:
    - Tutorial
    - Performance
    - Headless
    - Settings
---

# Run Browser in Headless Mode
## What Is Headless?
Headless simply means running the browser in the background and without viewing the browser on the screen.

## How to Configure
The default setting for `headless` is `False` in `BrowserSettings`. Simply alter this to `True`, and now your browser driver runs in headless mode:

```python linenums="1"
from browserist import Browser, BrowserSettings

settings = BrowserSettings(headless=True)

with Browser(settings) as browser:
    browser.open.url("https://example.com")
```

!!! note
    Not all browsers support headless mode, for instance Safari and Internet Explorer.

## Advantages and Disadvantages
When you want to run an automated browser in the background while doing something else, headless mode is a good option. Also, headless mode often is faster and takes up less resources now that the browser doesn't have to render a window on the screen.

In the other hand, the disadvantage is obviously that you can't observe what the browser is doing.

!!! tip
    Not all websites support interaction with an automated browser in headless mode. Sometimes you then need to revert back to the default non-headless mode.

## Standardised Settings Across Browser Types
If you want a headless browser with Selenium, you typically would use different settings from browser to browser. Browserist solves this problem so that settings for Chrome, Firefox, Edge, etc. are standardised.

For example, you can easily scale test runs across different browsers in a lightweight, headless configuration:

```python linenums="1"
from browserist import Browser, BrowserSettings, BrowserType

chrome = BrowserSettings(type=BrowserType.CHROME, headless=True)
edge = BrowserSettings(type=BrowserType.EDGE, headless=True)
firefox = BrowserSettings(type=BrowserType.FIREFOX, headless=True)

for settings in [chrome, edge, firefox]:
    with Browser(settings) as browser:
        browser.open.url("https://example.com")
```
