---
tags:
    - Tutorial
    - Settings
    - Combo
---

# Cookie Banner Combo Method
As you often need to accept cookie consent banners before you can scrape web pages, Browserist has a standardised method to do this at scale. The `CookieBannerSettings` class enables you to easily share the same settings across different browsers or scripts.

View all options in the [reference documentation](../../reference/browser/combo/cookie-banner.md#cookiebannersettings).

## Examples
Basic usage:

```python linenums="1"
from browserist import Browser, CookieBannerSettings

accept_cookies = CookieBannerSettings(
    url = "https://example.com",
    has_loaded_xpath = "//xpath/to/cookie_banner",
    button_xpath = "//xpath/to/accept_button")

with Browser() as browser:
    browser.combo.cookie_banner(accept_cookies)
    browser.open.url("https://example.com/some_page")
```

Let's expand the example and imagine that a website can personalise the content when returning users accept cookies. We want to test whether it's working as expected. For instance:

```python linenums="1"
from browserist import Browser, CookieBannerSettings

accept_cookies = CookieBannerSettings(
    url = "https://example.com",
    has_loaded_xpath = "//xpath/to/cookie_banner",
    button_xpath = "//xpath/to/accept_button")

decline_cookies = CookieBannerSettings(
    url = "https://example.com",
    has_loaded_xpath = "//xpath/to/cookie_banner",
    button_xpath = "//xpath/to/decline_button")

with Browser() as browser:
    browser.combo.cookie_banner(accept_cookies)
    assert browser.get.text("//xpath/to/headline") == "Welcome back!"

with Browser() as browser:
    browser.combo.cookie_banner(decline_cookies)
    assert browser.get.text("//xpath/to/headline") == "Hi there!"
```
