from ..... import constant, iteration_helper
from .....model.browser.base.driver import BrowserDriver
from .....model.type.xpath import XPath
from ....get.text import get_text
from ...for_element import wait_for_element


def wait_until_text_changes(browser_driver: BrowserDriver, xpath: str, baseline_text: str, timeout: int) -> None:
    def has_text_changed(browser_driver: BrowserDriver, baseline_text: str) -> bool:
        return get_text(browser_driver, xpath, constant.timeout.BYPASS) != baseline_text

    xpath = XPath(xpath)
    wait_for_element(browser_driver, xpath, timeout)
    iteration_helper.retry.until_condition_is_true(
        browser_driver.webdriver, browser_driver.settings, baseline_text, func=has_text_changed, timeout=timeout)
