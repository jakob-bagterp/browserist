from ..... import helper_iteration
from .....model.browser.base.driver import BrowserDriver
from .....model.type.url import URL
from ....get.url.current import get_current_url


def wait_until_url_changes(browser_driver: BrowserDriver, baseline_url: str, timeout: float) -> None:
    def has_url_changed(browser_driver: BrowserDriver, baseline_url: str) -> bool:
        return get_current_url(browser_driver) != baseline_url

    baseline_url = URL(baseline_url)
    helper_iteration.retry.until_condition_is_true(
        browser_driver, baseline_url, func=has_url_changed, timeout=timeout)
