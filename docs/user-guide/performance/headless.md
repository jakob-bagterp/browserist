---
title: How to Run Browsers in Headless Mode
description: Learn how to run automated browsers in headless mode for improved performance and resource efficiency. With Browserist it's easy to configure Chrome, Firefox and Edge to run in the background.
tags:
    - Tutorial
    - Performance
    - Headless
    - Settings
---

# How to Run Browsers in Headless Mode
## What Is Headless?
Headless simply means that the browser runs in the background without being visible on the screen. This is also more efficient because it uses fewer resources, while headless browsers often are faster.

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
