---
title: How to Disable Images in Selenium
description: Learn how to boost web scraping performance by disabling images in Selenium. Or use the Browserist extension that makes the configuration even easier. Includes code examples for beginners and advanced users.
tags:
    - Selenium
    - Tutorial
    - Disable Images
    - Settings
---

# Disable Images in Selenium and Browserist
## Why Disable Images? Advantages and Disadvantages
If you want to scrape a website that loads images, you can gain a [performance boost by disabling images](../../performance/disable-images.md).

This is often done in combination with [headless mode](headless-mode.md), since you can't see any graphics in a headless browser. On the other hand, the disadvantage is obviously that you can't observe what the browser is doing.

## How to Configure
### Selenium
With Selenium, each browser type has its own configuration:

=== "Chrome"
    ```python linenums="1" hl_lines="5-9"
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options as ChromeOptions

    chrome_options = ChromeOptions()
    preferences = {
        "profile.managed_default_content_settings.images": 2,
        "profile.default_content_settings.images": 2
    }
    chrome_options.add_experimental_option("prefs", preferences)

    driver = webdriver.Chrome(options=chrome_options)
    ```

=== "Edge"
    ```python linenums="1" hl_lines="5-10"
    from selenium import webdriver
    from selenium.webdriver.edge.options import Options as EdgeOptions

    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    preferences = {
        "profile.managed_default_content_settings.images": 2,
        "profile.default_content_settings.images": 2
    }
    edge_options.add_experimental_option("prefs", preferences)

    driver = webdriver.Edge(options=edge_options)
    ```

=== "Firefox"
    ```python linenums="1" hl_lines="4-5"
    from selenium import webdriver

    firefox_options = webdriver.FirefoxOptions()
    firefox_options.set_preference("permissions.default.image", 2)
    firefox_options.set_preference("dom.ipc.plugins.enabled.libflashplayer.so", "false")

    driver = webdriver.Firefox(options=firefox_options)
    ```

### Browserist
Or use Browserist where the configuration is the same for all browser types – less hassle as the configuration of Selenium is automatically handled in the background. Simply set `disable_images=True` in the `BrowserSettings` class:

```python linenums="1" hl_lines="3-5"
from browserist import Browser, BrowserSettings, BrowserType

chrome = BrowserSettings(type=BrowserType.CHROME, disable_images=True)
edge = BrowserSettings(type=BrowserType.EDGE, disable_images=True)
firefox = BrowserSettings(type=BrowserType.FIREFOX, disable_images=True)

for settings in [chrome, edge, firefox]:
    with Browser(settings) as browser:
        browser.open.url("https://example.com")
        browser.wait.seconds(5)
```

## Supported Browsers

!!! note
    Not all browsers support disabling of images well: Both Safari and Internet Explorer requires us to update global settings in the operating system that may impact how these browsers behave outside Browserist.

Browsers that support disabling of images:

<div id="disable-images-supported-browsers-table"></div>

| Chrome           | Edge             | Firefox          | Safari                                | Internet Explorer                     |
| :--------------: | :--------------: | :--------------: | :-----------------------------------: | :-----------------------------------: |
| :material-check: | :material-check: | :material-check: | :material-alert-circle-check-outline: | :material-alert-circle-check-outline: |
