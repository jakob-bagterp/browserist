from ..... import constant, helper
from .....model.browser.base.settings import BrowserSettings
from .....model.type.xpath import XPath
from ....get.text import get_text
from ...for_element import wait_for_element


def wait_until_text_changes(driver: object, settings: BrowserSettings, xpath: str, baseline_text: str, timeout: int) -> None:
    def has_text_changed(driver: object, settings: BrowserSettings, baseline_text: str) -> bool:
        return get_text(driver, settings, xpath, constant.timeout.BYPASS) != baseline_text

    xpath = XPath(xpath)
    wait_for_element(driver, settings, xpath, timeout)
    helper.retry.until_condition_is_true(driver, settings, baseline_text, func=has_text_changed, timeout=timeout)
