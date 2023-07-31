---
tags:
    - Tutorial
    - Settings
    - Combo
---

# Cookie Banner Combo Method
As you often need to accept cookie consent banners before you can scrape web pages, Browserist has a standardised method to do this at scale. The `CookieBannerSettings` class enables you to easily share the same settings across different browsers or scripts.

View all options in the [reference documentation](../../reference/browser/combo.md#cookiebannersettings).

## Example
```python title=""
from browserist import Browser, CookieBannerSettings

accept_cookies = CookieBannerSettings(
    url = "https://example.com",
    has_loaded_xpath = "//xpath/to/cookie_banner",
    button_xpath = "//xpath/to/accept_button")

with Browser() as browser:
    browser.combo.cookie_banner(accept_cookies)
    browser.open.url("https://example.com/some_page")
```
