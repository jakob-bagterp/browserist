from ..... import iteration_helper
from .....model.browser.base.driver import BrowserDriver
from ....get.page_title import get_page_title


def wait_until_page_title_changes(browser_driver: BrowserDriver, baseline_text: str, timeout: int) -> None:
    def has_page_title_changed(browser_driver: BrowserDriver, baseline_text: str) -> bool:
        return get_page_title(browser_driver) != baseline_text

    iteration_helper.retry.until_condition_is_true(
        browser_driver, baseline_text, func=has_page_title_changed, timeout=timeout)
