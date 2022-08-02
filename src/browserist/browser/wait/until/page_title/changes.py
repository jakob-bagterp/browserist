from ..... import iteration_helper
from .....model.browser.base.settings import BrowserSettings
from ....get.page_title import get_page_title


def wait_until_page_title_changes(driver: object, settings: BrowserSettings, baseline_text: str, timeout: int) -> None:
    def has_page_title_changed(driver: object, _: BrowserSettings, baseline_text: str) -> bool:
        return get_page_title(driver) != baseline_text

    iteration_helper.retry.until_condition_is_true(
        driver, settings, baseline_text, func=has_page_title_changed, timeout=timeout)
