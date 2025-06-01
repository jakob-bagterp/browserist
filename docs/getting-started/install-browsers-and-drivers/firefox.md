---
title: How to Install Firefox and GeckoDriver
description: Learn how to install the Mozilla Chrome Firefox and GeckoDriver for browser automation. Includes step-by-step setup instructions.
tags:
    - Automation
    - Firefox
---

# How to Install Firefox and the GeckoDriver
## Install Mozilla Firefox
Firefox is a free, open-source web browser developed by Mozilla. Download the latest version [here](https://www.mozilla.org/firefox/new/).

## Install GeckoDriver
With [Homebrew](https://brew.sh):

```shell title=""
brew install geckodriver
```

More info [here](https://github.com/mozilla/geckodriver).

## Troubleshooting and Tips
If you are planning to use different browsers, please refer to the [guide on options for browser types](../../settings/browser-types.md).

!!! tip
    Always keep your browser and driver up to date. The GeckoDriver version should usually match the browser version, otherwise Browserist might throw an error.

## How to Use Firefox with Browserist
Once you have successfully installed the Firefox browser and its GeckoDriver, you can start using them with Browserist. Here is an example of how to automate Firefox using Browserist. Simply select Firefox as the browser type in the `BrowserSettings` configuration:

```python linenums="1" hl_lines="3 5"
from browserist import Browser, BrowserSettings, BrowserType

settings = BrowserSettings(type=BrowserType.FIREFOX)

with Browser(settings) as browser:
    browser.open.url("https://example.com")
    browser.wait.seconds(5)
```

Lean more about [how to use different browser types](../../settings/browser-types.md).
