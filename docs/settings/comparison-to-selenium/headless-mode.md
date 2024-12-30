---
title: How to Configure Selenium in Headless Mode
description: Or do the same with Browserist, a powerful Python extension to Selenium that makes it easier to configure your browser in headless mode with less code. Includes code examples for beginners and advanced users.
tags:
    - Selenium
    - Tutorial
    - Headless
    - Settings
---

# Headless Mode in Selenium and Browserist
## Why Headless Mode? Advantages and Disadvantages
When you want to run an automated browser in the background while doing something else, you can gain a [performance boost by running the browser in headless mode](../../performance/headless.md). This is often done in combination with [disabling images](disable-images.md), since you can't see any graphics in a headless browser.

On the other hand, the disadvantage is obviously that you can't observe what the browser is doing.

## How to Configure
### Selenium
With Selenium, each browser type has its own configuration:

=== "Chrome"
    ```python linenums="1" hl_lines="5"
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options as ChromeOptions

    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    ```

=== "Edge"
    ```python linenums="1" hl_lines="6"
    from selenium import webdriver
    from selenium.webdriver.edge.options import Options as EdgeOptions

    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument("headless")

    driver = webdriver.Edge(options=edge_options)
    ```

=== "Firefox"
    ```python linenums="1" hl_lines="4-5"
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options as FirefoxOptions

    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--disable-gpu")

    driver = webdriver.Firefox(options=firefox_options)
    ```

### Browserist
Or use Browserist where the configuration is the same for all browser types – less hassle as the configuration of Selenium is automatically handled in the background. Simply set `headless=True` in the `BrowserSettings` class:

```python linenums="1" hl_lines="3-5"
from browserist import Browser, BrowserSettings, BrowserType

chrome_headless = BrowserSettings(type=BrowserType.CHROME, headless=True)
edge_headless = BrowserSettings(type=BrowserType.EDGE, headless=True)
firefox_headless = BrowserSettings(type=BrowserType.FIREFOX, headless=True)

for settings in [chrome_headless, edge_headless, firefox_headless]:
    with Browser(settings) as browser:
        browser.open.url("https://example.com")
        browser.wait.seconds(5)
```

## Supported Browsers

!!! note
    Not all browsers support headless mode, for instance Safari and Internet Explorer.

Browsers that support headless mode:

<div id="headless-supported-browsers-table"></div>

| Chrome           | Edge             | Firefox          | Safari                          | Internet Explorer               |
| :--------------: | :--------------: | :--------------: | :-----------------------------: | :-----------------------------: |
| :material-check: | :material-check: | :material-check: | :material-minus-circle-outline: | :material-minus-circle-outline: |
