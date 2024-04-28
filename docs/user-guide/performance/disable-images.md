---
tags:
    - Tutorial
    - Performance
    - Disable Images
    - Settings
---

# Disable Images
## Why Disable Images?
It's often faster to load pages when you don't download images. So if you don't need to process images when scraping a web page, simply don't wait for such media data – often heavy payloads – and use less bandwidth.

## How to Configure
With Browserist, it's simple to configure. As the default setting for `disable_images` is `False` in `BrowserSettings`, we simply alter it to `True` like this:

```python linenums="1"
from browserist import Browser, BrowserSettings

settings = BrowserSettings(disable_images=True)

with Browser(settings) as browser:
    browser.open.url("https://example.com")
```

!!! note
    Not all browsers support disabling of images well: Both Safari and Internet Explorer requires us to update global settings in the operating system that may impact how these browsers behave outside Browserist.

## Standardised Settings Across Browser Types
If you want to disable image downloads with Selenium, you typically would use different settings from browser to browser. Browserist solves this problem so that settings for Chrome, Firefox, Edge, etc. are standardised.

For example, you can easily scale test runs across different browsers with a configuration like this:

```python linenums="1"
from browserist import Browser, BrowserSettings, BrowserType

chrome = BrowserSettings(type=BrowserType.CHROME, disable_images=True)
edge = BrowserSettings(type=BrowserType.EDGE, disable_images=True)
firefox = BrowserSettings(type=BrowserType.FIREFOX, disable_images=True)

for settings in [chrome, edge, firefox]:
    with Browser(settings) as browser:
        browser.open.url("https://example.com")
```
