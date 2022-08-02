from ..... import iteration_helper
from .....model.browser.base.settings import BrowserSettings
from .....model.type.url import URL
from ....get.url.current import get_current_url


def wait_until_url_changes(driver: object, settings: BrowserSettings, baseline_url: str, timeout: int) -> None:
    def has_url_changed(driver: object, _: BrowserSettings, baseline_url: str) -> bool:
        return get_current_url(driver) != baseline_url

    baseline_url = URL(baseline_url)
    iteration_helper.retry.until_condition_is_true(
        driver, settings, baseline_url, func=has_url_changed, timeout=timeout)
