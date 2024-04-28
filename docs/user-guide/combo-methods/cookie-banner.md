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
### Basic Usage
Gettning started:

```python linenums="1"
from browserist import Browser, CookieBannerSettings

accept_cookies = CookieBannerSettings(
    url="https://example.com",
    has_loaded_xpath="//xpath/to/cookie_banner",
    button_xpath="//xpath/to/accept_button")

with Browser() as browser:
    browser.combo.cookie_banner(accept_cookies)
    browser.open.url("https://example.com/some_page")
```

### Conditional Flows
Sometimes it's useful to let a flow be dependent of succesfull handling of the cookie banner. This is possible by setting `return_bool` to `True` as parameter in the settings class and using a conditional `if` statement in combination with the cookie banner combo. For example:

```python linenums="1"
from browserist import Browser, CookieBannerSettings

accept_cookies = CookieBannerSettings(
    url="https://example.com",
    has_loaded_xpath="//xpath/to/cookie_banner",
    button_xpath="//xpath/to/accept_button",
    return_bool=True)

with Browser() as browser:
    if browser.combo.cookie_banner(accept_cookies):
        browser.open.url("https://example.com/some_page")
        browser.click.button("//xpath/to/button")
```

### Testing Purposes
Let's expand the examples and imagine that a website can personalise the content when returning users accept cookies. We want to test whether it's working as expected. For instance:

```python linenums="1"
from browserist import Browser, CookieBannerSettings

accept_cookies = CookieBannerSettings(
    url="https://example.com",
    has_loaded_xpath="//xpath/to/cookie_banner",
    button_xpath="//xpath/to/accept_button")

decline_cookies = CookieBannerSettings(
    url="https://example.com",
    has_loaded_xpath="//xpath/to/cookie_banner",
    button_xpath="//xpath/to/decline_button")

with Browser() as browser:
    browser.combo.cookie_banner(accept_cookies)
    assert browser.get.text("//xpath/to/headline") == "Welcome back!"

with Browser() as browser:
    browser.combo.cookie_banner(decline_cookies)
    assert browser.get.text("//xpath/to/headline") == "Hi there!"
```
