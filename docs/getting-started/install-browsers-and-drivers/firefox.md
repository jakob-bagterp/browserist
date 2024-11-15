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
If you need to use different browser types, find more info [here](../../settings/browser-types.md).

!!! tip
    Always keep your browser and driver up to date. The GeckoDriver version should usually match the browser version, otherwise Browserist might throw an error.
