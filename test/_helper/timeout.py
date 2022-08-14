from browserist import Browser, TimeoutStrategy


def reset_to_not_timed_out(browser: Browser) -> Browser:
    browser._browser_driver.settings.timeout._is_timed_out = False
    return browser


def set_to_timed_out(browser: Browser) -> Browser:
    browser._browser_driver.settings.timeout._is_timed_out = True
    return browser


def set_timeout_strategy_to_stop(browser: Browser) -> Browser:
    browser._browser_driver.settings.timeout.strategy = TimeoutStrategy.STOP
    return browser


def set_timeout_strategy_to_continue(browser: Browser) -> Browser:
    browser._browser_driver.settings.timeout.strategy = TimeoutStrategy.CONTINUE
    return browser
