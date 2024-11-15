---
title: How to Configure Page Load Strategy
description: Learn how to configure and optimize page load strategies in web automation and scraping. With Browserist as extension to Selenium, it's easy to configure with few lines of code.
tags:
    - Tutorial
    - Settings
    - Selenium
    - Performance
---

# What Is a Page Load Strategy?
When is a page considered to be loaded? When all resources – stylesheets, images, scripts, etc. – have finished loading, or perhaps earlier when you can interact with the page?

This choice is important if you want to tweak the performance of how fast your automation script runs. Just be aware that the page load strategy options are a trade-off between speed and stability, and the browser may hang idle or crash if you choose the wrong strategy.

The default – and most commonly used – strategy is to wait for all resources to be downloaded: `PageLoadStrategy.NORMAL`. However, if your script doesn't need to download images or need to interact with the page, try the `PageLoadStrategy.EAGER` or `PageLoadStrategy.NONE` strategies to speed up the execution.

## Strategy Options
Configure the page load strategy with the `PageLoadStrategy` class. This is then passed on to the underlying [Selenium web driver](https://www.selenium.dev/documentation/webdriver/drivers/options/#pageloadstrategy). The options are:

| Option                    | Description                                                                | Ready State |
| ------------------------- | -------------------------------------------------------------------------- | ----------- |
| `PageLoadStrategy.NORMAL` | Default. Waits for all resources to download.                              | Complete    |
| `PageLoadStrategy.EAGER`  | DOM access is ready, but other resources like images may still be loading. | Interactive |
| `PageLoadStrategy.NONE`   | Does not block web driver at all.                                          | Any         |

!!! note
    The page load strategy is set for the entire browser session. It can't be changed later for individual functions.

## Example
How to set the page load strategy when opening a new browser:

```python linenums="1"
from browserist import Browser, BrowserSettings, PageLoadStrategy

settings = BrowserSettings(page_load_strategy=PageLoadStrategy.EAGER)

with Browser(settings) as browser:
    browser.open.url("https://example.com")
```

## Details on Document Ready State
The `document.readyState` is a property of the DOM that indicates the loading status of the page. When navigating to a new page via URL, the browser driver waits until the document ready state is complete by default.

Note that this doesn't mean that the page has finished loading. This is especially the case for single-page applications that use JavaScript to dynamically load content after the document ready state is complete. Furthermore, the behavior does not apply to navigation that is a result of clicking an element or submitting a form.

If a page takes a long time to load as a result of downloading assets (e.g. images, CSS, JavaScript) that aren't important to the automation, you can change from the default `PageLoadStrategy.NORMAL` to `PageLoadStrategy.EAGER` or `PageLoadStrategy.NONE` to speed up the session.

!!! warning
    Though you may gain some performance by using either `PageLoadStrategy.NONE` or `PageLoadStrategy.EAGER`, it's usually not recommended. The browser may not be ready to execute the next function, which can lead to unstability. It's often better to use `PageLoadStrategy.NORMAL` and, if the browser allows it, [disable images](../user-guide/performance/disable-images.md) instead.
