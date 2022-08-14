from browserist import Browser


def reset_to_not_timed_out(browser: Browser) -> Browser:
    browser._browser_driver.settings.timeout._is_timed_out = False
    return browser


def set_to_timed_out(browser: Browser) -> Browser:
    browser._browser_driver.settings.timeout._is_timed_out = True
    return browser
